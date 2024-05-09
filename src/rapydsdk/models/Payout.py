from __future__ import annotations
from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Beneficiary import Beneficiary
from .PayoutFees import PayoutFees
from .Sender import Sender
from .PayoutStatus import PayoutStatus


@JsonMap({})
class Ewallets1(BaseModel):
    def __init__(
        self, amount: float = None, ewallet_id: str = None, percent: float = None
    ):
        self.amount = amount
        self.ewallet_id = ewallet_id
        self.percent = percent


@JsonMap({})
class Instructions1(BaseModel):
    def __init__(self, name: str = None, steps: List[dict] = None):
        self.name = name
        self.steps = steps


class PayoutType(Enum):
    CARD = "card"
    CASH = "cash"
    EWALLET = "ewallet"
    BANK = "bank"
    RAPYD_EWALLET = "rapyd_ewallet"

    def list():
        return list(map(lambda x: x.value, PayoutType._member_map_.values()))


@JsonMap({})
class Payout(BaseModel):
    def __init__(
        self,
        amount: float = None,
        beneficiary: Beneficiary = None,
        beneficiary_country: str = None,
        created_at: int = None,
        description: str = None,
        error: str = None,
        estimated_time_of_arrival: str = None,
        ewallets: List[Ewallets1] = None,
        expiration: float = None,
        fx_rate: str = None,
        gc_error_code: str = None,
        id: str = None,
        identifier_type: str = None,
        identifier_value: str = None,
        instructions: List[Instructions1] = None,
        instructions_value: dict = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        paid_amount: float = None,
        paid_at: str = None,
        payout_currency: str = None,
        payout_fees: PayoutFees = None,
        payout_method_type: str = None,
        payout_type: PayoutType = None,
        sender: Sender = None,
        sender_amount: float = None,
        sender_country: str = None,
        sender_currency: str = None,
        statement_descriptor: str = None,
        status: PayoutStatus = None,
    ):
        self.amount = amount
        self.beneficiary = self._define_object(beneficiary, Beneficiary)
        self.beneficiary_country = (
            self._pattern_matching(
                beneficiary_country,
                "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
                "beneficiary_country",
            )
            if beneficiary_country
            else None
        )
        self.created_at = created_at
        self.description = description
        self.error = error
        self.estimated_time_of_arrival = estimated_time_of_arrival
        self.ewallets = self._define_list(ewallets, Ewallets1)
        self.expiration = expiration
        self.fx_rate = fx_rate
        self.gc_error_code = gc_error_code
        self.id = id
        self.identifier_type = identifier_type
        self.identifier_value = identifier_value
        self.instructions = self._define_list(instructions, Instructions1)
        self.instructions_value = instructions_value
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.paid_amount = paid_amount
        self.paid_at = paid_at
        self.payout_currency = (
            self._pattern_matching(
                payout_currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "payout_currency",
            )
            if payout_currency
            else None
        )
        self.payout_fees = self._define_object(payout_fees, PayoutFees)
        self.payout_method_type = payout_method_type
        self.payout_type = (
            self._enum_matching(payout_type, PayoutType.list(), "payout_type")
            if payout_type
            else None
        )
        self.sender = self._define_object(sender, Sender)
        self.sender_amount = sender_amount
        self.sender_country = (
            self._pattern_matching(
                sender_country,
                "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
                "sender_country",
            )
            if sender_country
            else None
        )
        self.sender_currency = (
            self._pattern_matching(
                sender_currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "sender_currency",
            )
            if sender_currency
            else None
        )
        self.statement_descriptor = statement_descriptor
        self.status = (
            self._enum_matching(status, PayoutStatus.list(), "status")
            if status
            else None
        )
