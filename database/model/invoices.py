from sqlalchemy import Column, Integer, String

from database.database import Database

BASE = Database().BASE


class Invoices(BASE):
    """Class to create the invoices table"""

    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer)
    invoice_title = Column(String(40))
    status = Column(String(40))
    comment = Column(String(100))

    def __init__(
        self,
        order_id: int,
        invoice_title: str,
        status: str,
        comment: str,
    ):
        self.order_id = order_id
        self.invoice_title = invoice_title
        self.status = status
        self.comment = comment
