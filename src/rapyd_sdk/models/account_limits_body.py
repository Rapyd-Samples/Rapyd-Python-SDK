from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"type_": "type"})
class AccountLimitsBody(BaseModel):
    """AccountLimitsBody

    :param account_id: The ID of the account within the wallet., defaults to None
    :type account_id: str, optional
    :param amount: The amount of the limit.
    :type amount: str
    :param currency: Three-letter ISO 4217 code for the currency of an existing account.
    :type currency: str
    :param type_: The limit type.
    :type type_: str
    """

    def __init__(self, amount: str, currency: str, type_: str, account_id: str = None):
        """AccountLimitsBody

        :param account_id: The ID of the account within the wallet., defaults to None
        :type account_id: str, optional
        :param amount: The amount of the limit.
        :type amount: str
        :param currency: Three-letter ISO 4217 code for the currency of an existing account.
        :type currency: str
        :param type_: The limit type.
        :type type_: str
        """
        self.account_id = self._define_str("account_id", account_id, nullable=True)
        self.amount = amount
        self.currency = currency
        self.type_ = type_
