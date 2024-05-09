from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class PayInvoiceRequest(BaseModel):
    def __init__(self, payment_method: str = None):
        self.payment_method = payment_method
