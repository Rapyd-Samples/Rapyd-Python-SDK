from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class IssueCardRequest(BaseModel):
    def __init__(
        self,
        card_program: str,
        ewallet_contact: str,
        country: str = None,
        expiration_month: str = None,
        expiration_year: str = None,
        metadata: dict = None,
    ):
        self.card_program = card_program
        self.country = country
        self.ewallet_contact = ewallet_contact
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.metadata = metadata
