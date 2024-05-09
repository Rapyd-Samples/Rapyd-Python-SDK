from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class PaymentParams(BaseModel):
    def __init__(self, complete_payment_url: str = None, error_payment_url: str = None):
        self.complete_payment_url = complete_payment_url
        self.error_payment_url = error_payment_url
