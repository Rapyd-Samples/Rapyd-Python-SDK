from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.PerformIdentityVerificationRequest import (
    PerformIdentityVerificationRequest as PerformIdentityVerificationRequestModel,
)
from ..models.PerformIdentityVerification200Response import (
    PerformIdentityVerification200Response as PerformIdentityVerification200ResponseModel,
)
from ..models.GetKycIdVerificationSupportedDocTypes200Response import (
    GetKycIdVerificationSupportedDocTypes200Response as GetKycIdVerificationSupportedDocTypes200ResponseModel,
)
from ..models.GetApplicationTypesByCountry200Response import (
    GetApplicationTypesByCountry200Response as GetApplicationTypesByCountry200ResponseModel,
)
from ..models.GetApplicationStatus200Response import (
    GetApplicationStatus200Response as GetApplicationStatus200ResponseModel,
)
from ..models.CreateHostedApplicationTokenRequest import (
    CreateHostedApplicationTokenRequest as CreateHostedApplicationTokenRequestModel,
)
from ..models.CreateHostedApplicationToken200Response import (
    CreateHostedApplicationToken200Response as CreateHostedApplicationToken200ResponseModel,
)
from ..models.GetHostedApplicationByToken200Response import (
    GetHostedApplicationByToken200Response as GetHostedApplicationByToken200ResponseModel,
)


class Verify(BaseService):
    def perform_identity_verification(
        self, request_input: PerformIdentityVerificationRequestModel
    ) -> PerformIdentityVerification200ResponseModel:
        """
        Verify the identity of an individual or a personal contact for a 'person' wallet.
        """

        if isinstance(request_input, dict):
            request_input = PerformIdentityVerificationRequestModel(**request_input)
        url_endpoint = "/v1/identities"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return PerformIdentityVerification200ResponseModel._unmap(res)
        return res

    def get_kyc_id_verification_supported_doc_types(
        self, country: str
    ) -> GetKycIdVerificationSupportedDocTypes200ResponseModel:
        """
        Retrieve a list of the types of official identification documents for a country.
        Parameters:
        ----------
            country: str
                Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase.
        """

        url_endpoint = "/v1/identities/types"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not country:
            raise ValueError("Parameter country is required, cannot be empty or blank.")
        validated_country = self._pattern_matching(
            country,
            "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
            "country",
        )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "country", validated_country
            )
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetKycIdVerificationSupportedDocTypes200ResponseModel._unmap(res)
        return res

    def get_application_types_by_country(
        self, country: str
    ) -> GetApplicationTypesByCountry200ResponseModel:
        """
        List Rapyd Verify Application Types.
        Parameters:
        ----------
            country: str
                Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase.
        """

        url_endpoint = "/v1/verify/applications/types/country/{country}"
        headers = {}
        self._add_required_headers(headers)
        if not country:
            raise ValueError("Parameter country is required, cannot be empty or blank.")
        validated_country = self._pattern_matching(
            country,
            "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
            "country",
        )
        url_endpoint = url_endpoint.replace(
            "{country}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, validated_country, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetApplicationTypesByCountry200ResponseModel._unmap(res)
        return res

    def get_application_status(
        self, application: str
    ) -> GetApplicationStatus200ResponseModel:
        """
        Retrieve Status of Rapyd Verify Application
        Parameters:
        ----------
            application: str
                ID of the application. String starting with app_.
        """

        url_endpoint = "/v1/verify/applications/status/{application}"
        headers = {}
        self._add_required_headers(headers)
        if not application:
            raise ValueError(
                "Parameter application is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{application}",
            quote(
                str(query_serializer.serialize_path("simple", False, application, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetApplicationStatus200ResponseModel._unmap(res)
        return res

    def create_hosted_application_token(
        self, request_input: CreateHostedApplicationTokenRequestModel = None
    ) -> CreateHostedApplicationToken200ResponseModel:
        """
        Create Rapyd Verify Application
        """

        if isinstance(request_input, dict):
            request_input = CreateHostedApplicationTokenRequestModel(**request_input)
        url_endpoint = "/v1/verify/applications/hosted"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateHostedApplicationToken200ResponseModel._unmap(res)
        return res

    def get_hosted_application_by_token(
        self, verify_app_id: str
    ) -> GetHostedApplicationByToken200ResponseModel:
        """
        Create Rapyd Verify Application
        Parameters:
        ----------
            verify_app_id: str
                ID of the Rapyd Verify application. String starting with happ_.
        """

        url_endpoint = "/v1/verify/applications/hosted/{verify_app_id}"
        headers = {}
        self._add_required_headers(headers)
        if not verify_app_id:
            raise ValueError(
                "Parameter verify_app_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{verify_app_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, verify_app_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetHostedApplicationByToken200ResponseModel._unmap(res)
        return res
