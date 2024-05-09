from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .CustomerPaymentMethod import CustomerPaymentMethod, CustomerPaymentMethodGuard
from .Status import Status


@JsonMap({})
class GetCustomerPaymentMethods200Response(BaseModel):
    def __init__(self, data: List[CustomerPaymentMethod] = None, status: Status = None):
        self.data = self._define_list(data, CustomerPaymentMethod)
        self.status = self._define_object(status, Status)
