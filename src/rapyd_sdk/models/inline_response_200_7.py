from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .virtual_account_issuing import VirtualAccountIssuing
from .status_1 import Status1


@JsonMap({})
class InlineResponse200_7(BaseModel):
    """InlineResponse200_7

    :param data: data, defaults to None
    :type data: VirtualAccountIssuing, optional
    :param status: status, defaults to None
    :type status: Status1, optional
    """

    def __init__(self, data: VirtualAccountIssuing = None, status: Status1 = None):
        """InlineResponse200_7

        :param data: data, defaults to None
        :type data: VirtualAccountIssuing, optional
        :param status: status, defaults to None
        :type status: Status1, optional
        """
        self.data = self._define_object(data, VirtualAccountIssuing)
        self.status = self._define_object(status, Status1)
