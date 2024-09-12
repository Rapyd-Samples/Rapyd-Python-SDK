from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .customer_payment_method import CustomerPaymentMethod
from .status import Status


@JsonMap({})
class InlineResponse200_37(BaseModel):
    """InlineResponse200_37

    :param data: data, defaults to None
    :type data: List[CustomerPaymentMethod], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[CustomerPaymentMethod] = None, status: Status = None):
        """InlineResponse200_37

        :param data: data, defaults to None
        :type data: List[CustomerPaymentMethod], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, CustomerPaymentMethod)
        self.status = self._define_object(status, Status)
