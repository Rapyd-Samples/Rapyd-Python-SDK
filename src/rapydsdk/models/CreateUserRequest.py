from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Contact import Contact


@JsonMap({})
class Contact1(BaseModel):
    def __init__(
        self,
        data: List[Contact] = None,
        total_count: float = None,
        has_more: bool = None,
        url: str = None,
    ):
        self.data = self._define_list(data, Contact)
        self.total_count = total_count
        self.has_more = has_more
        self.url = url


@JsonMap({"type_": "type"})
class CreateUserRequest(BaseModel):
    def __init__(
        self,
        contact: Contact1 = None,
        ewallet_reference_id: str = None,
        first_name: str = None,
        last_name: str = None,
        metadata: dict = None,
        type_: str = None,
    ):
        self.contact = self._define_object(contact, Contact1)
        self.ewallet_reference_id = ewallet_reference_id
        self.first_name = first_name
        self.last_name = last_name
        self.metadata = metadata
        self.type_ = type_
