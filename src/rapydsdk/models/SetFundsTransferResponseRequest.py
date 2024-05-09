from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class SetFundsTransferResponseRequest(BaseModel):
    def __init__(self, id: str, status: str, metadata: dict = None):
        self.id = id
        self.metadata = metadata
        self.status = status
