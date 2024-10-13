from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class V1SubscriptionItemsBody(BaseModel):
    """V1SubscriptionItemsBody

    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param plan: ID of the plan assigned to this subscription item. Cannot be a plan that is already part of the subscription.
    :type plan: str
    :param prorate: Determines whether the charge is prorated when a subscription item is switched from one subscription to another in a billing cycle., defaults to None
    :type prorate: bool, optional
    :param proration_date: Indicates the date in the middle of the billing period that is the start of the prorated charges., defaults to None
    :type proration_date: float, optional
    :param quantity: The number of units of the service defined in the plan., defaults to None
    :type quantity: float, optional
    :param subscription: ID of the subscription that this item belongs to. String starting with **sub_**.
    :type subscription: str
    """

    def __init__(
        self,
        plan: str,
        subscription: str,
        metadata: dict = None,
        prorate: bool = None,
        proration_date: float = None,
        quantity: float = None,
    ):
        """V1SubscriptionItemsBody

        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param plan: ID of the plan assigned to this subscription item. Cannot be a plan that is already part of the subscription.
        :type plan: str
        :param prorate: Determines whether the charge is prorated when a subscription item is switched from one subscription to another in a billing cycle., defaults to None
        :type prorate: bool, optional
        :param proration_date: Indicates the date in the middle of the billing period that is the start of the prorated charges., defaults to None
        :type proration_date: float, optional
        :param quantity: The number of units of the service defined in the plan., defaults to None
        :type quantity: float, optional
        :param subscription: ID of the subscription that this item belongs to. String starting with **sub_**.
        :type subscription: str
        """
        self.metadata = metadata
        self.plan = plan
        self.prorate = prorate
        self.proration_date = self._define_number(
            "proration_date", proration_date, nullable=True
        )
        self.quantity = self._define_number("quantity", quantity, nullable=True)
        self.subscription = subscription
