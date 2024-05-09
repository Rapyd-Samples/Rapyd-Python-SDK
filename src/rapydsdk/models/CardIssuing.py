from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Contact import Contact


@JsonMap({})
class CardIssuing(BaseModel):
    def __init__(
        self,
        activated_at: float = None,
        assigned_at: float = None,
        blocked_reason: str = None,
        card_id: str = None,
        card_program: str = None,
        country_iso_alpha_2: str = None,
        created_at: float = None,
        ewallet_contact: Contact = None,
        id: str = None,
        metadata: dict = None,
        public_details: dict = None,
        status: str = None,
        card_tracking_id: str = None,
    ):
        self.activated_at = activated_at
        self.assigned_at = assigned_at
        self.blocked_reason = blocked_reason
        self.card_id = card_id
        self.card_program = card_program
        self.country_iso_alpha_2 = country_iso_alpha_2
        self.created_at = created_at
        self.ewallet_contact = self._define_object(ewallet_contact, Contact)
        self.id = id
        self.metadata = metadata
        self.public_details = public_details
        self.status = status
        self.card_tracking_id = card_tracking_id
