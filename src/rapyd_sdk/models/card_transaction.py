from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class PosEntryMode(Enum):
    """An enumeration representing different categories.

    :cvar MAGSTRIPE: "magstripe"
    :vartype MAGSTRIPE: str
    :cvar MANUALENTERED: "manual_entered"
    :vartype MANUALENTERED: str
    :cvar EMV: "emv"
    :vartype EMV: str
    :cvar EMVSTANDIN: "emv_standin"
    :vartype EMVSTANDIN: str
    :cvar NFC: "nfc"
    :vartype NFC: str
    :cvar NETWORKTOKEN: "network_token"
    :vartype NETWORKTOKEN: str
    :cvar ECOMMERCE: "ecommerce"
    :vartype ECOMMERCE: str
    :cvar _3DSECOMMERCE: "3ds_ecommerce"
    :vartype _3DSECOMMERCE: str
    :cvar ADJUSTMENT: "adjustment"
    :vartype ADJUSTMENT: str
    """

    MAGSTRIPE = "magstripe"
    MANUALENTERED = "manual_entered"
    EMV = "emv"
    EMVSTANDIN = "emv_standin"
    NFC = "nfc"
    NETWORKTOKEN = "network_token"
    ECOMMERCE = "ecommerce"
    _3DSECOMMERCE = "3ds_ecommerce"
    ADJUSTMENT = "adjustment"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PosEntryMode._member_map_.values()))


@JsonMap({"id_": "id"})
class CardTransaction(BaseModel):
    """CardTransaction

    :param amount: Amount of the transaction, in units defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. Response only., defaults to None
    :type amount: float, optional
    :param auth_code: Authorization code sent to the merchant. Relevant to authorizations approved by Rapyd. Response only., defaults to None
    :type auth_code: str, optional
    :param authorization_approved_by: Approver of the transaction when remote authorization is used. See Remote Authorization., defaults to None
    :type authorization_approved_by: str, optional
    :param bin: The first 6 digits of the card number. Response only., defaults to None
    :type bin: str, optional
    :param card_authorization: card_authorization, defaults to None
    :type card_authorization: str, optional
    :param card_id: ID of the card. String starting with card_. Response only., defaults to None
    :type card_id: str, optional
    :param card_program: ID of the card program that the card is issued from. String starting with cardprog_. Response only., defaults to None
    :type card_program: str, optional
    :param created_at: Time of creation of the transaction object, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param fx_rate: The exchange rate. Response only., defaults to None
    :type fx_rate: float, optional
    :param id_: ID of the issued card transaction object. String starting with cit_., defaults to None
    :type id_: str, optional
    :param issuing_txn_type: Type of the transaction., defaults to None
    :type issuing_txn_type: str, optional
    :param last4: The last 4 digits of the card number. Response only., defaults to None
    :type last4: str, optional
    :param merchant_category_code: Four-digit merchant category code (MCC) of the initiator of the transaction, as defined in ISO 18245. Response only., defaults to None
    :type merchant_category_code: str, optional
    :param merchant_name_location: Name and location of the merchant. Maximum 40 characters. Response only., defaults to None
    :type merchant_name_location: str, optional
    :param original_transaction_id: ID of the original card transaction. Response only., defaults to None
    :type original_transaction_id: str, optional
    :param original_txn_amount: Original amount for FX transactions, when currency is different from original_txn_currency. Response only., defaults to None
    :type original_txn_amount: float, optional
    :param original_txn_currency: Original currency in FX transaction. Three-letter ISO 4217 code. Response only., defaults to None
    :type original_txn_currency: str, optional
    :param pos_entry_mode: The mode of the POS entry. One of the following, defaults to None
    :type pos_entry_mode: PosEntryMode, optional
    :param retrieval_reference_number: Reserved., defaults to None
    :type retrieval_reference_number: str, optional
    :param systems_trace_audit_number: Reserved, defaults to None
    :type systems_trace_audit_number: str, optional
    :param wallet_transaction_id: ID of the wallet transaction. String starting with wt_. Response only., defaults to None
    :type wallet_transaction_id: str, optional
    """

    def __init__(
        self,
        amount: float = None,
        auth_code: str = None,
        authorization_approved_by: str = None,
        bin: str = None,
        card_authorization: str = None,
        card_id: str = None,
        card_program: str = None,
        created_at: float = None,
        currency: str = None,
        fx_rate: float = None,
        id_: str = None,
        issuing_txn_type: str = None,
        last4: str = None,
        merchant_category_code: str = None,
        merchant_name_location: str = None,
        original_transaction_id: str = None,
        original_txn_amount: float = None,
        original_txn_currency: str = None,
        pos_entry_mode: PosEntryMode = None,
        retrieval_reference_number: str = None,
        systems_trace_audit_number: str = None,
        wallet_transaction_id: str = None,
    ):
        """CardTransaction

        :param amount: Amount of the transaction, in units defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. Response only., defaults to None
        :type amount: float, optional
        :param auth_code: Authorization code sent to the merchant. Relevant to authorizations approved by Rapyd. Response only., defaults to None
        :type auth_code: str, optional
        :param authorization_approved_by: Approver of the transaction when remote authorization is used. See Remote Authorization., defaults to None
        :type authorization_approved_by: str, optional
        :param bin: The first 6 digits of the card number. Response only., defaults to None
        :type bin: str, optional
        :param card_authorization: card_authorization, defaults to None
        :type card_authorization: str, optional
        :param card_id: ID of the card. String starting with card_. Response only., defaults to None
        :type card_id: str, optional
        :param card_program: ID of the card program that the card is issued from. String starting with cardprog_. Response only., defaults to None
        :type card_program: str, optional
        :param created_at: Time of creation of the transaction object, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param fx_rate: The exchange rate. Response only., defaults to None
        :type fx_rate: float, optional
        :param id_: ID of the issued card transaction object. String starting with cit_., defaults to None
        :type id_: str, optional
        :param issuing_txn_type: Type of the transaction., defaults to None
        :type issuing_txn_type: str, optional
        :param last4: The last 4 digits of the card number. Response only., defaults to None
        :type last4: str, optional
        :param merchant_category_code: Four-digit merchant category code (MCC) of the initiator of the transaction, as defined in ISO 18245. Response only., defaults to None
        :type merchant_category_code: str, optional
        :param merchant_name_location: Name and location of the merchant. Maximum 40 characters. Response only., defaults to None
        :type merchant_name_location: str, optional
        :param original_transaction_id: ID of the original card transaction. Response only., defaults to None
        :type original_transaction_id: str, optional
        :param original_txn_amount: Original amount for FX transactions, when currency is different from original_txn_currency. Response only., defaults to None
        :type original_txn_amount: float, optional
        :param original_txn_currency: Original currency in FX transaction. Three-letter ISO 4217 code. Response only., defaults to None
        :type original_txn_currency: str, optional
        :param pos_entry_mode: The mode of the POS entry. One of the following, defaults to None
        :type pos_entry_mode: PosEntryMode, optional
        :param retrieval_reference_number: Reserved., defaults to None
        :type retrieval_reference_number: str, optional
        :param systems_trace_audit_number: Reserved, defaults to None
        :type systems_trace_audit_number: str, optional
        :param wallet_transaction_id: ID of the wallet transaction. String starting with wt_. Response only., defaults to None
        :type wallet_transaction_id: str, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.auth_code = self._define_str("auth_code", auth_code, nullable=True)
        self.authorization_approved_by = self._define_str(
            "authorization_approved_by", authorization_approved_by, nullable=True
        )
        self.bin = self._define_str("bin", bin, nullable=True)
        self.card_authorization = self._define_str(
            "card_authorization", card_authorization, nullable=True
        )
        self.card_id = self._define_str("card_id", card_id, nullable=True)
        self.card_program = self._define_str(
            "card_program", card_program, nullable=True
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.fx_rate = self._define_number("fx_rate", fx_rate, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.issuing_txn_type = self._define_str(
            "issuing_txn_type", issuing_txn_type, nullable=True
        )
        self.last4 = self._define_str("last4", last4, nullable=True)
        self.merchant_category_code = self._define_str(
            "merchant_category_code", merchant_category_code, nullable=True
        )
        self.merchant_name_location = self._define_str(
            "merchant_name_location", merchant_name_location, nullable=True
        )
        self.original_transaction_id = self._define_str(
            "original_transaction_id", original_transaction_id, nullable=True
        )
        self.original_txn_amount = self._define_number(
            "original_txn_amount", original_txn_amount, nullable=True
        )
        self.original_txn_currency = self._define_str(
            "original_txn_currency", original_txn_currency, nullable=True
        )
        self.pos_entry_mode = (
            self._enum_matching(pos_entry_mode, PosEntryMode.list(), "pos_entry_mode")
            if pos_entry_mode
            else None
        )
        self.retrieval_reference_number = self._define_str(
            "retrieval_reference_number", retrieval_reference_number, nullable=True
        )
        self.systems_trace_audit_number = self._define_str(
            "systems_trace_audit_number", systems_trace_audit_number, nullable=True
        )
        self.wallet_transaction_id = self._define_str(
            "wallet_transaction_id", wallet_transaction_id, nullable=True
        )
