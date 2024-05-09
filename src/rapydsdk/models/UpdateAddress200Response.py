from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Address import Address
from .Status import Status


@JsonMap({})
class UpdateAddress200Response(BaseModel):
    def __init__(self, data: Address = None, status: Status = None):
        self.data = self._define_object(data, Address)
        self.status = self._define_object(status, Status)
