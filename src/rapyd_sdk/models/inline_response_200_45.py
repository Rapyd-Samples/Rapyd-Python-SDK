from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .invoice_response import InvoiceResponse


@JsonMap({})
class InlineResponse200_45(BaseModel):
    """InlineResponse200_45

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: Invoice, defaults to None
    :type data: InvoiceResponse, optional
    """

    def __init__(self, status: Status = None, data: InvoiceResponse = None):
        """InlineResponse200_45

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: Invoice, defaults to None
        :type data: InvoiceResponse, optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, InvoiceResponse)
