from __future__ import annotations
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Status import Status
from .CardIssuing import CardIssuing
from .CardIssuingMasked import CardIssuingMasked


class Data20Guard(OneOfBaseModel):
    class_list = {"CardIssuing": CardIssuing, "CardIssuingMasked": CardIssuingMasked}


Data20 = Union[CardIssuing, CardIssuingMasked]


@JsonMap({})
class GetCardIssuingDetails200Response(BaseModel):
    def __init__(self, status: Status = None, data: Data20 = None):
        self.status = self._define_object(status, Status)
        self.data = Data20Guard.return_one_of(data)
