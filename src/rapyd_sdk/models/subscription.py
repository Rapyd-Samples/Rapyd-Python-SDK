from __future__ import annotations
from enum import Enum
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel
from .discount import Discount
from .subscription_items import SubscriptionItems


class BillingCycleAnchorGuard(OneOfBaseModel):
    class_list = {"str": str, "float": float}


BillingCycleAnchor = Union[str, float]


class SubscriptionStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACTIVE: "active"
    :vartype ACTIVE: str
    :cvar CANCELED: "canceled"
    :vartype CANCELED: str
    :cvar PASTDUE: "past_due"
    :vartype PASTDUE: str
    :cvar TRIALING: "trialing"
    :vartype TRIALING: str
    :cvar UNPAID: "unpaid"
    :vartype UNPAID: str
    """

    ACTIVE = "active"
    CANCELED = "canceled"
    PASTDUE = "past_due"
    TRIALING = "trialing"
    UNPAID = "unpaid"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SubscriptionStatus._member_map_.values()))


class SubscriptionType(Enum):
    """An enumeration representing different categories.

    :cvar PAYOUT: "payout"
    :vartype PAYOUT: str
    :cvar PAYMENT: "payment"
    :vartype PAYMENT: str
    """

    PAYOUT = "payout"
    PAYMENT = "payment"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SubscriptionType._member_map_.values()))


@JsonMap({"id_": "id", "type_": "type"})
class Subscription(BaseModel):
    """Subscription

    :param billing: Determines the method of billing at the end of the billing cycle. Set to pay_automatically - Rapyd generates a 'payment' object, then attempts to pay it using the designated payment method., defaults to None
    :type billing: str, optional
    :param billing_cycle_anchor: Determines the start of the next full billing cycle, as defined in the plan described in the 'items'. One of the following values:  * now - The present day. The next billing cycle starts right now.  * Timestamp in Unix time - A time in the future, at or after the end of the free trial period, not more than the length of the billing cycle. The current billing cycle will be shorter than all other billing cycles. Relevant to creation of the subscription.  * unchanged - The original billing cycle anchor is unchanged. Relevant to updating a subscription. , defaults to None
    :type billing_cycle_anchor: BillingCycleAnchor, optional
    :param cancel_at_period_end: Determines the last date that charges accrue. true - Charges accrue until the end of the current billing period, then the subscription is canceled.  * When no trial period is set, after cancel_at_period_end is set to true the subscription will not be renewed at the next interval.  * When a trial period is set after cancel_at_period_end is set to true, the subscription will not begin. false - This is the default.  * When the subscription is created, no end is defined. * When Cancel Subscription is run, charges stop immediately and the subscription is canceled. , defaults to None
    :type cancel_at_period_end: bool, optional
    :param canceled_at: Date and time that the subscription is canceled by the customer or by the client. Unix time. Response only., defaults to None
    :type canceled_at: float, optional
    :param created_at: Time of creation of this subscription, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param current_period_end: End of the current billing cycle, in Unix time. Response only., defaults to None
    :type current_period_end: float, optional
    :param current_period_start: Start of the current billing cycle, in Unix time. Response only., defaults to None
    :type current_period_start: float, optional
    :param customer_token: ID of the customer who pays for this subscription. String starting with cus_. Response only., defaults to None
    :type customer_token: str, optional
    :param days_until_due: Number of days from the invoice date for customer to complete the payment., defaults to None
    :type days_until_due: float, optional
    :param discount: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process - 1. Create Coupon, which returns a coupon ID. 2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
    :type discount: Discount, optional
    :param ended_at: Date that the subscription was canceled or otherwise terminated. Unix time. Response only., defaults to None
    :type ended_at: float, optional
    :param id_: ID of the Subscription object. String starting with sub_., defaults to None
    :type id_: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payment_fields: Additional payment_options fields., defaults to None
    :type payment_fields: dict, optional
    :param payment_method: Payment method ID or Payment Method object. if not specified in this field, the payment method is the default payment method specified for the customer., defaults to None
    :type payment_method: str, optional
    :param payout_fields: Reserved., defaults to None
    :type payout_fields: dict, optional
    :param simultaneous_invoice: Determines whether each upcoming subscription invoice is issued immediately.  * true - The invoice is issued when the subscription is created.  * false - The invoice is issued an hour after the subscription is created. This is the default. , defaults to None
    :type simultaneous_invoice: bool, optional
    :param status: Status of the subscription. One of the following:  * active - The customer is currently paying for this subscription.  * canceled - The customer has canceled this subscription, but it remains in the Rapyd database.  * past_due - Payment for this subscription was not received by the end of the billing period.  * trialing - The subscription is in its free trial period. * unpaid - An error occurred in the payment for this subscription. Response only. , defaults to None
    :type status: SubscriptionStatus, optional
    :param subscription_items: subscription_items, defaults to None
    :type subscription_items: SubscriptionItems, optional
    :param tax_percent: The percentage tax rate that is applied to the subtotal of the invoice, after subtracting all discounts. Decimal. Range: 0-100, with up to four decimal places., defaults to None
    :type tax_percent: float, optional
    :param trial_end: The date and time of the end of the customer's free trial period, in Unix time, or the string now. Takes precedence over trial_period_days. If trial_end is not set by the client, Rapyd calculates this date by adding trial_period_days to the date in created_at. Relevant when trial_period_days is not defined., defaults to None
    :type trial_end: float, optional
    :param trial_start: Date and time of the start of the customer's free trial period, in Unix time. Response only., defaults to None
    :type trial_start: float, optional
    :param type_: The type of the subscription. One of the following values: * payment  * payout  Response only. , defaults to None
    :type type_: SubscriptionType, optional
    """

    def __init__(
        self,
        billing: str = None,
        billing_cycle_anchor: BillingCycleAnchor = None,
        cancel_at_period_end: bool = None,
        canceled_at: float = None,
        created_at: float = None,
        current_period_end: float = None,
        current_period_start: float = None,
        customer_token: str = None,
        days_until_due: float = None,
        discount: Discount = None,
        ended_at: float = None,
        id_: str = None,
        metadata: dict = None,
        payment_fields: dict = None,
        payment_method: str = None,
        payout_fields: dict = None,
        simultaneous_invoice: bool = None,
        status: SubscriptionStatus = None,
        subscription_items: SubscriptionItems = None,
        tax_percent: float = None,
        trial_end: float = None,
        trial_start: float = None,
        type_: SubscriptionType = None,
    ):
        """Subscription

        :param billing: Determines the method of billing at the end of the billing cycle. Set to pay_automatically - Rapyd generates a 'payment' object, then attempts to pay it using the designated payment method., defaults to None
        :type billing: str, optional
        :param billing_cycle_anchor: Determines the start of the next full billing cycle, as defined in the plan described in the 'items'. One of the following values:  * now - The present day. The next billing cycle starts right now.  * Timestamp in Unix time - A time in the future, at or after the end of the free trial period, not more than the length of the billing cycle. The current billing cycle will be shorter than all other billing cycles. Relevant to creation of the subscription.  * unchanged - The original billing cycle anchor is unchanged. Relevant to updating a subscription. , defaults to None
        :type billing_cycle_anchor: BillingCycleAnchor, optional
        :param cancel_at_period_end: Determines the last date that charges accrue. true - Charges accrue until the end of the current billing period, then the subscription is canceled.  * When no trial period is set, after cancel_at_period_end is set to true the subscription will not be renewed at the next interval.  * When a trial period is set after cancel_at_period_end is set to true, the subscription will not begin. false - This is the default.  * When the subscription is created, no end is defined. * When Cancel Subscription is run, charges stop immediately and the subscription is canceled. , defaults to None
        :type cancel_at_period_end: bool, optional
        :param canceled_at: Date and time that the subscription is canceled by the customer or by the client. Unix time. Response only., defaults to None
        :type canceled_at: float, optional
        :param created_at: Time of creation of this subscription, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param current_period_end: End of the current billing cycle, in Unix time. Response only., defaults to None
        :type current_period_end: float, optional
        :param current_period_start: Start of the current billing cycle, in Unix time. Response only., defaults to None
        :type current_period_start: float, optional
        :param customer_token: ID of the customer who pays for this subscription. String starting with cus_. Response only., defaults to None
        :type customer_token: str, optional
        :param days_until_due: Number of days from the invoice date for customer to complete the payment., defaults to None
        :type days_until_due: float, optional
        :param discount: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process - 1. Create Coupon, which returns a coupon ID. 2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
        :type discount: Discount, optional
        :param ended_at: Date that the subscription was canceled or otherwise terminated. Unix time. Response only., defaults to None
        :type ended_at: float, optional
        :param id_: ID of the Subscription object. String starting with sub_., defaults to None
        :type id_: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payment_fields: Additional payment_options fields., defaults to None
        :type payment_fields: dict, optional
        :param payment_method: Payment method ID or Payment Method object. if not specified in this field, the payment method is the default payment method specified for the customer., defaults to None
        :type payment_method: str, optional
        :param payout_fields: Reserved., defaults to None
        :type payout_fields: dict, optional
        :param simultaneous_invoice: Determines whether each upcoming subscription invoice is issued immediately.  * true - The invoice is issued when the subscription is created.  * false - The invoice is issued an hour after the subscription is created. This is the default. , defaults to None
        :type simultaneous_invoice: bool, optional
        :param status: Status of the subscription. One of the following:  * active - The customer is currently paying for this subscription.  * canceled - The customer has canceled this subscription, but it remains in the Rapyd database.  * past_due - Payment for this subscription was not received by the end of the billing period.  * trialing - The subscription is in its free trial period. * unpaid - An error occurred in the payment for this subscription. Response only. , defaults to None
        :type status: SubscriptionStatus, optional
        :param subscription_items: subscription_items, defaults to None
        :type subscription_items: SubscriptionItems, optional
        :param tax_percent: The percentage tax rate that is applied to the subtotal of the invoice, after subtracting all discounts. Decimal. Range: 0-100, with up to four decimal places., defaults to None
        :type tax_percent: float, optional
        :param trial_end: The date and time of the end of the customer's free trial period, in Unix time, or the string now. Takes precedence over trial_period_days. If trial_end is not set by the client, Rapyd calculates this date by adding trial_period_days to the date in created_at. Relevant when trial_period_days is not defined., defaults to None
        :type trial_end: float, optional
        :param trial_start: Date and time of the start of the customer's free trial period, in Unix time. Response only., defaults to None
        :type trial_start: float, optional
        :param type_: The type of the subscription. One of the following values: * payment  * payout  Response only. , defaults to None
        :type type_: SubscriptionType, optional
        """
        self.billing = self._define_str("billing", billing, nullable=True)
        self.billing_cycle_anchor = BillingCycleAnchorGuard.return_one_of(
            billing_cycle_anchor
        )
        self.cancel_at_period_end = cancel_at_period_end
        self.canceled_at = self._define_number(
            "canceled_at", canceled_at, nullable=True
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.current_period_end = self._define_number(
            "current_period_end", current_period_end, nullable=True
        )
        self.current_period_start = self._define_number(
            "current_period_start", current_period_start, nullable=True
        )
        self.customer_token = self._define_str(
            "customer_token", customer_token, nullable=True
        )
        self.days_until_due = self._define_number(
            "days_until_due", days_until_due, nullable=True
        )
        self.discount = self._define_object(discount, Discount)
        self.ended_at = self._define_number("ended_at", ended_at, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.metadata = metadata
        self.payment_fields = payment_fields
        self.payment_method = self._define_str(
            "payment_method", payment_method, nullable=True
        )
        self.payout_fields = payout_fields
        self.simultaneous_invoice = simultaneous_invoice
        self.status = (
            self._enum_matching(status, SubscriptionStatus.list(), "status")
            if status
            else None
        )
        self.subscription_items = self._define_object(
            subscription_items, SubscriptionItems
        )
        self.tax_percent = self._define_number(
            "tax_percent", tax_percent, nullable=True
        )
        self.trial_end = self._define_number("trial_end", trial_end, nullable=True)
        self.trial_start = self._define_number(
            "trial_start", trial_start, nullable=True
        )
        self.type_ = (
            self._enum_matching(type_, SubscriptionType.list(), "type_")
            if type_
            else None
        )
