from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Account import Account
from .Status import Status


@JsonMap({})
class GetUserAccounts200Response(BaseModel):
    def __init__(self, data: List[Account] = None, status: Status = None):
        self.data = self._define_list(data, Account)
        self.status = self._define_object(status, Status)
