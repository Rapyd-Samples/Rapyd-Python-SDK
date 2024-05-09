from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class UpdateInvoiceRequest(BaseModel):
    def __init__(
        self,
        days_until_due: float = None,
        description: str = None,
        due_date: str = None,
        metadata: dict = None,
        payment_fields: dict = None,
        statement_descriptor: str = None,
        tax_percent: float = None,
    ):
        self.days_until_due = days_until_due
        self.description = description
        self.due_date = due_date
        self.metadata = metadata
        self.payment_fields = payment_fields
        self.statement_descriptor = statement_descriptor
        self.tax_percent = tax_percent
