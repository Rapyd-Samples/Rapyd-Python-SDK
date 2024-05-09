from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status
from .CustomerPaymentMethod import CustomerPaymentMethod, CustomerPaymentMethodGuard


@JsonMap({})
class CreateCustomerPaymentMethod200Response(BaseModel):
    def __init__(self, status: Status = None, data: CustomerPaymentMethod = None):
        self.status = self._define_object(status, Status)
        self.data = CustomerPaymentMethodGuard.return_one_of(data)
