from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class OrdersOrderIdBodyStatus(Enum):
    """An enumeration representing different categories.

    :cvar PAID: "paid"
    :vartype PAID: str
    :cvar PENDING: "pending"
    :vartype PENDING: str
    :cvar CANCELED: "canceled"
    :vartype CANCELED: str
    :cvar FULFILLED: "fulfilled"
    :vartype FULFILLED: str
    :cvar RETURNED: "returned"
    :vartype RETURNED: str
    :cvar PARTIAL: "partial"
    :vartype PARTIAL: str
    """

    PAID = "paid"
    PENDING = "pending"
    CANCELED = "canceled"
    FULFILLED = "fulfilled"
    RETURNED = "returned"
    PARTIAL = "partial"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, OrdersOrderIdBodyStatus._member_map_.values())
        )


@JsonMap({})
class OrdersOrderIdBody(BaseModel):
    """OrdersOrderIdBody

    :param coupon: ID of a coupon that is applied against this order. String starting with **coupon_**. The duration field of the coupon must be set to **repeating**, and the `duration_in_months` and `discount_duration_in_uses` fields must be set to **1**., defaults to None
    :type coupon: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param tax_percent: Percentage of tax to charge. Decimal., defaults to None
    :type tax_percent: float, optional
    :param status: Indicates the status of the order. Can be changed when status is pending, paid or fulfilled, defaults to None
    :type status: OrdersOrderIdBodyStatus, optional
    """

    def __init__(
        self,
        coupon: str = None,
        metadata: dict = None,
        tax_percent: float = None,
        status: OrdersOrderIdBodyStatus = None,
    ):
        """OrdersOrderIdBody

        :param coupon: ID of a coupon that is applied against this order. String starting with **coupon_**. The duration field of the coupon must be set to **repeating**, and the `duration_in_months` and `discount_duration_in_uses` fields must be set to **1**., defaults to None
        :type coupon: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param tax_percent: Percentage of tax to charge. Decimal., defaults to None
        :type tax_percent: float, optional
        :param status: Indicates the status of the order. Can be changed when status is pending, paid or fulfilled, defaults to None
        :type status: OrdersOrderIdBodyStatus, optional
        """
        self.coupon = self._define_str("coupon", coupon, nullable=True)
        self.metadata = metadata
        self.tax_percent = self._define_number(
            "tax_percent", tax_percent, nullable=True
        )
        self.status = (
            self._enum_matching(status, OrdersOrderIdBodyStatus.list(), "status")
            if status
            else None
        )
