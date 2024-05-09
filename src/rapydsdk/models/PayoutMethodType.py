from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .PayoutAmountRangePerCurrency import PayoutAmountRangePerCurrency
from .EntityType import EntityType
from .Category import Category


@JsonMap({})
class PayoutMethodType(BaseModel):
    def __init__(
        self,
        amount_range_per_currency: List[List[PayoutAmountRangePerCurrency]] = None,
        beneficiary_country: str = None,
        beneficiary_entity_types: List[EntityType] = None,
        category: Category = None,
        image: str = None,
        is_cancelable: int = None,
        is_expirable: int = None,
        is_location_specific: int = None,
        maximum_expiration_seconds: float = None,
        minimum_expiration_seconds: float = None,
        name: str = None,
        payout_currencies: List[str] = None,
        payout_method_type: str = None,
        sender_country: str = None,
        sender_currencies: List[str] = None,
        sender_entity_types: List[EntityType] = None,
        estimated_time_of_arrival: str = None,
        status: int = None,
    ):
        self.amount_range_per_currency = amount_range_per_currency
        self.beneficiary_country = (
            self._pattern_matching(
                beneficiary_country,
                "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
                "beneficiary_country",
            )
            if beneficiary_country
            else None
        )
        self.beneficiary_entity_types = self._define_list(
            beneficiary_entity_types, EntityType
        )
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.image = image
        self.is_cancelable = is_cancelable
        self.is_expirable = is_expirable
        self.is_location_specific = is_location_specific
        self.maximum_expiration_seconds = maximum_expiration_seconds
        self.minimum_expiration_seconds = minimum_expiration_seconds
        self.name = name
        self.payout_currencies = payout_currencies
        self.payout_method_type = payout_method_type
        self.sender_country = (
            self._pattern_matching(
                sender_country,
                "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
                "sender_country",
            )
            if sender_country
            else None
        )
        self.sender_currencies = sender_currencies
        self.sender_entity_types = self._define_list(sender_entity_types, EntityType)
        self.estimated_time_of_arrival = estimated_time_of_arrival
        self.status = status
