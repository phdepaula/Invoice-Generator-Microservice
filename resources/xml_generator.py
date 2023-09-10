import os
import xml.etree.ElementTree as ET


class XmlGenerator:
    """Responsible for generating an invoice in xml format"""

    TEMPLATE_XML = """\
    <Invoice SALES_ID="{sales_id}" ORDER_ID ="{order_id}">
        <Status>{status}</Status>
        <Comment>{comment}</Comment>
        <Product>
            <Name>{name}</Name>
            <Price>{price}</Price>
            <Supplier>{supplier}</Supplier>
            <Category>{category}</Category>
            <Description>{description}</Description>
        </Product>
        <Sale>
            <Quantity>{quantity}</Quantity>
            <Value>{value}</Value>
            <Date>{sale_date}</Date>
            <AddressInformation>
                <Country>{country}</Country>
                <State>{state}</State>
                <City>{city}</City>
                <ZipCode>{zip_code}</ZipCode>
                <Street>{street}</Street>
                <Neighborhood>{neighborhood}</Neighborhood>
            </AddressInformation>
        </Sale>
    </Invoice>
    """

    def __init__(self, data: dict, file_name: str):
        self._data = data
        self._file_name = file_name

    def _format_template(self) -> str:
        """Method to format template data"""
        formatted_template = self.TEMPLATE_XML.format(**self._data)

        return formatted_template

    def generate_xml(self) -> None:
        """Method to generate the xml file"""
        formatted_template = self._format_template()
        invoice_directory = "./invoices"

        if not os.path.exists(invoice_directory):
            os.makedirs(invoice_directory)

        root = ET.fromstring(formatted_template)
        tree = ET.ElementTree(root)
        path = f"./invoices/{self._file_name}"
        tree.write(path, encoding="utf-8", xml_declaration=True)
