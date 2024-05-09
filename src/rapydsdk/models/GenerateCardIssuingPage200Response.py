from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .HostedPageResponse import HostedPageResponse, HostedPageResponseGuard
from .Status import Status


@JsonMap({})
class GenerateCardIssuingPage200Response(BaseModel):
    def __init__(self, data: HostedPageResponse = None, status: Status = None):
        self.data = HostedPageResponseGuard.return_one_of(data)
        self.status = self._define_object(status, Status)
