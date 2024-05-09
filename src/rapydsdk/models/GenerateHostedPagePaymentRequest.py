from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Payment import Payment


@JsonMap({})
class CartItems1(BaseModel):
    def __init__(
        self,
        amount: float = None,
        name: str = None,
        quantity: float = None,
        image: str = None,
    ):
        self.amount = amount
        self.name = name
        self.quantity = quantity
        self.image = image


@JsonMap({})
class CustomElements1(BaseModel):
    def __init__(
        self,
        save_card_default: bool,
        payment_fees_display: bool,
        billing_address_collect: bool,
        display_description: bool,
        merchant_currency_only: bool,
        cardholder_name: str,
        cardholder_preferred_currency: str = None,
        dynamic_currency_conversion: bool = None,
    ):
        self.save_card_default = save_card_default
        self.payment_fees_display = payment_fees_display
        self.billing_address_collect = billing_address_collect
        self.display_description = display_description
        self.merchant_currency_only = merchant_currency_only
        self.cardholder_name = cardholder_name
        self.cardholder_preferred_currency = cardholder_preferred_currency
        self.dynamic_currency_conversion = dynamic_currency_conversion


@JsonMap({})
class GenerateHostedPagePaymentRequest(BaseModel):
    def __init__(
        self,
        amount: float,
        country: str,
        currency: str,
        account_funding_transaction: dict = None,
        cart_items: CartItems1 = None,
        customer: str = None,
        escrow: bool = None,
        escrow_release_days: float = None,
        id: str = None,
        merchant_main_button: str = None,
        merchant_privacy_policy: str = None,
        merchant_terms: str = None,
        merchant_website: str = None,
        custom_elements: CustomElements1 = None,
        page_expiration: float = None,
        payment: Payment = None,
        payment_expiration: float = None,
        payment_method_type: str = None,
        payment_method_type_categories: List[str] = None,
        payment_method_types_exclude: List[str] = None,
        payment_method_types_include: List[str] = None,
        timestamp: float = None,
    ):
        self.account_funding_transaction = account_funding_transaction
        self.amount = amount
        self.cart_items = self._define_object(cart_items, CartItems1)
        self.country = self._pattern_matching(
            country,
            "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
            "country",
        )
        self.currency = self._pattern_matching(
            currency,
            "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
            "currency",
        )
        self.customer = customer
        self.escrow = escrow
        self.escrow_release_days = escrow_release_days
        self.id = id
        self.merchant_main_button = merchant_main_button
        self.merchant_privacy_policy = merchant_privacy_policy
        self.merchant_terms = merchant_terms
        self.merchant_website = merchant_website
        self.custom_elements = self._define_object(custom_elements, CustomElements1)
        self.page_expiration = page_expiration
        self.payment = self._define_object(payment, Payment)
        self.payment_expiration = payment_expiration
        self.payment_method_type = payment_method_type
        self.payment_method_type_categories = payment_method_type_categories
        self.payment_method_types_exclude = payment_method_types_exclude
        self.payment_method_types_include = payment_method_types_include
        self.timestamp = timestamp
