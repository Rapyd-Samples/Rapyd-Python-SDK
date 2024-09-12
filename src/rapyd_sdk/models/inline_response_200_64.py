from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .refund import Refund
from .status import Status


@JsonMap({})
class InlineResponse200_64(BaseModel):
    """InlineResponse200_64

    :param data: data, defaults to None
    :type data: Refund, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Refund = None, status: Status = None):
        """InlineResponse200_64

        :param data: data, defaults to None
        :type data: Refund, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Refund)
        self.status = self._define_object(status, Status)
