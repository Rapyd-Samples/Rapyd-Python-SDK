from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class MerchantCustomerSupport2(BaseModel):
    def __init__(self, email: str = None, url: str = None, phone_number: str = None):
        self.email = email
        self.url = url
        self.phone_number = phone_number


@JsonMap({})
class MerchantDetails(BaseModel):
    def __init__(
        self,
        merchant_alias: str = None,
        merchant_language: str = None,
        merchant_logo: str = None,
        merchant_website: str = None,
        merchant_color: str = None,
        merchant_design: str = None,
        merchant_customer_support: MerchantCustomerSupport2 = None,
        merchant_terms: str = None,
        merchant_privacy_policy: str = None,
    ):
        self.merchant_alias = merchant_alias
        self.merchant_language = merchant_language
        self.merchant_logo = merchant_logo
        self.merchant_website = merchant_website
        self.merchant_color = merchant_color
        self.merchant_design = merchant_design
        self.merchant_customer_support = self._define_object(
            merchant_customer_support, MerchantCustomerSupport2
        )
        self.merchant_terms = merchant_terms
        self.merchant_privacy_policy = merchant_privacy_policy


@JsonMap({})
class VerifyHostedAppResponse(BaseModel):
    def __init__(
        self,
        token: str = None,
        rapyd_entity_token: str = None,
        cancel_url: str = None,
        complete_url: str = None,
        client_reference_id: str = None,
        application_token: str = None,
        phone_number: str = None,
        merchant_details: MerchantDetails = None,
        redirect_url: str = None,
        metadata: dict = None,
        authorized_user_email: str = None,
    ):
        self.token = token
        self.rapyd_entity_token = rapyd_entity_token
        self.cancel_url = cancel_url
        self.complete_url = complete_url
        self.client_reference_id = client_reference_id
        self.application_token = application_token
        self.phone_number = phone_number
        self.merchant_details = self._define_object(merchant_details, MerchantDetails)
        self.redirect_url = redirect_url
        self.metadata = metadata
        self.authorized_user_email = authorized_user_email
