from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .coupon import Coupon
from .status import Status


@JsonMap({})
class InlineResponse200_29(BaseModel):
    """InlineResponse200_29

    :param data: data, defaults to None
    :type data: List[Coupon], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Coupon] = None, status: Status = None):
        """InlineResponse200_29

        :param data: data, defaults to None
        :type data: List[Coupon], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Coupon)
        self.status = self._define_object(status, Status)
