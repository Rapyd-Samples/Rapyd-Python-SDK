from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .ewallet_transaction import EwalletTransaction
from .status import Status


@JsonMap({})
class InlineResponse200_26(BaseModel):
    """InlineResponse200_26

    :param data: data, defaults to None
    :type data: List[EwalletTransaction], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[EwalletTransaction] = None, status: Status = None):
        """InlineResponse200_26

        :param data: data, defaults to None
        :type data: List[EwalletTransaction], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, EwalletTransaction)
        self.status = self._define_object(status, Status)
