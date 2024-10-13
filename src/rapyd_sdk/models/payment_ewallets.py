from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PaymentEwallets(BaseModel):
    """PaymentEwallets

    :param ewallet_id: ewallet_id, defaults to None
    :type ewallet_id: str, optional
    :param amount: amount, defaults to None
    :type amount: float, optional
    :param percent: percent, defaults to None
    :type percent: float, optional
    :param refunded_amount: refunded_amount, defaults to None
    :type refunded_amount: float, optional
    :param released_amount: released_amount, defaults to None
    :type released_amount: float, optional
    """

    def __init__(
        self,
        ewallet_id: str = None,
        amount: float = None,
        percent: float = None,
        refunded_amount: float = None,
        released_amount: float = None,
    ):
        """PaymentEwallets

        :param ewallet_id: ewallet_id, defaults to None
        :type ewallet_id: str, optional
        :param amount: amount, defaults to None
        :type amount: float, optional
        :param percent: percent, defaults to None
        :type percent: float, optional
        :param refunded_amount: refunded_amount, defaults to None
        :type refunded_amount: float, optional
        :param released_amount: released_amount, defaults to None
        :type released_amount: float, optional
        """
        self.ewallet_id = self._define_str("ewallet_id", ewallet_id, nullable=True)
        self.amount = self._define_number("amount", amount, nullable=True)
        self.percent = self._define_number("percent", percent, nullable=True)
        self.refunded_amount = self._define_number(
            "refunded_amount", refunded_amount, nullable=True
        )
        self.released_amount = self._define_number(
            "released_amount", released_amount, nullable=True
        )
