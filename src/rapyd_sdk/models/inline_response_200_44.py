from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .invoice_response import InvoiceResponse
from .status import Status


@JsonMap({})
class InlineResponse200_44(BaseModel):
    """InlineResponse200_44

    :param data: Invoice, defaults to None
    :type data: InvoiceResponse, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: InvoiceResponse = None, status: Status = None):
        """InlineResponse200_44

        :param data: Invoice, defaults to None
        :type data: InvoiceResponse, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, InvoiceResponse)
        self.status = self._define_object(status, Status)
