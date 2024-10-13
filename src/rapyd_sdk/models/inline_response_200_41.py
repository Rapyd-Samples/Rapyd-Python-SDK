from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .discount_customer_response import DiscountCustomerResponse


@JsonMap({})
class InlineResponse200_41(BaseModel):
    """InlineResponse200_41

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process: <BR> 1. Create Coupon, which returns a coupon ID. <BR>2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
    :type data: DiscountCustomerResponse, optional
    """

    def __init__(self, status: Status1 = None, data: DiscountCustomerResponse = None):
        """InlineResponse200_41

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process: <BR> 1. Create Coupon, which returns a coupon ID. <BR>2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
        :type data: DiscountCustomerResponse, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, DiscountCustomerResponse)
