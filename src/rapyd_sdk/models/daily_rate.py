from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"date_": "date"})
class DailyRate(BaseModel):
    """Describes currency conversion for payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees.

    :param action_type: The type of transaction that the currency exchange applies to. One of the following - payment, payout, defaults to None
    :type action_type: str, optional
    :param buy_amount: If fixed_side is buy, the value of amount. If fixed_side is sell, the value of buy_currency following the currency exchange transaction. Relevant when amount and `fixed_side` are specified., defaults to None
    :type buy_amount: float, optional
    :param buy_currency: The currency purchased in the currency exchange transaction. Three-letter ISO 4217 code. Uppercase., defaults to None
    :type buy_currency: str, optional
    :param date_: The date when the rate is applicable. Today or earlier. Format is YYYY-MM-DD. Default is today., defaults to None
    :type date_: str, optional
    :param fixed_side: Indicates which currency the rate is fixed for. One of the following : * buy - The currency defined by buy_currency. * sell : The currency defined by sell_currency., defaults to None
    :type fixed_side: str, optional
    :param rate: The exchange rate. Includes FX markup fees., defaults to None
    :type rate: float, optional
    :param sell_amount: If `fixed_side` is **sell**, the value of amount. If `fixed_side` is **buy**, the value of `sell_currency` following the currency exchange transaction. Relevant when `amount` and `fixed_side` are specified., defaults to None
    :type sell_amount: float, optional
    :param sell_currency: Selling currency, defaults to None
    :type sell_currency: str, optional
    """

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
        """Describes currency conversion for payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees.

        :param action_type: The type of transaction that the currency exchange applies to. One of the following - payment, payout, defaults to None
        :type action_type: str, optional
        :param buy_amount: If fixed_side is buy, the value of amount. If fixed_side is sell, the value of buy_currency following the currency exchange transaction. Relevant when amount and `fixed_side` are specified., defaults to None
        :type buy_amount: float, optional
        :param buy_currency: The currency purchased in the currency exchange transaction. Three-letter ISO 4217 code. Uppercase., defaults to None
        :type buy_currency: str, optional
        :param date_: The date when the rate is applicable. Today or earlier. Format is YYYY-MM-DD. Default is today., defaults to None
        :type date_: str, optional
        :param fixed_side: Indicates which currency the rate is fixed for. One of the following : * buy - The currency defined by buy_currency. * sell : The currency defined by sell_currency., defaults to None
        :type fixed_side: str, optional
        :param rate: The exchange rate. Includes FX markup fees., defaults to None
        :type rate: float, optional
        :param sell_amount: If `fixed_side` is **sell**, the value of amount. If `fixed_side` is **buy**, the value of `sell_currency` following the currency exchange transaction. Relevant when `amount` and `fixed_side` are specified., defaults to None
        :type sell_amount: float, optional
        :param sell_currency: Selling currency, defaults to None
        :type sell_currency: str, optional
        """
        self.action_type = self._define_str("action_type", action_type, nullable=True)
        self.buy_amount = self._define_number("buy_amount", buy_amount, nullable=True)
        self.buy_currency = self._define_str(
            "buy_currency", buy_currency, nullable=True
        )
        self.date_ = self._define_str("date_", date_, nullable=True)
        self.fixed_side = self._define_str("fixed_side", fixed_side, nullable=True)
        self.rate = self._define_number("rate", rate, nullable=True)
        self.sell_amount = self._define_number(
            "sell_amount", sell_amount, nullable=True
        )
        self.sell_currency = self._define_str(
            "sell_currency", sell_currency, nullable=True
        )
