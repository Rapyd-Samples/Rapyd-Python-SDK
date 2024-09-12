from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address import Address


@JsonMap({})
class EwalletIdContactsBody(BaseModel):
    """EwalletIdContactsBody

    :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
    :type address: Address, optional
    :param contact_type: Type of contact: personal.
    :type contact_type: str
    :param country: 2-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase., defaults to None
    :type country: str, optional
    :param date_of_birth: Date of birth of the individual. Format: MM/DD/YYYY, defaults to None
    :type date_of_birth: str, optional
    :param email: Email address for the contact., defaults to None
    :type email: str, optional
    :param first_name: First name of the contact., defaults to None
    :type first_name: str, optional
    :param last_name: Family name of the personal contact or primary person associated with the business contact. For a personal contact type, alphabetic characters and spaces. Required for issuing a card to a personal contact. , defaults to None
    :type last_name: str, optional
    :param gender: Gender of the contact. One of the following values: male, female, other, not_applicable, defaults to None
    :type gender: str, optional
    :param house_type: Description of the type of residency. One of the following values: lease, live_with_family, own, owner, month_to_month, housing_project, defaults to None
    :type house_type: str, optional
    :param identification_number: ID number as shown by the ID document. Alphanumeric string, defaults to None
    :type identification_number: str, optional
    :param identification_type: Type of the identification document, defaults to None
    :type identification_type: str, optional
    :param marital_status: Marital status of the contact. One of the following values: married, single, divorced, widowed, cohabiting, not_applicable, defaults to None
    :type marital_status: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: str, optional
    :param middle_name: Middle name of the personal contact or primary person associated with the business contact., defaults to None
    :type middle_name: str, optional
    :param mothers_name: Name of the contact's mother., defaults to None
    :type mothers_name: str, optional
    :param nationality: The citizenship of the contact. Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase., defaults to None
    :type nationality: str, optional
    :param phone_number: Phone number of the contact in E.164 format., defaults to None
    :type phone_number: str, optional
    :param second_last_name: Second last name of the contact., defaults to None
    :type second_last_name: str, optional
    :param send_notifications: Determines whether Rapyd sends notifications to the contact. Default is false., defaults to None
    :type send_notifications: bool, optional
    :param contact_reference_id: Reference ID for the contact. Limited to 45 characters. Should be unique per merchant per e-wallet., defaults to None
    :type contact_reference_id: str, optional
    """

    def __init__(
        self,
        contact_type: str,
        address: Address = None,
        country: str = None,
        date_of_birth: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        gender: str = None,
        house_type: str = None,
        identification_number: str = None,
        identification_type: str = None,
        marital_status: str = None,
        metadata: str = None,
        middle_name: str = None,
        mothers_name: str = None,
        nationality: str = None,
        phone_number: str = None,
        second_last_name: str = None,
        send_notifications: bool = None,
        contact_reference_id: str = None,
    ):
        """EwalletIdContactsBody

        :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
        :type address: Address, optional
        :param contact_type: Type of contact: personal.
        :type contact_type: str
        :param country: 2-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase., defaults to None
        :type country: str, optional
        :param date_of_birth: Date of birth of the individual. Format: MM/DD/YYYY, defaults to None
        :type date_of_birth: str, optional
        :param email: Email address for the contact., defaults to None
        :type email: str, optional
        :param first_name: First name of the contact., defaults to None
        :type first_name: str, optional
        :param last_name: Family name of the personal contact or primary person associated with the business contact. For a personal contact type, alphabetic characters and spaces. Required for issuing a card to a personal contact. , defaults to None
        :type last_name: str, optional
        :param gender: Gender of the contact. One of the following values: male, female, other, not_applicable, defaults to None
        :type gender: str, optional
        :param house_type: Description of the type of residency. One of the following values: lease, live_with_family, own, owner, month_to_month, housing_project, defaults to None
        :type house_type: str, optional
        :param identification_number: ID number as shown by the ID document. Alphanumeric string, defaults to None
        :type identification_number: str, optional
        :param identification_type: Type of the identification document, defaults to None
        :type identification_type: str, optional
        :param marital_status: Marital status of the contact. One of the following values: married, single, divorced, widowed, cohabiting, not_applicable, defaults to None
        :type marital_status: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: str, optional
        :param middle_name: Middle name of the personal contact or primary person associated with the business contact., defaults to None
        :type middle_name: str, optional
        :param mothers_name: Name of the contact's mother., defaults to None
        :type mothers_name: str, optional
        :param nationality: The citizenship of the contact. Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase., defaults to None
        :type nationality: str, optional
        :param phone_number: Phone number of the contact in E.164 format., defaults to None
        :type phone_number: str, optional
        :param second_last_name: Second last name of the contact., defaults to None
        :type second_last_name: str, optional
        :param send_notifications: Determines whether Rapyd sends notifications to the contact. Default is false., defaults to None
        :type send_notifications: bool, optional
        :param contact_reference_id: Reference ID for the contact. Limited to 45 characters. Should be unique per merchant per e-wallet., defaults to None
        :type contact_reference_id: str, optional
        """
        self.address = self._define_object(address, Address)
        self.contact_type = contact_type
        self.country = self._define_str("country", country, nullable=True)
        self.date_of_birth = self._define_str(
            "date_of_birth", date_of_birth, nullable=True
        )
        self.email = self._define_str("email", email, nullable=True)
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.last_name = self._define_str("last_name", last_name, nullable=True)
        self.gender = self._define_str("gender", gender, nullable=True)
        self.house_type = self._define_str("house_type", house_type, nullable=True)
        self.identification_number = self._define_str(
            "identification_number", identification_number, nullable=True
        )
        self.identification_type = self._define_str(
            "identification_type", identification_type, nullable=True
        )
        self.marital_status = self._define_str(
            "marital_status", marital_status, nullable=True
        )
        self.metadata = self._define_str("metadata", metadata, nullable=True)
        self.middle_name = self._define_str("middle_name", middle_name, nullable=True)
        self.mothers_name = self._define_str(
            "mothers_name", mothers_name, nullable=True
        )
        self.nationality = self._define_str("nationality", nationality, nullable=True)
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
        self.second_last_name = self._define_str(
            "second_last_name", second_last_name, nullable=True
        )
        self.send_notifications = send_notifications
        self.contact_reference_id = self._define_str(
            "contact_reference_id", contact_reference_id, nullable=True
        )
