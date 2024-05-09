from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({"type_": "type"})
class RemoveAccountLimitRequest(BaseModel):
    def __init__(self, type_: str, account_id: str = None, currency: str = None):
        self.account_id = account_id
        self.currency = currency
        self.type_ = type_
