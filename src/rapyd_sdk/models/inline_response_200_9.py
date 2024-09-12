from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .virtual_account_transaction_response import VirtualAccountTransactionResponse
from .status import Status


@JsonMap({})
class InlineResponse200_9(BaseModel):
    """InlineResponse200_9

    :param data: data, defaults to None
    :type data: VirtualAccountTransactionResponse, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(
        self, data: VirtualAccountTransactionResponse = None, status: Status = None
    ):
        """InlineResponse200_9

        :param data: data, defaults to None
        :type data: VirtualAccountTransactionResponse, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, VirtualAccountTransactionResponse)
        self.status = self._define_object(status, Status)
