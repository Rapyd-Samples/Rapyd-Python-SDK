from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .coupon import Coupon
from .status import Status


@JsonMap({})
class InlineResponse200_30(BaseModel):
    """InlineResponse200_30

    :param data: The coupon can be applied to the following objects - * Subscription - All charges in the subscription are subject to the discount described in the coupon. To add a coupon to a subscription, first use Create Coupon. Then add the coupon ID to the coupon field of the subscription with Create Subscription or Update Subscription. * Customer - The discount applies to all charges to the customer. To add a coupon to a customer, first use Create Coupon. Then add the coupon ID to the coupon field of the customer with Create Customer or Update Customer. * Order - The discount applies to a single order. To add a coupon to an order, first use Create Coupon. The duration field of the coupon must be set to repeating, and the duration_in_months and discount_duration_in_uses fields must be set to 1. Then add the coupon ID to the coupon field of the order with Create an Order or Update Order. A coupon can be applied to one or more customers or subscriptions. However, a subscription can have only one coupon, and the only way to assign two or more coupons to a customer is to assign them to separate subscriptions. If there is a coupon for the customer and another coupon for the customer's subscription, the subscription coupon takes precedence., defaults to None
    :type data: Coupon, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Coupon = None, status: Status = None):
        """InlineResponse200_30

        :param data: The coupon can be applied to the following objects - * Subscription - All charges in the subscription are subject to the discount described in the coupon. To add a coupon to a subscription, first use Create Coupon. Then add the coupon ID to the coupon field of the subscription with Create Subscription or Update Subscription. * Customer - The discount applies to all charges to the customer. To add a coupon to a customer, first use Create Coupon. Then add the coupon ID to the coupon field of the customer with Create Customer or Update Customer. * Order - The discount applies to a single order. To add a coupon to an order, first use Create Coupon. The duration field of the coupon must be set to repeating, and the duration_in_months and discount_duration_in_uses fields must be set to 1. Then add the coupon ID to the coupon field of the order with Create an Order or Update Order. A coupon can be applied to one or more customers or subscriptions. However, a subscription can have only one coupon, and the only way to assign two or more coupons to a customer is to assign them to separate subscriptions. If there is a coupon for the customer and another coupon for the customer's subscription, the subscription coupon takes precedence., defaults to None
        :type data: Coupon, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Coupon)
        self.status = self._define_object(status, Status)
