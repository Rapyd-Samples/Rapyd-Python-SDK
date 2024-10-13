from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PayoutEwallets(BaseModel):
    """PayoutEwallets

    :param amount: The amount of the payment to the wallet, in units of the currency defined in currency. Decimal. If the total amount of the payment is not fully accounted for, the balance appears in the client wallet. Relevant when percentage is not set., defaults to None
    :type amount: float, optional
    :param ewallet_id: ID of the wallet. String starting with **ewallet_**. Read-only., defaults to None
    :type ewallet_id: str, optional
    :param percent: The percentage that is paid to the wallet out of the total payment. Read-only., defaults to None
    :type percent: float, optional
    """

    def __init__(
        self, amount: float = None, ewallet_id: str = None, percent: float = None
    ):
        """PayoutEwallets

        :param amount: The amount of the payment to the wallet, in units of the currency defined in currency. Decimal. If the total amount of the payment is not fully accounted for, the balance appears in the client wallet. Relevant when percentage is not set., defaults to None
        :type amount: float, optional
        :param ewallet_id: ID of the wallet. String starting with **ewallet_**. Read-only., defaults to None
        :type ewallet_id: str, optional
        :param percent: The percentage that is paid to the wallet out of the total payment. Read-only., defaults to None
        :type percent: float, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.ewallet_id = self._define_str("ewallet_id", ewallet_id, nullable=True)
        self.percent = self._define_number("percent", percent, nullable=True)
