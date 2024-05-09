from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class AttemptItem(BaseModel):
    def __init__(
        self,
        error: str = None,
        http_status_code: float = None,
        http_response_body: str = None,
        http_response_headers: dict = None,
    ):
        self.error = error
        self.http_status_code = http_status_code
        self.http_response_body = http_response_body
        self.http_response_headers = http_response_headers
