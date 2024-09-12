from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account import Account
from .status import Status


@JsonMap({})
class InlineResponse200_23(BaseModel):
    """InlineResponse200_23

    :param data: data, defaults to None
    :type data: List[Account], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Account] = None, status: Status = None):
        """InlineResponse200_23

        :param data: data, defaults to None
        :type data: List[Account], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Account)
        self.status = self._define_object(status, Status)
