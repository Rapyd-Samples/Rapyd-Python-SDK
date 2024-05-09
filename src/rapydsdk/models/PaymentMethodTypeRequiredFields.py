from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .PaymentMethodTypeField import PaymentMethodTypeField


@JsonMap({"type_": "type"})
class PaymentMethodTypeRequiredFields(BaseModel):
    def __init__(
        self,
        fields: List[PaymentMethodTypeField] = None,
        maximum_expiration_seconds: float = None,
        minimum_expiration_seconds: float = None,
        payment_method_options: List[PaymentMethodTypeField] = None,
        payment_options: List[PaymentMethodTypeField] = None,
        type_: str = None,
    ):
        self.fields = self._define_list(fields, PaymentMethodTypeField)
        self.maximum_expiration_seconds = maximum_expiration_seconds
        self.minimum_expiration_seconds = minimum_expiration_seconds
        self.payment_method_options = self._define_list(
            payment_method_options, PaymentMethodTypeField
        )
        self.payment_options = self._define_list(
            payment_options, PaymentMethodTypeField
        )
        self.type_ = type_
