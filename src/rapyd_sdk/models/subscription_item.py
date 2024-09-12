from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .plan import Plan


@JsonMap({"id_": "id"})
class SubscriptionItem(BaseModel):
    """SubscriptionItem

    :param created: The time the subscription item was created, in Unix time. Response only., defaults to None
    :type created: float, optional
    :param id_: ID of the Subscription Item object. String starting with subi_., defaults to None
    :type id_: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param plan: plan, defaults to None
    :type plan: Plan, optional
    :param quantity: The number of units of the service defined in the plan. Integer. This number can be updated during the billing cycle using Update Subscription or Update Subscription Item., defaults to None
    :type quantity: float, optional
    :param subscription_id: ID of the subscription that this item belongs to. String starting with sub_., defaults to None
    :type subscription_id: str, optional
    """

    def __init__(
        self,
        created: float = None,
        id_: str = None,
        metadata: dict = None,
        plan: Plan = None,
        quantity: float = None,
        subscription_id: str = None,
    ):
        """SubscriptionItem

        :param created: The time the subscription item was created, in Unix time. Response only., defaults to None
        :type created: float, optional
        :param id_: ID of the Subscription Item object. String starting with subi_., defaults to None
        :type id_: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param plan: plan, defaults to None
        :type plan: Plan, optional
        :param quantity: The number of units of the service defined in the plan. Integer. This number can be updated during the billing cycle using Update Subscription or Update Subscription Item., defaults to None
        :type quantity: float, optional
        :param subscription_id: ID of the subscription that this item belongs to. String starting with sub_., defaults to None
        :type subscription_id: str, optional
        """
        self.created = self._define_number("created", created, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.metadata = metadata
        self.plan = self._define_object(plan, Plan)
        self.quantity = self._define_number("quantity", quantity, nullable=True)
        self.subscription_id = self._define_str(
            "subscription_id", subscription_id, nullable=True
        )
