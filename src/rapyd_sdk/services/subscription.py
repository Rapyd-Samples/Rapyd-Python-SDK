from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.subscriptions_subscription_id_body import SubscriptionsSubscriptionIdBody
from ..models.payments_subscriptions_body import PaymentsSubscriptionsBody
from ..models.inline_response_200_57 import InlineResponse200_57
from ..models.inline_response_200_56 import InlineResponse200_56
from ..models.inline_response_200_55 import InlineResponse200_55


class SubscriptionService(BaseService):

    @cast_models
    def get_subscription_list(
        self,
        starting_after: str,
        billing: str = None,
        customer: str = None,
        status: str = None,
        product: str = None,
        ending_before: str = None,
        limit: str = None,
    ) -> InlineResponse200_55:
        """Retrieve a list of subscriptions. You can filter the list with query parameters.

        :param starting_after: The ID of a record in the list. The list begins with the record that was created next after the record with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used.
        :type starting_after: str
        :param billing: Method of billing. One of the following, pay_automatically, send_invoice., defaults to None
        :type billing: str, optional
        :param customer: ID of the customer. String starting with cus_, defaults to None
        :type customer: str, optional
        :param status: Status of the subscription. One of the following, active, canceled, trialing, defaults to None
        :type status: str, optional
        :param product: ID of a 'product' object. The product must have type set to service. String starting with product_. Filter for one product at a time., defaults to None
        :type product: str, optional
        :param ending_before: The ID of a record in the list. The list ends with the last record that was created before the record with this ID. Use this filter to get the previous page of results., defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of subscriptions to return. Range, 1-100. Default is 10., defaults to None
        :type limit: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of subscriptions,
        :rtype: InlineResponse200_55
        """

        Validator(str).validate(starting_after)
        Validator(str).is_optional().validate(billing)
        Validator(str).is_optional().validate(customer)
        Validator(str).is_optional().validate(status)
        Validator(str).is_optional().validate(product)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(limit)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/subscriptions", self.get_default_headers()
            )
            .add_query("billing", billing, explode=False)
            .add_query("customer", customer, explode=False)
            .add_query("status", status, explode=False)
            .add_query("product", product, explode=False)
            .add_query("starting_after", starting_after, explode=False)
            .add_query("ending_before", ending_before, explode=False)
            .add_query("limit", limit, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_55._unmap(response)

    @cast_models
    def create_subscription(
        self, request_body: PaymentsSubscriptionsBody
    ) -> InlineResponse200_56:
        """Create a subscription for regular, automatic payments.

        :param request_body: The request body.
        :type request_body: PaymentsSubscriptionsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Create a subscription
        :rtype: InlineResponse200_56
        """

        Validator(PaymentsSubscriptionsBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/subscriptions", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_56._unmap(response)

    @cast_models
    def get_subscription(self, subscription_id: str) -> InlineResponse200_56:
        """Retrieve the details of a subscription.

        :param subscription_id: ID of the subscription. String starting with sub_.
        :type subscription_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Get subscription details
        :rtype: InlineResponse200_56
        """

        Validator(str).validate(subscription_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/subscriptions/{{subscriptionId}}",
                self.get_default_headers(),
            )
            .add_path("subscriptionId", subscription_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_56._unmap(response)

    @cast_models
    def update_subscription(
        self, request_body: SubscriptionsSubscriptionIdBody, subscription_id: str
    ) -> InlineResponse200_56:
        """Update the details of a subscription.

        :param request_body: The request body.
        :type request_body: SubscriptionsSubscriptionIdBody
        :param subscription_id: ID of the subscription. String starting with sub_.
        :type subscription_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The subscription after updated
        :rtype: InlineResponse200_56
        """

        Validator(SubscriptionsSubscriptionIdBody).validate(request_body)
        Validator(str).validate(subscription_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/subscriptions/{{subscriptionId}}",
                self.get_default_headers(),
            )
            .add_path("subscriptionId", subscription_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_56._unmap(response)

    @cast_models
    def cancel_subscription(self, subscription_id: str) -> InlineResponse200_56:
        """Cancel a subscription.

        :param subscription_id: ID of the subscription. String starting with sub_.
        :type subscription_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The canceled subscription
        :rtype: InlineResponse200_56
        """

        Validator(str).validate(subscription_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/subscriptions/{{subscriptionId}}",
                self.get_default_headers(),
            )
            .add_path("subscriptionId", subscription_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_56._unmap(response)

    @cast_models
    def delete_subscription_discount(
        self, subscription_id: str
    ) -> InlineResponse200_57:
        """Delete the discount that was assigned to a subscription. This method does not affect the coupon that the discount was derived from.

        :param subscription_id: ID of the subscription. String starting with sub_
        :type subscription_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: discount was deleted
        :rtype: InlineResponse200_57
        """

        Validator(str).validate(subscription_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/subscriptions/{{subscriptionId}}/discount",
                self.get_default_headers(),
            )
            .add_path("subscriptionId", subscription_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_57._unmap(response)

    @cast_models
    def complete_subscription_cycle(self, subscription_id: str) -> InlineResponse200_56:
        """Cancel the subscription and create an invoice. This method is for testing purposes and runs only in the sandbox.

        :param subscription_id: ID of the subscription. String starting with sub_.
        :type subscription_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The subscription
        :rtype: InlineResponse200_56
        """

        Validator(str).validate(subscription_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/subscriptions/{{subscriptionId}}/complete_cycle",
                self.get_default_headers(),
            )
            .add_path("subscriptionId", subscription_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_56._unmap(response)

    @cast_models
    def simulate_start_new_cycle(self, subscription_id: str) -> InlineResponse200_56:
        """End a subscription cycle, create an invoice and move the subscription to the next cycle. This method is for testing purposes and runs only in the sandbox.

        :param subscription_id: ID of the subscription. String starting with sub_.
        :type subscription_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Subscription details
        :rtype: InlineResponse200_56
        """

        Validator(str).validate(subscription_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/subscriptions/{{subscriptionId}}/start_new_cycle",
                self.get_default_headers(),
            )
            .add_path("subscriptionId", subscription_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_56._unmap(response)
