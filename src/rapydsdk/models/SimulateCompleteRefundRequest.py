from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class SimulateCompleteRefundRequest(BaseModel):
    def __init__(self, token: str):
        self.token = token
