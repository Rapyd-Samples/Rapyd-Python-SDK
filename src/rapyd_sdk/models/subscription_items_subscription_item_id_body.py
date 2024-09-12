from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class SubscriptionItemsSubscriptionItemIdBody(BaseModel):
    """SubscriptionItemsSubscriptionItemIdBody

    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param prorate: Determines whether the charge is prorated when a subscription item is switched from one subscription to another in a billing cycle., defaults to None
    :type prorate: bool, optional
    :param proration_date: Indicates the date in the middle of the billing period that is the start of the prorated charges., defaults to None
    :type proration_date: float, optional
    :param quantity: The number of units of the service defined in the plan., defaults to None
    :type quantity: float, optional
    """

    def __init__(
        self,
        metadata: dict = None,
        prorate: bool = None,
        proration_date: float = None,
        quantity: float = None,
    ):
        """SubscriptionItemsSubscriptionItemIdBody

        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param prorate: Determines whether the charge is prorated when a subscription item is switched from one subscription to another in a billing cycle., defaults to None
        :type prorate: bool, optional
        :param proration_date: Indicates the date in the middle of the billing period that is the start of the prorated charges., defaults to None
        :type proration_date: float, optional
        :param quantity: The number of units of the service defined in the plan., defaults to None
        :type quantity: float, optional
        """
        self.metadata = metadata
        self.prorate = prorate
        self.proration_date = self._define_number(
            "proration_date", proration_date, nullable=True
        )
        self.quantity = self._define_number("quantity", quantity, nullable=True)
