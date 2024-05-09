from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data31(BaseModel):
    def __init__(self, id: str = None, deleted: bool = None):
        self.id = id
        self.deleted = deleted


@JsonMap({})
class DeleteSku200Response(BaseModel):
    def __init__(self, status: Status = None, data: Data31 = None):
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, Data31)
