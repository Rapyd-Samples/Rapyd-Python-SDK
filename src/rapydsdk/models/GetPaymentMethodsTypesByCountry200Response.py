from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .PaymentMethodType import PaymentMethodType
from .Status import Status


@JsonMap({})
class GetPaymentMethodsTypesByCountry200Response(BaseModel):
    def __init__(self, data: List[PaymentMethodType] = None, status: Status = None):
        self.data = self._define_list(data, PaymentMethodType)
        self.status = self._define_object(status, Status)
