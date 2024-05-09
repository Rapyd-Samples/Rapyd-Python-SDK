from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class Status(BaseModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        operation_id: str = None,
        response_code: str = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.message = message
        self.operation_id = operation_id
        self.response_code = response_code
        self.status = status
