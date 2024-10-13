from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class RefundsGroupPaymentsBody(BaseModel):
    """RefundsGroupPaymentsBody

    :param amount: The amount of the refund, in the currency of the group payment. Decimal. If this parameter is omitted, the entire group payment is refunded., defaults to None
    :type amount: float, optional
    :param group_payment: ID of the group payment that the refund is charged against. String starting with **gp_**.
    :type group_payment: str
    """

    def __init__(self, group_payment: str, amount: float = None):
        """RefundsGroupPaymentsBody

        :param amount: The amount of the refund, in the currency of the group payment. Decimal. If this parameter is omitted, the entire group payment is refunded., defaults to None
        :type amount: float, optional
        :param group_payment: ID of the group payment that the refund is charged against. String starting with **gp_**.
        :type group_payment: str
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.group_payment = group_payment
