from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status
from .Beneficiary import Beneficiary


@JsonMap({})
class Data22(BaseModel):
    def __init__(self, beneficiary: Beneficiary = None, validated: bool = None):
        self.beneficiary = self._define_object(beneficiary, Beneficiary)
        self.validated = validated


@JsonMap({})
class ValidateBeneficiary200Response(BaseModel):
    def __init__(self, data: Data22 = None, status: Status = None):
        self.data = self._define_object(data, Data22)
        self.status = self._define_object(status, Status)
