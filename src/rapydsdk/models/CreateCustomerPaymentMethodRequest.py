from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .PaymentMethodType import PaymentMethodType


@JsonMap({})
class CreateCustomerPaymentMethodRequest(BaseModel):
    def __init__(self, data: PaymentMethodType = None):
        self.data = self._define_object(data, PaymentMethodType)
