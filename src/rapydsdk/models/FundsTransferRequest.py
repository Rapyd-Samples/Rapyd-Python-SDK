from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class FundsTransferRequest(BaseModel):
    def __init__(
        self,
        amount: float,
        destination_ewallet: str,
        source_ewallet: str,
        currency: str = None,
        expiration: str = None,
        metadata: dict = None,
    ):
        self.amount = amount
        self.currency = currency
        self.destination_ewallet = destination_ewallet
        self.expiration = expiration
        self.metadata = metadata
        self.source_ewallet = source_ewallet
