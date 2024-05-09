from __future__ import annotations
from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Address import Address
from .ContactBusiness import ContactBusiness


class ContactType(Enum):
    PERSONAL = "personal"
    BUSINESS = "business"

    def list():
        return list(map(lambda x: x.value, ContactType._member_map_.values()))


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    NOT_APPLICABLE = "not_applicable"

    def list():
        return list(map(lambda x: x.value, Gender._member_map_.values()))


class HouseType(Enum):
    LEASE = "lease"
    LIVE_WITH_FAMILY = "live_with_family"
    OWN = "own"
    OWNER = "owner"
    MONTH_TO_MONTH = "month_to_month"
    HOUSING_PROJECT = "housing_project"

    def list():
        return list(map(lambda x: x.value, HouseType._member_map_.values()))


class MaritalStatus(Enum):
    MARRIED = "married"
    SINGLE = "single"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    COHABITING = "cohabiting"
    NOT_APPLICABLE = "not_applicable"

    def list():
        return list(map(lambda x: x.value, MaritalStatus._member_map_.values()))


class VerificationStatus(Enum):
    NOT_VERIFIED = "not verified"
    KY_CD = "KYCd"

    def list():
        return list(map(lambda x: x.value, VerificationStatus._member_map_.values()))


@JsonMap({})
class Contact(BaseModel):
    def __init__(
        self,
        address: Address = None,
        business_details: ContactBusiness = None,
        compliance_profile: float = None,
        contact_type: ContactType = None,
        country: str = None,
        created_at: float = None,
        date_of_birth: str = None,
        email: str = None,
        ewallet: str = None,
        first_name: str = None,
        gender: Gender = None,
        house_type: HouseType = None,
        id: str = None,
        identification_number: str = None,
        identification_type: str = None,
        issued_card_data: dict = None,
        last_name: str = None,
        marital_status: MaritalStatus = None,
        metadata: dict = None,
        middle_name: str = None,
        mothers_name: str = None,
        nationality: str = None,
        phone_number: str = None,
        second_last_name: str = None,
        send_notifications: bool = None,
        verification_status: VerificationStatus = None,
        contact_reference_id: str = None,
    ):
        self.address = self._define_object(address, Address)
        self.business_details = self._define_object(business_details, ContactBusiness)
        self.compliance_profile = compliance_profile
        self.contact_type = (
            self._enum_matching(contact_type, ContactType.list(), "contact_type")
            if contact_type
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
        self.created_at = created_at
        self.date_of_birth = date_of_birth
        self.email = (
            self._pattern_matching(
                email, "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", "email"
            )
            if email
            else None
        )
        self.ewallet = ewallet
        self.first_name = first_name
        self.gender = (
            self._enum_matching(gender, Gender.list(), "gender") if gender else None
        )
        self.house_type = (
            self._enum_matching(house_type, HouseType.list(), "house_type")
            if house_type
            else None
        )
        self.id = id
        self.identification_number = identification_number
        self.identification_type = identification_type
        self.issued_card_data = issued_card_data
        self.last_name = last_name
        self.marital_status = (
            self._enum_matching(marital_status, MaritalStatus.list(), "marital_status")
            if marital_status
            else None
        )
        self.metadata = metadata
        self.middle_name = middle_name
        self.mothers_name = mothers_name
        self.nationality = (
            self._pattern_matching(
                nationality,
                "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
                "nationality",
            )
            if nationality
            else None
        )
        self.phone_number = phone_number
        self.second_last_name = second_last_name
        self.send_notifications = send_notifications
        self.verification_status = (
            self._enum_matching(
                verification_status, VerificationStatus.list(), "verification_status"
            )
            if verification_status
            else None
        )
        self.contact_reference_id = contact_reference_id
