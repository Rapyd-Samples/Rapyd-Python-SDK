from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .beneficiary import Beneficiary
from .payout_ewallets import PayoutEwallets
from .payout_instructions import PayoutInstructions
from .fee import Fee
from .sender import Sender
from .payout_status import PayoutStatus


class PayoutType(Enum):
    """An enumeration representing different categories.

    :cvar CARD: "card"
    :vartype CARD: str
    :cvar CASH: "cash"
    :vartype CASH: str
    :cvar EWALLET: "ewallet"
    :vartype EWALLET: str
    :cvar BANK: "bank"
    :vartype BANK: str
    :cvar RAPYDEWALLET: "rapyd_ewallet"
    :vartype RAPYDEWALLET: str
    """

    CARD = "card"
    CASH = "cash"
    EWALLET = "ewallet"
    BANK = "bank"
    RAPYDEWALLET = "rapyd_ewallet"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PayoutType._member_map_.values()))


@JsonMap({"id_": "id"})
class Payout(BaseModel):
    """Payout

    :param amount: Amount of the payout, in units defined by payout_currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. Same as payout_amount. Response only., defaults to None
    :type amount: float, optional
    :param beneficiary: beneficiary, defaults to None
    :type beneficiary: Beneficiary, optional
    :param beneficiary_country: beneficiary_country, defaults to None
    :type beneficiary_country: str, optional
    :param created_at: Time of creation of the payout, in Unix time. Response only., defaults to None
    :type created_at: int, optional
    :param description: Description of the payout transaction., defaults to None
    :type description: str, optional
    :param error: Indicates the error code of the last unsuccessful operation on the Payout object., defaults to None
    :type error: str, optional
    :param estimated_time_of_arrival: The estimated time period in which the beneficiary will receive the funds., defaults to None
    :type estimated_time_of_arrival: str, optional
    :param ewallets: An array of one object, which contains the following fields: * ewallet_id - The ID of the wallet that the money is transferred from, a string starting with ewallet_. * amount - Amount of the transaction in currency units defined in currency. * percent - A decimal number representing a percentage of the total payout. Response only., defaults to None
    :type ewallets: List[PayoutEwallets], optional
    :param expiration: Determines the day the payout expires, in Unix time. The payout must be completed before the start of this day. Relevant to cash payout methods where the is_expirable field is true in the response to List Payout Method Types., defaults to None
    :type expiration: float, optional
    :param fx_rate: Currency conversion rate for the payout. Decimal. Response only., defaults to None
    :type fx_rate: str, optional
    :param gc_error_code: Reserved. Response only., defaults to None
    :type gc_error_code: str, optional
    :param id_: ID of the payout. String starting with payout_., defaults to None
    :type id_: str, optional
    :param identifier_type: Reserved. Response only., defaults to None
    :type identifier_type: str, optional
    :param identifier_value: Reserved. Response only., defaults to None
    :type identifier_value: str, optional
    :param instructions: Describes how the customer collects the payout. Contains the following fields: * name - Short description of the instructions. * steps - A 'steps' object containing a list of steps for the customer to take. Each step is named stepN, where N is an integer. , defaults to None
    :type instructions: List[PayoutInstructions], optional
    :param instructions_value: Additional information from the merchant. For example, the merchant's instructions and transaction number that must be presented for collecting the payout., defaults to None
    :type instructions_value: dict, optional
    :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param paid_amount: Cumulative amount received by the beneficiary, in units defined by payout_currency. Response only., defaults to None
    :type paid_amount: float, optional
    :param paid_at: Time of the payout, in Unix time. Response only., defaults to None
    :type paid_at: str, optional
    :param payout_currency: payout_currency, defaults to None
    :type payout_currency: str, optional
    :param payout_fees: payout_fees, defaults to None
    :type payout_fees: Fee, optional
    :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country computed., defaults to None
    :type payout_method_type: str, optional
    :param payout_type: The type of the payout method., defaults to None
    :type payout_type: PayoutType, optional
    :param sender: sender, defaults to None
    :type sender: Sender, optional
    :param sender_amount: Amount that the sender is paying in units of the currency defined in sender_currency.  This amount remains the same regardless of FX fees. Required when payout_amount is not used. Decimal. , defaults to None
    :type sender_amount: float, optional
    :param sender_country: sender_country, defaults to None
    :type sender_country: str, optional
    :param sender_currency: sender_currency, defaults to None
    :type sender_currency: str, optional
    :param statement_descriptor: A statement that includes the reason for the payout. Limited to 35 characters., defaults to None
    :type statement_descriptor: str, optional
    :param status: status, defaults to None
    :type status: PayoutStatus, optional
    """

    def __init__(
        self,
        amount: float = None,
        beneficiary: Beneficiary = None,
        beneficiary_country: str = None,
        created_at: int = None,
        description: str = None,
        error: str = None,
        estimated_time_of_arrival: str = None,
        ewallets: List[PayoutEwallets] = None,
        expiration: float = None,
        fx_rate: str = None,
        gc_error_code: str = None,
        id_: str = None,
        identifier_type: str = None,
        identifier_value: str = None,
        instructions: List[PayoutInstructions] = None,
        instructions_value: dict = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        paid_amount: float = None,
        paid_at: str = None,
        payout_currency: str = None,
        payout_fees: Fee = None,
        payout_method_type: str = None,
        payout_type: PayoutType = None,
        sender: Sender = None,
        sender_amount: float = None,
        sender_country: str = None,
        sender_currency: str = None,
        statement_descriptor: str = None,
        status: PayoutStatus = None,
    ):
        """Payout

        :param amount: Amount of the payout, in units defined by payout_currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. Same as payout_amount. Response only., defaults to None
        :type amount: float, optional
        :param beneficiary: beneficiary, defaults to None
        :type beneficiary: Beneficiary, optional
        :param beneficiary_country: beneficiary_country, defaults to None
        :type beneficiary_country: str, optional
        :param created_at: Time of creation of the payout, in Unix time. Response only., defaults to None
        :type created_at: int, optional
        :param description: Description of the payout transaction., defaults to None
        :type description: str, optional
        :param error: Indicates the error code of the last unsuccessful operation on the Payout object., defaults to None
        :type error: str, optional
        :param estimated_time_of_arrival: The estimated time period in which the beneficiary will receive the funds., defaults to None
        :type estimated_time_of_arrival: str, optional
        :param ewallets: An array of one object, which contains the following fields: * ewallet_id - The ID of the wallet that the money is transferred from, a string starting with ewallet_. * amount - Amount of the transaction in currency units defined in currency. * percent - A decimal number representing a percentage of the total payout. Response only., defaults to None
        :type ewallets: List[PayoutEwallets], optional
        :param expiration: Determines the day the payout expires, in Unix time. The payout must be completed before the start of this day. Relevant to cash payout methods where the is_expirable field is true in the response to List Payout Method Types., defaults to None
        :type expiration: float, optional
        :param fx_rate: Currency conversion rate for the payout. Decimal. Response only., defaults to None
        :type fx_rate: str, optional
        :param gc_error_code: Reserved. Response only., defaults to None
        :type gc_error_code: str, optional
        :param id_: ID of the payout. String starting with payout_., defaults to None
        :type id_: str, optional
        :param identifier_type: Reserved. Response only., defaults to None
        :type identifier_type: str, optional
        :param identifier_value: Reserved. Response only., defaults to None
        :type identifier_value: str, optional
        :param instructions: Describes how the customer collects the payout. Contains the following fields: * name - Short description of the instructions. * steps - A 'steps' object containing a list of steps for the customer to take. Each step is named stepN, where N is an integer. , defaults to None
        :type instructions: List[PayoutInstructions], optional
        :param instructions_value: Additional information from the merchant. For example, the merchant's instructions and transaction number that must be presented for collecting the payout., defaults to None
        :type instructions_value: dict, optional
        :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param paid_amount: Cumulative amount received by the beneficiary, in units defined by payout_currency. Response only., defaults to None
        :type paid_amount: float, optional
        :param paid_at: Time of the payout, in Unix time. Response only., defaults to None
        :type paid_at: str, optional
        :param payout_currency: payout_currency, defaults to None
        :type payout_currency: str, optional
        :param payout_fees: payout_fees, defaults to None
        :type payout_fees: Fee, optional
        :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country computed., defaults to None
        :type payout_method_type: str, optional
        :param payout_type: The type of the payout method., defaults to None
        :type payout_type: PayoutType, optional
        :param sender: sender, defaults to None
        :type sender: Sender, optional
        :param sender_amount: Amount that the sender is paying in units of the currency defined in sender_currency.  This amount remains the same regardless of FX fees. Required when payout_amount is not used. Decimal. , defaults to None
        :type sender_amount: float, optional
        :param sender_country: sender_country, defaults to None
        :type sender_country: str, optional
        :param sender_currency: sender_currency, defaults to None
        :type sender_currency: str, optional
        :param statement_descriptor: A statement that includes the reason for the payout. Limited to 35 characters., defaults to None
        :type statement_descriptor: str, optional
        :param status: status, defaults to None
        :type status: PayoutStatus, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.beneficiary = self._define_object(beneficiary, Beneficiary)
        self.beneficiary_country = self._define_str(
            "beneficiary_country",
            beneficiary_country,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.description = self._define_str("description", description, nullable=True)
        self.error = self._define_str("error", error, nullable=True)
        self.estimated_time_of_arrival = self._define_str(
            "estimated_time_of_arrival", estimated_time_of_arrival, nullable=True
        )
        self.ewallets = self._define_list(ewallets, PayoutEwallets)
        self.expiration = self._define_number("expiration", expiration, nullable=True)
        self.fx_rate = self._define_str("fx_rate", fx_rate, nullable=True)
        self.gc_error_code = self._define_str(
            "gc_error_code", gc_error_code, nullable=True
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.identifier_type = self._define_str(
            "identifier_type", identifier_type, nullable=True
        )
        self.identifier_value = self._define_str(
            "identifier_value", identifier_value, nullable=True
        )
        self.instructions = self._define_list(instructions, PayoutInstructions)
        self.instructions_value = instructions_value
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.paid_amount = self._define_number(
            "paid_amount", paid_amount, nullable=True
        )
        self.paid_at = self._define_str("paid_at", paid_at, nullable=True)
        self.payout_currency = self._define_str(
            "payout_currency",
            payout_currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.payout_fees = self._define_object(payout_fees, Fee)
        self.payout_method_type = self._define_str(
            "payout_method_type", payout_method_type, nullable=True
        )
        self.payout_type = (
            self._enum_matching(payout_type, PayoutType.list(), "payout_type")
            if payout_type
            else None
        )
        self.sender = self._define_object(sender, Sender)
        self.sender_amount = self._define_number(
            "sender_amount", sender_amount, nullable=True
        )
        self.sender_country = self._define_str(
            "sender_country",
            sender_country,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.sender_currency = self._define_str(
            "sender_currency",
            sender_currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.statement_descriptor = self._define_str(
            "statement_descriptor", statement_descriptor, nullable=True
        )
        self.status = (
            self._enum_matching(status, PayoutStatus.list(), "status")
            if status
            else None
        )
