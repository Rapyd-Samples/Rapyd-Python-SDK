from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_payments_body import V1PaymentsBody
from ..models.utils.cast_models import cast_models
from ..models.payments_payment_id_body import PaymentsPaymentIdBody
from ..models.inline_response_200_54 import InlineResponse200_54
from ..models.inline_response_200_53 import InlineResponse200_53
from ..models.customer import Customer


class PaymentService(BaseService):

    @cast_models
    def list_payments(
        self,
        created_after: str = None,
        created_before: str = None,
        customer: Customer = None,
        destination_card: str = None,
        ending_before: str = None,
        ewallet: str = None,
        group: bool = None,
        invoice: str = None,
        limit: str = None,
        payment_method: str = None,
        order: str = None,
        starting_after: str = None,
        subscription: str = None,
        merchant_reference_id: str = None,
    ) -> InlineResponse200_53:
        """Retrieve a list of all payments that you have created. You can filter the list with query parameters.

        :param created_after: The ID of the payment created before the first payment you want to retrieve. String starting with payment_., defaults to None
        :type created_after: str, optional
        :param created_before: The ID of the payment created after the last payment you want to retrieve. String starting with payment_., defaults to None
        :type created_before: str, optional
        :param customer: Filters the list for payments related to the specified customer., defaults to None
        :type customer: Customer, optional
        :param destination_card: Filters the list for payments related to the specified destination card., defaults to None
        :type destination_card: str, optional
        :param ending_before: The ID of the payment created after the last payment you want to retrieve. String starting with payment_. Deprecated., defaults to None
        :type ending_before: str, optional
        :param ewallet: Filters the list for payments related to the specified wallet., defaults to None
        :type ewallet: str, optional
        :param group: When true, includes only group payments in the response. When false, excludes group payments from the response. Default is false., defaults to None
        :type group: bool, optional
        :param invoice: Filters according to the invoice. String starting with invoice_., defaults to None
        :type invoice: str, optional
        :param limit: The maximum number of payments to return. Range, 1-100. Default is 10., defaults to None
        :type limit: str, optional
        :param payment_method: Filters the list for payments related to the specified payment method., defaults to None
        :type payment_method: str, optional
        :param order: Filters the list for payments related to the specified order., defaults to None
        :type order: str, optional
        :param starting_after: The ID of a payment in the list. The list begins with the payment that was created next after the payment with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used. String starting with payment_., defaults to None
        :type starting_after: str, optional
        :param subscription: Filters the list for payments related to the specified subscription., defaults to None
        :type subscription: str, optional
        :param merchant_reference_id: Merchant-defined ID., defaults to None
        :type merchant_reference_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Payments Fetched successfully
        :rtype: InlineResponse200_53
        """

        Validator(str).is_optional().validate(created_after)
        Validator(str).is_optional().validate(created_before)
        Validator(Customer).is_optional().validate(customer)
        Validator(str).is_optional().validate(destination_card)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(ewallet)
        Validator(bool).is_optional().validate(group)
        Validator(str).is_optional().validate(invoice)
        Validator(str).is_optional().validate(limit)
        Validator(str).is_optional().validate(payment_method)
        Validator(str).is_optional().validate(order)
        Validator(str).is_optional().validate(starting_after)
        Validator(str).is_optional().validate(subscription)
        Validator(str).is_optional().validate(merchant_reference_id)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/payments", self.get_default_headers())
            .add_query("created_after", created_after)
            .add_query("created_before", created_before)
            .add_query("customer", customer)
            .add_query("destination_card", destination_card)
            .add_query("ending_before", ending_before)
            .add_query("ewallet", ewallet)
            .add_query("group", group)
            .add_query("invoice", invoice)
            .add_query("limit", limit)
            .add_query("payment_method", payment_method)
            .add_query("order", order)
            .add_query("starting_after", starting_after)
            .add_query("subscription", subscription)
            .add_query("merchant_reference_id", merchant_reference_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_53._unmap(response)

    @cast_models
    def create_payment(self, request_body: V1PaymentsBody) -> InlineResponse200_54:
        """Create a payment

        :param request_body: The request body.
        :type request_body: V1PaymentsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Payment was created
        :rtype: InlineResponse200_54
        """

        Validator(V1PaymentsBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/payments", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_54._unmap(response)

    @cast_models
    def retrieve_payment(self, payment_id: str) -> InlineResponse200_54:
        """Retrieve details of a payment

        :param payment_id: ID of the payment. String starting with 'payment_'.
        :type payment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Payment object
        :rtype: InlineResponse200_54
        """

        Validator(str).validate(payment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/{{paymentId}}", self.get_default_headers()
            )
            .add_path("paymentId", payment_id, explode=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_54._unmap(response)

    @cast_models
    def update_payment(
        self, request_body: PaymentsPaymentIdBody, payment_id: str
    ) -> InlineResponse200_54:
        """Change or modify a payment when the status of the payment is ACT (active). You can update additional fields if they are listed under payment_options in the response from Get Payment Method Required Fields and is_updateable is set to true

        :param request_body: The request body.
        :type request_body: PaymentsPaymentIdBody
        :param payment_id: ID of the payment. String starting with payment_.
        :type payment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: payment updated successfully
        :rtype: InlineResponse200_54
        """

        Validator(PaymentsPaymentIdBody).validate(request_body)
        Validator(str).validate(payment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/{{paymentId}}", self.get_default_headers()
            )
            .add_path("paymentId", payment_id, explode=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_54._unmap(response)

    @cast_models
    def cancel_payment(self, payment_id: str) -> InlineResponse200_54:
        """Cancel a payment where the status of the payment is ACT. Relevant to payment methods where is_cancelable = true in the response to List Payment Methods by Country. This method triggers the Payment Canceled webhook. This webhook contains the same information as the response. NOTE: If the status is CLO, use the Create Refund method.

        :param payment_id: ID of the payment. String starting with payment_.
        :type payment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: payment canceled successfully
        :rtype: InlineResponse200_54
        """

        Validator(str).validate(payment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/{{paymentId}}", self.get_default_headers()
            )
            .add_path("paymentId", payment_id, explode=True)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_54._unmap(response)
