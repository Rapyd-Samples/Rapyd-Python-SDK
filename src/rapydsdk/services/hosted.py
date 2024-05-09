from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GenerateCardTokenizationPageRequest import (
    GenerateCardTokenizationPageRequest as GenerateCardTokenizationPageRequestModel,
)
from ..models.GenerateCardTokenizationPage200Response import (
    GenerateCardTokenizationPage200Response as GenerateCardTokenizationPage200ResponseModel,
)
from ..models.GenerateIdvPageRequest import (
    GenerateIdvPageRequest as GenerateIdvPageRequestModel,
)
from ..models.GenerateIdvPage200Response import (
    GenerateIdvPage200Response as GenerateIdvPage200ResponseModel,
)
from ..models.GenerateCardIssuingPageRequest import (
    GenerateCardIssuingPageRequest as GenerateCardIssuingPageRequestModel,
)
from ..models.GenerateCardIssuingPage200Response import (
    GenerateCardIssuingPage200Response as GenerateCardIssuingPage200ResponseModel,
)


class Hosted(BaseService):
    def generate_card_tokenization_page(
        self, request_input: GenerateCardTokenizationPageRequestModel
    ) -> GenerateCardTokenizationPage200ResponseModel:
        """
        Create a hosted page for a customer to save card details and manage cards.
        """

        if isinstance(request_input, dict):
            request_input = GenerateCardTokenizationPageRequestModel(**request_input)
        url_endpoint = "/v1/hosted/collect/card"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return GenerateCardTokenizationPage200ResponseModel._unmap(res)
        return res

    def generate_idv_page(
        self, request_input: GenerateIdvPageRequestModel
    ) -> GenerateIdvPage200ResponseModel:
        """
        Create Identity Verification Page
        """

        if isinstance(request_input, dict):
            request_input = GenerateIdvPageRequestModel(**request_input)
        url_endpoint = "/v1/hosted/idv"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return GenerateIdvPage200ResponseModel._unmap(res)
        return res

    def generate_card_issuing_page(
        self, request_input: GenerateCardIssuingPageRequestModel, card_token: str
    ) -> GenerateCardIssuingPage200ResponseModel:
        """
        Generate a hosted page that displays details of a virtual issued card directly to the customer.
        Parameters:
        ----------
            card_token: str
                ID of the Issued Card Details to Customer.
        """

        if isinstance(request_input, dict):
            request_input = GenerateCardIssuingPageRequestModel(**request_input)
        url_endpoint = "/v1/hosted/issuing/card_details/{card_token}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not card_token:
            raise ValueError(
                "Parameter card_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{card_token}",
            quote(
                str(query_serializer.serialize_path("simple", False, card_token, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return GenerateCardIssuingPage200ResponseModel._unmap(res)
        return res
