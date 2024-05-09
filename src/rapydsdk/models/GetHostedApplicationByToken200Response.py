from __future__ import annotations
from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


class ApplicationLevel(Enum):
    V1 = 1
    V2 = 2

    def list():
        return list(map(lambda x: x.value, ApplicationLevel._member_map_.values()))


@JsonMap({})
class ApplicationType(BaseModel):
    def __init__(
        self, application_type: str = None, entity_type: str = None, country: str = None
    ):
        self.application_type = application_type
        self.entity_type = entity_type
        self.country = country


@JsonMap({})
class MerchantCustomerSupport3(BaseModel):
    def __init__(self, url: str = None, email: str = None, phone_number: str = None):
        self.url = url
        self.email = email
        self.phone_number = phone_number


@JsonMap({})
class OrganizationDetails(BaseModel):
    def __init__(
        self,
        merchant_color: str = None,
        merchant_website: str = None,
        merchant_logo: str = None,
        merchant_design: str = None,
        merchant_language: str = None,
        merchant_alias: str = None,
        merchant_customer_support: MerchantCustomerSupport3 = None,
    ):
        self.merchant_color = merchant_color
        self.merchant_website = merchant_website
        self.merchant_logo = merchant_logo
        self.merchant_design = merchant_design
        self.merchant_language = merchant_language
        self.merchant_alias = merchant_alias
        self.merchant_customer_support = self._define_object(
            merchant_customer_support, MerchantCustomerSupport3
        )


@JsonMap({})
class RenewResult(BaseModel):
    def __init__(
        self, redirect_to_app_type_page: bool = None, need_to_renew: bool = None
    ):
        self.redirect_to_app_type_page = redirect_to_app_type_page
        self.need_to_renew = need_to_renew


@JsonMap({})
class Data34(BaseModel):
    def __init__(
        self,
        token: str = None,
        application_token: str = None,
        country: str = None,
        rapyd_entity_token: str = None,
        client_reference_id: str = None,
        cancel_url: str = None,
        complete_url: str = None,
        phone_number: str = None,
        application_level: ApplicationLevel = None,
        sell_type: str = None,
        business_industry: str = None,
        application_type: ApplicationType = None,
        organization_details: OrganizationDetails = None,
        renew_result: RenewResult = None,
    ):
        self.token = token
        self.application_token = application_token
        self.country = country
        self.rapyd_entity_token = rapyd_entity_token
        self.client_reference_id = client_reference_id
        self.cancel_url = cancel_url
        self.complete_url = complete_url
        self.phone_number = phone_number
        self.application_level = (
            self._enum_matching(
                application_level, ApplicationLevel.list(), "application_level"
            )
            if application_level
            else None
        )
        self.sell_type = sell_type
        self.business_industry = business_industry
        self.application_type = self._define_object(application_type, ApplicationType)
        self.organization_details = self._define_object(
            organization_details, OrganizationDetails
        )
        self.renew_result = self._define_object(renew_result, RenewResult)


@JsonMap({})
class GetHostedApplicationByToken200Response(BaseModel):
    def __init__(self, data: Data34 = None, status: Status = None):
        self.data = self._define_object(data, Data34)
        self.status = self._define_object(status, Status)
