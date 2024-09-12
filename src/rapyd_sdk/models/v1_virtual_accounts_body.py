from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class V1VirtualAccountsBody(BaseModel):
    """V1VirtualAccountsBody

    :param country: The country that the account number will be associated with. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.
    :type country: str
    :param currency: Currency of the account. Three-letter ISO 4217 code.
    :type currency: str
    :param description: Description of the account., defaults to None
    :type description: str, optional
    :param ewallet: ID of the wallet the bank account number is issued to. String starting with ewallet_.
    :type ewallet: str
    :param merchant_reference_id: ID of this account, as provided by the merchant. Limited to 45 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param requested_currency: *Currency received by the virtual account after conversion. Uppercase. One of the following: AUD - Australian Dollar EUR - Euro GBP - Pound Sterling HKD - Hong Kong Dollar SGD - Singapore Dollar USD - US Dollar When not specified, the funds appear in the walletâ€™s currency account for the currency of the transaction.*, defaults to None
    :type requested_currency: str, optional
    """

    def __init__(
        self,
        country: str,
        currency: str,
        ewallet: str,
        description: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        requested_currency: str = None,
    ):
        """V1VirtualAccountsBody

        :param country: The country that the account number will be associated with. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.
        :type country: str
        :param currency: Currency of the account. Three-letter ISO 4217 code.
        :type currency: str
        :param description: Description of the account., defaults to None
        :type description: str, optional
        :param ewallet: ID of the wallet the bank account number is issued to. String starting with ewallet_.
        :type ewallet: str
        :param merchant_reference_id: ID of this account, as provided by the merchant. Limited to 45 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param requested_currency: *Currency received by the virtual account after conversion. Uppercase. One of the following: AUD - Australian Dollar EUR - Euro GBP - Pound Sterling HKD - Hong Kong Dollar SGD - Singapore Dollar USD - US Dollar When not specified, the funds appear in the walletâ€™s currency account for the currency of the transaction.*, defaults to None
        :type requested_currency: str, optional
        """
        self.country = country
        self.currency = currency
        self.description = self._define_str("description", description, nullable=True)
        self.ewallet = ewallet
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.requested_currency = self._define_str(
            "requested_currency", requested_currency, nullable=True
        )
