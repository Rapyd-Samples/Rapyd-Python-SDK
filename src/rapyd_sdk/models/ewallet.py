from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account import Account
from .ewallet_contacts import EwalletContacts


class EwalletCategory(Enum):
    """An enumeration representing different categories.

    :cvar COLLECT: "collect"
    :vartype COLLECT: str
    :cvar DISBURSE: "disburse"
    :vartype DISBURSE: str
    :cvar CARDAUTHORIZATION: "card_authorization"
    :vartype CARDAUTHORIZATION: str
    :cvar GENERAL: "general"
    :vartype GENERAL: str
    """

    COLLECT = "collect"
    DISBURSE = "disburse"
    CARDAUTHORIZATION = "card_authorization"
    GENERAL = "general"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EwalletCategory._member_map_.values()))


class EwalletStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACT: "ACT"
    :vartype ACT: str
    :cvar DIS: "DIS"
    :vartype DIS: str
    """

    ACT = "ACT"
    DIS = "DIS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EwalletStatus._member_map_.values()))


class EwalletType(Enum):
    """An enumeration representing different categories.

    :cvar COMPANY: "company"
    :vartype COMPANY: str
    :cvar PERSON: "person"
    :vartype PERSON: str
    :cvar CLIENT: "client"
    :vartype CLIENT: str
    """

    COMPANY = "company"
    PERSON = "person"
    CLIENT = "client"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EwalletType._member_map_.values()))


@JsonMap({"id_": "id", "type_": "type"})
class Ewallet(BaseModel):
    """Ewallet

    :param accounts: accounts, defaults to None
    :type accounts: List[Account], optional
    :param category: Indicates the type of client wallet, defaults to None
    :type category: EwalletCategory, optional
    :param contacts: contacts, defaults to None
    :type contacts: EwalletContacts, optional
    :param email: Email address of the wallet owner. Response only. Deprecated., defaults to None
    :type email: str, optional
    :param ewallet_reference_id: Wallet ID defined by the customer or end user. Must be unique., defaults to None
    :type ewallet_reference_id: str, optional
    :param first_name: First name of the wallet owner., defaults to None
    :type first_name: str, optional
    :param id_: Unique identifier of the wallet object. String starting with **ewallet_**., defaults to None
    :type id_: str, optional
    :param last_name: Last name of the wallet owner., defaults to None
    :type last_name: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param phone_number: Phone number of the wallet owner in E.164 format. Response only. Deprecated., defaults to None
    :type phone_number: str, optional
    :param status: Status of the wallet, defaults to None
    :type status: EwalletStatus, optional
    :param type_: Type of wallet., defaults to None
    :type type_: EwalletType, optional
    :param verification_status: Result of the verification check., defaults to None
    :type verification_status: str, optional
    """

    def __init__(
        self,
        accounts: List[Account] = None,
        category: EwalletCategory = None,
        contacts: EwalletContacts = None,
        email: str = None,
        ewallet_reference_id: str = None,
        first_name: str = None,
        id_: str = None,
        last_name: str = None,
        metadata: dict = None,
        phone_number: str = None,
        status: EwalletStatus = None,
        type_: EwalletType = None,
        verification_status: str = None,
    ):
        """Ewallet

        :param accounts: accounts, defaults to None
        :type accounts: List[Account], optional
        :param category: Indicates the type of client wallet, defaults to None
        :type category: EwalletCategory, optional
        :param contacts: contacts, defaults to None
        :type contacts: EwalletContacts, optional
        :param email: Email address of the wallet owner. Response only. Deprecated., defaults to None
        :type email: str, optional
        :param ewallet_reference_id: Wallet ID defined by the customer or end user. Must be unique., defaults to None
        :type ewallet_reference_id: str, optional
        :param first_name: First name of the wallet owner., defaults to None
        :type first_name: str, optional
        :param id_: Unique identifier of the wallet object. String starting with **ewallet_**., defaults to None
        :type id_: str, optional
        :param last_name: Last name of the wallet owner., defaults to None
        :type last_name: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param phone_number: Phone number of the wallet owner in E.164 format. Response only. Deprecated., defaults to None
        :type phone_number: str, optional
        :param status: Status of the wallet, defaults to None
        :type status: EwalletStatus, optional
        :param type_: Type of wallet., defaults to None
        :type type_: EwalletType, optional
        :param verification_status: Result of the verification check., defaults to None
        :type verification_status: str, optional
        """
        self.accounts = self._define_list(accounts, Account)
        self.category = (
            self._enum_matching(category, EwalletCategory.list(), "category")
            if category
            else None
        )
        self.contacts = self._define_object(contacts, EwalletContacts)
        self.email = self._define_str("email", email, nullable=True)
        self.ewallet_reference_id = self._define_str(
            "ewallet_reference_id", ewallet_reference_id, nullable=True
        )
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.last_name = self._define_str("last_name", last_name, nullable=True)
        self.metadata = metadata
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
        self.status = (
            self._enum_matching(status, EwalletStatus.list(), "status")
            if status
            else None
        )
        self.type_ = (
            self._enum_matching(type_, EwalletType.list(), "type_") if type_ else None
        )
        self.verification_status = self._define_str(
            "verification_status", verification_status, nullable=True
        )
