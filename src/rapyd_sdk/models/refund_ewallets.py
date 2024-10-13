from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class RefundEwallets(BaseModel):
    """RefundEwallets

    :param amount: The amount of the payment to the wallet, in units of the currency defined in currency. Decimal. If the total amount of the payment is not fully accounted for, the balance appears in the client wallet. Relevant when percentage is not set., defaults to None
    :type amount: float, optional
    :param ewallet: ID of the wallet. String starting with **ewallet_**. Read-only., defaults to None
    :type ewallet: str, optional
    """

    def __init__(self, amount: float = None, ewallet: str = None):
        """RefundEwallets

        :param amount: The amount of the payment to the wallet, in units of the currency defined in currency. Decimal. If the total amount of the payment is not fully accounted for, the balance appears in the client wallet. Relevant when percentage is not set., defaults to None
        :type amount: float, optional
        :param ewallet: ID of the wallet. String starting with **ewallet_**. Read-only., defaults to None
        :type ewallet: str, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
