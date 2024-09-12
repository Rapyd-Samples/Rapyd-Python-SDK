from __future__ import annotations
from enum import Enum
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel
from .entity_type import EntityType
from .beneficiary import Beneficiary
from .sender import Sender


class V1PayoutsBody1BeneficiaryGuard(OneOfBaseModel):
    class_list = {"str": str, "Beneficiary": Beneficiary}


V1PayoutsBody1Beneficiary = Union[str, Beneficiary]


class V1PayoutsBody1BeneficiaryEntityType(Enum):
    """An enumeration representing different categories.

    :cvar INDIVIDUAL: "individual"
    :vartype INDIVIDUAL: str
    :cvar COMPANY: "company"
    :vartype COMPANY: str
    """

    INDIVIDUAL = "individual"
    COMPANY = "company"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                V1PayoutsBody1BeneficiaryEntityType._member_map_.values(),
            )
        )


class V1PayoutsBody1SenderGuard(OneOfBaseModel):
    class_list = {"str": str, "Sender": Sender}


V1PayoutsBody1Sender = Union[str, Sender]


@JsonMap({})
class V1PayoutsBody1(BaseModel):
    """V1PayoutsBody1

    :param beneficiary: String starting with beneficiary_ or the object describing the beneficiary.
    :type beneficiary: V1PayoutsBody1Beneficiary
    :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
    :type beneficiary_country: str, optional
    :param beneficiary_entity_type: Type of entity for the beneficiary. One of the following: individual, company
    :type beneficiary_entity_type: V1PayoutsBody1BeneficiaryEntityType
    :param confirm_automatically: Determines whether completion of the payout requires confirmation of the FX rate. Relevant to payouts with foreign exchange. Default is false., defaults to None
    :type confirm_automatically: bool, optional
    :param converstion_rate: conversion rate, defaults to None
    :type converstion_rate: float, optional
    :param description: Description of the payout transaction., defaults to None
    :type description: str, optional
    :param ewallet: ID of the wallet that the money is transferred from. String starting with ewallet_., defaults to None
    :type ewallet: str, optional
    :param expiration: Determines the day the payout expires, in Unix time. The payout must be completed before the start of this day. Relevant to cash payouts., defaults to None
    :type expiration: str, optional
    :param location: Location of the payout transaction., defaults to None
    :type location: str, optional
    :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payout_amount: Amount of the payout, in units of the currency defined in payout_currency. Mandatory when sender_amount is not used. Decimal.
    :type payout_amount: float
    :param payout_currency: payout_currency
    :type payout_currency: str
    :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country code. Required when the beneficiary does not have a default payout method type.
    :type payout_method_type: str
    :param payout_options: Payout options, defaults to None
    :type payout_options: dict, optional
    :param sender: String starting with sender_ or the object describing the sender.
    :type sender: V1PayoutsBody1Sender
    :param sender_country: sender_country
    :type sender_country: str
    :param sender_currency: sender_currency
    :type sender_currency: str
    :param sender_entity_type: sender_entity_type
    :type sender_entity_type: EntityType
    :param statement_descriptor: A statement that includes the reason for the payout. Limited to 35 characters., defaults to None
    :type statement_descriptor: str, optional
    """

    def __init__(
        self,
        beneficiary: V1PayoutsBody1Beneficiary,
        beneficiary_entity_type: V1PayoutsBody1BeneficiaryEntityType,
        payout_amount: float,
        payout_currency: str,
        payout_method_type: str,
        sender: V1PayoutsBody1Sender,
        sender_country: str,
        sender_currency: str,
        sender_entity_type: EntityType,
        beneficiary_country: str = None,
        confirm_automatically: bool = None,
        converstion_rate: float = None,
        description: str = None,
        ewallet: str = None,
        expiration: str = None,
        location: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payout_options: dict = None,
        statement_descriptor: str = None,
    ):
        """V1PayoutsBody1

        :param beneficiary: String starting with beneficiary_ or the object describing the beneficiary.
        :type beneficiary: V1PayoutsBody1Beneficiary
        :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
        :type beneficiary_country: str, optional
        :param beneficiary_entity_type: Type of entity for the beneficiary. One of the following: individual, company
        :type beneficiary_entity_type: V1PayoutsBody1BeneficiaryEntityType
        :param confirm_automatically: Determines whether completion of the payout requires confirmation of the FX rate. Relevant to payouts with foreign exchange. Default is false., defaults to None
        :type confirm_automatically: bool, optional
        :param converstion_rate: conversion rate, defaults to None
        :type converstion_rate: float, optional
        :param description: Description of the payout transaction., defaults to None
        :type description: str, optional
        :param ewallet: ID of the wallet that the money is transferred from. String starting with ewallet_., defaults to None
        :type ewallet: str, optional
        :param expiration: Determines the day the payout expires, in Unix time. The payout must be completed before the start of this day. Relevant to cash payouts., defaults to None
        :type expiration: str, optional
        :param location: Location of the payout transaction., defaults to None
        :type location: str, optional
        :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payout_amount: Amount of the payout, in units of the currency defined in payout_currency. Mandatory when sender_amount is not used. Decimal.
        :type payout_amount: float
        :param payout_currency: payout_currency
        :type payout_currency: str
        :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country code. Required when the beneficiary does not have a default payout method type.
        :type payout_method_type: str
        :param payout_options: Payout options, defaults to None
        :type payout_options: dict, optional
        :param sender: String starting with sender_ or the object describing the sender.
        :type sender: V1PayoutsBody1Sender
        :param sender_country: sender_country
        :type sender_country: str
        :param sender_currency: sender_currency
        :type sender_currency: str
        :param sender_entity_type: sender_entity_type
        :type sender_entity_type: EntityType
        :param statement_descriptor: A statement that includes the reason for the payout. Limited to 35 characters., defaults to None
        :type statement_descriptor: str, optional
        """
        self.beneficiary = V1PayoutsBody1BeneficiaryGuard.return_one_of(beneficiary)
        self.beneficiary_country = self._define_str(
            "beneficiary_country", beneficiary_country, nullable=True
        )
        self.beneficiary_entity_type = self._enum_matching(
            beneficiary_entity_type,
            V1PayoutsBody1BeneficiaryEntityType.list(),
            "beneficiary_entity_type",
        )
        self.confirm_automatically = confirm_automatically
        self.converstion_rate = self._define_number(
            "converstion_rate", converstion_rate, nullable=True
        )
        self.description = self._define_str("description", description, nullable=True)
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.expiration = self._define_str("expiration", expiration, nullable=True)
        self.location = self._define_str("location", location, nullable=True)
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.payout_amount = payout_amount
        self.payout_currency = self._define_str(
            "payout_currency",
            payout_currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.payout_method_type = payout_method_type
        self.payout_options = payout_options
        self.sender = V1PayoutsBody1SenderGuard.return_one_of(sender)
        self.sender_country = self._define_str(
            "sender_country",
            sender_country,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.sender_currency = self._define_str(
            "sender_currency",
            sender_currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.sender_entity_type = self._enum_matching(
            sender_entity_type, EntityType.list(), "sender_entity_type"
        )
        self.statement_descriptor = self._define_str(
            "statement_descriptor", statement_descriptor, nullable=True
        )


class V1PayoutsBody2BeneficiaryGuard(OneOfBaseModel):
    class_list = {"str": str, "Beneficiary": Beneficiary}


V1PayoutsBody2Beneficiary = Union[str, Beneficiary]


class V1PayoutsBody2BeneficiaryEntityType(Enum):
    """An enumeration representing different categories.

    :cvar INDIVIDUAL: "individual"
    :vartype INDIVIDUAL: str
    :cvar COMPANY: "company"
    :vartype COMPANY: str
    """

    INDIVIDUAL = "individual"
    COMPANY = "company"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                V1PayoutsBody2BeneficiaryEntityType._member_map_.values(),
            )
        )


class V1PayoutsBody2SenderGuard(OneOfBaseModel):
    class_list = {"str": str, "Sender": Sender}


V1PayoutsBody2Sender = Union[str, Sender]


@JsonMap({})
class V1PayoutsBody2(BaseModel):
    """V1PayoutsBody2

    :param beneficiary: String starting with beneficiary_ or the object describing the beneficiary.
    :type beneficiary: V1PayoutsBody2Beneficiary
    :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
    :type beneficiary_country: str, optional
    :param beneficiary_entity_type: Type of entity for the beneficiary. One of the following: individual, company
    :type beneficiary_entity_type: V1PayoutsBody2BeneficiaryEntityType
    :param confirm_automatically: Determines whether completion of the payout requires confirmation of the FX rate. Relevant to payouts with foreign exchange. Default is false., defaults to None
    :type confirm_automatically: bool, optional
    :param converstion_rate: conversion rate, defaults to None
    :type converstion_rate: float, optional
    :param description: Description of the payout transaction., defaults to None
    :type description: str, optional
    :param ewallet: ID of the wallet that the money is transferred from. String starting with ewallet_., defaults to None
    :type ewallet: str, optional
    :param expiration: Determines the day the payout expires, in Unix time. The payout must be completed before the start of this day. Relevant to cash payouts., defaults to None
    :type expiration: str, optional
    :param location: Location of the payout transaction., defaults to None
    :type location: str, optional
    :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payout_amount: Amount of the payout, in units of the currency defined in payout_currency. Mandatory when sender_amount is not used. Decimal.
    :type payout_amount: float
    :param payout_currency: payout_currency
    :type payout_currency: str
    :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country code. Required when the beneficiary does not have a default payout method type., defaults to None
    :type payout_method_type: str, optional
    :param payout_options: Payout options, defaults to None
    :type payout_options: dict, optional
    :param sender: String starting with sender_ or the object describing the sender.
    :type sender: V1PayoutsBody2Sender
    :param sender_country: sender_country
    :type sender_country: str
    :param sender_currency: sender_currency
    :type sender_currency: str
    :param sender_entity_type: sender_entity_type
    :type sender_entity_type: EntityType
    :param statement_descriptor: A statement that includes the reason for the payout. Limited to 35 characters., defaults to None
    :type statement_descriptor: str, optional
    """

    def __init__(
        self,
        beneficiary: V1PayoutsBody2Beneficiary,
        beneficiary_entity_type: V1PayoutsBody2BeneficiaryEntityType,
        payout_amount: float,
        payout_currency: str,
        sender: V1PayoutsBody2Sender,
        sender_country: str,
        sender_currency: str,
        sender_entity_type: EntityType,
        beneficiary_country: str = None,
        confirm_automatically: bool = None,
        converstion_rate: float = None,
        description: str = None,
        ewallet: str = None,
        expiration: str = None,
        location: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payout_method_type: str = None,
        payout_options: dict = None,
        statement_descriptor: str = None,
    ):
        """V1PayoutsBody2

        :param beneficiary: String starting with beneficiary_ or the object describing the beneficiary.
        :type beneficiary: V1PayoutsBody2Beneficiary
        :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
        :type beneficiary_country: str, optional
        :param beneficiary_entity_type: Type of entity for the beneficiary. One of the following: individual, company
        :type beneficiary_entity_type: V1PayoutsBody2BeneficiaryEntityType
        :param confirm_automatically: Determines whether completion of the payout requires confirmation of the FX rate. Relevant to payouts with foreign exchange. Default is false., defaults to None
        :type confirm_automatically: bool, optional
        :param converstion_rate: conversion rate, defaults to None
        :type converstion_rate: float, optional
        :param description: Description of the payout transaction., defaults to None
        :type description: str, optional
        :param ewallet: ID of the wallet that the money is transferred from. String starting with ewallet_., defaults to None
        :type ewallet: str, optional
        :param expiration: Determines the day the payout expires, in Unix time. The payout must be completed before the start of this day. Relevant to cash payouts., defaults to None
        :type expiration: str, optional
        :param location: Location of the payout transaction., defaults to None
        :type location: str, optional
        :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payout_amount: Amount of the payout, in units of the currency defined in payout_currency. Mandatory when sender_amount is not used. Decimal.
        :type payout_amount: float
        :param payout_currency: payout_currency
        :type payout_currency: str
        :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country code. Required when the beneficiary does not have a default payout method type., defaults to None
        :type payout_method_type: str, optional
        :param payout_options: Payout options, defaults to None
        :type payout_options: dict, optional
        :param sender: String starting with sender_ or the object describing the sender.
        :type sender: V1PayoutsBody2Sender
        :param sender_country: sender_country
        :type sender_country: str
        :param sender_currency: sender_currency
        :type sender_currency: str
        :param sender_entity_type: sender_entity_type
        :type sender_entity_type: EntityType
        :param statement_descriptor: A statement that includes the reason for the payout. Limited to 35 characters., defaults to None
        :type statement_descriptor: str, optional
        """
        self.beneficiary = V1PayoutsBody2BeneficiaryGuard.return_one_of(beneficiary)
        self.beneficiary_country = self._define_str(
            "beneficiary_country", beneficiary_country, nullable=True
        )
        self.beneficiary_entity_type = self._enum_matching(
            beneficiary_entity_type,
            V1PayoutsBody2BeneficiaryEntityType.list(),
            "beneficiary_entity_type",
        )
        self.confirm_automatically = confirm_automatically
        self.converstion_rate = self._define_number(
            "converstion_rate", converstion_rate, nullable=True
        )
        self.description = self._define_str("description", description, nullable=True)
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.expiration = self._define_str("expiration", expiration, nullable=True)
        self.location = self._define_str("location", location, nullable=True)
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.payout_amount = payout_amount
        self.payout_currency = self._define_str(
            "payout_currency",
            payout_currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.payout_method_type = self._define_str(
            "payout_method_type", payout_method_type, nullable=True
        )
        self.payout_options = payout_options
        self.sender = V1PayoutsBody2SenderGuard.return_one_of(sender)
        self.sender_country = self._define_str(
            "sender_country",
            sender_country,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.sender_currency = self._define_str(
            "sender_currency",
            sender_currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.sender_entity_type = self._enum_matching(
            sender_entity_type, EntityType.list(), "sender_entity_type"
        )
        self.statement_descriptor = self._define_str(
            "statement_descriptor", statement_descriptor, nullable=True
        )


class V1PayoutsBodyGuard(OneOfBaseModel):
    class_list = {"V1PayoutsBody1": V1PayoutsBody1, "V1PayoutsBody2": V1PayoutsBody2}


V1PayoutsBody = Union[V1PayoutsBody1, V1PayoutsBody2]
