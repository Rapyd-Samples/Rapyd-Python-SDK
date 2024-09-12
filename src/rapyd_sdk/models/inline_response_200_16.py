from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .sender import Sender
from .status import Status


@JsonMap({})
class InlineResponse200_16(BaseModel):
    """InlineResponse200_16

    :param data: data, defaults to None
    :type data: Sender, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Sender = None, status: Status = None):
        """InlineResponse200_16

        :param data: data, defaults to None
        :type data: Sender, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Sender)
        self.status = self._define_object(status, Status)
