from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Sender import Sender
from .Status import Status


@JsonMap({})
class GetPayer200Response(BaseModel):
    def __init__(self, data: Sender = None, status: Status = None):
        self.data = self._define_object(data, Sender)
        self.status = self._define_object(status, Status)
