from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class FxFee(BaseModel):
    """Describes the fees for processing the currency exchange. Relevant to payouts with FX.

    :param calc_type: Specifies how the fee is calculated. One of the following:  * net - The fee is deducted from the amount paid.  For example, in a payout of $100 with a fee of 5%, the recipient receives $95.00 and the $5.00 fee goes to the client wallet.  * gross - The fee is charged on top of the amount paid.  For example, for a transaction of $100 with a fee of 5%, the sender pays $105.00. The recipient receives $100.00 and the $5.00 fee goes to the client wallet. , defaults to None
    :type calc_type: str, optional
    :param value: The amount of the fee. Percentage., defaults to None
    :type value: float, optional
    """

    def __init__(self, calc_type: str = None, value: float = None):
        """Describes the fees for processing the currency exchange. Relevant to payouts with FX.

        :param calc_type: Specifies how the fee is calculated. One of the following:  * net - The fee is deducted from the amount paid.  For example, in a payout of $100 with a fee of 5%, the recipient receives $95.00 and the $5.00 fee goes to the client wallet.  * gross - The fee is charged on top of the amount paid.  For example, for a transaction of $100 with a fee of 5%, the sender pays $105.00. The recipient receives $100.00 and the $5.00 fee goes to the client wallet. , defaults to None
        :type calc_type: str, optional
        :param value: The amount of the fee. Percentage., defaults to None
        :type value: float, optional
        """
        self.calc_type = self._define_str("calc_type", calc_type, nullable=True)
        self.value = self._define_number("value", value, nullable=True)
