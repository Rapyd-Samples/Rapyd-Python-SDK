from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class FxFee(BaseModel):
    def __init__(self, calc_type: str = None, value: float = None):
        self.calc_type = calc_type
        self.value = value
