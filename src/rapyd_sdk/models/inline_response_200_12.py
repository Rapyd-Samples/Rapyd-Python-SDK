from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payout import Payout
from .status import Status


@JsonMap({})
class InlineResponse200_12(BaseModel):
    """InlineResponse200_12

    :param data: data, defaults to None
    :type data: Payout, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Payout = None, status: Status = None):
        """InlineResponse200_12

        :param data: data, defaults to None
        :type data: Payout, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Payout)
        self.status = self._define_object(status, Status)
