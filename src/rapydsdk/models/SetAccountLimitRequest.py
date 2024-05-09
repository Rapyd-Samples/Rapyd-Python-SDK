from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({"type_": "type"})
class SetAccountLimitRequest(BaseModel):
    def __init__(self, amount: str, currency: str, type_: str, account_id: str = None):
        self.account_id = account_id
        self.amount = amount
        self.currency = currency
        self.type_ = type_
