from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Plan import Plan
from .Status import Status


@JsonMap({})
class ListPlans200Response(BaseModel):
    def __init__(self, data: List[Plan] = None, status: Status = None):
        self.data = self._define_list(data, Plan)
        self.status = self._define_object(status, Status)
