from __future__ import annotations
from enum import Enum
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Address import Address
from .ClientDetailsObject import ClientDetailsObject
from .Ewallet import Ewallet
from .PaymentFee import PaymentFee


class InitiationType(Enum):
    CUSTOMER_PRESENT = "customer_present"
    INSTALLMENT = "installment"
    MOTO = "moto"
    RECURRING = "recurring"
    UNSCHEDULED = "unscheduled"

    def list():
        return list(map(lambda x: x.value, InitiationType._member_map_.values()))


@JsonMap({"type_": "type"})
class PaymentMethod5(BaseModel):
    def __init__(self, type_: str = None, fields: dict = None):
        self.type_ = type_
        self.fields = fields


class PaymentMethod4Guard(OneOfBaseModel):
    class_list = {"str": str, "PaymentMethod5": PaymentMethod5}


PaymentMethod4 = Union[str, PaymentMethod5]


@JsonMap({})
class CreatePaymentRequest1(BaseModel):
    def __init__(
        self,
        amount: float,
        currency: str,
        payment_method: PaymentMethod4,
        address: Address = None,
        capture: bool = None,
        client_details: ClientDetailsObject = None,
        complete_payment_url: str = None,
        customer: str = None,
        description: str = None,
        error_payment_url: str = None,
        escrow: bool = None,
        escrow_release_days: int = None,
        ewallet: str = None,
        ewallets: List[Ewallet] = None,
        expiration: float = None,
        fixed_side: str = None,
        group_payment: str = None,
        initiation_type: InitiationType = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payment_fees: PaymentFee = None,
        payment_method_options: dict = None,
        receipt_email: str = None,
        requested_currency: str = None,
        statement_descriptor: str = None,
    ):
        self.address = self._define_object(address, Address)
        self.amount = amount
        self.capture = capture
        self.client_details = self._define_object(client_details, ClientDetailsObject)
        self.complete_payment_url = complete_payment_url
        self.currency = self._pattern_matching(
            currency,
            "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
            "currency",
        )
        self.customer = customer
        self.description = description
        self.error_payment_url = error_payment_url
        self.escrow = escrow
        self.escrow_release_days = escrow_release_days
        self.ewallet = ewallet
        self.ewallets = self._define_list(ewallets, Ewallet)
        self.expiration = expiration
        self.fixed_side = fixed_side
        self.group_payment = group_payment
        self.initiation_type = (
            self._enum_matching(
                initiation_type, InitiationType.list(), "initiation_type"
            )
            if initiation_type
            else None
        )
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.payment_fees = self._define_object(payment_fees, PaymentFee)
        self.payment_method = PaymentMethod4Guard.return_one_of(payment_method)
        self.payment_method_options = payment_method_options
        self.receipt_email = receipt_email
        self.requested_currency = requested_currency
        self.statement_descriptor = statement_descriptor


class InitiationType1(Enum):
    CUSTOMER_PRESENT = "customer_present"
    INSTALLMENT = "installment"
    MOTO = "moto"
    RECURRING = "recurring"
    UNSCHEDULED = "unscheduled"

    def list():
        return list(map(lambda x: x.value, InitiationType1._member_map_.values()))


@JsonMap({"type_": "type"})
class PaymentMethod7(BaseModel):
    def __init__(self, type_: str = None, fields: dict = None):
        self.type_ = type_
        self.fields = fields


class PaymentMethod6Guard(OneOfBaseModel):
    class_list = {"str": str, "PaymentMethod7": PaymentMethod7}


PaymentMethod6 = Union[str, PaymentMethod7]


@JsonMap({})
class CreatePaymentRequest2(BaseModel):
    def __init__(
        self,
        amount: float,
        currency: str,
        customer: str,
        address: Address = None,
        capture: bool = None,
        client_details: ClientDetailsObject = None,
        complete_payment_url: str = None,
        description: str = None,
        error_payment_url: str = None,
        escrow: bool = None,
        escrow_release_days: int = None,
        ewallet: str = None,
        ewallets: List[Ewallet] = None,
        expiration: float = None,
        fixed_side: str = None,
        group_payment: str = None,
        initiation_type: InitiationType1 = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payment_fees: PaymentFee = None,
        payment_method: PaymentMethod6 = None,
        payment_method_options: dict = None,
        receipt_email: str = None,
        requested_currency: str = None,
        statement_descriptor: str = None,
    ):
        self.address = self._define_object(address, Address)
        self.amount = amount
        self.capture = capture
        self.client_details = self._define_object(client_details, ClientDetailsObject)
        self.complete_payment_url = complete_payment_url
        self.currency = self._pattern_matching(
            currency,
            "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
            "currency",
        )
        self.customer = customer
        self.description = description
        self.error_payment_url = error_payment_url
        self.escrow = escrow
        self.escrow_release_days = escrow_release_days
        self.ewallet = ewallet
        self.ewallets = self._define_list(ewallets, Ewallet)
        self.expiration = expiration
        self.fixed_side = fixed_side
        self.group_payment = group_payment
        self.initiation_type = (
            self._enum_matching(
                initiation_type, InitiationType1.list(), "initiation_type"
            )
            if initiation_type
            else None
        )
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.payment_fees = self._define_object(payment_fees, PaymentFee)
        self.payment_method = PaymentMethod6Guard.return_one_of(payment_method)
        self.payment_method_options = payment_method_options
        self.receipt_email = receipt_email
        self.requested_currency = requested_currency
        self.statement_descriptor = statement_descriptor


class CreatePaymentRequestGuard(OneOfBaseModel):
    class_list = {
        "CreatePaymentRequest1": CreatePaymentRequest1,
        "CreatePaymentRequest2": CreatePaymentRequest2,
    }


CreatePaymentRequest = Union[CreatePaymentRequest1, CreatePaymentRequest2]
