from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class RetrySchedule(Enum):
    FIXED = "fixed"

    def list():
        return list(map(lambda x: x.value, RetrySchedule._member_map_.values()))


class RetryInterval(Enum):
    DAYS = "days"
    WEEKS = "weeks"

    def list():
        return list(map(lambda x: x.value, RetryInterval._member_map_.values()))


@JsonMap({})
class SubscriptionRetryOptions(BaseModel):
    def __init__(
        self,
        max_retries: float = None,
        retry_schedule: RetrySchedule = None,
        retry_interval: RetryInterval = None,
        retry_interval_count: float = None,
    ):
        self.max_retries = max_retries
        self.retry_schedule = (
            self._enum_matching(retry_schedule, RetrySchedule.list(), "retry_schedule")
            if retry_schedule
            else None
        )
        self.retry_interval = (
            self._enum_matching(retry_interval, RetryInterval.list(), "retry_interval")
            if retry_interval
            else None
        )
        self.retry_interval_count = retry_interval_count
