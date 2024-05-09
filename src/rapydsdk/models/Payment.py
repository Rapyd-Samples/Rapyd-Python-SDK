from __future__ import annotations
from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Address import Address
from .Dispute import Dispute
from .NextAction import NextAction
from .Outcome import Outcome
from .PaymentFee import PaymentFee
from .PaymentStatus import PaymentStatus


@JsonMap({})
class Ewallets(BaseModel):
    def __init__(
        self,
        ewallet_id: str = None,
        amount: float = None,
        percent: float = None,
        refunded_amount: float = None,
    ):
        self.ewallet_id = ewallet_id
        self.amount = amount
        self.percent = percent
        self.refunded_amount = refunded_amount


@JsonMap({})
class Instructions(BaseModel):
    def __init__(self, name: str = None, steps: List[dict] = None):
        self.name = name
        self.steps = steps


class PaymentMethodTypeCategory(Enum):
    BANK_TRANSFER = "bank_transfer"
    BANK_REDIRECT = "bank_redirect"
    CARD = "card"
    CASH = "cash"
    EWALLET = "ewallet"

    def list():
        return list(
            map(lambda x: x.value, PaymentMethodTypeCategory._member_map_.values())
        )


@JsonMap({})
class Refunds(BaseModel):
    def __init__(
        self,
        data: List[str] = None,
        has_more: bool = None,
        total_count: int = None,
        url: str = None,
    ):
        self.data = data
        self.has_more = has_more
        self.total_count = total_count
        self.url = url


@JsonMap({})
class Payment(BaseModel):
    def __init__(
        self,
        address: Address = None,
        amount: float = None,
        auth_code: str = None,
        cancel_reason: str = None,
        captured: bool = None,
        complete_payment_url: str = None,
        country_code: str = None,
        created_at: int = None,
        currency_code: str = None,
        customer_token: str = None,
        description: str = None,
        dispute: Dispute = None,
        error_code: str = None,
        error_payment_url: str = None,
        escrow: dict = None,
        ewallet_id: str = None,
        ewallets: List[Ewallets] = None,
        expiration: float = None,
        failure_code: str = None,
        failure_message: str = None,
        fixed_side: str = None,
        flow_type: str = None,
        fx_rate: float = None,
        group_payment: str = None,
        id: str = None,
        initiation_type: str = None,
        instructions: List[Instructions] = None,
        invoice: str = None,
        is_partial: bool = None,
        merchant_reference_id: str = None,
        merchant_requested_amount: str = None,
        merchant_requested_currency: str = None,
        metadata: dict = None,
        mid: str = None,
        next_action: NextAction = None,
        order: str = None,
        original_amount: float = None,
        outcome: Outcome = None,
        paid: bool = None,
        paid_at: float = None,
        payment_fees: PaymentFee = None,
        payment_method: str = None,
        payment_method_data: dict = None,
        payment_method_options: dict = None,
        payment_method_type: str = None,
        payment_method_type_category: PaymentMethodTypeCategory = None,
        receipt_email: str = None,
        receipt_number: str = None,
        redirect_url: str = None,
        refunded: bool = None,
        refunded_amount: float = None,
        refunds: Refunds = None,
        remitter_information: dict = None,
        save_payment_method: bool = None,
        statement_descriptor: str = None,
        status: PaymentStatus = None,
        textual_codes: dict = None,
        transaction_id: str = None,
        visual_codes: dict = None,
    ):
        self.address = self._define_object(address, Address)
        self.amount = amount
        self.auth_code = auth_code
        self.cancel_reason = cancel_reason
        self.captured = captured
        self.complete_payment_url = complete_payment_url
        self.country_code = (
            self._pattern_matching(
                country_code,
                "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
                "country_code",
            )
            if country_code
            else None
        )
        self.created_at = created_at
        self.currency_code = (
            self._pattern_matching(
                currency_code,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "currency_code",
            )
            if currency_code
            else None
        )
        self.customer_token = customer_token
        self.description = description
        self.dispute = self._define_object(dispute, Dispute)
        self.error_code = error_code
        self.error_payment_url = error_payment_url
        self.escrow = escrow
        self.ewallet_id = ewallet_id
        self.ewallets = self._define_list(ewallets, Ewallets)
        self.expiration = expiration
        self.failure_code = failure_code
        self.failure_message = failure_message
        self.fixed_side = fixed_side
        self.flow_type = flow_type
        self.fx_rate = fx_rate
        self.group_payment = group_payment
        self.id = id
        self.initiation_type = initiation_type
        self.instructions = self._define_list(instructions, Instructions)
        self.invoice = invoice
        self.is_partial = is_partial
        self.merchant_reference_id = merchant_reference_id
        self.merchant_requested_amount = merchant_requested_amount
        self.merchant_requested_currency = merchant_requested_currency
        self.metadata = metadata
        self.mid = mid
        self.next_action = (
            self._enum_matching(next_action, NextAction.list(), "next_action")
            if next_action
            else None
        )
        self.order = order
        self.original_amount = original_amount
        self.outcome = self._define_object(outcome, Outcome)
        self.paid = paid
        self.paid_at = paid_at
        self.payment_fees = self._define_object(payment_fees, PaymentFee)
        self.payment_method = payment_method
        self.payment_method_data = payment_method_data
        self.payment_method_options = payment_method_options
        self.payment_method_type = payment_method_type
        self.payment_method_type_category = (
            self._enum_matching(
                payment_method_type_category,
                PaymentMethodTypeCategory.list(),
                "payment_method_type_category",
            )
            if payment_method_type_category
            else None
        )
        self.receipt_email = receipt_email
        self.receipt_number = receipt_number
        self.redirect_url = redirect_url
        self.refunded = refunded
        self.refunded_amount = refunded_amount
        self.refunds = self._define_object(refunds, Refunds)
        self.remitter_information = remitter_information
        self.save_payment_method = save_payment_method
        self.statement_descriptor = statement_descriptor
        self.status = (
            self._enum_matching(status, PaymentStatus.list(), "status")
            if status
            else None
        )
        self.textual_codes = textual_codes
        self.transaction_id = transaction_id
        self.visual_codes = visual_codes
