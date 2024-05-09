from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .PayoutMethodTypeDetails import PayoutMethodTypeDetails
from .Status import Status


@JsonMap({})
class GetPayoutMethodTypesDetails200Response(BaseModel):
    def __init__(self, data: PayoutMethodTypeDetails = None, status: Status = None):
        self.data = self._define_object(data, PayoutMethodTypeDetails)
        self.status = self._define_object(status, Status)
