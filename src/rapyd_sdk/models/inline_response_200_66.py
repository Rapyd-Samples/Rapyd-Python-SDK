from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .subscription import Subscription


@JsonMap({})
class InlineResponse200_66(BaseModel):
    """InlineResponse200_66

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: Subscription, optional
    """

    def __init__(self, status: Status1 = None, data: Subscription = None):
        """InlineResponse200_66

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: Subscription, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, Subscription)
