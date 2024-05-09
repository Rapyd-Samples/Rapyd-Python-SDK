from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data7(BaseModel):
    def __init__(self, delete: bool = None, id: str = None):
        self.delete = delete
        self.id = id


@JsonMap({})
class DeleteEwalletContact200Response(BaseModel):
    def __init__(self, data: Data7 = None, status: Status = None):
        self.data = self._define_object(data, Data7)
        self.status = self._define_object(status, Status)
