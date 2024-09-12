from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .subscription import Subscription
from .status import Status


@JsonMap({})
class InlineResponse200_55(BaseModel):
    """InlineResponse200_55

    :param data: data, defaults to None
    :type data: List[Subscription], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Subscription] = None, status: Status = None):
        """InlineResponse200_55

        :param data: data, defaults to None
        :type data: List[Subscription], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Subscription)
        self.status = self._define_object(status, Status)
