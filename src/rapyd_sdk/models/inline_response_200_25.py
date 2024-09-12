from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .ewallet_transaction_details import (
    EwalletTransactionDetails,
    EwalletTransactionDetailsGuard,
)
from .ewallet_transaction import EwalletTransaction
from .status import Status


@JsonMap({})
class InlineResponse200_25(BaseModel):
    """InlineResponse200_25

    :param data: data, defaults to None
    :type data: List[EwalletTransactionDetails], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(
        self, data: List[EwalletTransactionDetails] = None, status: Status = None
    ):
        """InlineResponse200_25

        :param data: data, defaults to None
        :type data: List[EwalletTransactionDetails], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, EwalletTransactionDetails)
        self.status = self._define_object(status, Status)
