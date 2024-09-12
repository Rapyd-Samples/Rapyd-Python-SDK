from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payout import Payout
from .status import Status


@JsonMap({})
class InlineResponse200_11(BaseModel):
    """InlineResponse200_11

    :param data: data, defaults to None
    :type data: List[Payout], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Payout] = None, status: Status = None):
        """InlineResponse200_11

        :param data: data, defaults to None
        :type data: List[Payout], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Payout)
        self.status = self._define_object(status, Status)
