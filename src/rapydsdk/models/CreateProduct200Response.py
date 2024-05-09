from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Product import Product
from .Status import Status


@JsonMap({})
class CreateProduct200Response(BaseModel):
    def __init__(self, data: Product = None, status: Status = None):
        self.data = self._define_object(data, Product)
        self.status = self._define_object(status, Status)
