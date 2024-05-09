from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data21(BaseModel):
    def __init__(self, id: str = None, deleted: bool = None):
        self.id = id
        self.deleted = deleted


@JsonMap({})
class DeleteSubscriptionDiscount200Response(BaseModel):
    def __init__(self, data: Data21 = None, status: Status = None):
        self.data = self._define_object(data, Data21)
        self.status = self._define_object(status, Status)
