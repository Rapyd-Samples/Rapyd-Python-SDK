from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address import Address


class ContactBusinessEntityType(Enum):
    """An enumeration representing different categories.

    :cvar SOLEPROP: "sole_prop"
    :vartype SOLEPROP: str
    :cvar PARTNERSHIP: "partnership"
    :vartype PARTNERSHIP: str
    :cvar COMPANY: "company"
    :vartype COMPANY: str
    :cvar GOVERNMENT: "government"
    :vartype GOVERNMENT: str
    :cvar CHARITY: "charity"
    :vartype CHARITY: str
    :cvar NPO: "NPO"
    :vartype NPO: str
    :cvar ASSOCIATION: "association"
    :vartype ASSOCIATION: str
    :cvar TRUST: "trust"
    :vartype TRUST: str
    """

    SOLEPROP = "sole_prop"
    PARTNERSHIP = "partnership"
    COMPANY = "company"
    GOVERNMENT = "government"
    CHARITY = "charity"
    NPO = "NPO"
    ASSOCIATION = "association"
    TRUST = "trust"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ContactBusinessEntityType._member_map_.values())
        )


@JsonMap({"id_": "id"})
class ContactBusiness(BaseModel):
    """ContactBusiness

    :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
    :type address: Address, optional
    :param annual_revenue: Annual revenue of the business in US dollars. Maximum value 100000000000000. Decimal., defaults to None
    :type annual_revenue: float, optional
    :param cnae_code: Business activity code of the business, according to the ClassificaÃ§Ã£o Nacional de Atividades EconÃ´micas of Brazil. Alphanumeric string. Maximum 7 characters., defaults to None
    :type cnae_code: str, optional
    :param created_at: Time of creation of the business_details object, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param entity_type: Type of business entity, defaults to None
    :type entity_type: ContactBusinessEntityType, optional
    :param establishment_date: Date that the business was established. Format YYYY-MM-DD, defaults to None
    :type establishment_date: str, optional
    :param id_: ID of the business_details object. String starting with busi_., defaults to None
    :type id_: str, optional
    :param industry_category: Name of the industry that this business belongs to. Required. Alphanumeric string with no special characters., defaults to None
    :type industry_category: str, optional
    :param industry_sub_category: Subcategory of the industry that this business belongs to., defaults to None
    :type industry_sub_category: str, optional
    :param legal_entity_type: Type of legal entity. Alphanumeric string., defaults to None
    :type legal_entity_type: str, optional
    :param name: Business name., defaults to None
    :type name: str, optional
    :param registration_number: Registration number., defaults to None
    :type registration_number: str, optional
    """

    def __init__(
        self,
        address: Address = None,
        annual_revenue: float = None,
        cnae_code: str = None,
        created_at: float = None,
        entity_type: ContactBusinessEntityType = None,
        establishment_date: str = None,
        id_: str = None,
        industry_category: str = None,
        industry_sub_category: str = None,
        legal_entity_type: str = None,
        name: str = None,
        registration_number: str = None,
    ):
        """ContactBusiness

        :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
        :type address: Address, optional
        :param annual_revenue: Annual revenue of the business in US dollars. Maximum value 100000000000000. Decimal., defaults to None
        :type annual_revenue: float, optional
        :param cnae_code: Business activity code of the business, according to the ClassificaÃ§Ã£o Nacional de Atividades EconÃ´micas of Brazil. Alphanumeric string. Maximum 7 characters., defaults to None
        :type cnae_code: str, optional
        :param created_at: Time of creation of the business_details object, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param entity_type: Type of business entity, defaults to None
        :type entity_type: ContactBusinessEntityType, optional
        :param establishment_date: Date that the business was established. Format YYYY-MM-DD, defaults to None
        :type establishment_date: str, optional
        :param id_: ID of the business_details object. String starting with busi_., defaults to None
        :type id_: str, optional
        :param industry_category: Name of the industry that this business belongs to. Required. Alphanumeric string with no special characters., defaults to None
        :type industry_category: str, optional
        :param industry_sub_category: Subcategory of the industry that this business belongs to., defaults to None
        :type industry_sub_category: str, optional
        :param legal_entity_type: Type of legal entity. Alphanumeric string., defaults to None
        :type legal_entity_type: str, optional
        :param name: Business name., defaults to None
        :type name: str, optional
        :param registration_number: Registration number., defaults to None
        :type registration_number: str, optional
        """
        self.address = self._define_object(address, Address)
        self.annual_revenue = self._define_number(
            "annual_revenue", annual_revenue, nullable=True
        )
        self.cnae_code = self._define_str("cnae_code", cnae_code, nullable=True)
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.entity_type = (
            self._enum_matching(
                entity_type, ContactBusinessEntityType.list(), "entity_type"
            )
            if entity_type
            else None
        )
        self.establishment_date = self._define_str(
            "establishment_date",
            establishment_date,
            nullable=True,
            pattern="^\d{4}-\d{2}-\d{2}$",
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.industry_category = self._define_str(
            "industry_category",
            industry_category,
            nullable=True,
            pattern="^[a-zA-Z0-9]+$",
        )
        self.industry_sub_category = self._define_str(
            "industry_sub_category", industry_sub_category, nullable=True
        )
        self.legal_entity_type = self._define_str(
            "legal_entity_type", legal_entity_type, nullable=True
        )
        self.name = self._define_str("name", name, nullable=True)
        self.registration_number = self._define_str(
            "registration_number", registration_number, nullable=True
        )
