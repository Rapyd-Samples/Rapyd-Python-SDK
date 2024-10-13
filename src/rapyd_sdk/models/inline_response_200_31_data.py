from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_31Data(BaseModel):
    """InlineResponse200_31Data

    :param account_name: Name of the bank account holder., defaults to None
    :type account_name: str, optional
    :param account_number: Number of the bank account., defaults to None
    :type account_number: str, optional
    :param amount: The amount of the transaction, in units of the currency defined in currency., defaults to None
    :type amount: str, optional
    :param bank_code: Bank identifier code, such as SWIFT, BIC, ABA, or other local identifier., defaults to None
    :type bank_code: str, optional
    :param bank_name: Name of the bank., defaults to None
    :type bank_name: str, optional
    :param country: The country that the account number will be associated with. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
    :type country: str, optional
    :param created_at: Time of creation of the transaction, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param currency: Currency of the account. Three-letter ISO 4217 code., defaults to None
    :type currency: str, optional
    :param iban: IBAN of the virtual bank account., defaults to None
    :type iban: str, optional
    :param id_: ID that is assigned by the remitter, defaults to None
    :type id_: str, optional
    :param partner_transaction_id: ID that is assigned by the client to the transaction., defaults to None
    :type partner_transaction_id: str, optional
    :param receiving_iban: IBAN that was assigned to the Rapyd Wallet., defaults to None
    :type receiving_iban: str, optional
    :param remitter_reference: Optional information that the remitter adds to the transaction, intended for the beneficiary. Supported by some payment methods., defaults to None
    :type remitter_reference: str, optional
    :param sort_code: sort_code, defaults to None
    :type sort_code: str, optional
    :param status: Indicates the status of the transfer., defaults to None
    :type status: str, optional
    :param updated_at: Time of update of the virtual account, in Unix time. Response only., defaults to None
    :type updated_at: float, optional
    :param created_at_gw: Time of creation of the transaction, in Unix time. Response only., defaults to None
    :type created_at_gw: str, optional
    :param original_currency: This field will display the currency in which the transaction was originally made., defaults to None
    :type original_currency: str, optional
    :param original_amount: This field will show the initial transaction amount before conversion., defaults to None
    :type original_amount: str, optional
    :param fx_rate: This field will indicate the exchange rate applied for the currency conversion, defaults to None
    :type fx_rate: str, optional
    """

    def __init__(
        self,
        account_name: str = None,
        account_number: str = None,
        amount: str = None,
        bank_code: str = None,
        bank_name: str = None,
        country: str = None,
        created_at: float = None,
        currency: str = None,
        iban: str = None,
        id_: str = None,
        partner_transaction_id: str = None,
        receiving_iban: str = None,
        remitter_reference: str = None,
        sort_code: str = None,
        status: str = None,
        updated_at: float = None,
        created_at_gw: str = None,
        original_currency: str = None,
        original_amount: str = None,
        fx_rate: str = None,
    ):
        """InlineResponse200_31Data

        :param account_name: Name of the bank account holder., defaults to None
        :type account_name: str, optional
        :param account_number: Number of the bank account., defaults to None
        :type account_number: str, optional
        :param amount: The amount of the transaction, in units of the currency defined in currency., defaults to None
        :type amount: str, optional
        :param bank_code: Bank identifier code, such as SWIFT, BIC, ABA, or other local identifier., defaults to None
        :type bank_code: str, optional
        :param bank_name: Name of the bank., defaults to None
        :type bank_name: str, optional
        :param country: The country that the account number will be associated with. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
        :type country: str, optional
        :param created_at: Time of creation of the transaction, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param currency: Currency of the account. Three-letter ISO 4217 code., defaults to None
        :type currency: str, optional
        :param iban: IBAN of the virtual bank account., defaults to None
        :type iban: str, optional
        :param id_: ID that is assigned by the remitter, defaults to None
        :type id_: str, optional
        :param partner_transaction_id: ID that is assigned by the client to the transaction., defaults to None
        :type partner_transaction_id: str, optional
        :param receiving_iban: IBAN that was assigned to the Rapyd Wallet., defaults to None
        :type receiving_iban: str, optional
        :param remitter_reference: Optional information that the remitter adds to the transaction, intended for the beneficiary. Supported by some payment methods., defaults to None
        :type remitter_reference: str, optional
        :param sort_code: sort_code, defaults to None
        :type sort_code: str, optional
        :param status: Indicates the status of the transfer., defaults to None
        :type status: str, optional
        :param updated_at: Time of update of the virtual account, in Unix time. Response only., defaults to None
        :type updated_at: float, optional
        :param created_at_gw: Time of creation of the transaction, in Unix time. Response only., defaults to None
        :type created_at_gw: str, optional
        :param original_currency: This field will display the currency in which the transaction was originally made., defaults to None
        :type original_currency: str, optional
        :param original_amount: This field will show the initial transaction amount before conversion., defaults to None
        :type original_amount: str, optional
        :param fx_rate: This field will indicate the exchange rate applied for the currency conversion, defaults to None
        :type fx_rate: str, optional
        """
        self.account_name = self._define_str(
            "account_name", account_name, nullable=True
        )
        self.account_number = self._define_str(
            "account_number", account_number, nullable=True
        )
        self.amount = self._define_str("amount", amount, nullable=True)
        self.bank_code = self._define_str("bank_code", bank_code, nullable=True)
        self.bank_name = self._define_str("bank_name", bank_name, nullable=True)
        self.country = self._define_str("country", country, nullable=True)
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.iban = self._define_str("iban", iban, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.partner_transaction_id = self._define_str(
            "partner_transaction_id", partner_transaction_id, nullable=True
        )
        self.receiving_iban = self._define_str(
            "receiving_iban", receiving_iban, nullable=True
        )
        self.remitter_reference = self._define_str(
            "remitter_reference", remitter_reference, nullable=True
        )
        self.sort_code = self._define_str("sort_code", sort_code, nullable=True)
        self.status = self._define_str("status", status, nullable=True)
        self.updated_at = self._define_number("updated_at", updated_at, nullable=True)
        self.created_at_gw = self._define_str(
            "created_at_gw", created_at_gw, nullable=True
        )
        self.original_currency = self._define_str(
            "original_currency", original_currency, nullable=True
        )
        self.original_amount = self._define_str(
            "original_amount", original_amount, nullable=True
        )
        self.fx_rate = self._define_str("fx_rate", fx_rate, nullable=True)
