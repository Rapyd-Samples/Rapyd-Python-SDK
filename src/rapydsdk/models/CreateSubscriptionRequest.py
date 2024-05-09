from __future__ import annotations
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Payment import Payment
from .PaymentMethodType import PaymentMethodType


class PaymentMethod8Guard(OneOfBaseModel):
    class_list = {"str": str, "PaymentMethodType": PaymentMethodType}


PaymentMethod8 = Union[str, PaymentMethodType]


@JsonMap({})
class SubscriptionItems1(BaseModel):
    def __init__(self, plan: str = None, quantity: float = None):
        self.plan = plan
        self.quantity = quantity


@JsonMap({})
class CreateSubscriptionRequest(BaseModel):
    def __init__(
        self,
        customer: str,
        subscription_items: List[SubscriptionItems1],
        billing: str = None,
        billing_cycle_anchor: float = None,
        cancel_at_period_end: bool = None,
        coupon: str = None,
        days_until_due: float = None,
        metadata: dict = None,
        payment_fields: Payment = None,
        payment_method: PaymentMethod8 = None,
        simultaneous_invoice: bool = None,
        tax_percent: float = None,
        trial_end: float = None,
        trial_from_plan: bool = None,
        trial_period_days: float = None,
    ):
        self.billing = billing
        self.billing_cycle_anchor = billing_cycle_anchor
        self.cancel_at_period_end = cancel_at_period_end
        self.coupon = coupon
        self.customer = customer
        self.days_until_due = days_until_due
        self.metadata = metadata
        self.payment_fields = self._define_object(payment_fields, Payment)
        self.payment_method = PaymentMethod8Guard.return_one_of(payment_method)
        self.simultaneous_invoice = simultaneous_invoice
        self.subscription_items = self._define_list(
            subscription_items, SubscriptionItems1
        )
        self.tax_percent = tax_percent
        self.trial_end = trial_end
        self.trial_from_plan = trial_from_plan
        self.trial_period_days = trial_period_days
