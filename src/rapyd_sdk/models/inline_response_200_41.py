from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .dispute import Dispute
from .status import Status


@JsonMap({})
class InlineResponse200_41(BaseModel):
    """InlineResponse200_41

    :param data: data, defaults to None
    :type data: List[Dispute], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Dispute] = None, status: Status = None):
        """InlineResponse200_41

        :param data: data, defaults to None
        :type data: List[Dispute], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Dispute)
        self.status = self._define_object(status, Status)
