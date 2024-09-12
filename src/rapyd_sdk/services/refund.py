from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_refunds_body import V1RefundsBody
from ..models.utils.cast_models import cast_models
from ..models.refunds_refund_id_body import RefundsRefundIdBody
from ..models.refunds_group_payments_body import RefundsGroupPaymentsBody
from ..models.refunds_complete_body import RefundsCompleteBody
from ..models.inline_response_200_65 import InlineResponse200_65
from ..models.inline_response_200_64 import InlineResponse200_64
from ..models.inline_response_200_63 import InlineResponse200_63


class RefundService(BaseService):

    @cast_models
    def all_refunds(
        self, ending_before: str = None, limit: str = None, starting_after: str = None
    ) -> InlineResponse200_63:
        """Retrieve a list of all refunds.

        :param ending_before: The ID of the refund created after the last refund you want to retrieve. String starting with refund_., defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of refunds to return. Range, 1-100. Default is 10., defaults to None
        :type limit: str, optional
        :param starting_after: The ID of the refund created before the first refund you want to retrieve. String starting with refund_., defaults to None
        :type starting_after: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet
        :rtype: InlineResponse200_63
        """

        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(limit)
        Validator(str).is_optional().validate(starting_after)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/refunds", self.get_default_headers())
            .add_query("ending_before", ending_before, explode=False)
            .add_query("limit", limit, explode=False)
            .add_query("starting_after", starting_after, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_63._unmap(response)

    @cast_models
    def request_total_create_refund(
        self, request_body: V1RefundsBody
    ) -> InlineResponse200_64:
        """Refund of a payment. The refund is credited against a specific payment. The money is returned to the payment method that was used for the payment, and the currency is the same as what was used in the payment. If the action of a third party is not required, this method triggers the Refund Completed webhook. This webhook contains the same information as the response.

        :param request_body: The request body.
        :type request_body: V1RefundsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet
        :rtype: InlineResponse200_64
        """

        Validator(V1RefundsBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/refunds", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_64._unmap(response)

    @cast_models
    def simulate_complete_refund(
        self, request_body: RefundsCompleteBody
    ) -> InlineResponse200_64:
        """Simulate the action of a third party that is required for completing the refund process. Relevant to sandbox. Use this method when a payment was made with a payment method such as cash, bank redirect or bank transfer, and the payment was completed by an action taken by the customer.

        :param request_body: The request body.
        :type request_body: RefundsCompleteBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet
        :rtype: InlineResponse200_64
        """

        Validator(RefundsCompleteBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/refunds/complete", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_64._unmap(response)

    @cast_models
    def refund_group_payment(
        self, request_body: RefundsGroupPaymentsBody
    ) -> InlineResponse200_65:
        """Refund a group payment when the status of the group payment is closed. The refund is credited against a specific group payment. The money is returned to the payment methods that were used for the payment. If the action of a third party is not required, this method triggers the Refund Completed webhook for each payment method.

        :param request_body: The request body.
        :type request_body: RefundsGroupPaymentsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet
        :rtype: InlineResponse200_65
        """

        Validator(RefundsGroupPaymentsBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/refunds/group_payments", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_65._unmap(response)

    @cast_models
    def refund_by_token(self, refund_id: str) -> InlineResponse200_64:
        """Retrieve the details of a refund object.

        :param refund_id: ID of the 'refund' object you want to retrieve. String starting with refund_.
        :type refund_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet
        :rtype: InlineResponse200_64
        """

        Validator(str).validate(refund_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/refunds/{{refundId}}", self.get_default_headers()
            )
            .add_path("refundId", refund_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_64._unmap(response)

    @cast_models
    def update_refund(
        self, request_body: RefundsRefundIdBody, refund_id: str
    ) -> InlineResponse200_64:
        """Change or modify the metadata in a refund object.

        :param request_body: The request body.
        :type request_body: RefundsRefundIdBody
        :param refund_id: ID of the 'refund' object you want to retrieve. String starting with refund_.
        :type refund_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet
        :rtype: InlineResponse200_64
        """

        Validator(RefundsRefundIdBody).validate(request_body)
        Validator(str).validate(refund_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/refunds/{{refundId}}", self.get_default_headers()
            )
            .add_path("refundId", refund_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_64._unmap(response)
