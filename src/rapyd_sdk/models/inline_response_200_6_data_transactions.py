from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_6DataTransactions(BaseModel):
    """InlineResponse200_6DataTransactions

    :param id_: ID of the issued card transaction object. String starting with cit_., defaults to None
    :type id_: str, optional
    :param ewallet: ID of the wallet the bank account number is issued to. String starting with ewallet_., defaults to None
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
    :param original_amount: This field will show the initial transaction amount before conversion., defaults to None
    :type original_amount: float, optional
    :param original_currency: original_currency, defaults to None
    :type original_currency: str, optional
    :param fx_rate: This field will indicate the exchange rate applied for the currency conversion, defaults to None
    :type fx_rate: float, optional
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
        original_amount: float = None,
        original_currency: str = None,
        fx_rate: float = None,
    ):
        """InlineResponse200_6DataTransactions

        :param id_: ID of the issued card transaction object. String starting with cit_., defaults to None
        :type id_: str, optional
        :param ewallet: ID of the wallet the bank account number is issued to. String starting with ewallet_., defaults to None
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
        :param original_amount: This field will show the initial transaction amount before conversion., defaults to None
        :type original_amount: float, optional
        :param original_currency: original_currency, defaults to None
        :type original_currency: str, optional
        :param fx_rate: This field will indicate the exchange rate applied for the currency conversion, defaults to None
        :type fx_rate: float, optional
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
        self.original_amount = self._define_number(
            "original_amount", original_amount, nullable=True
        )
        self.original_currency = self._define_str(
            "original_currency",
            original_currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.fx_rate = self._define_number("fx_rate", fx_rate, nullable=True)
