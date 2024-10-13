from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inline_response_200_90_data_organization_details_merchant_customer_support import (
    InlineResponse200_90DataOrganizationDetailsMerchantCustomerSupport,
)


@JsonMap({})
class InlineResponse200_90DataOrganizationDetails(BaseModel):
    """InlineResponse200_90DataOrganizationDetails

    :param merchant_color: merchant_color, defaults to None
    :type merchant_color: str, optional
    :param merchant_website: merchant_website, defaults to None
    :type merchant_website: str, optional
    :param merchant_logo: merchant_logo, defaults to None
    :type merchant_logo: str, optional
    :param merchant_design: merchant_design, defaults to None
    :type merchant_design: str, optional
    :param merchant_language: merchant_language, defaults to None
    :type merchant_language: str, optional
    :param merchant_alias: merchant_alias, defaults to None
    :type merchant_alias: str, optional
    :param merchant_customer_support: merchant_customer_support, defaults to None
    :type merchant_customer_support: InlineResponse200_90DataOrganizationDetailsMerchantCustomerSupport, optional
    """

    def __init__(
        self,
        merchant_color: str = None,
        merchant_website: str = None,
        merchant_logo: str = None,
        merchant_design: str = None,
        merchant_language: str = None,
        merchant_alias: str = None,
        merchant_customer_support: InlineResponse200_90DataOrganizationDetailsMerchantCustomerSupport = None,
    ):
        """InlineResponse200_90DataOrganizationDetails

        :param merchant_color: merchant_color, defaults to None
        :type merchant_color: str, optional
        :param merchant_website: merchant_website, defaults to None
        :type merchant_website: str, optional
        :param merchant_logo: merchant_logo, defaults to None
        :type merchant_logo: str, optional
        :param merchant_design: merchant_design, defaults to None
        :type merchant_design: str, optional
        :param merchant_language: merchant_language, defaults to None
        :type merchant_language: str, optional
        :param merchant_alias: merchant_alias, defaults to None
        :type merchant_alias: str, optional
        :param merchant_customer_support: merchant_customer_support, defaults to None
        :type merchant_customer_support: InlineResponse200_90DataOrganizationDetailsMerchantCustomerSupport, optional
        """
        self.merchant_color = self._define_str(
            "merchant_color", merchant_color, nullable=True
        )
        self.merchant_website = self._define_str(
            "merchant_website", merchant_website, nullable=True
        )
        self.merchant_logo = self._define_str(
            "merchant_logo", merchant_logo, nullable=True
        )
        self.merchant_design = self._define_str(
            "merchant_design", merchant_design, nullable=True
        )
        self.merchant_language = self._define_str(
            "merchant_language", merchant_language, nullable=True
        )
        self.merchant_alias = self._define_str(
            "merchant_alias", merchant_alias, nullable=True
        )
        self.merchant_customer_support = self._define_object(
            merchant_customer_support,
            InlineResponse200_90DataOrganizationDetailsMerchantCustomerSupport,
        )
