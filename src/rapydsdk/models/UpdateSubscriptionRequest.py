from __future__ import annotations
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .PaymentFields import PaymentFields
from .PaymentMethodType import PaymentMethodType


class PaymentMethod9Guard(OneOfBaseModel):
    class_list = {"str": str, "PaymentMethodType": PaymentMethodType}


PaymentMethod9 = Union[str, PaymentMethodType]


@JsonMap({})
class UpdateSubscriptionRequest(BaseModel):
    def __init__(
        self,
        billing: str = None,
        billing_cycle_anchor: str = None,
        cancel_at_period_end: bool = None,
        coupon: str = None,
        days_until_due: float = None,
        metadata: dict = None,
        payment_fields: PaymentFields = None,
        payment_method: PaymentMethod9 = None,
        simultaneous_invoice: bool = None,
        subscription_items: List[str] = None,
        tax_percent: float = None,
        trial_end: float = None,
        trial_from_plan: bool = None,
        trial_period_days: float = None,
    ):
        self.billing = billing
        self.billing_cycle_anchor = billing_cycle_anchor
        self.cancel_at_period_end = cancel_at_period_end
        self.coupon = coupon
        self.days_until_due = days_until_due
        self.metadata = metadata
        self.payment_fields = self._define_object(payment_fields, PaymentFields)
        self.payment_method = PaymentMethod9Guard.return_one_of(payment_method)
        self.simultaneous_invoice = simultaneous_invoice
        self.subscription_items = subscription_items
        self.tax_percent = tax_percent
        self.trial_end = trial_end
        self.trial_from_plan = trial_from_plan
        self.trial_period_days = trial_period_days
