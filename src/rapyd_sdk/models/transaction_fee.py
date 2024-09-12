from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class TransactionFee(BaseModel):
    """Describes the fee for processing the transaction.

    :param calc_type: Specifies how the fee is calculated. One of the following:  * net - The fee is deducted from the amount paid.  For example, in a payout of $100 with a fee of 5%, the recipient receives $95.00 and the $5.00 fee goes to the client wallet.  * gross - The fee is charged on top of the amount paid.  For example, for a transaction of $100 with a fee of 5%, the sender pays $105.00. The recipient receives $100.00 and the $5.00 fee goes to the client wallet. , defaults to None
    :type calc_type: str, optional
    :param fee_type: One of the following:  percentage - A percentage of the transaction amount.  For example, 5 percent is represented by value=5. absolute - A fixed amount , defaults to None
    :type fee_type: str, optional
    :param value: The amount of the fee. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal., defaults to None
    :type value: float, optional
    """

    def __init__(
        self, calc_type: str = None, fee_type: str = None, value: float = None
    ):
        """Describes the fee for processing the transaction.

        :param calc_type: Specifies how the fee is calculated. One of the following:  * net - The fee is deducted from the amount paid.  For example, in a payout of $100 with a fee of 5%, the recipient receives $95.00 and the $5.00 fee goes to the client wallet.  * gross - The fee is charged on top of the amount paid.  For example, for a transaction of $100 with a fee of 5%, the sender pays $105.00. The recipient receives $100.00 and the $5.00 fee goes to the client wallet. , defaults to None
        :type calc_type: str, optional
        :param fee_type: One of the following:  percentage - A percentage of the transaction amount.  For example, 5 percent is represented by value=5. absolute - A fixed amount , defaults to None
        :type fee_type: str, optional
        :param value: The amount of the fee. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal., defaults to None
        :type value: float, optional
        """
        self.calc_type = self._define_str("calc_type", calc_type, nullable=True)
        self.fee_type = self._define_str("fee_type", fee_type, nullable=True)
        self.value = self._define_number("value", value, nullable=True)
