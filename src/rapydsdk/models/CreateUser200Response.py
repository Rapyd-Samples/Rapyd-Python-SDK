from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Ewallet import Ewallet
from .Status import Status


@JsonMap({})
class CreateUser200Response(BaseModel):
    def __init__(self, data: Ewallet = None, status: Status = None):
        self.data = self._define_object(data, Ewallet)
        self.status = self._define_object(status, Status)
