from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .ewallet_transaction_details import (
    EwalletTransactionDetails,
    EwalletTransactionDetailsGuard,
)
from .ewallet_transaction import EwalletTransaction
from .status import Status


@JsonMap({})
class InlineResponse200_26(BaseModel):
    """InlineResponse200_26

    :param data: data, defaults to None
    :type data: EwalletTransactionDetails, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: EwalletTransactionDetails = None, status: Status = None):
        """InlineResponse200_26

        :param data: data, defaults to None
        :type data: EwalletTransactionDetails, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = EwalletTransactionDetailsGuard.return_one_of(data)
        self.status = self._define_object(status, Status)
