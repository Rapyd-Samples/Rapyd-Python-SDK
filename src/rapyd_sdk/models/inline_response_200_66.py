from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .subscription_item import SubscriptionItem
from .status import Status


@JsonMap({})
class InlineResponse200_66(BaseModel):
    """InlineResponse200_66

    :param data: data, defaults to None
    :type data: List[SubscriptionItem], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[SubscriptionItem] = None, status: Status = None):
        """InlineResponse200_66

        :param data: data, defaults to None
        :type data: List[SubscriptionItem], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, SubscriptionItem)
        self.status = self._define_object(status, Status)
