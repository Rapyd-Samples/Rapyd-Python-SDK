from __future__ import annotations
from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .PaymentAmountRangePerCurrency import PaymentAmountRangePerCurrency
from .Category import Category
from .PaymentMethodTypeField import PaymentMethodTypeField


class PaymentFlowType2(Enum):
    DIRECT = "direct"
    E_WALLET = "eWallet"
    EWALLET_PAYOUT = "ewallet_payout"
    CARD = "card"
    REDIRECT_URL = "redirect_url"
    CASH = "cash"
    BANK_TRANSFER = "bank_transfer"

    def list():
        return list(map(lambda x: x.value, PaymentFlowType2._member_map_.values()))


@JsonMap({"type_": "type"})
class PaymentMethodType(BaseModel):
    def __init__(
        self,
        amount_range_per_currency: List[PaymentAmountRangePerCurrency] = None,
        category: Category = None,
        country: str = None,
        currencies: List[str] = None,
        image: str = None,
        is_cancelable: bool = None,
        is_expirable: bool = None,
        is_online: bool = None,
        is_refundable: bool = None,
        is_tokenizable: bool = None,
        is_virtual: bool = None,
        maximum_expiration_seconds: float = None,
        minimum_expiration_seconds: float = None,
        multiple_overage_allowed: bool = None,
        name: str = None,
        payment_flow_type: PaymentFlowType2 = None,
        payment_options: List[PaymentMethodTypeField] = None,
        status: float = None,
        supported_digital_wallet_providers: List[str] = None,
        type_: str = None,
        virtual_payment_method_type: str = None,
        is_restricted: bool = None,
        supports_subscription: bool = None,
    ):
        self.amount_range_per_currency = self._define_list(
            amount_range_per_currency, PaymentAmountRangePerCurrency
        )
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.country = (
            self._pattern_matching(
                country,
                "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
                "country",
            )
            if country
            else None
        )
        self.currencies = currencies
        self.image = image
        self.is_cancelable = is_cancelable
        self.is_expirable = is_expirable
        self.is_online = is_online
        self.is_refundable = is_refundable
        self.is_tokenizable = is_tokenizable
        self.is_virtual = is_virtual
        self.maximum_expiration_seconds = maximum_expiration_seconds
        self.minimum_expiration_seconds = minimum_expiration_seconds
        self.multiple_overage_allowed = multiple_overage_allowed
        self.name = name
        self.payment_flow_type = (
            self._enum_matching(
                payment_flow_type, PaymentFlowType2.list(), "payment_flow_type"
            )
            if payment_flow_type
            else None
        )
        self.payment_options = self._define_list(
            payment_options, PaymentMethodTypeField
        )
        self.status = status
        self.supported_digital_wallet_providers = supported_digital_wallet_providers
        self.type_ = type_
        self.virtual_payment_method_type = virtual_payment_method_type
        self.is_restricted = is_restricted
        self.supports_subscription = supports_subscription
