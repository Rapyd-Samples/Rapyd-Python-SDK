from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_33Data(BaseModel):
    """InlineResponse200_33Data

    :param account_id: ID of the virtual bank account., defaults to None
    :type account_id: str, optional
    :param account_id_type: Type of the virtual account number., defaults to None
    :type account_id_type: str, optional
    :param amount: Amount of the transaction, in units defined in currency., defaults to None
    :type amount: float, optional
    :param created_at: Timestamp for the transaction, in Unix time, defaults to None
    :type created_at: int, optional
    :param currency: Currency of the account. Three-letter ISO 4217 code., defaults to None
    :type currency: str, optional
    :param ewallet: ID of the Rapyd Wallet that is attached to the virtual account. String starting with **ewallet_**., defaults to None
    :type ewallet: str, optional
    :param id_: ID of the transaction. String starting with **isutran_**., defaults to None
    :type id_: str, optional
    """

    def __init__(
        self,
        account_id: str = None,
        account_id_type: str = None,
        amount: float = None,
        created_at: int = None,
        currency: str = None,
        ewallet: str = None,
        id_: str = None,
    ):
        """InlineResponse200_33Data

        :param account_id: ID of the virtual bank account., defaults to None
        :type account_id: str, optional
        :param account_id_type: Type of the virtual account number., defaults to None
        :type account_id_type: str, optional
        :param amount: Amount of the transaction, in units defined in currency., defaults to None
        :type amount: float, optional
        :param created_at: Timestamp for the transaction, in Unix time, defaults to None
        :type created_at: int, optional
        :param currency: Currency of the account. Three-letter ISO 4217 code., defaults to None
        :type currency: str, optional
        :param ewallet: ID of the Rapyd Wallet that is attached to the virtual account. String starting with **ewallet_**., defaults to None
        :type ewallet: str, optional
        :param id_: ID of the transaction. String starting with **isutran_**., defaults to None
        :type id_: str, optional
        """
        self.account_id = self._define_str("account_id", account_id, nullable=True)
        self.account_id_type = self._define_str(
            "account_id_type", account_id_type, nullable=True
        )
        self.amount = self._define_number("amount", amount, nullable=True)
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
