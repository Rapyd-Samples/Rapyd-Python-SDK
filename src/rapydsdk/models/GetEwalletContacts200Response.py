from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Contact import Contact
from .Status import Status


@JsonMap({})
class GetEwalletContacts200Response(BaseModel):
    def __init__(self, data: List[Contact] = None, status: Status = None):
        self.data = self._define_list(data, Contact)
        self.status = self._define_object(status, Status)
