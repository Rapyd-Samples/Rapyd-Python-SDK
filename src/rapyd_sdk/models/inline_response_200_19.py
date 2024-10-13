from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payout import Payout
from .status_1 import Status1


@JsonMap({})
class InlineResponse200_19(BaseModel):
    """InlineResponse200_19

    :param data: data, defaults to None
    :type data: Payout, optional
    :param status: status, defaults to None
    :type status: Status1, optional
    """

    def __init__(self, data: Payout = None, status: Status1 = None):
        """InlineResponse200_19

        :param data: data, defaults to None
        :type data: Payout, optional
        :param status: status, defaults to None
        :type status: Status1, optional
        """
        self.data = self._define_object(data, Payout)
        self.status = self._define_object(status, Status1)
