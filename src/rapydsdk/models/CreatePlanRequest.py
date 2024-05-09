from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class CreatePlanRequest(BaseModel):
    def __init__(
        self,
        currency: str,
        interval: str,
        product: str,
        aggregate_usage: str = None,
        amount: float = None,
        billing_scheme: str = None,
        id: str = None,
        interval_count: float = None,
        metadata: dict = None,
        nickname: str = None,
        tiers: str = None,
        tiers_mode: str = None,
        transform_usage: dict = None,
        trial_period_days: float = None,
        usage_type: str = None,
    ):
        self.aggregate_usage = aggregate_usage
        self.amount = amount
        self.billing_scheme = billing_scheme
        self.currency = currency
        self.id = id
        self.interval = interval
        self.interval_count = interval_count
        self.metadata = metadata
        self.nickname = nickname
        self.product = product
        self.tiers = tiers
        self.tiers_mode = tiers_mode
        self.transform_usage = transform_usage
        self.trial_period_days = trial_period_days
        self.usage_type = usage_type
