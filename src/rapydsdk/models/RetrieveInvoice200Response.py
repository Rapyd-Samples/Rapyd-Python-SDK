from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .InvoiceResponse import InvoiceResponse
from .Status import Status


@JsonMap({})
class RetrieveInvoice200Response(BaseModel):
    def __init__(self, data: InvoiceResponse = None, status: Status = None):
        self.data = self._define_object(data, InvoiceResponse)
        self.status = self._define_object(status, Status)
