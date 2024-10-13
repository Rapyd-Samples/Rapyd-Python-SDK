from __future__ import annotations
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel
from .payment import Payment
from .v1paymentssubscriptions_subscription_items import (
    V1paymentssubscriptionsSubscriptionItems,
)
from .payment_method_type import PaymentMethodType


class PaymentsSubscriptionsBodyPaymentMethodGuard(OneOfBaseModel):
    class_list = {"str": str, "PaymentMethodType": PaymentMethodType}


PaymentsSubscriptionsBodyPaymentMethod = Union[str, PaymentMethodType]


@JsonMap({})
class PaymentsSubscriptionsBody(BaseModel):
    """PaymentsSubscriptionsBody

    :param billing: Determines the method of billing. Set to **pay_automatically**., defaults to None
    :type billing: str, optional
    :param billing_cycle_anchor: Determines the start of the next billing cycle, as defined in the plan described in the 'items'. Value must be timestamp in Unix time., defaults to None
    :type billing_cycle_anchor: float, optional
    :param cancel_at_period_end: Terminates the subscription at the end of the current billing period., defaults to None
    :type cancel_at_period_end: bool, optional
    :param coupon: The ID of a discount coupon that applies to all subscription items associated with this subscription. If the coupon defines a fixed monetary discount, it must use the same currency as the subscription's plan., defaults to None
    :type coupon: str, optional
    :param customer: ID of the customer who pays for this subscription. String starting with cus_.
    :type customer: str
    :param days_until_due: Number of days from the invoice date for customer to complete the payment., defaults to None
    :type days_until_due: float, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payment_fields: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
    :type payment_fields: Payment, optional
    :param payment_method: Payment Method object or ID., defaults to None
    :type payment_method: PaymentsSubscriptionsBodyPaymentMethod, optional
    :param simultaneous_invoice: Determines whether each upcoming subscription invoice is issued immediately. When true, the invoice is issued when the subscription is created. When false (the default), the invoice is issued an hour after the subscription is created., defaults to None
    :type simultaneous_invoice: bool, optional
    :param subscription_items: Array of subscription items. Each item contains a plan (required) and a quantity
    :type subscription_items: List[V1paymentssubscriptionsSubscriptionItems]
    :param tax_percent: The percentage of tax that is applied to the entire amount of the invoice., defaults to None
    :type tax_percent: float, optional
    :param trial_end: The time of the end of the customer's free trial period. If trial_from_plan is set, leave this parameter unset., defaults to None
    :type trial_end: float, optional
    :param trial_from_plan: Determines whether a free trial period can be defined in a 'plan' object attached to the subscription. If trial_end is set, leave this parameter unset., defaults to None
    :type trial_from_plan: bool, optional
    :param trial_period_days: The number of days in the customer's free trial period., defaults to None
    :type trial_period_days: float, optional
    """

    def __init__(
        self,
        customer: str,
        subscription_items: List[V1paymentssubscriptionsSubscriptionItems],
        billing: str = None,
        billing_cycle_anchor: float = None,
        cancel_at_period_end: bool = None,
        coupon: str = None,
        days_until_due: float = None,
        metadata: dict = None,
        payment_fields: Payment = None,
        payment_method: PaymentsSubscriptionsBodyPaymentMethod = None,
        simultaneous_invoice: bool = None,
        tax_percent: float = None,
        trial_end: float = None,
        trial_from_plan: bool = None,
        trial_period_days: float = None,
    ):
        """PaymentsSubscriptionsBody

        :param billing: Determines the method of billing. Set to **pay_automatically**., defaults to None
        :type billing: str, optional
        :param billing_cycle_anchor: Determines the start of the next billing cycle, as defined in the plan described in the 'items'. Value must be timestamp in Unix time., defaults to None
        :type billing_cycle_anchor: float, optional
        :param cancel_at_period_end: Terminates the subscription at the end of the current billing period., defaults to None
        :type cancel_at_period_end: bool, optional
        :param coupon: The ID of a discount coupon that applies to all subscription items associated with this subscription. If the coupon defines a fixed monetary discount, it must use the same currency as the subscription's plan., defaults to None
        :type coupon: str, optional
        :param customer: ID of the customer who pays for this subscription. String starting with cus_.
        :type customer: str
        :param days_until_due: Number of days from the invoice date for customer to complete the payment., defaults to None
        :type days_until_due: float, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payment_fields: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
        :type payment_fields: Payment, optional
        :param payment_method: Payment Method object or ID., defaults to None
        :type payment_method: PaymentsSubscriptionsBodyPaymentMethod, optional
        :param simultaneous_invoice: Determines whether each upcoming subscription invoice is issued immediately. When true, the invoice is issued when the subscription is created. When false (the default), the invoice is issued an hour after the subscription is created., defaults to None
        :type simultaneous_invoice: bool, optional
        :param subscription_items: Array of subscription items. Each item contains a plan (required) and a quantity
        :type subscription_items: List[V1paymentssubscriptionsSubscriptionItems]
        :param tax_percent: The percentage of tax that is applied to the entire amount of the invoice., defaults to None
        :type tax_percent: float, optional
        :param trial_end: The time of the end of the customer's free trial period. If trial_from_plan is set, leave this parameter unset., defaults to None
        :type trial_end: float, optional
        :param trial_from_plan: Determines whether a free trial period can be defined in a 'plan' object attached to the subscription. If trial_end is set, leave this parameter unset., defaults to None
        :type trial_from_plan: bool, optional
        :param trial_period_days: The number of days in the customer's free trial period., defaults to None
        :type trial_period_days: float, optional
        """
        self.billing = self._define_str("billing", billing, nullable=True)
        self.billing_cycle_anchor = self._define_number(
            "billing_cycle_anchor", billing_cycle_anchor, nullable=True
        )
        self.cancel_at_period_end = cancel_at_period_end
        self.coupon = self._define_str("coupon", coupon, nullable=True)
        self.customer = customer
        self.days_until_due = self._define_number(
            "days_until_due", days_until_due, nullable=True
        )
        self.metadata = metadata
        self.payment_fields = self._define_object(payment_fields, Payment)
        self.payment_method = PaymentsSubscriptionsBodyPaymentMethodGuard.return_one_of(
            payment_method
        )
        self.simultaneous_invoice = simultaneous_invoice
        self.subscription_items = self._define_list(
            subscription_items, V1paymentssubscriptionsSubscriptionItems
        )
        self.tax_percent = self._define_number(
            "tax_percent", tax_percent, nullable=True
        )
        self.trial_end = self._define_number("trial_end", trial_end, nullable=True)
        self.trial_from_plan = trial_from_plan
        self.trial_period_days = self._define_number(
            "trial_period_days", trial_period_days, nullable=True
        )
