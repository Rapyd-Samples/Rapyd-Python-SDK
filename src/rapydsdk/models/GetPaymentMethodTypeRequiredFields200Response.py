from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .PaymentMethodTypeRequiredFields import PaymentMethodTypeRequiredFields
from .Status import Status


@JsonMap({})
class GetPaymentMethodTypeRequiredFields200Response(BaseModel):
    def __init__(
        self, data: PaymentMethodTypeRequiredFields = None, status: Status = None
    ):
        self.data = self._define_object(data, PaymentMethodTypeRequiredFields)
        self.status = self._define_object(status, Status)
