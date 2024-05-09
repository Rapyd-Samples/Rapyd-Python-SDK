from __future__ import annotations
from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Address import Address


class EntityType1(Enum):
    SOLE_PROP = "sole_prop"
    PARTNERSHIP = "partnership"
    COMPANY = "company"
    GOVERNMENT = "government"
    CHARITY = "charity"
    NPO = "NPO"
    ASSOCIATION = "association"
    TRUST = "trust"

    def list():
        return list(map(lambda x: x.value, EntityType1._member_map_.values()))


@JsonMap({})
class ContactBusiness(BaseModel):
    def __init__(
        self,
        address: Address = None,
        annual_revenue: float = None,
        cnae_code: str = None,
        created_at: float = None,
        entity_type: EntityType1 = None,
        establishment_date: str = None,
        id: str = None,
        industry_category: str = None,
        industry_sub_category: str = None,
        legal_entity_type: str = None,
        name: str = None,
        registration_number: str = None,
    ):
        self.address = self._define_object(address, Address)
        self.annual_revenue = annual_revenue
        self.cnae_code = cnae_code
        self.created_at = created_at
        self.entity_type = (
            self._enum_matching(entity_type, EntityType1.list(), "entity_type")
            if entity_type
            else None
        )
        self.establishment_date = (
            self._pattern_matching(
                establishment_date, "^\d{4}-\d{2}-\d{2}$", "establishment_date"
            )
            if establishment_date
            else None
        )
        self.id = id
        self.industry_category = (
            self._pattern_matching(
                industry_category, "^[a-zA-Z0-9]+$", "industry_category"
            )
            if industry_category
            else None
        )
        self.industry_sub_category = industry_sub_category
        self.legal_entity_type = legal_entity_type
        self.name = name
        self.registration_number = registration_number
