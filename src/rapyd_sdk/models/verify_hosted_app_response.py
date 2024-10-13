from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .verify_hosted_app_response_merchant_details import (
    VerifyHostedAppResponseMerchantDetails,
)


@JsonMap({})
class VerifyHostedAppResponse(BaseModel):
    """VerifyHostedAppResponse

    :param token: Identifier of the hosted application. String starting with happ_., defaults to None
    :type token: str, optional
    :param rapyd_entity_token: The ID of the Rapyd wallet of the company. String starting with ewallet_. Must be a company type wallet., defaults to None
    :type rapyd_entity_token: str, optional
    :param cancel_url: URL where the customer is redirected after pressing Back to Website to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
    :type cancel_url: str, optional
    :param complete_url: URL where the customer is redirected after pressing Close to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
    :type complete_url: str, optional
    :param client_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
    :type client_reference_id: str, optional
    :param application_token: Identifier of the application. String starting with app_., defaults to None
    :type application_token: str, optional
    :param phone_number: The phone number of the applicant. This is the phone number where an authentication code is sent. Must have a leading plus sign (+)., defaults to None
    :type phone_number: str, optional
    :param merchant_details: Object containing information about the merchant., defaults to None
    :type merchant_details: VerifyHostedAppResponseMerchantDetails, optional
    :param redirect_url: URL of the hosted page that is shown to the customer., defaults to None
    :type redirect_url: str, optional
    :param metadata: A JSON object defined by the client, defaults to None
    :type metadata: dict, optional
    :param authorized_user_email: authorized_user_email, defaults to None
    :type authorized_user_email: str, optional
    """

    def __init__(
        self,
        token: str = None,
        rapyd_entity_token: str = None,
        cancel_url: str = None,
        complete_url: str = None,
        client_reference_id: str = None,
        application_token: str = None,
        phone_number: str = None,
        merchant_details: VerifyHostedAppResponseMerchantDetails = None,
        redirect_url: str = None,
        metadata: dict = None,
        authorized_user_email: str = None,
    ):
        """VerifyHostedAppResponse

        :param token: Identifier of the hosted application. String starting with happ_., defaults to None
        :type token: str, optional
        :param rapyd_entity_token: The ID of the Rapyd wallet of the company. String starting with ewallet_. Must be a company type wallet., defaults to None
        :type rapyd_entity_token: str, optional
        :param cancel_url: URL where the customer is redirected after pressing Back to Website to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
        :type cancel_url: str, optional
        :param complete_url: URL where the customer is redirected after pressing Close to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
        :type complete_url: str, optional
        :param client_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
        :type client_reference_id: str, optional
        :param application_token: Identifier of the application. String starting with app_., defaults to None
        :type application_token: str, optional
        :param phone_number: The phone number of the applicant. This is the phone number where an authentication code is sent. Must have a leading plus sign (+)., defaults to None
        :type phone_number: str, optional
        :param merchant_details: Object containing information about the merchant., defaults to None
        :type merchant_details: VerifyHostedAppResponseMerchantDetails, optional
        :param redirect_url: URL of the hosted page that is shown to the customer., defaults to None
        :type redirect_url: str, optional
        :param metadata: A JSON object defined by the client, defaults to None
        :type metadata: dict, optional
        :param authorized_user_email: authorized_user_email, defaults to None
        :type authorized_user_email: str, optional
        """
        self.token = self._define_str("token", token, nullable=True)
        self.rapyd_entity_token = self._define_str(
            "rapyd_entity_token", rapyd_entity_token, nullable=True
        )
        self.cancel_url = self._define_str("cancel_url", cancel_url, nullable=True)
        self.complete_url = self._define_str(
            "complete_url", complete_url, nullable=True
        )
        self.client_reference_id = self._define_str(
            "client_reference_id", client_reference_id, nullable=True
        )
        self.application_token = self._define_str(
            "application_token", application_token, nullable=True
        )
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
        self.merchant_details = self._define_object(
            merchant_details, VerifyHostedAppResponseMerchantDetails
        )
        self.redirect_url = self._define_str(
            "redirect_url", redirect_url, nullable=True
        )
        self.metadata = metadata
        self.authorized_user_email = self._define_str(
            "authorized_user_email", authorized_user_email, nullable=True
        )
