from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .account import Account


@JsonMap({})
class InlineResponse200_25(BaseModel):
    """InlineResponse200_25

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: data, defaults to None
    :type data: Account, optional
    """

    def __init__(self, status: Status = None, data: Account = None):
        """InlineResponse200_25

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: data, defaults to None
        :type data: Account, optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, Account)
