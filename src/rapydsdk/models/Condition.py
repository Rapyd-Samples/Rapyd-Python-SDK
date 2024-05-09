from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel


class ThresholdValueGuard(OneOfBaseModel):
    class_list = {"str": str, "int": int}


ThresholdValue = Union[str, int]


@JsonMap({})
class Condition(BaseModel):
    def __init__(
        self,
        description: str = None,
        element_name: str = None,
        operator: str = None,
        threshold_value: ThresholdValue = None,
    ):
        self.description = description
        self.element_name = element_name
        self.operator = operator
        self.threshold_value = ThresholdValueGuard.return_one_of(threshold_value)
