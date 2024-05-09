from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class Status4(Enum):
    PAID = "paid"
    PENDING = "pending"
    CANCELED = "canceled"
    FULFILLED = "fulfilled"
    RETURNED = "returned"
    PARTIAL = "partial"

    def list():
        return list(map(lambda x: x.value, Status4._member_map_.values()))


@JsonMap({})
class UpdateOrderRequest(BaseModel):
    def __init__(
        self,
        coupon: str = None,
        metadata: dict = None,
        tax_percent: float = None,
        status: Status4 = None,
    ):
        self.coupon = coupon
        self.metadata = metadata
        self.tax_percent = tax_percent
        self.status = (
            self._enum_matching(status, Status4.list(), "status") if status else None
        )
