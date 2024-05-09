from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class RefundGroupPaymentRequest(BaseModel):
    def __init__(self, group_payment: str, amount: float = None):
        self.amount = amount
        self.group_payment = group_payment
