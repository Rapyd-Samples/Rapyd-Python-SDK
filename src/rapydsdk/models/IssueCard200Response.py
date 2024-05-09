from __future__ import annotations
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Status import Status
from .CardIssuing import CardIssuing
from .CardIssuingMasked import CardIssuingMasked


class Data19Guard(OneOfBaseModel):
    class_list = {"CardIssuing": CardIssuing, "CardIssuingMasked": CardIssuingMasked}


Data19 = Union[CardIssuing, CardIssuingMasked]


@JsonMap({})
class IssueCard200Response(BaseModel):
    def __init__(self, data: Data19 = None, status: Status = None):
        self.data = Data19Guard.return_one_of(data)
        self.status = self._define_object(status, Status)
