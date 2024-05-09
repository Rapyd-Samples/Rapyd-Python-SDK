from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateHostedApplicationTokenRequest(BaseModel):
    def __init__(
        self,
        country: str,
        rapyd_entity_token: str,
        phone_number: str,
        application_type: str = None,
        metadata: dict = None,
        client_reference_id: str = None,
        cancel_url: str = None,
        complete_url: str = None,
    ):
        self.application_type = application_type
        self.country = country
        self.rapyd_entity_token = rapyd_entity_token
        self.phone_number = phone_number
        self.metadata = metadata
        self.client_reference_id = client_reference_id
        self.cancel_url = cancel_url
        self.complete_url = complete_url
