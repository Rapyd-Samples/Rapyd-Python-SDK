from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class UpdatePlanRequest(BaseModel):
    def __init__(self, metadata: dict = None, nickname: str = None):
        self.metadata = metadata
        self.nickname = nickname
