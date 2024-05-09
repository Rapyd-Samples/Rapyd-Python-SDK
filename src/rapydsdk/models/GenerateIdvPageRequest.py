from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class RequestType(Enum):
    STORE = "store"
    VERIFY = "verify"

    def list():
        return list(map(lambda x: x.value, RequestType._member_map_.values()))


@JsonMap({})
class GenerateIdvPageRequest(BaseModel):
    def __init__(
        self,
        reference_id: str,
        ewallet: str,
        contact: str,
        country: str = None,
        request_type: RequestType = None,
        document_type: str = None,
        cancel_url: str = None,
        complete_url: str = None,
        language: str = None,
        page_expiration: float = None,
        force_camera: bool = None,
    ):
        self.reference_id = reference_id
        self.ewallet = ewallet
        self.contact = contact
        self.country = country
        self.request_type = (
            self._enum_matching(request_type, RequestType.list(), "request_type")
            if request_type
            else None
        )
        self.document_type = document_type
        self.cancel_url = cancel_url
        self.complete_url = complete_url
        self.language = language
        self.page_expiration = page_expiration
        self.force_camera = force_camera
