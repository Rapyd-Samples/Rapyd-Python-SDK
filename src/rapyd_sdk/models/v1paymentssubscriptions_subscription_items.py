from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class V1paymentssubscriptionsSubscriptionItems(BaseModel):
    """V1paymentssubscriptionsSubscriptionItems

    :param plan: ID of the plan assigned to this subscription item., defaults to None
    :type plan: str, optional
    :param quantity: quantity, defaults to None
    :type quantity: float, optional
    """

    def __init__(self, plan: str = None, quantity: float = None):
        """V1paymentssubscriptionsSubscriptionItems

        :param plan: ID of the plan assigned to this subscription item., defaults to None
        :type plan: str, optional
        :param quantity: quantity, defaults to None
        :type quantity: float, optional
        """
        self.plan = self._define_str("plan", plan, nullable=True)
        self.quantity = self._define_number("quantity", quantity, nullable=True)
