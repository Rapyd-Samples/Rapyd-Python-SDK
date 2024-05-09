from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Webhook import Webhook
from .Status import Status


@JsonMap({})
class GetWebhookByToken200Response(BaseModel):
    def __init__(self, data: Webhook = None, status: Status = None):
        self.data = self._define_object(data, Webhook)
        self.status = self._define_object(status, Status)
