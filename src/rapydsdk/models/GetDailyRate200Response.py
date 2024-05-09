from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .DailyRate import DailyRate
from .Status import Status


@JsonMap({})
class GetDailyRate200Response(BaseModel):
    def __init__(self, data: DailyRate = None, status: Status = None):
        self.data = self._define_object(data, DailyRate)
        self.status = self._define_object(status, Status)
