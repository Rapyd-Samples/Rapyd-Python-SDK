from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .escrow_response import EscrowResponse


@JsonMap({})
class InlineResponse200_49(BaseModel):
    """InlineResponse200_49

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: EscrowResponse, optional
    """

    def __init__(self, status: Status1 = None, data: EscrowResponse = None):
        """InlineResponse200_49

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: EscrowResponse, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, EscrowResponse)
