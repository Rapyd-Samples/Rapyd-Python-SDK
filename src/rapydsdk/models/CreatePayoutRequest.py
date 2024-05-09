from __future__ import annotations
from enum import Enum
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .EntityType import EntityType
from .Beneficiary import Beneficiary
from .Sender import Sender


class Beneficiary1Guard(OneOfBaseModel):
    class_list = {"str": str, "Beneficiary": Beneficiary}


Beneficiary1 = Union[str, Beneficiary]


class BeneficiaryEntityType(Enum):
    INDIVIDUAL = "individual"
    COMPANY = "company"

    def list():
        return list(map(lambda x: x.value, BeneficiaryEntityType._member_map_.values()))


class Sender1Guard(OneOfBaseModel):
    class_list = {"str": str, "Sender": Sender}


Sender1 = Union[str, Sender]


@JsonMap({})
class CreatePayoutRequest1(BaseModel):
    def __init__(
        self,
        payout_method_type: str,
        beneficiary: Beneficiary1 = None,
        beneficiary_country: str = None,
        beneficiary_entity_type: BeneficiaryEntityType = None,
        confirm_automatically: bool = None,
        converstion_rate: float = None,
        description: str = None,
        ewallet: str = None,
        expiration: str = None,
        location: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payout_amount: float = None,
        payout_currency: str = None,
        payout_options: dict = None,
        sender: Sender1 = None,
        sender_country: str = None,
        sender_currency: str = None,
        sender_entity_type: EntityType = None,
        statement_descriptor: str = None,
    ):
        self.beneficiary = Beneficiary1Guard.return_one_of(beneficiary)
        self.beneficiary_country = beneficiary_country
        self.beneficiary_entity_type = (
            self._enum_matching(
                beneficiary_entity_type,
                BeneficiaryEntityType.list(),
                "beneficiary_entity_type",
            )
            if beneficiary_entity_type
            else None
        )
        self.confirm_automatically = confirm_automatically
        self.converstion_rate = converstion_rate
        self.description = description
        self.ewallet = ewallet
        self.expiration = expiration
        self.location = location
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.payout_amount = payout_amount
        self.payout_currency = (
            self._pattern_matching(
                payout_currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "payout_currency",
            )
            if payout_currency
            else None
        )
        self.payout_method_type = payout_method_type
        self.payout_options = payout_options
        self.sender = Sender1Guard.return_one_of(sender)
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
        self.sender_entity_type = (
            self._enum_matching(
                sender_entity_type, EntityType.list(), "sender_entity_type"
            )
            if sender_entity_type
            else None
        )
        self.statement_descriptor = statement_descriptor


class Beneficiary2Guard(OneOfBaseModel):
    class_list = {"str": str, "Beneficiary": Beneficiary}


Beneficiary2 = Union[str, Beneficiary]


class BeneficiaryEntityType1(Enum):
    INDIVIDUAL = "individual"
    COMPANY = "company"

    def list():
        return list(
            map(lambda x: x.value, BeneficiaryEntityType1._member_map_.values())
        )


class Sender2Guard(OneOfBaseModel):
    class_list = {"str": str, "Sender": Sender}


Sender2 = Union[str, Sender]


@JsonMap({})
class CreatePayoutRequest2(BaseModel):
    def __init__(
        self,
        beneficiary: Beneficiary2 = None,
        beneficiary_country: str = None,
        beneficiary_entity_type: BeneficiaryEntityType1 = None,
        confirm_automatically: bool = None,
        converstion_rate: float = None,
        description: str = None,
        ewallet: str = None,
        expiration: str = None,
        location: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payout_amount: float = None,
        payout_currency: str = None,
        payout_method_type: str = None,
        payout_options: dict = None,
        sender: Sender2 = None,
        sender_country: str = None,
        sender_currency: str = None,
        sender_entity_type: EntityType = None,
        statement_descriptor: str = None,
    ):
        self.beneficiary = Beneficiary2Guard.return_one_of(beneficiary)
        self.beneficiary_country = beneficiary_country
        self.beneficiary_entity_type = (
            self._enum_matching(
                beneficiary_entity_type,
                BeneficiaryEntityType1.list(),
                "beneficiary_entity_type",
            )
            if beneficiary_entity_type
            else None
        )
        self.confirm_automatically = confirm_automatically
        self.converstion_rate = converstion_rate
        self.description = description
        self.ewallet = ewallet
        self.expiration = expiration
        self.location = location
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.payout_amount = payout_amount
        self.payout_currency = (
            self._pattern_matching(
                payout_currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "payout_currency",
            )
            if payout_currency
            else None
        )
        self.payout_method_type = payout_method_type
        self.payout_options = payout_options
        self.sender = Sender2Guard.return_one_of(sender)
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
        self.sender_entity_type = (
            self._enum_matching(
                sender_entity_type, EntityType.list(), "sender_entity_type"
            )
            if sender_entity_type
            else None
        )
        self.statement_descriptor = statement_descriptor


class CreatePayoutRequestGuard(OneOfBaseModel):
    class_list = {
        "CreatePayoutRequest1": CreatePayoutRequest1,
        "CreatePayoutRequest2": CreatePayoutRequest2,
    }


CreatePayoutRequest = Union[CreatePayoutRequest1, CreatePayoutRequest2]
