from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import Address, InlineResponse200_64


class PaymentAddressService(BaseService):

    @cast_models
    def create_address(self, request_body: Address = None) -> InlineResponse200_64:
        """Create an address.

        :param request_body: The request body., defaults to None
        :type request_body: Address, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Creates an address.
        :rtype: InlineResponse200_64
        """

        Validator(Address).is_optional().validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/addresses", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_64._unmap(response)

    @cast_models
    def get_address(self, address_id: str) -> InlineResponse200_64:
        """Retrieve an address.

        :param address_id: ID of the address object. String starting with **address_**.
        :type address_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieves an address.
        :rtype: InlineResponse200_64
        """

        Validator(str).validate(address_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/addresses{{addressId}}", self.get_default_headers()
            )
            .add_path("addressId", address_id, explode=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_64._unmap(response)

    @cast_models
    def update_address(
        self, request_body: Address, address_id: str
    ) -> InlineResponse200_64:
        """Change or modify an address. To clear a field, set it to an empty string.

        :param request_body: The request body.
        :type request_body: Address
        :param address_id: ID of the address object. String starting with **address_**.
        :type address_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Update an address.
        :rtype: InlineResponse200_64
        """

        Validator(Address).validate(request_body)
        Validator(str).validate(address_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/addresses{{addressId}}", self.get_default_headers()
            )
            .add_path("addressId", address_id, explode=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_64._unmap(response)

    @cast_models
    def delete_address(self, address_id: str) -> InlineResponse200_64:
        """Remove an address that is linked to a customer or is not linked to any object.

        :param address_id: ID of the address object. String starting with **address_**.
        :type address_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Removes an address.
        :rtype: InlineResponse200_64
        """

        Validator(str).validate(address_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/addresses{{addressId}}", self.get_default_headers()
            )
            .add_path("addressId", address_id, explode=True)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_64._unmap(response)
