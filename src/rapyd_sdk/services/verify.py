from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    ApplicationsHostedBody,
    InlineResponse200_85,
    InlineResponse200_86,
    InlineResponse200_87,
    InlineResponse200_88,
    InlineResponse200_89,
    InlineResponse200_90,
    V1IdentitiesBody,
)


class VerifyService(BaseService):

    @cast_models
    def create_v1_identities(
        self, request_body: V1IdentitiesBody
    ) -> InlineResponse200_85:
        """Verification of the identity of a personal contact associated with a wallet.

        :param request_body: The request body.
        :type request_body: V1IdentitiesBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieve the Rapyd ID and merchant reference ID.
        :rtype: InlineResponse200_85
        """

        Validator(V1IdentitiesBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/identities", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_85._unmap(response)

    @cast_models
    def get_kyc_id_verification_supported_doc_types(
        self, country: str
    ) -> InlineResponse200_86:
        """Use this method to determine the types of documents to use for identification purposes, and also whether you need the reverse side of the document. You can filter your search results by country with the country query parameter.

        :param country: Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase.
        :type country: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet
        :rtype: InlineResponse200_86
        """

        Validator(str).pattern(
            "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$"
        ).validate(country)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/identities/types", self.get_default_headers()
            )
            .add_query("country", country, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_86._unmap(response)

    @cast_models
    def get_application_types_by_country(self, country: str) -> InlineResponse200_87:
        """Retrieve a List types of identity verification applications by country. You can filter the list with query parameters.

        :param country: Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase.
        :type country: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List types of identity verification applications by country.
        :rtype: InlineResponse200_87
        """

        Validator(str).pattern(
            "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$"
        ).validate(country)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/verify/applications/types/country/{{country}}",
                self.get_default_headers(),
            )
            .add_path("country", country)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_87._unmap(response)

    @cast_models
    def get_application_status(self, application: str) -> InlineResponse200_88:
        """Retrieve the status of an application for verification of identity. You can filter the list with query parameters.

        :param application: ID of the application. String starting with app_.
        :type application: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List types of identity verification applications by country.
        :rtype: InlineResponse200_88
        """

        Validator(str).validate(application)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/verify/applications/status/{{application}}",
                self.get_default_headers(),
            )
            .add_path("application", application)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_88._unmap(response)

    @cast_models
    def create_hosted_application_token(
        self, request_body: ApplicationsHostedBody = None
    ) -> InlineResponse200_89:
        """Create an application for Rapyd Verify where the client (applicant) provides information directly to Rapyd. After the applicant submits the application on the hosted page, Rapyd verifies the information. When the status of the application changes, Rapyd sends you a webhook.

        :param request_body: The request body., defaults to None
        :type request_body: ApplicationsHostedBody, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Hosted application details.
        :rtype: InlineResponse200_89
        """

        Validator(ApplicationsHostedBody).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/verify/applications/hosted",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_89._unmap(response)

    @cast_models
    def get_hosted_application_by_token(
        self, verify_app_id: str
    ) -> InlineResponse200_90:
        """Retrieve Rapyd Verify Application

        :param verify_app_id: ID of the Rapyd Verify application. String starting with happ_.
        :type verify_app_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Hosted application details.
        :rtype: InlineResponse200_90
        """

        Validator(str).validate(verify_app_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/verify/applications/hosted/{{verifyAppId}}",
                self.get_default_headers(),
            )
            .add_path("verifyAppId", verify_app_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_90._unmap(response)
