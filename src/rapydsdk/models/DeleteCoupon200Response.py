from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data(BaseModel):
    def __init__(self, deleted: bool = None, id: str = None):
        self.deleted = deleted
        self.id = id


@JsonMap({})
class DeleteCoupon200Response(BaseModel):
    def __init__(self, status: Status = None, data: Data = None):
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, Data)
