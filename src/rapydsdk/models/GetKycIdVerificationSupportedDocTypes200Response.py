from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({"type_": "type"})
class Data11(BaseModel):
    def __init__(
        self,
        country: str = None,
        type_: str = None,
        name: str = None,
        is_back_required: bool = None,
        is_address_extractable: bool = None,
    ):
        self.country = country
        self.type_ = type_
        self.name = name
        self.is_back_required = is_back_required
        self.is_address_extractable = is_address_extractable


@JsonMap({})
class GetKycIdVerificationSupportedDocTypes200Response(BaseModel):
    def __init__(self, data: List[Data11] = None, status: Status = None):
        self.data = self._define_list(data, Data11)
        self.status = self._define_object(status, Status)
