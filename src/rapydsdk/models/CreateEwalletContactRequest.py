from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Address import Address


@JsonMap({})
class CreateEwalletContactRequest(BaseModel):
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
        self.address = self._define_object(address, Address)
        self.contact_type = contact_type
        self.country = country
        self.date_of_birth = date_of_birth
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.house_type = house_type
        self.identification_number = identification_number
        self.identification_type = identification_type
        self.marital_status = marital_status
        self.metadata = metadata
        self.middle_name = middle_name
        self.mothers_name = mothers_name
        self.nationality = nationality
        self.phone_number = phone_number
        self.second_last_name = second_last_name
        self.send_notifications = send_notifications
        self.contact_reference_id = contact_reference_id
