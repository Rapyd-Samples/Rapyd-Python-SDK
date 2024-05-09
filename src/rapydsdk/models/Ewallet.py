from __future__ import annotations
from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Account import Account
from .Contact import Contact


class Category1(Enum):
    COLLECT = "collect"
    DISBURSE = "disburse"
    CARD_AUTHORIZATION = "card_authorization"
    GENERAL = "general"

    def list():
        return list(map(lambda x: x.value, Category1._member_map_.values()))


@JsonMap({})
class Contacts(BaseModel):
    def __init__(
        self,
        data: List[Contact] = None,
        has_more: bool = None,
        total_count: int = None,
        url: str = None,
    ):
        self.data = self._define_list(data, Contact)
        self.has_more = has_more
        self.total_count = total_count
        self.url = url


class Status5(Enum):
    ACT = "ACT"
    DIS = "DIS"

    def list():
        return list(map(lambda x: x.value, Status5._member_map_.values()))


class Type5(Enum):
    COMPANY = "company"
    PERSON = "person"
    CLIENT = "client"

    def list():
        return list(map(lambda x: x.value, Type5._member_map_.values()))


@JsonMap({"type_": "type"})
class Ewallet(BaseModel):
    def __init__(
        self,
        accounts: List[Account] = None,
        category: Category1 = None,
        contacts: Contacts = None,
        email: str = None,
        ewallet_reference_id: str = None,
        first_name: str = None,
        id: str = None,
        last_name: str = None,
        metadata: dict = None,
        phone_number: str = None,
        status: Status5 = None,
        type_: Type5 = None,
        verification_status: str = None,
    ):
        self.accounts = self._define_list(accounts, Account)
        self.category = (
            self._enum_matching(category, Category1.list(), "category")
            if category
            else None
        )
        self.contacts = self._define_object(contacts, Contacts)
        self.email = email
        self.ewallet_reference_id = ewallet_reference_id
        self.first_name = first_name
        self.id = id
        self.last_name = last_name
        self.metadata = metadata
        self.phone_number = phone_number
        self.status = (
            self._enum_matching(status, Status5.list(), "status") if status else None
        )
        self.type_ = (
            self._enum_matching(type_, Type5.list(), "type_") if type_ else None
        )
        self.verification_status = verification_status
