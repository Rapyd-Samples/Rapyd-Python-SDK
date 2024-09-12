from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_customers_body import V1CustomersBody
from ..models.utils.cast_models import cast_models
from ..models.inline_response_200_36 import InlineResponse200_36
from ..models.inline_response_200_35 import InlineResponse200_35
from ..models.inline_response_200_34 import InlineResponse200_34
from ..models.inline_response_200_33 import InlineResponse200_33
from ..models.customer_request import CustomerRequest


class CustomerService(BaseService):

    @cast_models
    def list_customer(
        self, starting_after: str = None, ending_before: str = None, limit: str = None
    ) -> InlineResponse200_33:
        """Retrieve a list of all customers

        :param starting_after: The ID of the customer created before the first customer you want to retrieve, defaults to None
        :type starting_after: str, optional
        :param ending_before: The ID of the customer created after the last customer you want to retrieve, defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of customers to return. Range is 1-100. Default is 10, defaults to None
        :type limit: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: get customers details
        :rtype: InlineResponse200_33
        """

        Validator(str).is_optional().validate(starting_after)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().pattern("([1-9]|[1-9]\d|100)").validate(limit)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/customers", self.get_default_headers())
            .add_query("starting_after", starting_after)
            .add_query("ending_before", ending_before)
            .add_query("limit", limit)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_33._unmap(response)

    @cast_models
    def create_customer(self, request_body: V1CustomersBody) -> InlineResponse200_34:
        """Adds a customer to merchant

        :param request_body: The request body.
        :type request_body: V1CustomersBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: customer was created successfully
        :rtype: InlineResponse200_34
        """

        Validator(V1CustomersBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/customers", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_34._unmap(response)

    @cast_models
    def retrieve_customer(self, customer_id: str) -> InlineResponse200_35:
        """Retrieve a customer

        :param customer_id: customer Id
        :type customer_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: get customer details By customer Id
        :rtype: InlineResponse200_35
        """

        Validator(str).validate(customer_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/customers/{{customerId}}",
                self.get_default_headers(),
            )
            .add_path("customerId", customer_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_35._unmap(response)

    @cast_models
    def update_customer(
        self, customer_id: str, request_body: CustomerRequest = None
    ) -> InlineResponse200_35:
        """Update a customer with customer Id in Path

        :param request_body: The request body., defaults to None
        :type request_body: CustomerRequest, optional
        :param customer_id: customer Id
        :type customer_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: customer was updated successfully
        :rtype: InlineResponse200_35
        """

        Validator(CustomerRequest).is_optional().validate(request_body)
        Validator(str).validate(customer_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/customers/{{customerId}}",
                self.get_default_headers(),
            )
            .add_path("customerId", customer_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_35._unmap(response)

    @cast_models
    def delete_customer(self, customer_id: str) -> InlineResponse200_36:
        """This method triggers the Customer Deleted webhook. This webhook contains the same information as the response

        :param customer_id: customer Id
        :type customer_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: customer was deleted
        :rtype: InlineResponse200_36
        """

        Validator(str).validate(customer_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/customers/{{customerId}}",
                self.get_default_headers(),
            )
            .add_path("customerId", customer_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_36._unmap(response)

    @cast_models
    def delete_customer_discount(self, customer_id: str) -> InlineResponse200_36:
        """Delete the discount that has been assigned to a customer through a coupon. This action does not affect the coupon that the discount was derived from. This method triggers the Customer Discount Deleted webhook.

        :param customer_id: customer Id
        :type customer_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: discount was deleted
        :rtype: InlineResponse200_36
        """

        Validator(str).validate(customer_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/customers/{{customerId}}/discount",
                self.get_default_headers(),
            )
            .add_path("customerId", customer_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_36._unmap(response)
