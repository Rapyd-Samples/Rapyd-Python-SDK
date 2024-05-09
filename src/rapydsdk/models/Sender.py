from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .EntityType import EntityType


@JsonMap({})
class Sender(BaseModel):
    def __init__(
        self,
        account_number: str = None,
        additional_data: dict = None,
        additional_last_name: str = None,
        address: str = None,
        bank_code: str = None,
        bank_name: str = None,
        beneficiary_relationship: str = None,
        city: str = None,
        company_name: str = None,
        country: str = None,
        currency: str = None,
        date_of_birth: str = None,
        date_of_incorporation: str = None,
        email: str = None,
        entity_type: EntityType = None,
        first_name: str = None,
        id: str = None,
        id_date_of_issue: str = None,
        id_expiry: str = None,
        id_issue_authority: str = None,
        id_issue_location: str = None,
        identification_type: str = None,
        identification_value: str = None,
        last_name: str = None,
        merchant_reference_id: str = None,
        middle_name: str = None,
        mobile_number: str = None,
        name: str = None,
        nationality: str = None,
        occupation: str = None,
        phone_country_code: str = None,
        phone_number: str = None,
        postcode: str = None,
        province: str = None,
        purpose_code: str = None,
        source_of_income: str = None,
        state: str = None,
        suburb: str = None,
        tax_id: str = None,
    ):
        self.account_number = account_number
        self.additional_data = additional_data
        self.additional_last_name = additional_last_name
        self.address = address
        self.bank_code = bank_code
        self.bank_name = bank_name
        self.beneficiary_relationship = beneficiary_relationship
        self.city = city
        self.company_name = company_name
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
        self.email = email
        self.entity_type = (
            self._enum_matching(entity_type, EntityType.list(), "entity_type")
            if entity_type
            else None
        )
        self.first_name = first_name
        self.id = id
        self.id_date_of_issue = id_date_of_issue
        self.id_expiry = id_expiry
        self.id_issue_authority = id_issue_authority
        self.id_issue_location = id_issue_location
        self.identification_type = identification_type
        self.identification_value = identification_value
        self.last_name = last_name
        self.merchant_reference_id = merchant_reference_id
        self.middle_name = middle_name
        self.mobile_number = mobile_number
        self.name = name
        self.nationality = nationality
        self.occupation = occupation
        self.phone_country_code = phone_country_code
        self.phone_number = phone_number
        self.postcode = postcode
        self.province = province
        self.purpose_code = purpose_code
        self.source_of_income = source_of_income
        self.state = state
        self.suburb = suburb
        self.tax_id = tax_id
