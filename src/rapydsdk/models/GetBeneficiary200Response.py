from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Beneficiary import Beneficiary
from .Status import Status


@JsonMap({})
class GetBeneficiary200Response(BaseModel):
    def __init__(self, data: Beneficiary = None, status: Status = None):
        self.data = self._define_object(data, Beneficiary)
        self.status = self._define_object(status, Status)
