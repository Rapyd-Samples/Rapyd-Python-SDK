from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_checkout_body import V1CheckoutBody
from ..models.utils.cast_models import cast_models
from ..models.inline_response_200_28 import InlineResponse200_28
from ..models.inline_response_200_27 import InlineResponse200_27


class CheckoutPageService(BaseService):

    @cast_models
    def get_hosted_page_payment(self, checkout_token: str) -> InlineResponse200_27:
        """Retrieve a checkout page

        :param checkout_token: ID of the checkout page. String starting with checkout_.
        :type checkout_token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieve a checkout page
        :rtype: InlineResponse200_27
        """

        Validator(str).validate(checkout_token)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/checkout/{{checkout_token}}",
                self.get_default_headers(),
            )
            .add_path("checkout_token", checkout_token)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_27._unmap(response)

    @cast_models
    def generate_hosted_page_payment(
        self, request_body: V1CheckoutBody = None
    ) -> InlineResponse200_28:
        """Create a checkout page that makes a payment.

        :param request_body: The request body., defaults to None
        :type request_body: V1CheckoutBody, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Create a checkout page that makes a payment.
        :rtype: InlineResponse200_28
        """

        Validator(V1CheckoutBody).is_optional().validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/checkout", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_28._unmap(response)
