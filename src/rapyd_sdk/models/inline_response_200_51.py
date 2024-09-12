from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payment_method_type import PaymentMethodType
from .status import Status


@JsonMap({})
class InlineResponse200_51(BaseModel):
    """InlineResponse200_51

    :param data: data, defaults to None
    :type data: List[PaymentMethodType], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[PaymentMethodType] = None, status: Status = None):
        """InlineResponse200_51

        :param data: data, defaults to None
        :type data: List[PaymentMethodType], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, PaymentMethodType)
        self.status = self._define_object(status, Status)
