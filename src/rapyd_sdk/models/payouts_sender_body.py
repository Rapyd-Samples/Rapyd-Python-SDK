from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .entity_type import EntityType


@JsonMap({})
class PayoutsSenderBody(BaseModel):
    """PayoutsSenderBody

    :param company_name: Name of the sender company. Relevant when entity_type is company., defaults to None
    :type company_name: str, optional
    :param country: country
    :type country: str
    :param currency: currency
    :type currency: str
    :param entity_type: entity_type
    :type entity_type: EntityType
    :param first_name: First name of the sebder. Relevant when entity_type is individual., defaults to None
    :type first_name: str, optional
    :param identification_type: Type of identification document for the sender., defaults to None
    :type identification_type: str, optional
    :param identification_value: Identification number on the document mentioned in identification_type., defaults to None
    :type identification_value: str, optional
    :param last_name: Last name of the sender. Relevant when entity_type is individual., defaults to None
    :type last_name: str, optional
    """

    def __init__(
        self,
        country: str,
        currency: str,
        entity_type: EntityType,
        company_name: str = None,
        first_name: str = None,
        identification_type: str = None,
        identification_value: str = None,
        last_name: str = None,
    ):
        """PayoutsSenderBody

        :param company_name: Name of the sender company. Relevant when entity_type is company., defaults to None
        :type company_name: str, optional
        :param country: country
        :type country: str
        :param currency: currency
        :type currency: str
        :param entity_type: entity_type
        :type entity_type: EntityType
        :param first_name: First name of the sebder. Relevant when entity_type is individual., defaults to None
        :type first_name: str, optional
        :param identification_type: Type of identification document for the sender., defaults to None
        :type identification_type: str, optional
        :param identification_value: Identification number on the document mentioned in identification_type., defaults to None
        :type identification_value: str, optional
        :param last_name: Last name of the sender. Relevant when entity_type is individual., defaults to None
        :type last_name: str, optional
        """
        self.company_name = self._define_str(
            "company_name", company_name, nullable=True
        )
        self.country = self._define_str(
            "country",
            country,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.currency = self._define_str(
            "currency",
            currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.entity_type = self._enum_matching(
            entity_type, EntityType.list(), "entity_type"
        )
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.identification_type = self._define_str(
            "identification_type", identification_type, nullable=True
        )
        self.identification_value = self._define_str(
            "identification_value", identification_value, nullable=True
        )
        self.last_name = self._define_str("last_name", last_name, nullable=True)
