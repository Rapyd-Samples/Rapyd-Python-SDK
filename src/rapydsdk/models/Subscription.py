from __future__ import annotations
from enum import Enum
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .SubscriptionDiscount import SubscriptionDiscount
from .SubscriptionItems import SubscriptionItems
from .SubscriptionRetryOptions import SubscriptionRetryOptions


class BillingCycleAnchorGuard(OneOfBaseModel):
    class_list = {"str": str, "float": float}


BillingCycleAnchor = Union[str, float]


class Status3(Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    PAST_DUE = "past_due"
    TRIALING = "trialing"
    UNPAID = "unpaid"

    def list():
        return list(map(lambda x: x.value, Status3._member_map_.values()))


class Type1(Enum):
    PAYOUT = "payout"
    PAYMENT = "payment"

    def list():
        return list(map(lambda x: x.value, Type1._member_map_.values()))


@JsonMap({"type_": "type"})
class Subscription(BaseModel):
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
        discount: SubscriptionDiscount = None,
        ended_at: float = None,
        id: str = None,
        metadata: dict = None,
        payment_fields: dict = None,
        payment_method: str = None,
        payout_fields: dict = None,
        simultaneous_invoice: bool = None,
        status: Status3 = None,
        subscription_items: SubscriptionItems = None,
        tax_percent: float = None,
        trial_end: float = None,
        trial_start: float = None,
        type_: Type1 = None,
        enable_retries: bool = None,
        retry_options: SubscriptionRetryOptions = None,
    ):
        self.billing = billing
        self.billing_cycle_anchor = BillingCycleAnchorGuard.return_one_of(
            billing_cycle_anchor
        )
        self.cancel_at_period_end = cancel_at_period_end
        self.canceled_at = canceled_at
        self.created_at = created_at
        self.current_period_end = current_period_end
        self.current_period_start = current_period_start
        self.customer_token = customer_token
        self.days_until_due = days_until_due
        self.discount = self._define_object(discount, SubscriptionDiscount)
        self.ended_at = ended_at
        self.id = id
        self.metadata = metadata
        self.payment_fields = payment_fields
        self.payment_method = payment_method
        self.payout_fields = payout_fields
        self.simultaneous_invoice = simultaneous_invoice
        self.status = (
            self._enum_matching(status, Status3.list(), "status") if status else None
        )
        self.subscription_items = self._define_object(
            subscription_items, SubscriptionItems
        )
        self.tax_percent = tax_percent
        self.trial_end = trial_end
        self.trial_start = trial_start
        self.type_ = (
            self._enum_matching(type_, Type1.list(), "type_") if type_ else None
        )
        self.enable_retries = enable_retries
        self.retry_options = self._define_object(
            retry_options, SubscriptionRetryOptions
        )
