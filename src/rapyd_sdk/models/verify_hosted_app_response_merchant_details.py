from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .verify_hosted_app_response_merchant_details_merchant_customer_support import (
    VerifyHostedAppResponseMerchantDetailsMerchantCustomerSupport,
)


@JsonMap({})
class VerifyHostedAppResponseMerchantDetails(BaseModel):
    """Object containing information about the merchant.

    :param merchant_alias: The name that appears on the hosted page when merchant_logo is not specified. To change this value, contact Client Support. Response only., defaults to None
    :type merchant_alias: str, optional
    :param merchant_language: Determines the default language of the application page.  The values are documented in List Hosted Page Supported Languages. , defaults to None
    :type merchant_language: str, optional
    :param merchant_logo: URL for the image of the client's logo. Response only. To configure this feature, use the Client Portal., defaults to None
    :type merchant_logo: str, optional
    :param merchant_website: The URL where the customer is redirected after exiting the hosted page., defaults to None
    :type merchant_website: str, optional
    :param merchant_color: merchant_color, defaults to None
    :type merchant_color: str, optional
    :param merchant_design: merchant_design, defaults to None
    :type merchant_design: str, optional
    :param merchant_customer_support: merchant_customer_support, defaults to None
    :type merchant_customer_support: VerifyHostedAppResponseMerchantDetailsMerchantCustomerSupport, optional
    :param merchant_terms: merchant_terms, defaults to None
    :type merchant_terms: str, optional
    :param merchant_privacy_policy: merchant_privacy_policy, defaults to None
    :type merchant_privacy_policy: str, optional
    """

    def __init__(
        self,
        merchant_alias: str = None,
        merchant_language: str = None,
        merchant_logo: str = None,
        merchant_website: str = None,
        merchant_color: str = None,
        merchant_design: str = None,
        merchant_customer_support: VerifyHostedAppResponseMerchantDetailsMerchantCustomerSupport = None,
        merchant_terms: str = None,
        merchant_privacy_policy: str = None,
    ):
        """Object containing information about the merchant.

        :param merchant_alias: The name that appears on the hosted page when merchant_logo is not specified. To change this value, contact Client Support. Response only., defaults to None
        :type merchant_alias: str, optional
        :param merchant_language: Determines the default language of the application page.  The values are documented in List Hosted Page Supported Languages. , defaults to None
        :type merchant_language: str, optional
        :param merchant_logo: URL for the image of the client's logo. Response only. To configure this feature, use the Client Portal., defaults to None
        :type merchant_logo: str, optional
        :param merchant_website: The URL where the customer is redirected after exiting the hosted page., defaults to None
        :type merchant_website: str, optional
        :param merchant_color: merchant_color, defaults to None
        :type merchant_color: str, optional
        :param merchant_design: merchant_design, defaults to None
        :type merchant_design: str, optional
        :param merchant_customer_support: merchant_customer_support, defaults to None
        :type merchant_customer_support: VerifyHostedAppResponseMerchantDetailsMerchantCustomerSupport, optional
        :param merchant_terms: merchant_terms, defaults to None
        :type merchant_terms: str, optional
        :param merchant_privacy_policy: merchant_privacy_policy, defaults to None
        :type merchant_privacy_policy: str, optional
        """
        self.merchant_alias = self._define_str(
            "merchant_alias", merchant_alias, nullable=True
        )
        self.merchant_language = self._define_str(
            "merchant_language", merchant_language, nullable=True
        )
        self.merchant_logo = self._define_str(
            "merchant_logo", merchant_logo, nullable=True
        )
        self.merchant_website = self._define_str(
            "merchant_website", merchant_website, nullable=True
        )
        self.merchant_color = self._define_str(
            "merchant_color", merchant_color, nullable=True
        )
        self.merchant_design = self._define_str(
            "merchant_design", merchant_design, nullable=True
        )
        self.merchant_customer_support = self._define_object(
            merchant_customer_support,
            VerifyHostedAppResponseMerchantDetailsMerchantCustomerSupport,
        )
        self.merchant_terms = self._define_str(
            "merchant_terms", merchant_terms, nullable=True
        )
        self.merchant_privacy_policy = self._define_str(
            "merchant_privacy_policy", merchant_privacy_policy, nullable=True
        )
