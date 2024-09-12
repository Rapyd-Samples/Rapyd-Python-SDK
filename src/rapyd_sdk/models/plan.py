from __future__ import annotations
from enum import Enum
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel
from .plan_tiers import PlanTiers
from .plan_transform_usage import PlanTransformUsage
from .product import Product


class AggregateUsage(Enum):
    """An enumeration representing different categories.

    :cvar MAX: "max"
    :vartype MAX: str
    :cvar SUM: "sum"
    :vartype SUM: str
    :cvar LASTDURINGPERIOD: "last_during_period"
    :vartype LASTDURINGPERIOD: str
    :cvar LASTEVER: "last_ever"
    :vartype LASTEVER: str
    """

    MAX = "max"
    SUM = "sum"
    LASTDURINGPERIOD = "last_during_period"
    LASTEVER = "last_ever"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AggregateUsage._member_map_.values()))


class BillingScheme(Enum):
    """An enumeration representing different categories.

    :cvar PERUNIT: "per_unit"
    :vartype PERUNIT: str
    :cvar TIERED: "tiered"
    :vartype TIERED: str
    """

    PERUNIT = "per_unit"
    TIERED = "tiered"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, BillingScheme._member_map_.values()))


class Interval(Enum):
    """An enumeration representing different categories.

    :cvar MONTH: "month"
    :vartype MONTH: str
    :cvar DAY: "day"
    :vartype DAY: str
    :cvar WEEK: "week"
    :vartype WEEK: str
    :cvar YEAR: "year"
    :vartype YEAR: str
    """

    MONTH = "month"
    DAY = "day"
    WEEK = "week"
    YEAR = "year"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Interval._member_map_.values()))


class PlanProductGuard(OneOfBaseModel):
    class_list = {"Product": Product, "str": str}


PlanProduct = Union[Product, str]


class TiersMode(Enum):
    """An enumeration representing different categories.

    :cvar GRADUATED: "graduated"
    :vartype GRADUATED: str
    :cvar VOLUME: "volume"
    :vartype VOLUME: str
    """

    GRADUATED = "graduated"
    VOLUME = "volume"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TiersMode._member_map_.values()))


class UsageType(Enum):
    """An enumeration representing different categories.

    :cvar METERED: "metered"
    :vartype METERED: str
    :cvar LICENSED: "licensed"
    :vartype LICENSED: str
    """

    METERED = "metered"
    LICENSED = "licensed"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, UsageType._member_map_.values()))


@JsonMap({"id_": "id"})
class Plan(BaseModel):
    """Plan

    :param aggregate_usage: Determines which quantity is used to calculate the pricing. One of the following:  * max - The maximum reported usage within the billing cycle.  * sum - The sum of all usage during a billing cycle. This is the default.  * last_during_period - The last usage reported within the billing cycle.  * last_ever - The last usage ever reported, if the latest billing cycles contain no usage at all. Required when usage_type is metered. Relevant when billing_scheme is set to per_unit. , defaults to None
    :type aggregate_usage: AggregateUsage, optional
    :param amount: The amount to charge, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal. For a free service, use 0. Must be null when tiers is set. Relevant when billing_scheme is set to per_unit., defaults to None
    :type amount: float, optional
    :param billing_scheme: Describes how to compute the price. One of the following:  * per_unit - The amount specified in amount is charged for each unit. Also set these related fields: amount, transform_usage, usage_type, aggregate_usage. This is the default.  * tiered - The unit pricing is computed using a tiering strategy as defined with the tiers and tiers_mode fields. , defaults to None
    :type billing_scheme: BillingScheme, optional
    :param created_at: Time the 'plan' object was created, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param id_: Unique ID for this plan. English alphanumeric characters with no special characters except underscore. If the client does not define an ID, Rapyd generates a string starting with plan_., defaults to None
    :type id_: str, optional
    :param interval: Specifies the units used in defining the billing cycle. One of the following:  * day  * week  * month  * year Maximum interval is 1 year.  , defaults to None
    :type interval: Interval, optional
    :param interval_count: Number of time intervals in the billing cycle. Integer, defaults to None
    :type interval_count: float, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param nickname: Brief description of the plan., defaults to None
    :type nickname: str, optional
    :param product: The ID of the product that this plan is for, and fields describing this product in the plan., defaults to None
    :type product: PlanProduct, optional
    :param tiers: Defines a tiered pricing structure. Each tier object represents a pricing tier., defaults to None
    :type tiers: List[PlanTiers], optional
    :param tiers_mode: Determines the mode for calculating the total tiered charge. One of the following values:  * graduated - The total cost at each price tier is calculated separately, then all tier charges are added together.  * volume - The total cost is calculated as the number of items times the applicable tier price. Relevant when billing_scheme is set to tiered , defaults to None
    :type tiers_mode: TiersMode, optional
    :param transform_usage: Defines the transformation that is applied to the reported usage before the billed price is computed. The transformation divides the quantity by the divisor specified in divide_by, then rounds up or down according to the setting in round. Relevant when billing_scheme is set to per_unit., defaults to None
    :type transform_usage: PlanTransformUsage, optional
    :param trial_period_days: Specifies the number of days before charges begin to accrue. Use this parameter to define a free trial period for a service., defaults to None
    :type trial_period_days: float, optional
    :param usage_type: Determines whether the customer is billed when the service is not actually used. Relevant when billing_scheme is set to per_unit. One of the following:  * metered - The customer is billed only for actual usage. You must also set aggregate_usage.  * licensed - The customer is billed even if the service is not used. This is the default. , defaults to None
    :type usage_type: UsageType, optional
    """

    def __init__(
        self,
        aggregate_usage: AggregateUsage = None,
        amount: float = None,
        billing_scheme: BillingScheme = None,
        created_at: float = None,
        currency: str = None,
        id_: str = None,
        interval: Interval = None,
        interval_count: float = None,
        metadata: dict = None,
        nickname: str = None,
        product: PlanProduct = None,
        tiers: List[PlanTiers] = None,
        tiers_mode: TiersMode = None,
        transform_usage: PlanTransformUsage = None,
        trial_period_days: float = None,
        usage_type: UsageType = None,
    ):
        """Plan

        :param aggregate_usage: Determines which quantity is used to calculate the pricing. One of the following:  * max - The maximum reported usage within the billing cycle.  * sum - The sum of all usage during a billing cycle. This is the default.  * last_during_period - The last usage reported within the billing cycle.  * last_ever - The last usage ever reported, if the latest billing cycles contain no usage at all. Required when usage_type is metered. Relevant when billing_scheme is set to per_unit. , defaults to None
        :type aggregate_usage: AggregateUsage, optional
        :param amount: The amount to charge, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal. For a free service, use 0. Must be null when tiers is set. Relevant when billing_scheme is set to per_unit., defaults to None
        :type amount: float, optional
        :param billing_scheme: Describes how to compute the price. One of the following:  * per_unit - The amount specified in amount is charged for each unit. Also set these related fields: amount, transform_usage, usage_type, aggregate_usage. This is the default.  * tiered - The unit pricing is computed using a tiering strategy as defined with the tiers and tiers_mode fields. , defaults to None
        :type billing_scheme: BillingScheme, optional
        :param created_at: Time the 'plan' object was created, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param id_: Unique ID for this plan. English alphanumeric characters with no special characters except underscore. If the client does not define an ID, Rapyd generates a string starting with plan_., defaults to None
        :type id_: str, optional
        :param interval: Specifies the units used in defining the billing cycle. One of the following:  * day  * week  * month  * year Maximum interval is 1 year.  , defaults to None
        :type interval: Interval, optional
        :param interval_count: Number of time intervals in the billing cycle. Integer, defaults to None
        :type interval_count: float, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param nickname: Brief description of the plan., defaults to None
        :type nickname: str, optional
        :param product: The ID of the product that this plan is for, and fields describing this product in the plan., defaults to None
        :type product: PlanProduct, optional
        :param tiers: Defines a tiered pricing structure. Each tier object represents a pricing tier., defaults to None
        :type tiers: List[PlanTiers], optional
        :param tiers_mode: Determines the mode for calculating the total tiered charge. One of the following values:  * graduated - The total cost at each price tier is calculated separately, then all tier charges are added together.  * volume - The total cost is calculated as the number of items times the applicable tier price. Relevant when billing_scheme is set to tiered , defaults to None
        :type tiers_mode: TiersMode, optional
        :param transform_usage: Defines the transformation that is applied to the reported usage before the billed price is computed. The transformation divides the quantity by the divisor specified in divide_by, then rounds up or down according to the setting in round. Relevant when billing_scheme is set to per_unit., defaults to None
        :type transform_usage: PlanTransformUsage, optional
        :param trial_period_days: Specifies the number of days before charges begin to accrue. Use this parameter to define a free trial period for a service., defaults to None
        :type trial_period_days: float, optional
        :param usage_type: Determines whether the customer is billed when the service is not actually used. Relevant when billing_scheme is set to per_unit. One of the following:  * metered - The customer is billed only for actual usage. You must also set aggregate_usage.  * licensed - The customer is billed even if the service is not used. This is the default. , defaults to None
        :type usage_type: UsageType, optional
        """
        self.aggregate_usage = (
            self._enum_matching(
                aggregate_usage, AggregateUsage.list(), "aggregate_usage"
            )
            if aggregate_usage
            else None
        )
        self.amount = self._define_number("amount", amount, nullable=True)
        self.billing_scheme = (
            self._enum_matching(billing_scheme, BillingScheme.list(), "billing_scheme")
            if billing_scheme
            else None
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.interval = (
            self._enum_matching(interval, Interval.list(), "interval")
            if interval
            else None
        )
        self.interval_count = self._define_number(
            "interval_count", interval_count, nullable=True
        )
        self.metadata = metadata
        self.nickname = self._define_str("nickname", nickname, nullable=True)
        self.product = PlanProductGuard.return_one_of(product)
        self.tiers = self._define_list(tiers, PlanTiers)
        self.tiers_mode = (
            self._enum_matching(tiers_mode, TiersMode.list(), "tiers_mode")
            if tiers_mode
            else None
        )
        self.transform_usage = self._define_object(transform_usage, PlanTransformUsage)
        self.trial_period_days = self._define_number(
            "trial_period_days", trial_period_days, nullable=True
        )
        self.usage_type = (
            self._enum_matching(usage_type, UsageType.list(), "usage_type")
            if usage_type
            else None
        )
