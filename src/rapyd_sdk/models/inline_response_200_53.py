from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .invoice_response import InvoiceResponse


@JsonMap({})
class InlineResponse200_53(BaseModel):
    """InlineResponse200_53

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: Invoice, defaults to None
    :type data: InvoiceResponse, optional
    """

    def __init__(self, status: Status1 = None, data: InvoiceResponse = None):
        """InlineResponse200_53

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: Invoice, defaults to None
        :type data: InvoiceResponse, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, InvoiceResponse)
