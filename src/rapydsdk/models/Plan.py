from __future__ import annotations
from enum import Enum
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Product import Product


class AggregateUsage(Enum):
    MAX = "max"
    SUM = "sum"
    LAST_DURING_PERIOD = "last_during_period"
    LAST_EVER = "last_ever"

    def list():
        return list(map(lambda x: x.value, AggregateUsage._member_map_.values()))


class BillingScheme(Enum):
    PER_UNIT = "per_unit"
    TIERED = "tiered"

    def list():
        return list(map(lambda x: x.value, BillingScheme._member_map_.values()))


class Interval(Enum):
    MONTH = "month"
    DAY = "day"
    WEEK = "week"
    YEAR = "year"

    def list():
        return list(map(lambda x: x.value, Interval._member_map_.values()))


class Product1Guard(OneOfBaseModel):
    class_list = {"Product": Product, "str": str}


Product1 = Union[Product, str]


class UpToGuard(OneOfBaseModel):
    class_list = {"str": str, "float": float}


UpTo = Union[str, float]


@JsonMap({})
class Tiers(BaseModel):
    def __init__(
        self, amount: float = None, flat_amount: float = None, up_to: UpTo = None
    ):
        self.amount = amount
        self.flat_amount = flat_amount
        self.up_to = UpToGuard.return_one_of(up_to)


class TiersMode(Enum):
    GRADUATED = "graduated"
    VOLUME = "volume"

    def list():
        return list(map(lambda x: x.value, TiersMode._member_map_.values()))


@JsonMap({})
class TransformUsage(BaseModel):
    def __init__(self, divide_by: float = None, round: str = None):
        self.divide_by = divide_by
        self.round = round


class UsageType(Enum):
    METERED = "metered"
    LICENSED = "licensed"

    def list():
        return list(map(lambda x: x.value, UsageType._member_map_.values()))


@JsonMap({})
class Plan(BaseModel):
    def __init__(
        self,
        active: bool = None,
        aggregate_usage: AggregateUsage = None,
        amount: float = None,
        billing_scheme: BillingScheme = None,
        created_at: float = None,
        currency: str = None,
        id: str = None,
        interval: Interval = None,
        interval_count: float = None,
        metadata: dict = None,
        nickname: str = None,
        product: Product1 = None,
        tiers: List[Tiers] = None,
        tiers_mode: TiersMode = None,
        transform_usage: TransformUsage = None,
        trial_period_days: float = None,
        usage_type: UsageType = None,
    ):
        self.active = active
        self.aggregate_usage = (
            self._enum_matching(
                aggregate_usage, AggregateUsage.list(), "aggregate_usage"
            )
            if aggregate_usage
            else None
        )
        self.amount = amount
        self.billing_scheme = (
            self._enum_matching(billing_scheme, BillingScheme.list(), "billing_scheme")
            if billing_scheme
            else None
        )
        self.created_at = created_at
        self.currency = (
            self._pattern_matching(
                currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "currency",
            )
            if currency
            else None
        )
        self.id = id
        self.interval = (
            self._enum_matching(interval, Interval.list(), "interval")
            if interval
            else None
        )
        self.interval_count = interval_count
        self.metadata = metadata
        self.nickname = nickname
        self.product = Product1Guard.return_one_of(product)
        self.tiers = self._define_list(tiers, Tiers)
        self.tiers_mode = (
            self._enum_matching(tiers_mode, TiersMode.list(), "tiers_mode")
            if tiers_mode
            else None
        )
        self.transform_usage = self._define_object(transform_usage, TransformUsage)
        self.trial_period_days = trial_period_days
        self.usage_type = (
            self._enum_matching(usage_type, UsageType.list(), "usage_type")
            if usage_type
            else None
        )
