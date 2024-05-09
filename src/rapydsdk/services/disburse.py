from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetPayoutMethodTypesDetails200Response import (
    GetPayoutMethodTypesDetails200Response as GetPayoutMethodTypesDetails200ResponseModel,
)
from ..models.ListPayouts200Response import (
    ListPayouts200Response as ListPayouts200ResponseModel,
)
from ..models.CreatePayoutRequest import CreatePayoutRequest as CreatePayoutRequestModel
from ..models.CreatePayoutRequest import (
    CreatePayoutRequestGuard as CreatePayoutRequestGuardModel,
)
from ..models.CreatePayout200Response import (
    CreatePayout200Response as CreatePayout200ResponseModel,
)
from ..models.CreateBeneficiaryRequest import (
    CreateBeneficiaryRequest as CreateBeneficiaryRequestModel,
)
from ..models.CreateBeneficiary200Response import (
    CreateBeneficiary200Response as CreateBeneficiary200ResponseModel,
)
from ..models.ValidateBeneficiaryRequest import (
    ValidateBeneficiaryRequest as ValidateBeneficiaryRequestModel,
)
from ..models.ValidateBeneficiary200Response import (
    ValidateBeneficiary200Response as ValidateBeneficiary200ResponseModel,
)
from ..models.GetBeneficiary200Response import (
    GetBeneficiary200Response as GetBeneficiary200ResponseModel,
)
from ..models.DeleteBeneficiary200Response import (
    DeleteBeneficiary200Response as DeleteBeneficiary200ResponseModel,
)
from ..models.SimulateCompletePayout200Response import (
    SimulateCompletePayout200Response as SimulateCompletePayout200ResponseModel,
)
from ..models.ConfirmPayout200Response import (
    ConfirmPayout200Response as ConfirmPayout200ResponseModel,
)
from ..models.CreateSenderRequest import CreateSenderRequest as CreateSenderRequestModel
from ..models.CreateSender200Response import (
    CreateSender200Response as CreateSender200ResponseModel,
)
from ..models.GetPayer200Response import GetPayer200Response as GetPayer200ResponseModel
from ..models.DeletePayer200Response import (
    DeletePayer200Response as DeletePayer200ResponseModel,
)
from ..models.GetPayoutMethodTypes200Response import (
    GetPayoutMethodTypes200Response as GetPayoutMethodTypes200ResponseModel,
)
from ..models.GetPayout200Response import (
    GetPayout200Response as GetPayout200ResponseModel,
)
from ..models.UpdatePayoutRequest import UpdatePayoutRequest as UpdatePayoutRequestModel
from ..models.UpdatePayout200Response import (
    UpdatePayout200Response as UpdatePayout200ResponseModel,
)
from ..models.CancelPayout200Response import (
    CancelPayout200Response as CancelPayout200ResponseModel,
)


class Disburse(BaseService):
    def get_payout_method_types_details(
        self,
        sender_entity_type: str,
        sender_currency: str,
        sender_country: str,
        payout_currency: str,
        payout_amount: float,
        beneficiary_entity_type: str,
        beneficiary_country: str,
        pomt: str,
    ) -> GetPayoutMethodTypesDetails200ResponseModel:
        """
        Get Payout Required Fields
        Parameters:
        ----------
            pomt: str
                The type of the payout method. Set to the name of a payout method listed in the response to List Payout Method Types. The two-letter prefix must match the beneficiary country code.
            beneficiary_country: str
                Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.
            beneficiary_entity_type: str
                Type of entity for the beneficiary. One of the following, individual, company
            payout_amount: float
                Amount of the payout, in units of the currency that the beneficiary is receiving. Decimal.
            payout_currency: str
                Currency received by the beneficiary. Three-letter ISO 4217 code. Uppercase.
            sender_country: str
                Country of the sender. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.
            sender_currency: str
                Currency that the sender is paying with. Three-letter ISO 4217 code. Uppercase.
            sender_entity_type: str
                Type of entity for the sender. One of the following: individual, company
        """

        url_endpoint = "/v1/payout_methods/{pomt}/required_fields"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not pomt:
            raise ValueError("Parameter pomt is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{pomt}",
            quote(str(query_serializer.serialize_path("simple", True, pomt, None))),
        )
        if not beneficiary_country:
            raise ValueError(
                "Parameter beneficiary_country is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", True, "beneficiary_country", beneficiary_country
            )
        )
        if not beneficiary_entity_type:
            raise ValueError(
                "Parameter beneficiary_entity_type is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", True, "beneficiary_entity_type", beneficiary_entity_type
            )
        )
        if not payout_amount:
            raise ValueError(
                "Parameter payout_amount is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", True, "payout_amount", payout_amount
            )
        )
        if not payout_currency:
            raise ValueError(
                "Parameter payout_currency is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", True, "payout_currency", payout_currency
            )
        )
        if not sender_country:
            raise ValueError(
                "Parameter sender_country is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", True, "sender_country", sender_country
            )
        )
        if not sender_currency:
            raise ValueError(
                "Parameter sender_currency is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", True, "sender_currency", sender_currency
            )
        )
        if not sender_entity_type:
            raise ValueError(
                "Parameter sender_entity_type is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", True, "sender_entity_type", sender_entity_type
            )
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetPayoutMethodTypesDetails200ResponseModel._unmap(res)
        return res

    def list_payouts(
        self,
        beneficiary: str = None,
        created_after: str = None,
        created_before: str = None,
        ending_before: str = None,
        ewallet: str = None,
        limit: str = None,
        merchant_reference_id: str = None,
        payout_method_type: str = None,
        sender: str = None,
        sender_country: str = None,
        sender_currency: str = None,
        starting_after: str = None,
    ) -> ListPayouts200ResponseModel:
        """
        List Payouts
        Parameters:
        ----------
            beneficiary: str
                Filters according to the beneficiary ID. String starting with beneficiary_.
            created_after: str
                The ID of the payout created before the first payout you want to retrieve. String starting with payout_.
            created_before: str
                The ID of the payout created after the last payout you want to retrieve. String starting with payout_.
            ending_before: str
                The ID of a payout in the list. The list ends with the payout that was created before the payout with this ID. Use this filter to get the previous page of results. String starting with payout_. Deprecated.
            ewallet: str
                Filters according to the wallet ID. String starting with ewallet_.
            limit: str
                The maximum number of payouts to return. Range: 1-100. Default is 10.
            merchant_reference_id: str
                Filters according to the merchant reference ID.
            payout_method_type: str
                Filters according to the type of payout method. The two-letter prefix must match the beneficiary country code.
            sender: str
                Filters according to the sender ID. String starting with sender_.
            sender_country: str
                Filters according to the country of the sender. Two-letter ISO 3166-1 ALPHA-2 code.
            sender_currency: str
                Filters according to the currency that the sender is paying with. Three-letter ISO 4217 code.
            starting_after: str
                The ID of a payout in the list. The list begins with the payout that was created next after the payout with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used. String starting with payout_. Deprecated
        """

        url_endpoint = "/v1/payouts"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if beneficiary:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "beneficiary", beneficiary
                )
            )
        if created_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "created_after", created_after
                )
            )
        if created_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "created_before", created_before
                )
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "ending_before", ending_before
                )
            )
        if ewallet:
            query_params.append(
                query_serializer.serialize_query("form", True, "ewallet", ewallet)
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", True, "limit", limit)
            )
        if merchant_reference_id:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "merchant_reference_id", merchant_reference_id
                )
            )
        if payout_method_type:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "payout_method_type", payout_method_type
                )
            )
        if sender:
            query_params.append(
                query_serializer.serialize_query("form", True, "sender", sender)
            )
        if sender_country:
            validated_sender_country = self._pattern_matching(
                sender_country,
                "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
                "sender_country",
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "sender_country", validated_sender_country
                )
            )
        if sender_currency:
            validated_sender_currency = self._pattern_matching(
                sender_currency,
                "^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$",
                "sender_currency",
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "sender_currency", validated_sender_currency
                )
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "starting_after", starting_after
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListPayouts200ResponseModel._unmap(res)
        return res

    def create_payout(
        self, request_input: CreatePayoutRequestModel
    ) -> CreatePayout200ResponseModel:
        """
        Create Payout
        """

        if isinstance(request_input, dict):
            request_input = CreatePayoutRequestGuardModel.return_one_of(request_input)
        url_endpoint = "/v1/payouts"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreatePayout200ResponseModel._unmap(res)
        return res

    def create_beneficiary(
        self, request_input: CreateBeneficiaryRequestModel
    ) -> CreateBeneficiary200ResponseModel:
        """
        Create Beneficiary
        """

        if isinstance(request_input, dict):
            request_input = CreateBeneficiaryRequestModel(**request_input)
        url_endpoint = "/v1/payouts/beneficiary"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateBeneficiary200ResponseModel._unmap(res)
        return res

    def validate_beneficiary(
        self, request_input: ValidateBeneficiaryRequestModel
    ) -> ValidateBeneficiary200ResponseModel:
        """
        Validate Beneficiary
        """

        if isinstance(request_input, dict):
            request_input = ValidateBeneficiaryRequestModel(**request_input)
        url_endpoint = "/v1/payouts/beneficiary/validate"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ValidateBeneficiary200ResponseModel._unmap(res)
        return res

    def get_beneficiary(self, beneficiary_id: str) -> GetBeneficiary200ResponseModel:
        """
        Retrieve Beneficiary
        Parameters:
        ----------
            beneficiary_id: str
                ID of the 'beneficiary' object. String starting with beneficiary_.
        """

        url_endpoint = "/v1/payouts/beneficiary/{beneficiary_id}"
        headers = {}
        self._add_required_headers(headers)
        if not beneficiary_id:
            raise ValueError(
                "Parameter beneficiary_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{beneficiary_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", True, beneficiary_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetBeneficiary200ResponseModel._unmap(res)
        return res

    def delete_beneficiary(
        self, beneficiary_id: str
    ) -> DeleteBeneficiary200ResponseModel:
        """
        Delete Beneficiary
        Parameters:
        ----------
            beneficiary_id: str
                ID of the 'beneficiary' object. String starting with beneficiary_.
        """

        url_endpoint = "/v1/payouts/beneficiary/{beneficiary_id}"
        headers = {}
        self._add_required_headers(headers)
        if not beneficiary_id:
            raise ValueError(
                "Parameter beneficiary_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{beneficiary_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", True, beneficiary_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteBeneficiary200ResponseModel._unmap(res)
        return res

    def simulate_complete_payout(
        self, amount: str, payout_token: str
    ) -> SimulateCompletePayout200ResponseModel:
        """
        Complete the Payout
        Parameters:
        ----------
            payout_token: str
                ID of the payout. String starting with 'payout_'.
            amount: str
                The payout amount. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015.
        """

        url_endpoint = "/v1/payouts/complete/{payout_token}/{amount}"
        headers = {}
        self._add_required_headers(headers)
        if not payout_token:
            raise ValueError(
                "Parameter payout_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{payout_token}",
            quote(
                str(query_serializer.serialize_path("simple", True, payout_token, None))
            ),
        )
        if not amount:
            raise ValueError("Parameter amount is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{amount}",
            quote(str(query_serializer.serialize_path("simple", True, amount, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return SimulateCompletePayout200ResponseModel._unmap(res)
        return res

    def confirm_payout(self, payout_token: str) -> ConfirmPayout200ResponseModel:
        """
        Confirm Payout that involves foreign exchange
        Parameters:
        ----------
            payout_token: str
                ID of the payout. String starting with 'payout_'.
        """

        url_endpoint = "/v1/payouts/confirm/{payout_token}"
        headers = {}
        self._add_required_headers(headers)
        if not payout_token:
            raise ValueError(
                "Parameter payout_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{payout_token}",
            quote(
                str(query_serializer.serialize_path("simple", True, payout_token, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return ConfirmPayout200ResponseModel._unmap(res)
        return res

    def create_sender(
        self, request_input: CreateSenderRequestModel
    ) -> CreateSender200ResponseModel:
        """
        Create Sender
        """

        if isinstance(request_input, dict):
            request_input = CreateSenderRequestModel(**request_input)
        url_endpoint = "/v1/payouts/sender"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateSender200ResponseModel._unmap(res)
        return res

    def get_payer(self, sender_id: str) -> GetPayer200ResponseModel:
        """
        Retrieve details of a payout sender.
        Parameters:
        ----------
            sender_id: str
                ID of the Sender object. String starting with 'sender_'.
        """

        url_endpoint = "/v1/payouts/sender/{sender_id}"
        headers = {}
        self._add_required_headers(headers)
        if not sender_id:
            raise ValueError(
                "Parameter sender_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{sender_id}",
            quote(
                str(query_serializer.serialize_path("simple", True, sender_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetPayer200ResponseModel._unmap(res)
        return res

    def delete_payer(self, sender_id: str) -> DeletePayer200ResponseModel:
        """
        Delete Sender
        Parameters:
        ----------
            sender_id: str
                ID of the 'sender' object. String starting with sender_.
        """

        url_endpoint = "/v1/payouts/sender/{sender_id}"
        headers = {}
        self._add_required_headers(headers)
        if not sender_id:
            raise ValueError(
                "Parameter sender_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{sender_id}",
            quote(
                str(query_serializer.serialize_path("simple", True, sender_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeletePayer200ResponseModel._unmap(res)
        return res

    def get_payout_method_types(
        self,
        sender_entity_type: str = None,
        beneficiary_country: str = None,
        payout_currency: str = None,
        sender_currency: str = None,
        sender_country: str = None,
        beneficiary_entity_type: str = None,
        category: str = None,
        is_cancelable: bool = None,
        is_location_specific: bool = None,
        is_expirable: bool = None,
        starting_after: str = None,
        ending_before: str = None,
        limit: str = None,
    ) -> GetPayoutMethodTypes200ResponseModel:
        """
        List Payout Method Types
        Parameters:
        ----------
            sender_entity_type: str
                Filters the type of entity for the payer. One of the following: individual, company
            beneficiary_country: str
                Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code.
            payout_currency: str
                Currency received by the beneficiary. Three-letter ISO 4217 code.
            sender_currency: str
                Currency that the sender is paying with. Three-letter ISO 4217 code.
            sender_country: str
                Country of the sender. Two-letter ISO 3166-1 ALPHA-2 code. Note: This field does not appear in the response.
            beneficiary_entity_type: str
                Filters the type of entity for the beneficiary. One of the following: individual, company
            category: str
                The category of payout method. One of the following: bank, card, cash, rapyd_ewallet, ewallet
            is_cancelable: bool
                Indicates whether the payout can be canceled. Relevant when category is cash.
            is_location_specific: bool
                Indicates whether the payout must be made at a specific physical location. Relevant when category is cash.
            is_expirable: bool
                Indicates whether the payout expires if not completed. Relevant when category is cash.
            starting_after: str
                The name of a payout method in the list. The list begins with the record that was created next after the record with this payout method. Use this filter to get the next page of results. Relevant when ending_before is not used.
            ending_before: str
                The name of a payout method in the list. The list ends with the last record that was created before the record with this payout method. Use this filter to get the previous page of results.
            limit: str
                The maximum number of payout methods to return. Range: 1-100. Default is 10.
        """

        url_endpoint = "/v1/payout_methods"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if sender_entity_type:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "sender_entity_type", sender_entity_type
                )
            )
        if beneficiary_country:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "beneficiary_country", beneficiary_country
                )
            )
        if payout_currency:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "payout_currency", payout_currency
                )
            )
        if sender_currency:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "sender_currency", sender_currency
                )
            )
        if sender_country:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "sender_country", sender_country
                )
            )
        if beneficiary_entity_type:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "beneficiary_entity_type", beneficiary_entity_type
                )
            )
        if category:
            query_params.append(
                query_serializer.serialize_query("form", True, "category", category)
            )
        if is_cancelable:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "is_cancelable", is_cancelable
                )
            )
        if is_location_specific:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "is_location_specific", is_location_specific
                )
            )
        if is_expirable:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "is_expirable", is_expirable
                )
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "starting_after", starting_after
                )
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "ending_before", ending_before
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", True, "limit", limit)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetPayoutMethodTypes200ResponseModel._unmap(res)
        return res

    def get_payout(self, payout_id: str) -> GetPayout200ResponseModel:
        """
        Retrieve Payout
        Parameters:
        ----------
            payout_id: str
                ID of the payout. String starting with 'payout_'.
        """

        url_endpoint = "/v1/payouts/{payout_id}"
        headers = {}
        self._add_required_headers(headers)
        if not payout_id:
            raise ValueError(
                "Parameter payout_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{payout_id}",
            quote(
                str(query_serializer.serialize_path("simple", True, payout_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetPayout200ResponseModel._unmap(res)
        return res

    def update_payout(
        self, request_input: UpdatePayoutRequestModel, payout_id: str
    ) -> UpdatePayout200ResponseModel:
        """
        Update Payout
        Parameters:
        ----------
            payout_id: str
                ID of the payout. String starting with payout_.
        """

        if isinstance(request_input, dict):
            request_input = UpdatePayoutRequestModel(**request_input)
        url_endpoint = "/v1/payouts/{payout_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not payout_id:
            raise ValueError(
                "Parameter payout_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{payout_id}",
            quote(
                str(query_serializer.serialize_path("simple", True, payout_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdatePayout200ResponseModel._unmap(res)
        return res

    def cancel_payout(self, payout_id: str) -> CancelPayout200ResponseModel:
        """
        Cancel Payout
        Parameters:
        ----------
            payout_id: str
                ID of the payout. String starting with payout_.
        """

        url_endpoint = "/v1/payouts/{payout_id}"
        headers = {}
        self._add_required_headers(headers)
        if not payout_id:
            raise ValueError(
                "Parameter payout_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{payout_id}",
            quote(
                str(query_serializer.serialize_path("simple", True, payout_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return CancelPayout200ResponseModel._unmap(res)
        return res
