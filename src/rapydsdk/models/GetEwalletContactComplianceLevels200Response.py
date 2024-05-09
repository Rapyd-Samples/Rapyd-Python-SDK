from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Elements(BaseModel):
    def __init__(self, element_name: str = None, verified: bool = None):
        self.element_name = element_name
        self.verified = verified


@JsonMap({})
class ComplianceLevels(BaseModel):
    def __init__(self, level: float = None, elements: List[Elements] = None):
        self.level = level
        self.elements = self._define_list(elements, Elements)


@JsonMap({})
class Data8(BaseModel):
    def __init__(self, compliance_levels: List[ComplianceLevels] = None):
        self.compliance_levels = self._define_list(compliance_levels, ComplianceLevels)


@JsonMap({})
class GetEwalletContactComplianceLevels200Response(BaseModel):
    def __init__(self, data: Data8 = None, status: Status = None):
        self.data = self._define_object(data, Data8)
        self.status = self._define_object(status, Status)
