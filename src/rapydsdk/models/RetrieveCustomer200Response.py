from __future__ import annotations
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Status import Status
from .Customer import Customer
from .CustomerDetailsPmt import CustomerDetailsPmt


class Data2Guard(OneOfBaseModel):
    class_list = {"Customer": Customer, "CustomerDetailsPmt": CustomerDetailsPmt}


Data2 = Union[Customer, CustomerDetailsPmt]


@JsonMap({})
class RetrieveCustomer200Response(BaseModel):
    def __init__(self, data: Data2 = None, status: Status = None):
        self.data = Data2Guard.return_one_of(data)
        self.status = self._define_object(status, Status)
