from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .CheckoutPageResponse import CheckoutPageResponse
from .Status import Status


@JsonMap({})
class GenerateHostedPagePayment200Response(BaseModel):
    def __init__(self, data: CheckoutPageResponse = None, status: Status = None):
        self.data = self._define_object(data, CheckoutPageResponse)
        self.status = self._define_object(status, Status)
