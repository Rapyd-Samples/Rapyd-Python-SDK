from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class ModifyCardRequest(BaseModel):
    def __init__(self, card: str, ewallet_contact: str):
        self.card = card
        self.ewallet_contact = ewallet_contact
