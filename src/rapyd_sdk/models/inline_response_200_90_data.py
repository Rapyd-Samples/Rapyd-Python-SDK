from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inline_response_200_90_data_application_type import (
    InlineResponse200_90DataApplicationType,
)
from .inline_response_200_90_data_organization_details import (
    InlineResponse200_90DataOrganizationDetails,
)
from .inline_response_200_90_data_renew_result import (
    InlineResponse200_90DataRenewResult,
)


class ApplicationLevel(Enum):
    """An enumeration representing different categories.

    :cvar _1: 1
    :vartype _1: float
    :cvar _2: 2
    :vartype _2: float
    """

    _1 = 1
    _2 = 2

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ApplicationLevel._member_map_.values()))


@JsonMap({})
class InlineResponse200_90Data(BaseModel):
    """InlineResponse200_90Data

    :param token: token, defaults to None
    :type token: str, optional
    :param application_token: application_token, defaults to None
    :type application_token: str, optional
    :param country: country, defaults to None
    :type country: str, optional
    :param rapyd_entity_token: rapyd_entity_token, defaults to None
    :type rapyd_entity_token: str, optional
    :param client_reference_id: client_reference_id, defaults to None
    :type client_reference_id: str, optional
    :param cancel_url: cancel_url, defaults to None
    :type cancel_url: str, optional
    :param complete_url: complete_url, defaults to None
    :type complete_url: str, optional
    :param phone_number: phone_number, defaults to None
    :type phone_number: str, optional
    :param application_level: application_level, defaults to None
    :type application_level: ApplicationLevel, optional
    :param sell_type: sell_type, defaults to None
    :type sell_type: str, optional
    :param business_industry: business_industry, defaults to None
    :type business_industry: str, optional
    :param application_type: application_type, defaults to None
    :type application_type: InlineResponse200_90DataApplicationType, optional
    :param organization_details: organization_details, defaults to None
    :type organization_details: InlineResponse200_90DataOrganizationDetails, optional
    :param renew_result: renew_result, defaults to None
    :type renew_result: InlineResponse200_90DataRenewResult, optional
    """

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
        application_type: InlineResponse200_90DataApplicationType = None,
        organization_details: InlineResponse200_90DataOrganizationDetails = None,
        renew_result: InlineResponse200_90DataRenewResult = None,
    ):
        """InlineResponse200_90Data

        :param token: token, defaults to None
        :type token: str, optional
        :param application_token: application_token, defaults to None
        :type application_token: str, optional
        :param country: country, defaults to None
        :type country: str, optional
        :param rapyd_entity_token: rapyd_entity_token, defaults to None
        :type rapyd_entity_token: str, optional
        :param client_reference_id: client_reference_id, defaults to None
        :type client_reference_id: str, optional
        :param cancel_url: cancel_url, defaults to None
        :type cancel_url: str, optional
        :param complete_url: complete_url, defaults to None
        :type complete_url: str, optional
        :param phone_number: phone_number, defaults to None
        :type phone_number: str, optional
        :param application_level: application_level, defaults to None
        :type application_level: ApplicationLevel, optional
        :param sell_type: sell_type, defaults to None
        :type sell_type: str, optional
        :param business_industry: business_industry, defaults to None
        :type business_industry: str, optional
        :param application_type: application_type, defaults to None
        :type application_type: InlineResponse200_90DataApplicationType, optional
        :param organization_details: organization_details, defaults to None
        :type organization_details: InlineResponse200_90DataOrganizationDetails, optional
        :param renew_result: renew_result, defaults to None
        :type renew_result: InlineResponse200_90DataRenewResult, optional
        """
        self.token = self._define_str("token", token, nullable=True)
        self.application_token = self._define_str(
            "application_token", application_token, nullable=True
        )
        self.country = self._define_str("country", country, nullable=True)
        self.rapyd_entity_token = self._define_str(
            "rapyd_entity_token", rapyd_entity_token, nullable=True
        )
        self.client_reference_id = self._define_str(
            "client_reference_id", client_reference_id, nullable=True
        )
        self.cancel_url = self._define_str("cancel_url", cancel_url, nullable=True)
        self.complete_url = self._define_str(
            "complete_url", complete_url, nullable=True
        )
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
        self.application_level = (
            self._enum_matching(
                application_level, ApplicationLevel.list(), "application_level"
            )
            if application_level
            else None
        )
        self.sell_type = self._define_str("sell_type", sell_type, nullable=True)
        self.business_industry = self._define_str(
            "business_industry", business_industry, nullable=True
        )
        self.application_type = self._define_object(
            application_type, InlineResponse200_90DataApplicationType
        )
        self.organization_details = self._define_object(
            organization_details, InlineResponse200_90DataOrganizationDetails
        )
        self.renew_result = self._define_object(
            renew_result, InlineResponse200_90DataRenewResult
        )
