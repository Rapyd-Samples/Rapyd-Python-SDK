from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class UpdateCardStatusRequest(BaseModel):
    def __init__(self, card: str, status: str, blocked_reason: str = None):
        self.blocked_reason = blocked_reason
        self.card = card
        self.status = status
