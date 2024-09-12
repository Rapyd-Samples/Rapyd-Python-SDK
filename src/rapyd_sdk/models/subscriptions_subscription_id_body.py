from __future__ import annotations
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel
from .payment_options import PaymentOptions
from .payment_method_type import PaymentMethodType


class SubscriptionsSubscriptionIdBodyPaymentMethodGuard(OneOfBaseModel):
    class_list = {"str": str, "PaymentMethodType": PaymentMethodType}


SubscriptionsSubscriptionIdBodyPaymentMethod = Union[str, PaymentMethodType]


@JsonMap({})
class SubscriptionsSubscriptionIdBody(BaseModel):
    """SubscriptionsSubscriptionIdBody

    :param billing: Determines the method of billing. Set to pay_automatically., defaults to None
    :type billing: str, optional
    :param billing_cycle_anchor: Determines the start of the next billing cycle, as defined in the plan described in the 'items'. Value must be timestamp in Unix time., defaults to None
    :type billing_cycle_anchor: str, optional
    :param cancel_at_period_end: Terminates the subscription at the end of the current billing period., defaults to None
    :type cancel_at_period_end: bool, optional
    :param coupon: The ID of a discount coupon that applies to all subscription items associated with this subscription. If the coupon defines a fixed monetary discount, it must use the same currency as the subscription's plan., defaults to None
    :type coupon: str, optional
    :param days_until_due: Number of days from the invoice date for customer to complete the payment., defaults to None
    :type days_until_due: float, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payment_fields: A payment method type is a type of payment method that any customer can use, for example, ee_mastercard_card, Mastercard for Estonia. When it is added to a customer profile, it becomes a payment method that is specific to that one customer. The name of the payment method type starts with a prefix for the country, the 2-letter ISO 3166-1 alpha-2 code. If the payment method is valid in multiple countries, the prefix is xx_. The payment method type has a suffix with one of the following values - _bank - Bank transfer or bank redirect _card - Credit card, debit card or other card _cash - Cash _ewallet - Local eWallet, defaults to None
    :type payment_fields: PaymentOptions, optional
    :param payment_method: Payment Method object or ID., defaults to None
    :type payment_method: SubscriptionsSubscriptionIdBodyPaymentMethod, optional
    :param simultaneous_invoice: Determines whether each upcoming subscription invoice is issued immediately. When true, the invoice is issued when the subscription is created. When false (the default), the invoice is issued an hour after the subscription is created., defaults to None
    :type simultaneous_invoice: bool, optional
    :param subscription_items: Array of subscription items. Each item contains a plan (required) and a quantity, defaults to None
    :type subscription_items: List[str], optional
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
        billing: str = None,
        billing_cycle_anchor: str = None,
        cancel_at_period_end: bool = None,
        coupon: str = None,
        days_until_due: float = None,
        metadata: dict = None,
        payment_fields: PaymentOptions = None,
        payment_method: SubscriptionsSubscriptionIdBodyPaymentMethod = None,
        simultaneous_invoice: bool = None,
        subscription_items: List[str] = None,
        tax_percent: float = None,
        trial_end: float = None,
        trial_from_plan: bool = None,
        trial_period_days: float = None,
    ):
        """SubscriptionsSubscriptionIdBody

        :param billing: Determines the method of billing. Set to pay_automatically., defaults to None
        :type billing: str, optional
        :param billing_cycle_anchor: Determines the start of the next billing cycle, as defined in the plan described in the 'items'. Value must be timestamp in Unix time., defaults to None
        :type billing_cycle_anchor: str, optional
        :param cancel_at_period_end: Terminates the subscription at the end of the current billing period., defaults to None
        :type cancel_at_period_end: bool, optional
        :param coupon: The ID of a discount coupon that applies to all subscription items associated with this subscription. If the coupon defines a fixed monetary discount, it must use the same currency as the subscription's plan., defaults to None
        :type coupon: str, optional
        :param days_until_due: Number of days from the invoice date for customer to complete the payment., defaults to None
        :type days_until_due: float, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payment_fields: A payment method type is a type of payment method that any customer can use, for example, ee_mastercard_card, Mastercard for Estonia. When it is added to a customer profile, it becomes a payment method that is specific to that one customer. The name of the payment method type starts with a prefix for the country, the 2-letter ISO 3166-1 alpha-2 code. If the payment method is valid in multiple countries, the prefix is xx_. The payment method type has a suffix with one of the following values - _bank - Bank transfer or bank redirect _card - Credit card, debit card or other card _cash - Cash _ewallet - Local eWallet, defaults to None
        :type payment_fields: PaymentOptions, optional
        :param payment_method: Payment Method object or ID., defaults to None
        :type payment_method: SubscriptionsSubscriptionIdBodyPaymentMethod, optional
        :param simultaneous_invoice: Determines whether each upcoming subscription invoice is issued immediately. When true, the invoice is issued when the subscription is created. When false (the default), the invoice is issued an hour after the subscription is created., defaults to None
        :type simultaneous_invoice: bool, optional
        :param subscription_items: Array of subscription items. Each item contains a plan (required) and a quantity, defaults to None
        :type subscription_items: List[str], optional
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
        self.billing_cycle_anchor = self._define_str(
            "billing_cycle_anchor", billing_cycle_anchor, nullable=True
        )
        self.cancel_at_period_end = cancel_at_period_end
        self.coupon = self._define_str("coupon", coupon, nullable=True)
        self.days_until_due = self._define_number(
            "days_until_due", days_until_due, nullable=True
        )
        self.metadata = metadata
        self.payment_fields = self._define_object(payment_fields, PaymentOptions)
        self.payment_method = (
            SubscriptionsSubscriptionIdBodyPaymentMethodGuard.return_one_of(
                payment_method
            )
        )
        self.simultaneous_invoice = simultaneous_invoice
        self.subscription_items = subscription_items
        self.tax_percent = self._define_number(
            "tax_percent", tax_percent, nullable=True
        )
        self.trial_end = self._define_number("trial_end", trial_end, nullable=True)
        self.trial_from_plan = trial_from_plan
        self.trial_period_days = self._define_number(
            "trial_period_days", trial_period_days, nullable=True
        )
