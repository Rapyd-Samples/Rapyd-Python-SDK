from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class UpdateEwalletStatus200Response(BaseModel):
    def __init__(self, status: Status = None):
        self.status = self._define_object(status, Status)
