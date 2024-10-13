from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .coupon import Coupon


@JsonMap({})
class InlineResponse200_35(BaseModel):
    """InlineResponse200_35

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: List[Coupon], optional
    """

    def __init__(self, status: Status1 = None, data: List[Coupon] = None):
        """InlineResponse200_35

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: List[Coupon], optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_list(data, Coupon)
