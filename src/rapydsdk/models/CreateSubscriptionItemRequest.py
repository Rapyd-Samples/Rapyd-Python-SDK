from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateSubscriptionItemRequest(BaseModel):
    def __init__(
        self,
        plan: str,
        subscription: str,
        metadata: dict = None,
        prorate: bool = None,
        proration_date: float = None,
        quantity: float = None,
    ):
        self.metadata = metadata
        self.plan = plan
        self.prorate = prorate
        self.proration_date = proration_date
        self.quantity = quantity
        self.subscription = subscription
