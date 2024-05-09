from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status
from .Account import Account


@JsonMap({})
class RemoveAccountLimit200Response(BaseModel):
    def __init__(self, status: Status = None, data: List[Account] = None):
        self.status = self._define_object(status, Status)
        self.data = self._define_list(data, Account)
