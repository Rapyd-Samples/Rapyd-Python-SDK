from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .sku import Sku


@JsonMap({})
class InlineResponse200_74(BaseModel):
    """InlineResponse200_74

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: data, defaults to None
    :type data: List[Sku], optional
    """

    def __init__(self, status: Status = None, data: List[Sku] = None):
        """InlineResponse200_74

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: data, defaults to None
        :type data: List[Sku], optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_list(data, Sku)
