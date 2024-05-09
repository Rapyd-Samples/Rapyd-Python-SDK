from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data4(BaseModel):
    def __init__(self, id: str = None, deleted: bool = None):
        self.id = id
        self.deleted = deleted


@JsonMap({})
class DeleteCustomer200Response(BaseModel):
    def __init__(self, data: Data4 = None, status: Status = None):
        self.data = self._define_object(data, Data4)
        self.status = self._define_object(status, Status)
