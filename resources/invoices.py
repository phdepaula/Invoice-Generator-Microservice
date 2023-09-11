import requests
from flask_openapi3 import Tag

from app import app, database
from database.model.invoices import Invoices
from resources.xml_generator import XmlGenerator
from schemas.invoices import MessageInvoiceSchema, SingleMessageSchema

TAG_INVOICES = Tag(
    name="Invoices",
    description="Routes to control the generation of invoices."
)


@app.post(
    "/add_invoices",
    tags=[TAG_INVOICES],
    responses={
        "200": MessageInvoiceSchema,
        "400": SingleMessageSchema,
    },
)
def add_invoices():
    """Get invoices that are pending \
    via order management API.
    """
    try:
        invoices_url = (
            "http://order-management-microservice:5001/get_pending_invoices"
        )
        response_invoices_url = requests.get(invoices_url)
        response_invoices_data = response_invoices_url.json()

        if response_invoices_url.status_code == 400:
            raise Exception(
                response_invoices_data["message"].replace("Error: ", "")
            )

        orders = response_invoices_data.get("orders", [])
        invoices_generated = []

        for order in orders:
            empty_data = [key for key, value in order.items() if value == ""]
            order["status"] = (
                "Approved" if len(empty_data) == 0 else "Rejected"
            )
            order["comment"] = (
                "Complete invoice"
                if len(empty_data) == 0
                else f"Items {', '.join(map(str, empty_data))} are empty"
            )
            invoice_title = (
                f"Invoice_{order['order_id']}_{order['status']}.xml"
            )

            new_invoice = Invoices(
                order_id=order["order_id"],
                invoice_title=invoice_title,
                status=order["status"],
                comment=order["comment"],
            )
            database.insert_data_table(new_invoice)

            invoice = XmlGenerator(data=order, file_name=invoice_title)
            invoice.generate_xml()

            invoices_generated.append(invoice_title)

            complete_order_url = (
                "http://order-management-microservice:5001/complete_order"
            )
            order_id = {"order_id": int(order["order_id"])}
            response_complete_order = requests.put(
                complete_order_url, data=order_id
            )
            complete_order_data = response_complete_order.json()

            if response_complete_order.status_code == 400:
                raise Exception(
                    complete_order_data["message"].replace("Error: ", "")
                )

        return {"message": "Success", "invoices": invoices_generated}, 200
    except Exception as error:
        return {"message": f"Error: {error}"}, 400
