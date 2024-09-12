from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payment import Payment
from .status import Status


@JsonMap({})
class InlineResponse200_53(BaseModel):
    """InlineResponse200_53

    :param data: data, defaults to None
    :type data: List[Payment], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Payment] = None, status: Status = None):
        """InlineResponse200_53

        :param data: data, defaults to None
        :type data: List[Payment], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Payment)
        self.status = self._define_object(status, Status)
