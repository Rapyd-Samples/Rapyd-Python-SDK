from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class RequestTotalCreateRefundRequest(BaseModel):
    def __init__(
        self,
        payment: str,
        amount: float = None,
        currency: str = None,
        ewallets: List[str] = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        reason: str = None,
    ):
        self.amount = amount
        self.currency = currency
        self.ewallets = ewallets
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.payment = payment
        self.reason = reason
