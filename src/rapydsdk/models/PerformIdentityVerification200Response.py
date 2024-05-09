from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data10(BaseModel):
    def __init__(self, id: str = None, reference_id: str = None):
        self.id = id
        self.reference_id = reference_id


@JsonMap({})
class PerformIdentityVerification200Response(BaseModel):
    def __init__(self, data: Data10 = None, status: Status = None):
        self.data = self._define_object(data, Data10)
        self.status = self._define_object(status, Status)
