from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({"type_": "type"})
class Limit(BaseModel):
    def __init__(
        self,
        amount: float = None,
        currency: str = None,
        type_: str = None,
        updated_at: int = None,
    ):
        self.amount = amount
        self.currency = currency
        self.type_ = type_
        self.updated_at = updated_at
