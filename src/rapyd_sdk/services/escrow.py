from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    EscrowEscrowReleasesBody,
    InlineResponse200_49,
    InlineResponse200_50,
)


class EscrowService(BaseService):

    @cast_models
    def list_escrow_releases(self, payment: str, escrow: str) -> InlineResponse200_49:
        """Retrieve a list of all releases of funds from a specified escrow.

        :param payment: ID of the payment. String starting with **payment_**.
        :type payment: str
        :param escrow: ID of the escrow. String starting with **escrow_**.
        :type escrow: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Escrow details after specifying it.
        :rtype: InlineResponse200_49
        """

        Validator(str).validate(payment)
        Validator(str).validate(escrow)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/{{payment}}/escrows/{{escrow}}/escrow_releases",
                self.get_default_headers(),
            )
            .add_path("payment", payment)
            .add_path("escrow", escrow)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_49._unmap(response)

    @cast_models
    def release_funds_from_escrow(
        self, payment: str, escrow: str, request_body: EscrowEscrowReleasesBody = None
    ) -> InlineResponse200_50:
        """Retrieve a list of all releases of funds from a specified escrow.

        :param request_body: The request body., defaults to None
        :type request_body: EscrowEscrowReleasesBody, optional
        :param payment: ID of the payment. String starting with **payment_**.
        :type payment: str
        :param escrow: ID of the escrow. String starting with **escrow_**.
        :type escrow: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Escrow details after creating it.
        :rtype: InlineResponse200_50
        """

        Validator(EscrowEscrowReleasesBody).is_optional().validate(request_body)
        Validator(str).validate(payment)
        Validator(str).validate(escrow)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/{{payment}}/escrows/{{escrow}}/escrow_releases",
                self.get_default_headers(),
            )
            .add_path("payment", payment)
            .add_path("escrow", escrow)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_50._unmap(response)

    @cast_models
    def get_escrow(self, payment: str, escrow: str) -> InlineResponse200_49:
        """Retrieve details of the escrow for a payment.

        :param payment: ID of the payment. String starting with **payment_**.
        :type payment: str
        :param escrow: ID of the escrow. String starting with **escrow_**.
        :type escrow: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Escrow details after specifying it.
        :rtype: InlineResponse200_49
        """

        Validator(str).validate(payment)
        Validator(str).validate(escrow)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payments/{{payment}}/escrows/{{escrow}}",
                self.get_default_headers(),
            )
            .add_path("payment", payment)
            .add_path("escrow", escrow)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_49._unmap(response)
