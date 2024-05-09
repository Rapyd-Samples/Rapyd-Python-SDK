from __future__ import annotations
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .PaymentParams import PaymentParams
from .CustomerPaymentMethod import CustomerPaymentMethod, CustomerPaymentMethodGuard
from .MerchantCustomerSupport import MerchantCustomerSupport
from .HostedPageStatus import HostedPageStatus


@JsonMap({})
class HostedPageResponse1(BaseModel):
    def __init__(
        self,
        billing_address_collect: bool = None,
        cancel_url: str = None,
        category: str = None,
        complete_url: str = None,
        country: str = None,
        currency: str = None,
        customer: str = None,
        id: str = None,
        page_expiration: float = None,
        payment_method_type: str = None,
        payment_params: PaymentParams = None,
        customer_card_payment_methods: CustomerPaymentMethod = None,
        language: str = None,
        merchant_alias: str = None,
        merchant_color: str = None,
        merchant_customer_support: MerchantCustomerSupport = None,
        merchant_logo: str = None,
        merchant_website: str = None,
        redirect_url: str = None,
        merchant_terms: str = None,
        merchant_privacy_policy: str = None,
        status: HostedPageStatus = None,
    ):
        self.billing_address_collect = billing_address_collect
        self.cancel_url = cancel_url
        self.category = category
        self.complete_url = complete_url
        self.country = (
            self._pattern_matching(
                country,
                "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
                "country",
            )
            if country
            else None
        )
        self.currency = (
            self._pattern_matching(
                currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "currency",
            )
            if currency
            else None
        )
        self.customer = customer
        self.id = id
        self.page_expiration = page_expiration
        self.payment_method_type = payment_method_type
        self.payment_params = self._define_object(payment_params, PaymentParams)
        self.customer_card_payment_methods = CustomerPaymentMethodGuard.return_one_of(
            customer_card_payment_methods
        )
        self.language = language
        self.merchant_alias = merchant_alias
        self.merchant_color = merchant_color
        self.merchant_customer_support = self._define_object(
            merchant_customer_support, MerchantCustomerSupport
        )
        self.merchant_logo = merchant_logo
        self.merchant_website = merchant_website
        self.redirect_url = redirect_url
        self.merchant_terms = merchant_terms
        self.merchant_privacy_policy = merchant_privacy_policy
        self.status = (
            self._enum_matching(status, HostedPageStatus.list(), "status")
            if status
            else None
        )


@JsonMap({})
class Card(BaseModel):
    def __init__(self, name: str = None, network: str = None):
        self.name = name
        self.network = network


@JsonMap({})
class HostedPageResponse2(BaseModel):
    def __init__(
        self,
        card: Card = None,
        card_color: str = None,
        expiration: float = None,
        id: str = None,
        logo: str = None,
        logo_orientation: str = None,
        language: str = None,
        merchant_alias: str = None,
        merchant_color: str = None,
        merchant_customer_support: MerchantCustomerSupport = None,
        merchant_logo: str = None,
        merchant_website: str = None,
        redirect_url: str = None,
        merchant_terms: str = None,
        merchant_privacy_policy: str = None,
        page_expiration: float = None,
        status: HostedPageStatus = None,
        complete_url: str = None,
        cancel_url: str = None,
    ):
        self.card = self._define_object(card, Card)
        self.card_color = card_color
        self.expiration = expiration
        self.id = id
        self.logo = logo
        self.logo_orientation = logo_orientation
        self.language = language
        self.merchant_alias = merchant_alias
        self.merchant_color = merchant_color
        self.merchant_customer_support = self._define_object(
            merchant_customer_support, MerchantCustomerSupport
        )
        self.merchant_logo = merchant_logo
        self.merchant_website = merchant_website
        self.redirect_url = redirect_url
        self.merchant_terms = merchant_terms
        self.merchant_privacy_policy = merchant_privacy_policy
        self.page_expiration = page_expiration
        self.status = (
            self._enum_matching(status, HostedPageStatus.list(), "status")
            if status
            else None
        )
        self.complete_url = complete_url
        self.cancel_url = cancel_url


class HostedPageResponseGuard(OneOfBaseModel):
    class_list = {
        "HostedPageResponse1": HostedPageResponse1,
        "HostedPageResponse2": HostedPageResponse2,
    }


HostedPageResponse = Union[HostedPageResponse1, HostedPageResponse2]
