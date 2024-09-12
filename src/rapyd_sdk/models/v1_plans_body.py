from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class V1PlansBody(BaseModel):
    """V1PlansBody

    :param aggregate_usage: Determines which quantity is used to calculate the pricing. Relevant when usage_type is metered. Default is sum., defaults to None
    :type aggregate_usage: str, optional
    :param amount: The amount to charge in the billing cycle. For a free service, use 0. Relevant when billing_scheme is set to per_unit. When the billing_scheme is set to tiered, set the amount in the tiers array., defaults to None
    :type amount: float, optional
    :param billing_scheme: Describes how to compute the price per billing period. One of the following values - per_unit, tiered, defaults to None
    :type billing_scheme: str, optional
    :param currency: Three-letter ISO 4217 code for the currency used in fields that represent monetary amounts. Uppercase.
    :type currency: str
    :param id_: Unique ID for this payment plan. English alphanumeric characters and underscore. Limited to 44 characters. If the merchant does not define an ID, Rapyd generates a string starting with plan_., defaults to None
    :type id_: str, optional
    :param interval: Specifies the units used in defining the billing cycle.
    :type interval: str
    :param interval_count: Number of intervals in the billing cycle. Default is 1., defaults to None
    :type interval_count: float, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param nickname: Brief description of the pricing plan., defaults to None
    :type nickname: str, optional
    :param product: ID of the 'product' object that this plan is for. The product must have type set to service.
    :type product: str
    :param tiers: Defines a tiered pricing structure. Array of objects. Must be null when billing_scheme is set to per_unit., defaults to None
    :type tiers: str, optional
    :param tiers_mode: Determines the mode for calculating the total tiered charge., defaults to None
    :type tiers_mode: str, optional
    :param transform_usage: Defines the transformation that is applied to the reported usage before the billed price is computed., defaults to None
    :type transform_usage: dict, optional
    :param trial_period_days: Specifies the number of days before charges begin to accrue. Use this parameter to define a free trial period for a service., defaults to None
    :type trial_period_days: float, optional
    :param usage_type: Determines whether the customer is billed when the service is not actually used. One of the following values - metered, licensed, defaults to None
    :type usage_type: str, optional
    """

    def __init__(
        self,
        currency: str,
        interval: str,
        product: str,
        aggregate_usage: str = None,
        amount: float = None,
        billing_scheme: str = None,
        id_: str = None,
        interval_count: float = None,
        metadata: dict = None,
        nickname: str = None,
        tiers: str = None,
        tiers_mode: str = None,
        transform_usage: dict = None,
        trial_period_days: float = None,
        usage_type: str = None,
    ):
        """V1PlansBody

        :param aggregate_usage: Determines which quantity is used to calculate the pricing. Relevant when usage_type is metered. Default is sum., defaults to None
        :type aggregate_usage: str, optional
        :param amount: The amount to charge in the billing cycle. For a free service, use 0. Relevant when billing_scheme is set to per_unit. When the billing_scheme is set to tiered, set the amount in the tiers array., defaults to None
        :type amount: float, optional
        :param billing_scheme: Describes how to compute the price per billing period. One of the following values - per_unit, tiered, defaults to None
        :type billing_scheme: str, optional
        :param currency: Three-letter ISO 4217 code for the currency used in fields that represent monetary amounts. Uppercase.
        :type currency: str
        :param id_: Unique ID for this payment plan. English alphanumeric characters and underscore. Limited to 44 characters. If the merchant does not define an ID, Rapyd generates a string starting with plan_., defaults to None
        :type id_: str, optional
        :param interval: Specifies the units used in defining the billing cycle.
        :type interval: str
        :param interval_count: Number of intervals in the billing cycle. Default is 1., defaults to None
        :type interval_count: float, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param nickname: Brief description of the pricing plan., defaults to None
        :type nickname: str, optional
        :param product: ID of the 'product' object that this plan is for. The product must have type set to service.
        :type product: str
        :param tiers: Defines a tiered pricing structure. Array of objects. Must be null when billing_scheme is set to per_unit., defaults to None
        :type tiers: str, optional
        :param tiers_mode: Determines the mode for calculating the total tiered charge., defaults to None
        :type tiers_mode: str, optional
        :param transform_usage: Defines the transformation that is applied to the reported usage before the billed price is computed., defaults to None
        :type transform_usage: dict, optional
        :param trial_period_days: Specifies the number of days before charges begin to accrue. Use this parameter to define a free trial period for a service., defaults to None
        :type trial_period_days: float, optional
        :param usage_type: Determines whether the customer is billed when the service is not actually used. One of the following values - metered, licensed, defaults to None
        :type usage_type: str, optional
        """
        self.aggregate_usage = self._define_str(
            "aggregate_usage", aggregate_usage, nullable=True
        )
        self.amount = self._define_number("amount", amount, nullable=True)
        self.billing_scheme = self._define_str(
            "billing_scheme", billing_scheme, nullable=True
        )
        self.currency = currency
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.interval = interval
        self.interval_count = self._define_number(
            "interval_count", interval_count, nullable=True
        )
        self.metadata = metadata
        self.nickname = self._define_str("nickname", nickname, nullable=True)
        self.product = product
        self.tiers = self._define_str("tiers", tiers, nullable=True)
        self.tiers_mode = self._define_str("tiers_mode", tiers_mode, nullable=True)
        self.transform_usage = transform_usage
        self.trial_period_days = self._define_number(
            "trial_period_days", trial_period_days, nullable=True
        )
        self.usage_type = self._define_str("usage_type", usage_type, nullable=True)
