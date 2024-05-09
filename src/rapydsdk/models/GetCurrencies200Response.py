from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .CurrencyObject import CurrencyObject
from .Status import Status


@JsonMap({})
class GetCurrencies200Response(BaseModel):
    def __init__(self, data: List[CurrencyObject] = None, status: Status = None):
        self.data = self._define_list(data, CurrencyObject)
        self.status = self._define_object(status, Status)
