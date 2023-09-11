from pydantic import BaseModel


class MessageInvoiceSchema(BaseModel):
    """Defines how the API response should be \
    like for a successful invoice generated."""

    message: str
    invoices: list


class SingleMessageSchema(BaseModel):
    """
    Defines how the API response should be \
    when you want to send just one message.
    """

    message: str
