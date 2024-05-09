from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class GenerateCardIssuingPageRequest(BaseModel):
    def __init__(
        self,
        card_color: str = None,
        language: str = None,
        logo: str = None,
        logo_orientation: str = None,
    ):
        self.card_color = card_color
        self.language = language
        self.logo = logo
        self.logo_orientation = logo_orientation
