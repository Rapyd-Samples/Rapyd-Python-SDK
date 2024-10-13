from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import InlineResponse200_51, PaymentsGroupPaymentsBody


class GroupPaymentService(BaseService):

    @cast_models
    def create_group_payment(
        self, request_body: PaymentsGroupPaymentsBody
    ) -> InlineResponse200_51:
        """Create a group payment.

        :param request_body: The request body.
        :type request_body: PaymentsGroupPaymentsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: get group payment details after creating it.
        :rtype: InlineResponse200_51
        """

        Validator(PaymentsGroupPaymentsBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/group_payments",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_51._unmap(response)

    @cast_models
    def retrieve_group_payment_id(self, group_payment_id: str) -> InlineResponse200_51:
        """Retrieve details of a group payment.

        :param group_payment_id: ID of the group payment. String starting with **gp_**
        :type group_payment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: get group payment details By group payment Id
        :rtype: InlineResponse200_51
        """

        Validator(str).validate(group_payment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/group_payments/{{groupPaymentId}}",
                self.get_default_headers(),
            )
            .add_path("groupPaymentId", group_payment_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_51._unmap(response)

    @cast_models
    def deletegroup_payment_id(self, group_payment_id: str) -> InlineResponse200_51:
        """Cancel a group payment.

        :param group_payment_id: ID of the group payment. String starting with **gp_**
        :type group_payment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Cancel group payment by group_payment Id
        :rtype: InlineResponse200_51
        """

        Validator(str).validate(group_payment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/group_payments/{{groupPaymentId}}",
                self.get_default_headers(),
            )
            .add_path("groupPaymentId", group_payment_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_51._unmap(response)
