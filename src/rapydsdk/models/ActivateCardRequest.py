from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class ActivateCardRequest(BaseModel):
    def __init__(self, card: str):
        self.card = card
