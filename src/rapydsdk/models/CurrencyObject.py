from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class CurrencyObject(BaseModel):
    def __init__(
        self,
        code: str = None,
        digits_after_decimal_separator: float = None,
        name: str = None,
        numeric_code: str = None,
        symbol: str = None,
    ):
        self.code = code
        self.digits_after_decimal_separator = digits_after_decimal_separator
        self.name = name
        self.numeric_code = numeric_code
        self.symbol = symbol
