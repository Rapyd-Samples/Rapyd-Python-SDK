from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Payment import Payment
from .Status import Status


@JsonMap({})
class CreatePayment200Response(BaseModel):
    def __init__(self, data: Payment = None, status: Status = None):
        self.data = self._define_object(data, Payment)
        self.status = self._define_object(status, Status)
