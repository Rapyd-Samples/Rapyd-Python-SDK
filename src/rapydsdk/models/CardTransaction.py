from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class PosEntryMode(Enum):
    MAGSTRIPE = "magstripe"
    MANUAL_ENTERED = "manual_entered"
    EMV = "emv"
    EMV_STANDIN = "emv_standin"
    NFC = "nfc"
    NETWORK_TOKEN = "network_token"
    ECOMMERCE = "ecommerce"
    V3_DS_ECOMMERCE = "3ds_ecommerce"
    ADJUSTMENT = "adjustment"

    def list():
        return list(map(lambda x: x.value, PosEntryMode._member_map_.values()))


@JsonMap({})
class CardTransaction(BaseModel):
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
        id: str = None,
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
        self.amount = amount
        self.auth_code = auth_code
        self.authorization_approved_by = authorization_approved_by
        self.bin = bin
        self.card_authorization = card_authorization
        self.card_id = card_id
        self.card_program = card_program
        self.created_at = created_at
        self.currency = (
            self._pattern_matching(
                currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "currency",
            )
            if currency
            else None
        )
        self.fx_rate = fx_rate
        self.id = id
        self.issuing_txn_type = issuing_txn_type
        self.last4 = last4
        self.merchant_category_code = merchant_category_code
        self.merchant_name_location = merchant_name_location
        self.original_transaction_id = original_transaction_id
        self.original_txn_amount = original_txn_amount
        self.original_txn_currency = original_txn_currency
        self.pos_entry_mode = (
            self._enum_matching(pos_entry_mode, PosEntryMode.list(), "pos_entry_mode")
            if pos_entry_mode
            else None
        )
        self.retrieval_reference_number = retrieval_reference_number
        self.systems_trace_audit_number = systems_trace_audit_number
        self.wallet_transaction_id = wallet_transaction_id
