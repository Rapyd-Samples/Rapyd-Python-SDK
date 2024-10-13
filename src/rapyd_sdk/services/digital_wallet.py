from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import ApplePayObject, InlineResponse200_46


class DigitalWalletService(BaseService):

    @cast_models
    def get_apple_pay_session(
        self, request_body: ApplePayObject
    ) -> InlineResponse200_46:
        """Retrieve the details of an Apple Pay payment session. Each payment that uses Apple Pay has a unique session.  [Activating Apple Pay](https://docs.rapyd.net/en/activating-apple-pay.html) is a prerequisite.

        :param request_body: The request body.
        :type request_body: ApplePayObject
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Apple Pay response fetched successfuly.
        :rtype: InlineResponse200_46
        """

        Validator(ApplePayObject).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/digital_wallets/session/apple_pay",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_46._unmap(response)
