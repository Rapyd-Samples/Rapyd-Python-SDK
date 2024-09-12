from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.inline_response_200_19 import InlineResponse200_19


class FxService(BaseService):

    @cast_models
    def get_daily_rate(
        self,
        action_type: str,
        buy_currency: str,
        sell_currency: str,
        amount: float = None,
        date_: str = None,
        fixed_side: str = None,
    ) -> InlineResponse200_19:
        """Retrieve a daily rate for conversion of currencies in payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees.

        :param action_type: Determines the type of transaction that the currency exchange applies to. One of the following - payment, payout
        :type action_type: str
        :param buy_currency: Defines the currency purchased in the currency exchange transaction. Three-letter ISO 4217 code in Uppercase.
        :type buy_currency: str
        :param sell_currency: Defines the currency sold in the currency exchange transaction. Three-letter ISO 4217 code in Uppercase.
        :type sell_currency: str
        :param amount: Amount of the currency exchange transaction, in units of the fixed-side currency in Decimal., defaults to None
        :type amount: float, optional
        :param date_: The date when the rate is applicable. Today or earlier. Format YYYY-MM-DD, defaults to None
        :type date_: str, optional
        :param fixed_side: Indicates whether the rate is fixed for the currency defined by buy_currency or sell_currency. One of the following - buy, sell., defaults to None
        :type fixed_side: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieve fixed daily rate
        :rtype: InlineResponse200_19
        """

        Validator(str).validate(action_type)
        Validator(str).validate(buy_currency)
        Validator(str).validate(sell_currency)
        Validator(float).is_optional().validate(amount)
        Validator(str).is_optional().validate(date_)
        Validator(str).is_optional().validate(fixed_side)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/rates/daily", self.get_default_headers())
            .add_query("action_type", action_type)
            .add_query("amount", amount)
            .add_query("buy_currency", buy_currency)
            .add_query("date", date_)
            .add_query("fixed_side", fixed_side)
            .add_query("sell_currency", sell_currency)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_19._unmap(response)
