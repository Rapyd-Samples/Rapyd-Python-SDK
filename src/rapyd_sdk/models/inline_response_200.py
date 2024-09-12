from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .transfer import Transfer
from .status import Status


@JsonMap({})
class InlineResponse200(BaseModel):
    """InlineResponse200

    :param data: data, defaults to None
    :type data: Transfer, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Transfer = None, status: Status = None):
        """InlineResponse200

        :param data: data, defaults to None
        :type data: Transfer, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Transfer)
        self.status = self._define_object(status, Status)
