from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payout_method_type import PayoutMethodType
from .status import Status


@JsonMap({})
class InlineResponse200_18(BaseModel):
    """InlineResponse200_18

    :param data: data, defaults to None
    :type data: List[PayoutMethodType], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[PayoutMethodType] = None, status: Status = None):
        """InlineResponse200_18

        :param data: data, defaults to None
        :type data: List[PayoutMethodType], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, PayoutMethodType)
        self.status = self._define_object(status, Status)
