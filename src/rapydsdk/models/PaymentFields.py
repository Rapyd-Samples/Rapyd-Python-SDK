from __future__ import annotations
from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Address import Address
from .PaymentAmountRangePerCurrency import PaymentAmountRangePerCurrency
from .BinDetails import BinDetails
from .Category import Category
from .Condition import Condition
from .Customer import Customer


class PaymentFlowType1(Enum):
    DIRECT = "direct"
    E_WALLET = "eWallet"
    EWALLET_PAYOUT = "ewallet_payout"
    CARD = "card"
    REDIRECT_URL = "redirect_url"

    def list():
        return list(map(lambda x: x.value, PaymentFlowType1._member_map_.values()))


@JsonMap({})
class PaymentFields(BaseModel):
    def __init__(
        self,
        address: Address = None,
        amount_range_per_currency: List[PaymentAmountRangePerCurrency] = None,
        bin_details: BinDetails = None,
        category: Category = None,
        conditions: List[Condition] = None,
        country: str = None,
        currencies: List[str] = None,
        customer: Customer = None,
        fingerprint: str = None,
        image: str = None,
        instructions: str = None,
        is_cancelable: bool = None,
        is_expirable: bool = None,
        is_online: bool = None,
        is_refundable: bool = None,
        is_required: bool = None,
        is_tokenizable: bool = None,
        is_virtual: bool = None,
        last4: str = None,
        maximum_expiration_seconds: int = None,
        minimum_expiration_seconds: int = None,
        multiple_overage_allowed: bool = None,
        name: str = None,
        payment_flow_type: PaymentFlowType1 = None,
    ):
        self.address = self._define_object(address, Address)
        self.amount_range_per_currency = self._define_list(
            amount_range_per_currency, PaymentAmountRangePerCurrency
        )
        self.bin_details = self._define_object(bin_details, BinDetails)
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.conditions = self._define_list(conditions, Condition)
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
        self.customer = self._define_object(customer, Customer)
        self.fingerprint = fingerprint
        self.image = image
        self.instructions = instructions
        self.is_cancelable = is_cancelable
        self.is_expirable = is_expirable
        self.is_online = is_online
        self.is_refundable = is_refundable
        self.is_required = is_required
        self.is_tokenizable = is_tokenizable
        self.is_virtual = is_virtual
        self.last4 = (
            self._pattern_matching(last4, "^\d{4}$", "last4") if last4 else None
        )
        self.maximum_expiration_seconds = maximum_expiration_seconds
        self.minimum_expiration_seconds = minimum_expiration_seconds
        self.multiple_overage_allowed = multiple_overage_allowed
        self.name = name
        self.payment_flow_type = (
            self._enum_matching(
                payment_flow_type, PaymentFlowType1.list(), "payment_flow_type"
            )
            if payment_flow_type
            else None
        )
