from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Dispute import Dispute
from .Status import Status


@JsonMap({})
class GetDispute200Response(BaseModel):
    def __init__(self, data: Dispute = None, status: Status = None):
        self.data = self._define_object(data, Dispute)
        self.status = self._define_object(status, Status)
