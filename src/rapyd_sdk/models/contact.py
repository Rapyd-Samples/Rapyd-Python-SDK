from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address import Address
from .contact_business import ContactBusiness


class ContactType(Enum):
    """An enumeration representing different categories.

    :cvar PERSONAL: "personal"
    :vartype PERSONAL: str
    :cvar BUSINESS: "business"
    :vartype BUSINESS: str
    """

    PERSONAL = "personal"
    BUSINESS = "business"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ContactType._member_map_.values()))


class Gender(Enum):
    """An enumeration representing different categories.

    :cvar MALE: "male"
    :vartype MALE: str
    :cvar FEMALE: "female"
    :vartype FEMALE: str
    :cvar OTHER: "other"
    :vartype OTHER: str
    :cvar NOTAPPLICABLE: "not_applicable"
    :vartype NOTAPPLICABLE: str
    """

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    NOTAPPLICABLE = "not_applicable"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Gender._member_map_.values()))


class HouseType(Enum):
    """An enumeration representing different categories.

    :cvar LEASE: "lease"
    :vartype LEASE: str
    :cvar LIVEWITHFAMILY: "live_with_family"
    :vartype LIVEWITHFAMILY: str
    :cvar OWN: "own"
    :vartype OWN: str
    :cvar OWNER: "owner"
    :vartype OWNER: str
    :cvar MONTHTOMONTH: "month_to_month"
    :vartype MONTHTOMONTH: str
    :cvar HOUSINGPROJECT: "housing_project"
    :vartype HOUSINGPROJECT: str
    """

    LEASE = "lease"
    LIVEWITHFAMILY = "live_with_family"
    OWN = "own"
    OWNER = "owner"
    MONTHTOMONTH = "month_to_month"
    HOUSINGPROJECT = "housing_project"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, HouseType._member_map_.values()))


class MaritalStatus(Enum):
    """An enumeration representing different categories.

    :cvar MARRIED: "married"
    :vartype MARRIED: str
    :cvar SINGLE: "single"
    :vartype SINGLE: str
    :cvar DIVORCED: "divorced"
    :vartype DIVORCED: str
    :cvar WIDOWED: "widowed"
    :vartype WIDOWED: str
    :cvar COHABITING: "cohabiting"
    :vartype COHABITING: str
    :cvar NOTAPPLICABLE: "not_applicable"
    :vartype NOTAPPLICABLE: str
    """

    MARRIED = "married"
    SINGLE = "single"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    COHABITING = "cohabiting"
    NOTAPPLICABLE = "not_applicable"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MaritalStatus._member_map_.values()))


class VerificationStatus(Enum):
    """An enumeration representing different categories.

    :cvar NOTVERIFIED: "not verified"
    :vartype NOTVERIFIED: str
    :cvar KYCD: "KYCd"
    :vartype KYCD: str
    """

    NOTVERIFIED = "not verified"
    KYCD = "KYCd"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, VerificationStatus._member_map_.values()))


@JsonMap({"id_": "id"})
class Contact(BaseModel):
    """Contact

    :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
    :type address: Address, optional
    :param business_details: business_details, defaults to None
    :type business_details: ContactBusiness, optional
    :param compliance_profile: Indicates the degree to which this contact can use the wallet., defaults to None
    :type compliance_profile: float, optional
    :param contact_type: Type of contact., defaults to None
    :type contact_type: ContactType, optional
    :param country: country, defaults to None
    :type country: str, optional
    :param created_at: created_at, defaults to None
    :type created_at: float, optional
    :param date_of_birth: Date of birth of the individua, defaults to None
    :type date_of_birth: str, optional
    :param email: Email address of the contact, defaults to None
    :type email: str, optional
    :param ewallet: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_., defaults to None
    :type ewallet: str, optional
    :param first_name: First name of the personal contact or primary person associated with the business contact., defaults to None
    :type first_name: str, optional
    :param gender: Gender of the personal contact or primary person associated with the business contact, defaults to None
    :type gender: Gender, optional
    :param house_type: Description of the type of residency at the contact's residence., defaults to None
    :type house_type: HouseType, optional
    :param id_: ID of the contact object. String starting with cont_., defaults to None
    :type id_: str, optional
    :param identification_number: ID number as shown by the ID document., defaults to None
    :type identification_number: str, optional
    :param identification_type: Type of the identification document associated with the contact. Uppercase., defaults to None
    :type identification_type: str, optional
    :param issued_card_data: Describes additional information about the business contact for a company wallet., defaults to None
    :type issued_card_data: dict, optional
    :param last_name: Family name of the personal contact or primary person associated with the business contact. Required for issuing a card to a personal contact., defaults to None
    :type last_name: str, optional
    :param marital_status: Marital status of the personal contact or primary person associated with the business contact., defaults to None
    :type marital_status: MaritalStatus, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param middle_name: Middle name of the personal contact or primary person associated with the business contact., defaults to None
    :type middle_name: str, optional
    :param mothers_name: Name of the contact's mother, defaults to None
    :type mothers_name: str, optional
    :param nationality: nationality, defaults to None
    :type nationality: str, optional
    :param phone_number: Phone number of the contact in E.164 format., defaults to None
    :type phone_number: str, optional
    :param second_last_name: Second last name of the personal contact or primary person associated with the business contact., defaults to None
    :type second_last_name: str, optional
    :param send_notifications: Determines whether Rapyd sends notifications to the contact. Default is false., defaults to None
    :type send_notifications: bool, optional
    :param verification_status: Result of the verification check., defaults to None
    :type verification_status: VerificationStatus, optional
    :param contact_reference_id: Reference ID for the contact. Limited to 45 characters. Should be unique per merchant per e-wallet., defaults to None
    :type contact_reference_id: str, optional
    """

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
        id_: str = None,
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
        """Contact

        :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
        :type address: Address, optional
        :param business_details: business_details, defaults to None
        :type business_details: ContactBusiness, optional
        :param compliance_profile: Indicates the degree to which this contact can use the wallet., defaults to None
        :type compliance_profile: float, optional
        :param contact_type: Type of contact., defaults to None
        :type contact_type: ContactType, optional
        :param country: country, defaults to None
        :type country: str, optional
        :param created_at: created_at, defaults to None
        :type created_at: float, optional
        :param date_of_birth: Date of birth of the individua, defaults to None
        :type date_of_birth: str, optional
        :param email: Email address of the contact, defaults to None
        :type email: str, optional
        :param ewallet: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_., defaults to None
        :type ewallet: str, optional
        :param first_name: First name of the personal contact or primary person associated with the business contact., defaults to None
        :type first_name: str, optional
        :param gender: Gender of the personal contact or primary person associated with the business contact, defaults to None
        :type gender: Gender, optional
        :param house_type: Description of the type of residency at the contact's residence., defaults to None
        :type house_type: HouseType, optional
        :param id_: ID of the contact object. String starting with cont_., defaults to None
        :type id_: str, optional
        :param identification_number: ID number as shown by the ID document., defaults to None
        :type identification_number: str, optional
        :param identification_type: Type of the identification document associated with the contact. Uppercase., defaults to None
        :type identification_type: str, optional
        :param issued_card_data: Describes additional information about the business contact for a company wallet., defaults to None
        :type issued_card_data: dict, optional
        :param last_name: Family name of the personal contact or primary person associated with the business contact. Required for issuing a card to a personal contact., defaults to None
        :type last_name: str, optional
        :param marital_status: Marital status of the personal contact or primary person associated with the business contact., defaults to None
        :type marital_status: MaritalStatus, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param middle_name: Middle name of the personal contact or primary person associated with the business contact., defaults to None
        :type middle_name: str, optional
        :param mothers_name: Name of the contact's mother, defaults to None
        :type mothers_name: str, optional
        :param nationality: nationality, defaults to None
        :type nationality: str, optional
        :param phone_number: Phone number of the contact in E.164 format., defaults to None
        :type phone_number: str, optional
        :param second_last_name: Second last name of the personal contact or primary person associated with the business contact., defaults to None
        :type second_last_name: str, optional
        :param send_notifications: Determines whether Rapyd sends notifications to the contact. Default is false., defaults to None
        :type send_notifications: bool, optional
        :param verification_status: Result of the verification check., defaults to None
        :type verification_status: VerificationStatus, optional
        :param contact_reference_id: Reference ID for the contact. Limited to 45 characters. Should be unique per merchant per e-wallet., defaults to None
        :type contact_reference_id: str, optional
        """
        self.address = self._define_object(address, Address)
        self.business_details = self._define_object(business_details, ContactBusiness)
        self.compliance_profile = self._define_number(
            "compliance_profile", compliance_profile, nullable=True
        )
        self.contact_type = (
            self._enum_matching(contact_type, ContactType.list(), "contact_type")
            if contact_type
            else None
        )
        self.country = self._define_str(
            "country",
            country,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.date_of_birth = self._define_str(
            "date_of_birth", date_of_birth, nullable=True
        )
        self.email = self._define_str(
            "email",
            email,
            nullable=True,
            pattern="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        )
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.gender = (
            self._enum_matching(gender, Gender.list(), "gender") if gender else None
        )
        self.house_type = (
            self._enum_matching(house_type, HouseType.list(), "house_type")
            if house_type
            else None
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.identification_number = self._define_str(
            "identification_number", identification_number, nullable=True
        )
        self.identification_type = self._define_str(
            "identification_type", identification_type, nullable=True
        )
        self.issued_card_data = issued_card_data
        self.last_name = self._define_str("last_name", last_name, nullable=True)
        self.marital_status = (
            self._enum_matching(marital_status, MaritalStatus.list(), "marital_status")
            if marital_status
            else None
        )
        self.metadata = metadata
        self.middle_name = self._define_str("middle_name", middle_name, nullable=True)
        self.mothers_name = self._define_str(
            "mothers_name", mothers_name, nullable=True
        )
        self.nationality = self._define_str(
            "nationality",
            nationality,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
        self.second_last_name = self._define_str(
            "second_last_name", second_last_name, nullable=True
        )
        self.send_notifications = send_notifications
        self.verification_status = (
            self._enum_matching(
                verification_status, VerificationStatus.list(), "verification_status"
            )
            if verification_status
            else None
        )
        self.contact_reference_id = self._define_str(
            "contact_reference_id", contact_reference_id, nullable=True
        )
