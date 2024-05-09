from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class UpdatedUserRequest(BaseModel):
    def __init__(
        self,
        ewallet_reference_id: str = None,
        first_name: str = None,
        last_name: str = None,
        metadata: dict = None,
    ):
        self.ewallet_reference_id = ewallet_reference_id
        self.first_name = first_name
        self.last_name = last_name
        self.metadata = metadata
