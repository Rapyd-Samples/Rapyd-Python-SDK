from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    Category,
    CustomerIdPaymentMethodsBody,
    CustomerPaymentMethod,
    InlineResponse200_43,
    InlineResponse200_44,
    InlineResponse200_45,
)


class CustomerPaymentMethodService(BaseService):

    @cast_models
    def get_customer_payment_methods(
        self,
        customer_id: str,
        category: Category = None,
        starting_after: str = None,
        ending_before: str = None,
        limit: str = None,
        type_: str = None,
    ) -> InlineResponse200_43:
        """Retrieve payment methods for a customer

        :param customer_id: customer Id
        :type customer_id: str
        :param category: category, defaults to None
        :type category: Category, optional
        :param starting_after: The ID of the coupon created before the first coupon you want to retrieve, defaults to None
        :type starting_after: str, optional
        :param ending_before: The ID of the coupon created after the last coupon you want to retrieve, defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of coupons to return. Range is 1-100. Default is 10, defaults to None
        :type limit: str, optional
        :param type_: The type of payment method to find., defaults to None
        :type type_: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: get customer details By customer Id
        :rtype: InlineResponse200_43
        """

        Validator(str).validate(customer_id)
        Validator(Category).is_optional().validate(category)
        Validator(str).is_optional().validate(starting_after)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(limit)
        Validator(str).is_optional().validate(type_)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/customers/{{customerId}}/payment_methods",
                self.get_default_headers(),
            )
            .add_path("customerId", customer_id)
            .add_query("category", category)
            .add_query("starting_after", starting_after)
            .add_query("ending_before", ending_before)
            .add_query("limit", limit)
            .add_query("type", type_)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_43._unmap(response)

    @cast_models
    def create_customer_payment_method(
        self, request_body: CustomerIdPaymentMethodsBody, customer_id: str
    ) -> InlineResponse200_44:
        """Add a payment method to a customer profile

        :param request_body: The request body.
        :type request_body: CustomerIdPaymentMethodsBody
        :param customer_id: customer Id
        :type customer_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Payment method was created for this customer successfully
        :rtype: InlineResponse200_44
        """

        Validator(CustomerIdPaymentMethodsBody).validate(request_body)
        Validator(str).validate(customer_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/customers/{{customerId}}/payment_methods",
                self.get_default_headers(),
            )
            .add_path("customerId", customer_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_44._unmap(response)

    @cast_models
    def get_customer_payment_method(
        self, customer_id: str, pmt_id: str
    ) -> InlineResponse200_44:
        """Retrieve a payment method for a specific customer

        :param customer_id: customer Id
        :type customer_id: str
        :param pmt_id: Pmt Id
        :type pmt_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: get customer details By customer Id
        :rtype: InlineResponse200_44
        """

        Validator(str).validate(customer_id)
        Validator(str).validate(pmt_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/customers/{{customerId}}/payment_methods/{{pmtId}}",
                self.get_default_headers(),
            )
            .add_path("customerId", customer_id)
            .add_path("pmtId", pmt_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_44._unmap(response)

    @cast_models
    def update_customer_payment_method(
        self, request_body: CustomerPaymentMethod, customer_id: str, pmt_id: str
    ) -> InlineResponse200_44:
        """Change or modify a payment method that was stored in a customer profile

        :param request_body: The request body.
        :type request_body: CustomerPaymentMethod
        :param customer_id: customer Id
        :type customer_id: str
        :param pmt_id: Pmt Id
        :type pmt_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: customer was updated successfully
        :rtype: InlineResponse200_44
        """

        Validator(CustomerPaymentMethod).validate(request_body)
        Validator(str).validate(customer_id)
        Validator(str).validate(pmt_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/customers/{{customerId}}/payment_methods/{{pmtId}}",
                self.get_default_headers(),
            )
            .add_path("customerId", customer_id)
            .add_path("pmtId", pmt_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_44._unmap(response)

    @cast_models
    def delete_customer_payment_method(
        self, customer_id: str, pmt_id: str
    ) -> InlineResponse200_45:
        """This method triggers the Webhook - Payment Method Canceled webhook. This webhook contains more information than the response.

        :param customer_id: customer Id
        :type customer_id: str
        :param pmt_id: Pmt Id
        :type pmt_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: payment method was deleted for this customer
        :rtype: InlineResponse200_45
        """

        Validator(str).validate(customer_id)
        Validator(str).validate(pmt_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/customers/{{customerId}}/payment_methods/{{pmtId}}",
                self.get_default_headers(),
            )
            .add_path("customerId", customer_id)
            .add_path("pmtId", pmt_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_45._unmap(response)
