from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status
from .Sku import Sku


@JsonMap({})
class UpdateSku200Response(BaseModel):
    def __init__(self, status: Status = None, data: Sku = None):
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, Sku)
