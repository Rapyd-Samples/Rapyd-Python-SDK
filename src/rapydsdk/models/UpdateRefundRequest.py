from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class UpdateRefundRequest(BaseModel):
    def __init__(self, metadata: dict = None):
        self.metadata = metadata
