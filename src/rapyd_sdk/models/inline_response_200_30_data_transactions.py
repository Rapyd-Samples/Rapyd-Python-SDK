from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_30DataTransactions(BaseModel):
    """InlineResponse200_30DataTransactions

    :param id_: ID of the issued card transaction object. String starting with **cit_**., defaults to None
    :type id_: str, optional
    :param ewallet: ID of the wallet the bank account number is issued to. String starting with **ewallet_**., defaults to None
    :type ewallet: str, optional
    :param account_id: ID of the virtual bank account., defaults to None
    :type account_id: str, optional
    :param account_id_type: Type of the virtual account number., defaults to None
    :type account_id_type: str, optional
    :param amount: Amount of the transaction., defaults to None
    :type amount: float, optional
    :param currency: Currency of the transaction. Three-letter ISO 4217., defaults to None
    :type currency: str, optional
    :param created_at: Time of creation of the transaction, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param receiving_currency: receiving_currency, defaults to None
    :type receiving_currency: bool, optional
    """

    def __init__(
        self,
        id_: str = None,
        ewallet: str = None,
        account_id: str = None,
        account_id_type: str = None,
        amount: float = None,
        currency: str = None,
        created_at: float = None,
        receiving_currency: bool = None,
    ):
        """InlineResponse200_30DataTransactions

        :param id_: ID of the issued card transaction object. String starting with **cit_**., defaults to None
        :type id_: str, optional
        :param ewallet: ID of the wallet the bank account number is issued to. String starting with **ewallet_**., defaults to None
        :type ewallet: str, optional
        :param account_id: ID of the virtual bank account., defaults to None
        :type account_id: str, optional
        :param account_id_type: Type of the virtual account number., defaults to None
        :type account_id_type: str, optional
        :param amount: Amount of the transaction., defaults to None
        :type amount: float, optional
        :param currency: Currency of the transaction. Three-letter ISO 4217., defaults to None
        :type currency: str, optional
        :param created_at: Time of creation of the transaction, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param receiving_currency: receiving_currency, defaults to None
        :type receiving_currency: bool, optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.account_id = self._define_str("account_id", account_id, nullable=True)
        self.account_id_type = self._define_str(
            "account_id_type", account_id_type, nullable=True
        )
        self.amount = self._define_number("amount", amount, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.receiving_currency = receiving_currency
