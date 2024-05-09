from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Condition import Condition


@JsonMap({"type_": "type"})
class PaymentMethodTypeField(BaseModel):
    def __init__(
        self,
        name: str,
        type_: str,
        regex: str,
        is_required: bool,
        is_updatable: bool = None,
        description: str = None,
        required_fields: List[PaymentMethodTypeField] = None,
        conditions: List[Condition] = None,
        instructions: str = None,
    ):
        self.name = name
        self.type_ = type_
        self.regex = regex
        self.is_required = is_required
        self.is_updatable = is_updatable
        self.description = description
        self.required_fields = self._define_list(
            required_fields, PaymentMethodTypeField
        )
        self.conditions = self._define_list(conditions, Condition)
        self.instructions = instructions
