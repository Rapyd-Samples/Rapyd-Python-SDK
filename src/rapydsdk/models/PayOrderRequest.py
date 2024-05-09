from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class PayOrderRequest(BaseModel):
    def __init__(
        self, metadata: dict = None, payment_method: str = None, customer: str = None
    ):
        self.metadata = metadata
        self.payment_method = payment_method
        self.customer = customer
