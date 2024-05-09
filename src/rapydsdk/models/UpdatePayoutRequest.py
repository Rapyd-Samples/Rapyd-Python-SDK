from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class UpdatePayoutRequest(BaseModel):
    def __init__(self, description: str = None, metadata: dict = None):
        self.description = description
        self.metadata = metadata
