from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Dispute import Dispute
from .Status import Status


@JsonMap({})
class GetDisputesListByOrgId200Response(BaseModel):
    def __init__(self, data: List[Dispute] = None, status: Status = None):
        self.data = self._define_list(data, Dispute)
        self.status = self._define_object(status, Status)
