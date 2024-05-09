from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.CreateIssuingRequest import (
    CreateIssuingRequest as CreateIssuingRequestModel,
)
from ..models.CreateIssuing200Response import (
    CreateIssuing200Response as CreateIssuing200ResponseModel,
)
from ..models.SimulateCompleteBankAccountIssuingTransactionRequest import (
    SimulateCompleteBankAccountIssuingTransactionRequest as SimulateCompleteBankAccountIssuingTransactionRequestModel,
)
from ..models.SimulateCompleteBankAccountIssuingTransaction200Response import (
    SimulateCompleteBankAccountIssuingTransaction200Response as SimulateCompleteBankAccountIssuingTransaction200ResponseModel,
)
from ..models.RetrieveIssuingByRapydToken200Response import (
    RetrieveIssuingByRapydToken200Response as RetrieveIssuingByRapydToken200ResponseModel,
)
from ..models.UpdateReceivingCurrencyRequest import (
    UpdateReceivingCurrencyRequest as UpdateReceivingCurrencyRequestModel,
)
from ..models.UpdateReceivingCurrency200Response import (
    UpdateReceivingCurrency200Response as UpdateReceivingCurrency200ResponseModel,
)
from ..models.CloseIssuing200Response import (
    CloseIssuing200Response as CloseIssuing200ResponseModel,
)
from ..models.RetrieveIssuingTransaction200Response import (
    RetrieveIssuingTransaction200Response as RetrieveIssuingTransaction200ResponseModel,
)
from ..models.GetCardIssuingList200Response import (
    GetCardIssuingList200Response as GetCardIssuingList200ResponseModel,
)
from ..models.IssueCardRequest import IssueCardRequest as IssueCardRequestModel
from ..models.IssueCard200Response import (
    IssueCard200Response as IssueCard200ResponseModel,
)
from ..models.GetCardIssuingDetails200Response import (
    GetCardIssuingDetails200Response as GetCardIssuingDetails200ResponseModel,
)
from ..models.ActivateCardRequest import ActivateCardRequest as ActivateCardRequestModel
from ..models.ActivateCard200Response import (
    ActivateCard200Response as ActivateCard200ResponseModel,
)
from ..models.ModifyCardRequest import ModifyCardRequest as ModifyCardRequestModel
from ..models.ModifyCard200Response import (
    ModifyCard200Response as ModifyCard200ResponseModel,
)
from ..models.UpdateCardStatusRequest import (
    UpdateCardStatusRequest as UpdateCardStatusRequestModel,
)
from ..models.UpdateCardStatus200Response import (
    UpdateCardStatus200Response as UpdateCardStatus200ResponseModel,
)
from ..models.GetCardIssuingTransactions200Response import (
    GetCardIssuingTransactions200Response as GetCardIssuingTransactions200ResponseModel,
)
from ..models.GetCardIssuingTransaction200Response import (
    GetCardIssuingTransaction200Response as GetCardIssuingTransaction200ResponseModel,
)


class Issuing(BaseService):
    def create_issuing(
        self, request_input: CreateIssuingRequestModel
    ) -> CreateIssuing200ResponseModel:
        """
        Issue Virtual Account Number to Wallet
        """

        if isinstance(request_input, dict):
            request_input = CreateIssuingRequestModel(**request_input)
        url_endpoint = "/v1/virtual_accounts"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateIssuing200ResponseModel._unmap(res)
        return res

    def simulate_complete_bank_account_issuing_transaction(
        self, request_input: SimulateCompleteBankAccountIssuingTransactionRequestModel
    ) -> SimulateCompleteBankAccountIssuingTransaction200ResponseModel:
        """
        Simulate a Bank Transfer to a Wallet
        """

        if isinstance(request_input, dict):
            request_input = SimulateCompleteBankAccountIssuingTransactionRequestModel(
                **request_input
            )
        url_endpoint = "/v1/virtual_accounts/transactions"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return SimulateCompleteBankAccountIssuingTransaction200ResponseModel._unmap(
                res
            )
        return res

    def retrieve_issuing_by_rapyd_token(
        self, virtual_account_id: str
    ) -> RetrieveIssuingByRapydToken200ResponseModel:
        """
        Retrieve Virtual Account History
        Parameters:
        ----------
            virtual_account_id: str
                ID of the Virtual Account Number object. String starting with issuing_.
        """

        url_endpoint = "/v1/virtual_accounts/{virtual_account_id}"
        headers = {}
        self._add_required_headers(headers)
        if not virtual_account_id:
            raise ValueError(
                "Parameter virtual_account_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{virtual_account_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, virtual_account_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveIssuingByRapydToken200ResponseModel._unmap(res)
        return res

    def update_receiving_currency(
        self,
        request_input: UpdateReceivingCurrencyRequestModel,
        virtual_account_id: str,
    ) -> UpdateReceivingCurrency200ResponseModel:
        if isinstance(request_input, dict):
            request_input = UpdateReceivingCurrencyRequestModel(**request_input)
        url_endpoint = "/v1/virtual_accounts/{virtual_account_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not virtual_account_id:
            raise ValueError(
                "Parameter virtual_account_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{virtual_account_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, virtual_account_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateReceivingCurrency200ResponseModel._unmap(res)
        return res

    def close_issuing(self, virtual_account_id: str) -> CloseIssuing200ResponseModel:
        """
        Close VA
        Parameters:
        ----------
            virtual_account_id: str
                ID of the virtual account. String starting with issuing_.
        """

        url_endpoint = "/v1/virtual_accounts/{virtual_account_id}"
        headers = {}
        self._add_required_headers(headers)
        if not virtual_account_id:
            raise ValueError(
                "Parameter virtual_account_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{virtual_account_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, virtual_account_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return CloseIssuing200ResponseModel._unmap(res)
        return res

    def retrieve_issuing_transaction(
        self, transaction_id: str, virtual_account_id: str
    ) -> RetrieveIssuingTransaction200ResponseModel:
        """
        Retrieve Virtual Account Transaction
        Parameters:
        ----------
            virtual_account_id: str
                ID of the Virtual Account Number object. String starting with issuing_.
            transaction_id: str
                ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'.
        """

        url_endpoint = (
            "/v1/virtual_accounts/{virtual_account_id}/transactions/{transaction_id}"
        )
        headers = {}
        self._add_required_headers(headers)
        if not virtual_account_id:
            raise ValueError(
                "Parameter virtual_account_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{virtual_account_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, virtual_account_id, None
                    )
                )
            ),
        )
        if not transaction_id:
            raise ValueError(
                "Parameter transaction_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{transaction_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, transaction_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveIssuingTransaction200ResponseModel._unmap(res)
        return res

    def get_card_issuing_list(
        self,
        contact: str = None,
        page_number: float = None,
        page_size: float = None,
        creation_start_date: float = None,
        creation_end_date: float = None,
        activation_start_date: float = None,
        activation_end_date: float = None,
        card_program: str = None,
        status: str = None,
        allow_deleted: bool = None,
    ) -> GetCardIssuingList200ResponseModel:
        """
        List issuing cards.
        Parameters:
        ----------
            contact: str
                ID of a wallet contact. String starting with cont_.
            page_number: float
                Page number to retrieve.
            page_size: float
                Number of results per page.
            creation_start_date: float
                Start date of card creation.
            creation_end_date: float
                End date of card creation.
            activation_start_date: float
                Start date of card activation.
            activation_end_date: float
                End date of card activation.
            card_program: str
                Card program token.
            status: str
                Card status.
            allow_deleted: bool
                Is card allow delete.
        """

        url_endpoint = "/v1/issuing/cards"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if contact:
            query_params.append(
                query_serializer.serialize_query("form", False, "contact", contact)
            )
        if page_number:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "page_number", page_number
                )
            )
        if page_size:
            query_params.append(
                query_serializer.serialize_query("form", False, "page_size", page_size)
            )
        if creation_start_date:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "creation_start_date", creation_start_date
                )
            )
        if creation_end_date:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "creation_end_date", creation_end_date
                )
            )
        if activation_start_date:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "activation_start_date", activation_start_date
                )
            )
        if activation_end_date:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "activation_end_date", activation_end_date
                )
            )
        if card_program:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "card_program", card_program
                )
            )
        if status:
            query_params.append(
                query_serializer.serialize_query("form", False, "status", status)
            )
        if allow_deleted:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "allow_deleted", allow_deleted
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetCardIssuingList200ResponseModel._unmap(res)
        return res

    def issue_card(
        self, request_input: IssueCardRequestModel
    ) -> IssueCard200ResponseModel:
        """
        Issue Card
        """

        if isinstance(request_input, dict):
            request_input = IssueCardRequestModel(**request_input)
        url_endpoint = "/v1/issuing/cards"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return IssueCard200ResponseModel._unmap(res)
        return res

    def get_card_issuing_details(
        self, card_id: str
    ) -> GetCardIssuingDetails200ResponseModel:
        """
        Card details.
        Parameters:
        ----------
            card_id: str
                ID of a cardId. String starting with ci_.
        """

        url_endpoint = "/v1/issuing/cards/{card_id}"
        headers = {}
        self._add_required_headers(headers)
        if not card_id:
            raise ValueError("Parameter card_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{card_id}",
            quote(str(query_serializer.serialize_path("simple", False, card_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetCardIssuingDetails200ResponseModel._unmap(res)
        return res

    def activate_card(
        self, request_input: ActivateCardRequestModel
    ) -> ActivateCard200ResponseModel:
        """
        Activate Issued Card Using API
        """

        if isinstance(request_input, dict):
            request_input = ActivateCardRequestModel(**request_input)
        url_endpoint = "/v1/issuing/cards/activate"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ActivateCard200ResponseModel._unmap(res)
        return res

    def modify_card(
        self, request_input: ModifyCardRequestModel
    ) -> ModifyCard200ResponseModel:
        """
        Personalize Bulk-Issued Card
        """

        if isinstance(request_input, dict):
            request_input = ModifyCardRequestModel(**request_input)
        url_endpoint = "/v1/issuing/cards/personalize"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ModifyCard200ResponseModel._unmap(res)
        return res

    def update_card_status(
        self, request_input: UpdateCardStatusRequestModel
    ) -> UpdateCardStatus200ResponseModel:
        """
        Update Card Status
        """

        if isinstance(request_input, dict):
            request_input = UpdateCardStatusRequestModel(**request_input)
        url_endpoint = "/v1/issuing/cards/status"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateCardStatus200ResponseModel._unmap(res)
        return res

    def get_card_issuing_transactions(
        self,
        page_number: str,
        page_size: str,
        card_id: str,
        end_date: str = None,
        min_amount: str = None,
        max_amount: str = None,
        merchant_name_search: str = None,
        start_date: str = None,
    ) -> GetCardIssuingTransactions200ResponseModel:
        """
        List Issued Card Transactions
        Parameters:
        ----------
            card_id: str
                ID of the issued card. String starting with card_.
            end_date: str
                Timestamp of the last transaction or later, in Unix time.
            min_amount: str
                Transactions greater than a specific amount.
            max_amount: str
                Transactions smaller than a specific amount.
            merchant_name_search: str
                Filters the results to return only transactions that have this string as part of the name or location.
            page_size: str
                ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'.
            page_number: str
                Page number to retrieve.
            start_date: str
                ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'.
        """

        url_endpoint = "/v1/issuing/cards/{card_id}/transactions"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not card_id:
            raise ValueError("Parameter card_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{card_id}",
            quote(str(query_serializer.serialize_path("simple", False, card_id, None))),
        )
        if end_date:
            query_params.append(
                query_serializer.serialize_query("form", False, "end_date", end_date)
            )
        if min_amount:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "min_amount", min_amount
                )
            )
        if max_amount:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "max_amount", max_amount
                )
            )
        if merchant_name_search:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "merchant_name_search", merchant_name_search
                )
            )
        if not page_size:
            raise ValueError(
                "Parameter page_size is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "page_size", page_size)
        )
        if not page_number:
            raise ValueError(
                "Parameter page_number is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "page_number", page_number)
        )
        if start_date:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "start_date", start_date
                )
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetCardIssuingTransactions200ResponseModel._unmap(res)
        return res

    def get_card_issuing_transaction(
        self, transaction_id: str, card_id: str
    ) -> GetCardIssuingTransaction200ResponseModel:
        """
        Retrieve Issued Card Transaction Details
        Parameters:
        ----------
            card_id: str
                Card id
            transaction_id: str
                Card transaction id
        """

        url_endpoint = "/v1/issuing/cards/{card_id}/transactions/{transaction_id}"
        headers = {}
        self._add_required_headers(headers)
        if not card_id:
            raise ValueError("Parameter card_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{card_id}",
            quote(str(query_serializer.serialize_path("simple", False, card_id, None))),
        )
        if not transaction_id:
            raise ValueError(
                "Parameter transaction_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{transaction_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, transaction_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetCardIssuingTransaction200ResponseModel._unmap(res)
        return res
