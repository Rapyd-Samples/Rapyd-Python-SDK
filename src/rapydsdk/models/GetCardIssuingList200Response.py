from __future__ import annotations
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Status import Status
from .CardIssuing import CardIssuing
from .CardIssuingMasked import CardIssuingMasked


class Data18Guard(OneOfBaseModel):
    class_list = {"CardIssuing": CardIssuing, "CardIssuingMasked": CardIssuingMasked}


Data18 = Union[CardIssuing, CardIssuingMasked]


@JsonMap({})
class GetCardIssuingList200Response(BaseModel):
    def __init__(self, status: Status = None, data: List[Data18] = None):
        self.status = self._define_object(status, Status)
        self.data = self._define_list(data, Data18)
