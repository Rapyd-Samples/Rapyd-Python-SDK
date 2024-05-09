from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateSubscriptionItemUsageRecordRequest(BaseModel):
    def __init__(
        self,
        quantity: float,
        timestamp: float,
        action: str = None,
        metadata: dict = None,
    ):
        self.action = action
        self.metadata = metadata
        self.quantity = quantity
        self.timestamp = timestamp
