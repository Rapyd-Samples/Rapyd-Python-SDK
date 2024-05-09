from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Category import Category
from .EntityType import EntityType


@JsonMap({})
class Beneficiary(BaseModel):
    def __init__(
        self,
        aba: str = None,
        account_number: str = None,
        ach_code: str = None,
        additional_data: dict = None,
        additional_last_name: str = None,
        address: str = None,
        bank_account_holder_name: str = None,
        bank_account_type: str = None,
        bank_address: str = None,
        bank_branch_code: str = None,
        bank_branch_name: str = None,
        bank_city: str = None,
        bank_code: str = None,
        bank_country: str = None,
        bank_name: str = None,
        bank_province: str = None,
        beneficiary_bic_local: str = None,
        beneficiary_relationship: str = None,
        bic_swift: str = None,
        bsb_code: str = None,
        card_expiration_month: str = None,
        card_expiration_year: str = None,
        card_number: str = None,
        category: Category = None,
        city: str = None,
        clabe: str = None,
        cnaps: str = None,
        company_name: str = None,
        confirmation_required: bool = None,
        country: str = None,
        currency: str = None,
        date_of_birth: str = None,
        date_of_incorporation: str = None,
        default_payout_method_type: str = None,
        email: str = None,
        entity_type: EntityType = None,
        ewallet: str = None,
        first_name: str = None,
        iban: str = None,
        id: str = None,
        id_date_of_issue: str = None,
        id_issue_authority: str = None,
        id_issue_location: str = None,
        identification_type: str = None,
        identification_value: str = None,
        ifsc: str = None,
        issuer_code: str = None,
        last_name: str = None,
        merchant_reference_id: str = None,
        middle_name: str = None,
        mobile_number: str = None,
        name: str = None,
        nationality: str = None,
        payment_type: str = None,
        phone_country_code: str = None,
        phone_number: str = None,
        postcode: str = None,
        province: str = None,
        purpose_code: str = None,
        routing_code_type_1: str = None,
        routing_code_type_2: str = None,
        routing_code_type_3: str = None,
        routing_code_value_1: str = None,
        routing_code_value_2: str = None,
        routing_code_value_3: str = None,
        sort_code: str = None,
        state: str = None,
        statement_narrative: str = None,
        suburb: str = None,
        tax_id: str = None,
        vpa: str = None,
    ):
        self.aba = aba
        self.account_number = account_number
        self.ach_code = ach_code
        self.additional_data = additional_data
        self.additional_last_name = additional_last_name
        self.address = address
        self.bank_account_holder_name = bank_account_holder_name
        self.bank_account_type = bank_account_type
        self.bank_address = bank_address
        self.bank_branch_code = bank_branch_code
        self.bank_branch_name = bank_branch_name
        self.bank_city = bank_city
        self.bank_code = bank_code
        self.bank_country = bank_country
        self.bank_name = bank_name
        self.bank_province = bank_province
        self.beneficiary_bic_local = beneficiary_bic_local
        self.beneficiary_relationship = beneficiary_relationship
        self.bic_swift = bic_swift
        self.bsb_code = bsb_code
        self.card_expiration_month = card_expiration_month
        self.card_expiration_year = card_expiration_year
        self.card_number = card_number
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.city = city
        self.clabe = clabe
        self.cnaps = cnaps
        self.company_name = company_name
        self.confirmation_required = confirmation_required
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
        self.date_of_birth = date_of_birth
        self.date_of_incorporation = date_of_incorporation
        self.default_payout_method_type = default_payout_method_type
        self.email = email
        self.entity_type = (
            self._enum_matching(entity_type, EntityType.list(), "entity_type")
            if entity_type
            else None
        )
        self.ewallet = ewallet
        self.first_name = first_name
        self.iban = iban
        self.id = id
        self.id_date_of_issue = id_date_of_issue
        self.id_issue_authority = id_issue_authority
        self.id_issue_location = id_issue_location
        self.identification_type = identification_type
        self.identification_value = identification_value
        self.ifsc = ifsc
        self.issuer_code = issuer_code
        self.last_name = last_name
        self.merchant_reference_id = merchant_reference_id
        self.middle_name = middle_name
        self.mobile_number = mobile_number
        self.name = name
        self.nationality = nationality
        self.payment_type = payment_type
        self.phone_country_code = phone_country_code
        self.phone_number = phone_number
        self.postcode = postcode
        self.province = province
        self.purpose_code = purpose_code
        self.routing_code_type_1 = routing_code_type_1
        self.routing_code_type_2 = routing_code_type_2
        self.routing_code_type_3 = routing_code_type_3
        self.routing_code_value_1 = routing_code_value_1
        self.routing_code_value_2 = routing_code_value_2
        self.routing_code_value_3 = routing_code_value_3
        self.sort_code = sort_code
        self.state = state
        self.statement_narrative = statement_narrative
        self.suburb = suburb
        self.tax_id = tax_id
        self.vpa = vpa
