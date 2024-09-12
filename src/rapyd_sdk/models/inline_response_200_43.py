from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .invoice_response import InvoiceResponse
from .status import Status


@JsonMap({})
class InlineResponse200_43(BaseModel):
    """InlineResponse200_43

    :param data: data, defaults to None
    :type data: List[InvoiceResponse], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[InvoiceResponse] = None, status: Status = None):
        """InlineResponse200_43

        :param data: data, defaults to None
        :type data: List[InvoiceResponse], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, InvoiceResponse)
        self.status = self._define_object(status, Status)
