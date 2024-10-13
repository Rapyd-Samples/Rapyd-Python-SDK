from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .coupon import Coupon


@JsonMap({"id_": "id"})
class Discount(BaseModel):
    """Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process: <BR> 1. Create Coupon, which returns a coupon ID. <BR>2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer.

    :param coupon: The coupon can be applied to the following objects - * Subscription - All charges in the subscription are subject to the discount described in the coupon. To add a coupon to a subscription, first use Create Coupon. Then add the coupon ID to the coupon field of the subscription with Create Subscription or Update Subscription. * Customer - The discount applies to all charges to the customer. To add a coupon to a customer, first use Create Coupon. Then add the coupon ID to the coupon field of the customer with Create Customer or Update Customer. * Order - The discount applies to a single order. To add a coupon to an order, first use Create Coupon. The duration field of the coupon must be set to repeating, and the duration_in_months and discount_duration_in_uses fields must be set to 1. Then add the coupon ID to the coupon field of the order with Create an Order or Update Order. A coupon can be applied to one or more customers or subscriptions. However, a subscription can have only one coupon, and the only way to assign two or more coupons to a customer is to assign them to separate subscriptions. If there is a coupon for the customer and another coupon for the customer's subscription, the subscription coupon takes precedence., defaults to None
    :type coupon: Coupon, optional
    :param customer: ID of the Customer object that the discount applies to. String starting with **cus_**. Response only., defaults to None
    :type customer: str, optional
    :param end: The final time that a discount can be used, in Unix time. When the value is -1, the discount never expires. Response only., defaults to None
    :type end: float, optional
    :param id_: ID of the Discount object. String starting with **dis_**. Response only., defaults to None
    :type id_: str, optional
    :param number_of_uses: The number of times that the discount was used for a specific customer or subscription. The initial value is 0. The value is incremented by 1 each time that the discount is used. Response only., defaults to None
    :type number_of_uses: float, optional
    :param start: The time that a discount was created, in Unix time. Response only., defaults to None
    :type start: float, optional
    :param subscription: ID of the Subscription object that the discount applies to. String starting with **sub_**. Response only., defaults to None
    :type subscription: str, optional
    :param valid: Indicates whether the discount can be used. Response only., defaults to None
    :type valid: bool, optional
    """

    def __init__(
        self,
        coupon: Coupon = None,
        customer: str = None,
        end: float = None,
        id_: str = None,
        number_of_uses: float = None,
        start: float = None,
        subscription: str = None,
        valid: bool = None,
    ):
        """Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process: <BR> 1. Create Coupon, which returns a coupon ID. <BR>2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer.

        :param coupon: The coupon can be applied to the following objects - * Subscription - All charges in the subscription are subject to the discount described in the coupon. To add a coupon to a subscription, first use Create Coupon. Then add the coupon ID to the coupon field of the subscription with Create Subscription or Update Subscription. * Customer - The discount applies to all charges to the customer. To add a coupon to a customer, first use Create Coupon. Then add the coupon ID to the coupon field of the customer with Create Customer or Update Customer. * Order - The discount applies to a single order. To add a coupon to an order, first use Create Coupon. The duration field of the coupon must be set to repeating, and the duration_in_months and discount_duration_in_uses fields must be set to 1. Then add the coupon ID to the coupon field of the order with Create an Order or Update Order. A coupon can be applied to one or more customers or subscriptions. However, a subscription can have only one coupon, and the only way to assign two or more coupons to a customer is to assign them to separate subscriptions. If there is a coupon for the customer and another coupon for the customer's subscription, the subscription coupon takes precedence., defaults to None
        :type coupon: Coupon, optional
        :param customer: ID of the Customer object that the discount applies to. String starting with **cus_**. Response only., defaults to None
        :type customer: str, optional
        :param end: The final time that a discount can be used, in Unix time. When the value is -1, the discount never expires. Response only., defaults to None
        :type end: float, optional
        :param id_: ID of the Discount object. String starting with **dis_**. Response only., defaults to None
        :type id_: str, optional
        :param number_of_uses: The number of times that the discount was used for a specific customer or subscription. The initial value is 0. The value is incremented by 1 each time that the discount is used. Response only., defaults to None
        :type number_of_uses: float, optional
        :param start: The time that a discount was created, in Unix time. Response only., defaults to None
        :type start: float, optional
        :param subscription: ID of the Subscription object that the discount applies to. String starting with **sub_**. Response only., defaults to None
        :type subscription: str, optional
        :param valid: Indicates whether the discount can be used. Response only., defaults to None
        :type valid: bool, optional
        """
        self.coupon = self._define_object(coupon, Coupon)
        self.customer = self._define_str("customer", customer, nullable=True)
        self.end = self._define_number("end", end, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.number_of_uses = self._define_number(
            "number_of_uses", number_of_uses, nullable=True
        )
        self.start = self._define_number("start", start, nullable=True)
        self.subscription = self._define_str(
            "subscription", subscription, nullable=True
        )
        self.valid = valid
