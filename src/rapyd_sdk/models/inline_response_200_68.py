from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .subscription import Subscription
from .status_1 import Status1


@JsonMap({})
class InlineResponse200_68(BaseModel):
    """InlineResponse200_68

    :param data: data, defaults to None
    :type data: Subscription, optional
    :param status: status, defaults to None
    :type status: Status1, optional
    """

    def __init__(self, data: Subscription = None, status: Status1 = None):
        """InlineResponse200_68

        :param data: data, defaults to None
        :type data: Subscription, optional
        :param status: status, defaults to None
        :type status: Status1, optional
        """
        self.data = self._define_object(data, Subscription)
        self.status = self._define_object(status, Status1)
