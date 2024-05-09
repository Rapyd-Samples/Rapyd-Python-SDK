from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .CustomerPaymentMethod import CustomerPaymentMethod, CustomerPaymentMethodGuard
from .Status import Status


@JsonMap({})
class GetCustomerPaymentMethod200Response(BaseModel):
    def __init__(self, data: CustomerPaymentMethod = None, status: Status = None):
        self.data = CustomerPaymentMethodGuard.return_one_of(data)
        self.status = self._define_object(status, Status)
