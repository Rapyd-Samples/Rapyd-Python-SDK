from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data23(BaseModel):
    def __init__(self, deleted: bool = None, id: str = None):
        self.deleted = deleted
        self.id = id


@JsonMap({})
class DeleteBeneficiary200Response(BaseModel):
    def __init__(self, data: Data23 = None, status: Status = None):
        self.data = self._define_object(data, Data23)
        self.status = self._define_object(status, Status)
