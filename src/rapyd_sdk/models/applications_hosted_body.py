from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ApplicationsHostedBody(BaseModel):
    """ApplicationsHostedBody

    :param application_type: Code for the type of application., defaults to None
    :type application_type: str, optional
    :param country: The country where the company is domiciled. Two-letter ISO 3166-1 ALPHA-2 code. The hosted application displays the country as the default setting.
    :type country: str
    :param rapyd_entity_token: The ID of the Rapyd wallet of the company. String starting with ewallet_.
    :type rapyd_entity_token: str
    :param phone_number: The phone number of the applicant. This is the phone number where an authentication code is sent. Must have a leading plus sign (+).
    :type phone_number: str
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param client_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
    :type client_reference_id: str, optional
    :param cancel_url: URL where the customer is redirected after pressing Back to Website to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
    :type cancel_url: str, optional
    :param complete_url: URL where the customer is redirected after pressing Close to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
    :type complete_url: str, optional
    """

    def __init__(
        self,
        country: str,
        rapyd_entity_token: str,
        phone_number: str,
        application_type: str = None,
        metadata: dict = None,
        client_reference_id: str = None,
        cancel_url: str = None,
        complete_url: str = None,
    ):
        """ApplicationsHostedBody

        :param application_type: Code for the type of application., defaults to None
        :type application_type: str, optional
        :param country: The country where the company is domiciled. Two-letter ISO 3166-1 ALPHA-2 code. The hosted application displays the country as the default setting.
        :type country: str
        :param rapyd_entity_token: The ID of the Rapyd wallet of the company. String starting with ewallet_.
        :type rapyd_entity_token: str
        :param phone_number: The phone number of the applicant. This is the phone number where an authentication code is sent. Must have a leading plus sign (+).
        :type phone_number: str
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param client_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
        :type client_reference_id: str, optional
        :param cancel_url: URL where the customer is redirected after pressing Back to Website to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
        :type cancel_url: str, optional
        :param complete_url: URL where the customer is redirected after pressing Close to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
        :type complete_url: str, optional
        """
        self.application_type = self._define_str(
            "application_type", application_type, nullable=True
        )
        self.country = country
        self.rapyd_entity_token = rapyd_entity_token
        self.phone_number = phone_number
        self.metadata = metadata
        self.client_reference_id = self._define_str(
            "client_reference_id", client_reference_id, nullable=True
        )
        self.cancel_url = self._define_str("cancel_url", cancel_url, nullable=True)
        self.complete_url = self._define_str(
            "complete_url", complete_url, nullable=True
        )
