from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateIssuingRequest(BaseModel):
    def __init__(
        self,
        country: str,
        currency: str,
        ewallet: str,
        description: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        requested_currency: str = None,
    ):
        self.country = country
        self.currency = currency
        self.description = description
        self.ewallet = ewallet
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.requested_currency = requested_currency
