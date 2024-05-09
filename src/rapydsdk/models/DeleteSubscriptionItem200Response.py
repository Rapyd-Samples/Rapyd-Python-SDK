from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data28(BaseModel):
    def __init__(self, deleted: bool = None, id: str = None):
        self.deleted = deleted
        self.id = id


@JsonMap({})
class DeleteSubscriptionItem200Response(BaseModel):
    def __init__(self, data: Data28 = None, status: Status = None):
        self.data = self._define_object(data, Data28)
        self.status = self._define_object(status, Status)
