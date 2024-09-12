from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .discount import Discount
from .status import Status


@JsonMap({})
class InlineResponse200_71(BaseModel):
    """InlineResponse200_71

    :param data: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process - 1. Create Coupon, which returns a coupon ID. 2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
    :type data: Discount, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Discount = None, status: Status = None):
        """InlineResponse200_71

        :param data: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process - 1. Create Coupon, which returns a coupon ID. 2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
        :type data: Discount, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Discount)
        self.status = self._define_object(status, Status)
