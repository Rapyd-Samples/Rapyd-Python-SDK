from __future__ import annotations
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Status import Status
from .Customer import Customer
from .CustomerDetailsPmt import CustomerDetailsPmt


class Data1Guard(OneOfBaseModel):
    class_list = {"Customer": Customer, "CustomerDetailsPmt": CustomerDetailsPmt}


Data1 = Union[Customer, CustomerDetailsPmt]


@JsonMap({})
class CreateCustomer200Response(BaseModel):
    def __init__(self, status: Status = None, data: Data1 = None):
        self.status = self._define_object(status, Status)
        self.data = Data1Guard.return_one_of(data)
