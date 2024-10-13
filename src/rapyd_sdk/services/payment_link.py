from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import CollectPaymentsBody, InlineResponse200_60


class PaymentLinkService(BaseService):

    @cast_models
    def payment_link(self, payment_link: str) -> InlineResponse200_60:
        """Retrieve details of a payment link.

        :param payment_link: ID of the payment link. String starting with **hp_reuse_**.
        :type payment_link: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Payment Link Fetched successfully
        :rtype: InlineResponse200_60
        """

        Validator(str).validate(payment_link)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/hosted/collect/payments/{{paymentLink}}",
                self.get_default_headers(),
            )
            .add_path("paymentLink", payment_link, explode=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_60._unmap(response)

    @cast_models
    def create_payment_link(
        self, request_body: CollectPaymentsBody = None
    ) -> InlineResponse200_60:
        """Creates a reusable link for a hosted payment page. <BR> A customer can use the link and the hosted payment page multiple times. After providing required information, the customer is redirected seamlessly to a Rapyd Checkout page to complete the payment.You can create the link for everyone or for a specific customer. You can make the payment amount fixed, editable, or open.

        :param request_body: The request body., defaults to None
        :type request_body: CollectPaymentsBody, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Payment Link Fetched successfully
        :rtype: InlineResponse200_60
        """

        Validator(CollectPaymentsBody).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/hosted/collect/payments/",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_60._unmap(response)
