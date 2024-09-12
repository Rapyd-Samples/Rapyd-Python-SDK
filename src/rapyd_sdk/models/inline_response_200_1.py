from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .contact import Contact
from .status import Status


@JsonMap({})
class InlineResponse200_1(BaseModel):
    """InlineResponse200_1

    :param data: data, defaults to None
    :type data: List[Contact], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Contact] = None, status: Status = None):
        """InlineResponse200_1

        :param data: data, defaults to None
        :type data: List[Contact], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Contact)
        self.status = self._define_object(status, Status)
