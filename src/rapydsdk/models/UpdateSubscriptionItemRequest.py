from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class UpdateSubscriptionItemRequest(BaseModel):
    def __init__(
        self,
        metadata: dict = None,
        prorate: bool = None,
        proration_date: float = None,
        quantity: float = None,
    ):
        self.metadata = metadata
        self.prorate = prorate
        self.proration_date = proration_date
        self.quantity = quantity
