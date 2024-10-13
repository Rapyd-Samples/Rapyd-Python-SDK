from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import CollectCardBody, InlineResponse200_61


class PaymentCardTokenService(BaseService):

    @cast_models
    def create_card_token(
        self, request_body: CollectCardBody = None
    ) -> InlineResponse200_61:
        """Create a hosted page for a customer to save card details and manage cards. Prerequisite: [Create Customer](https://docs.rapyd.net/en/create-customer.html).

        :param request_body: The request body., defaults to None
        :type request_body: CollectCardBody, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Card Token created successfully
        :rtype: InlineResponse200_61
        """

        Validator(CollectCardBody).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/hosted/collect/card/", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_61._unmap(response)
