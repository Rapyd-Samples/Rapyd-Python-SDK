from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .VerifyHostedAppResponse import VerifyHostedAppResponse
from .Status import Status


@JsonMap({})
class CreateHostedApplicationToken200Response(BaseModel):
    def __init__(self, data: VerifyHostedAppResponse = None, status: Status = None):
        self.data = self._define_object(data, VerifyHostedAppResponse)
        self.status = self._define_object(status, Status)
