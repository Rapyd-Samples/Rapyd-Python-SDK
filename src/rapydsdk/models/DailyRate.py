from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({"date_": "date"})
class DailyRate(BaseModel):
    def __init__(
        self,
        action_type: str = None,
        buy_amount: float = None,
        buy_currency: str = None,
        date_: str = None,
        fixed_side: str = None,
        rate: float = None,
        sell_amount: float = None,
        sell_currency: str = None,
    ):
        self.action_type = action_type
        self.buy_amount = buy_amount
        self.buy_currency = buy_currency
        self.date_ = date_
        self.fixed_side = fixed_side
        self.rate = rate
        self.sell_amount = sell_amount
        self.sell_currency = sell_currency
