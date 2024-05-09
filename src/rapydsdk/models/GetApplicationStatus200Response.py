from __future__ import annotations
from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


class Status6(Enum):
    NEW = "NEW"
    DON = "DON"
    EXP = "EXP"

    def list():
        return list(map(lambda x: x.value, Status6._member_map_.values()))


@JsonMap({})
class Data33(BaseModel):
    def __init__(self, status: Status6 = None):
        self.status = (
            self._enum_matching(status, Status6.list(), "status") if status else None
        )


@JsonMap({})
class GetApplicationStatus200Response(BaseModel):
    def __init__(self, status: Status = None, data: Data33 = None):
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, Data33)
