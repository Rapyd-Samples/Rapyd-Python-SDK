from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.FundsTransferRequest import (
    FundsTransferRequest as FundsTransferRequestModel,
)
from ..models.FundsTransfer200Response import (
    FundsTransfer200Response as FundsTransfer200ResponseModel,
)
from ..models.SetFundsTransferResponseRequest import (
    SetFundsTransferResponseRequest as SetFundsTransferResponseRequestModel,
)
from ..models.SetFundsTransferResponse200Response import (
    SetFundsTransferResponse200Response as SetFundsTransferResponse200ResponseModel,
)
from ..models.GetEwalletContacts200Response import (
    GetEwalletContacts200Response as GetEwalletContacts200ResponseModel,
)
from ..models.CreateEwalletContactRequest import (
    CreateEwalletContactRequest as CreateEwalletContactRequestModel,
)
from ..models.CreateEwalletContact200Response import (
    CreateEwalletContact200Response as CreateEwalletContact200ResponseModel,
)
from ..models.GetEwalletContact200Response import (
    GetEwalletContact200Response as GetEwalletContact200ResponseModel,
)
from ..models.Contact import Contact as ContactModel
from ..models.UpdateEwalletContact200Response import (
    UpdateEwalletContact200Response as UpdateEwalletContact200ResponseModel,
)
from ..models.DeleteEwalletContact200Response import (
    DeleteEwalletContact200Response as DeleteEwalletContact200ResponseModel,
)
from ..models.GetEwalletContactComplianceLevels200Response import (
    GetEwalletContactComplianceLevels200Response as GetEwalletContactComplianceLevels200ResponseModel,
)
from ..models.GetUsers200Response import GetUsers200Response as GetUsers200ResponseModel
from ..models.CreateUserRequest import CreateUserRequest as CreateUserRequestModel
from ..models.CreateUser200Response import (
    CreateUser200Response as CreateUser200ResponseModel,
)
from ..models.GetUser200Response import GetUser200Response as GetUser200ResponseModel
from ..models.UpdatedUserRequest import UpdatedUserRequest as UpdatedUserRequestModel
from ..models.UpdatedUser200Response import (
    UpdatedUser200Response as UpdatedUser200ResponseModel,
)
from ..models.DeleteUser200Response import (
    DeleteUser200Response as DeleteUser200ResponseModel,
)
from ..models.EWalletsStatus import EWalletsStatus as EWalletsStatusModel
from ..models.UpdateEwalletStatus200Response import (
    UpdateEwalletStatus200Response as UpdateEwalletStatus200ResponseModel,
)
from ..models.SetAccountLimitRequest import (
    SetAccountLimitRequest as SetAccountLimitRequestModel,
)
from ..models.SetAccountLimit200Response import (
    SetAccountLimit200Response as SetAccountLimit200ResponseModel,
)
from ..models.RemoveAccountLimitRequest import (
    RemoveAccountLimitRequest as RemoveAccountLimitRequestModel,
)
from ..models.RemoveAccountLimit200Response import (
    RemoveAccountLimit200Response as RemoveAccountLimit200ResponseModel,
)
from ..models.GetUserAccounts200Response import (
    GetUserAccounts200Response as GetUserAccounts200ResponseModel,
)
from ..models.GetUserTransactions200Response import (
    GetUserTransactions200Response as GetUserTransactions200ResponseModel,
)
from ..models.GetUserTransactionDetails200Response import (
    GetUserTransactionDetails200Response as GetUserTransactionDetails200ResponseModel,
)


class EWallets(BaseService):
    def funds_transfer(
        self, request_input: FundsTransferRequestModel
    ) -> FundsTransfer200ResponseModel:
        """
        Transfer Funds Between Wallets
        """

        if isinstance(request_input, dict):
            request_input = FundsTransferRequestModel(**request_input)
        url_endpoint = "/v1/account/transfer"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return FundsTransfer200ResponseModel._unmap(res)
        return res

    def set_funds_transfer_response(
        self, request_input: SetFundsTransferResponseRequestModel
    ) -> SetFundsTransferResponse200ResponseModel:
        """
        Set Transfer Response
        """

        if isinstance(request_input, dict):
            request_input = SetFundsTransferResponseRequestModel(**request_input)
        url_endpoint = "/v1/account/transfer/response"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return SetFundsTransferResponse200ResponseModel._unmap(res)
        return res

    def get_ewallet_contacts(
        self, ewallet_id: str
    ) -> GetEwalletContacts200ResponseModel:
        """
        List Contacts for a Rapyd Wallet
        Parameters:
        ----------
            ewallet_id: str
                ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
        """

        url_endpoint = "/v1/ewallets/{ewallet_id}/contacts"
        headers = {}
        self._add_required_headers(headers)
        if not ewallet_id:
            raise ValueError(
                "Parameter ewallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, ewallet_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetEwalletContacts200ResponseModel._unmap(res)
        return res

    def create_ewallet_contact(
        self, request_input: CreateEwalletContactRequestModel, ewallet_id: str
    ) -> CreateEwalletContact200ResponseModel:
        """
        Add Contact to Wallet
        Parameters:
        ----------
            ewallet_id: str
                ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
        """

        if isinstance(request_input, dict):
            request_input = CreateEwalletContactRequestModel(**request_input)
        url_endpoint = "/v1/ewallets/{ewallet_id}/contacts"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not ewallet_id:
            raise ValueError(
                "Parameter ewallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, ewallet_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateEwalletContact200ResponseModel._unmap(res)
        return res

    def get_ewallet_contact(
        self, contact_id: str, ewallet_id: str
    ) -> GetEwalletContact200ResponseModel:
        """
        Retrieve Wallet Contact.
        Parameters:
        ----------
            ewallet_id: str
                ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
            contact_id: str
                One of two values. either ID of the contact - String starting with the prefix cont_ or Contact reference ID.
        """

        url_endpoint = "/v1/ewallets/{ewallet_id}/contacts/{contact_id}"
        headers = {}
        self._add_required_headers(headers)
        if not ewallet_id:
            raise ValueError(
                "Parameter ewallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, ewallet_id, None))
            ),
        )
        if not contact_id:
            raise ValueError(
                "Parameter contact_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{contact_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, contact_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetEwalletContact200ResponseModel._unmap(res)
        return res

    def update_ewallet_contact(
        self, request_input: ContactModel, contact_id: str, ewallet_id: str
    ) -> UpdateEwalletContact200ResponseModel:
        """
        Update Wallet Contact
        Parameters:
        ----------
            ewallet_id: str
                ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
            contact_id: str
                ID of the contact. String starting with the prefix cont_.
        """

        if isinstance(request_input, dict):
            request_input = ContactModel(**request_input)
        url_endpoint = "/v1/ewallets/{ewallet_id}/contacts/{contact_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not ewallet_id:
            raise ValueError(
                "Parameter ewallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, ewallet_id, None))
            ),
        )
        if not contact_id:
            raise ValueError(
                "Parameter contact_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{contact_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, contact_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateEwalletContact200ResponseModel._unmap(res)
        return res

    def delete_ewallet_contact(
        self, contact_id: str, ewallet_id: str
    ) -> DeleteEwalletContact200ResponseModel:
        """
        Delete Wallet Contact
        Parameters:
        ----------
            ewallet_id: str
                ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
            contact_id: str
                ID of the contact. String starting with the prefix cont_.
        """

        url_endpoint = "/v1/ewallets/{ewallet_id}/contacts/{contact_id}"
        headers = {}
        self._add_required_headers(headers)
        if not ewallet_id:
            raise ValueError(
                "Parameter ewallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, ewallet_id, None))
            ),
        )
        if not contact_id:
            raise ValueError(
                "Parameter contact_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{contact_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, contact_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteEwalletContact200ResponseModel._unmap(res)
        return res

    def get_ewallet_contact_compliance_levels(
        self, contact_id: str, ewallet_id: str
    ) -> GetEwalletContactComplianceLevels200ResponseModel:
        """
        Get the compliance status of a personal contact.
        Parameters:
        ----------
            ewallet_id: str
                ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
            contact_id: str
                ID of the contact. String starting with cont_.
        """

        url_endpoint = (
            "/v1/ewallets/{ewallet_id}/contacts/{contact_id}/compliance_levels"
        )
        headers = {}
        self._add_required_headers(headers)
        if not ewallet_id:
            raise ValueError(
                "Parameter ewallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, ewallet_id, None))
            ),
        )
        if not contact_id:
            raise ValueError(
                "Parameter contact_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{contact_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, contact_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetEwalletContactComplianceLevels200ResponseModel._unmap(res)
        return res

    def get_users(
        self,
        phone_number: str = None,
        email: str = None,
        ewallet_reference_id: str = None,
        page_number: float = None,
        page_size: float = None,
        type_: str = None,
        min_balance: float = None,
        currency: str = None,
    ) -> GetUsers200ResponseModel:
        """
        List eWallets.
        Parameters:
        ----------
            phone_number: str
                Phone number of the Rapyd Wallet in E.164 format.
            email: str
                Email address of the wallet owner.
            ewallet_reference_id: str
                Wallet ID defined by the customer or end user.
            page_number: float
                Page number to retrieve. If page_number is not specified, page 1 is retrieved.
            page_size: float
                Number of results per page.
            type_: str
                Type of wallet - company, person, client.
            min_balance: float
            currency: str
        """

        url_endpoint = "/v1/ewallets"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if phone_number:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "phone_number", phone_number
                )
            )
        if email:
            query_params.append(
                query_serializer.serialize_query("form", False, "email", email)
            )
        if ewallet_reference_id:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ewallet_reference_id", ewallet_reference_id
                )
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
        if type_:
            query_params.append(
                query_serializer.serialize_query("form", False, "type", type_)
            )
        if min_balance:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "min_balance", min_balance
                )
            )
        if currency:
            query_params.append(
                query_serializer.serialize_query("form", False, "currency", currency)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetUsers200ResponseModel._unmap(res)
        return res

    def create_user(
        self, request_input: CreateUserRequestModel
    ) -> CreateUser200ResponseModel:
        """
        Create Wallet
        """

        if isinstance(request_input, dict):
            request_input = CreateUserRequestModel(**request_input)
        url_endpoint = "/v1/ewallets"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateUser200ResponseModel._unmap(res)
        return res

    def get_user(self, ewallet_token: str) -> GetUser200ResponseModel:
        """
        Retrieve Wallet
        Parameters:
        ----------
            ewallet_token: str
                ID of the wallet. String starting with ewallet_.
        """

        url_endpoint = "/v1/ewallets/{ewallet_token}"
        headers = {}
        self._add_required_headers(headers)
        if not ewallet_token:
            raise ValueError(
                "Parameter ewallet_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_token}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, ewallet_token, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetUser200ResponseModel._unmap(res)
        return res

    def updated_user(
        self, request_input: UpdatedUserRequestModel, ewallet_token: str
    ) -> UpdatedUser200ResponseModel:
        """
        Update Wallet
        Parameters:
        ----------
            ewallet_token: str
                ID of the wallet. String starting with ewallet_.
        """

        if isinstance(request_input, dict):
            request_input = UpdatedUserRequestModel(**request_input)
        url_endpoint = "/v1/ewallets/{ewallet_token}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not ewallet_token:
            raise ValueError(
                "Parameter ewallet_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_token}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, ewallet_token, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdatedUser200ResponseModel._unmap(res)
        return res

    def delete_user(self, ewallet_token: str) -> DeleteUser200ResponseModel:
        """
        Delete a Wallet.
        Parameters:
        ----------
            ewallet_token: str
                ID of the wallet. String starting with ewallet_.
        """

        url_endpoint = "/v1/ewallets/{ewallet_token}"
        headers = {}
        self._add_required_headers(headers)
        if not ewallet_token:
            raise ValueError(
                "Parameter ewallet_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_token}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, ewallet_token, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteUser200ResponseModel._unmap(res)
        return res

    def update_ewallet_status(
        self, status: EWalletsStatusModel, ewallet_token: str
    ) -> UpdateEwalletStatus200ResponseModel:
        """
        Change Wallet status
        Parameters:
        ----------
            ewallet_token: str
                ID of the Rapyd Wallet. String starting with ewallet_. Required when phone number is not used.
            status: EWalletsStatus
                Status of the wallet. One of the following: enable, disable, close. disable - Change to disabled status (DIS). close - Close the wallet. Changes the status to closed (CLO). enable - Change to active status (ACT).

        """

        if isinstance(status, dict):
            status = EWalletsStatusModel(**status)
        url_endpoint = "/v1/ewallets/{ewallet_token}/statuses/{status}"
        headers = {}
        self._add_required_headers(headers)
        if not ewallet_token:
            raise ValueError(
                "Parameter ewallet_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{ewallet_token}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, ewallet_token, None
                    )
                )
            ),
        )
        if not status:
            raise ValueError("Parameter status is required, cannot be empty or blank.")
        validated_status = self._enum_matching(
            status, EWalletsStatusModel.list(), "status"
        )
        url_endpoint = url_endpoint.replace(
            "{status}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, validated_status, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return UpdateEwalletStatus200ResponseModel._unmap(res)
        return res

    def set_account_limit(
        self, wallet_id: str, request_input: SetAccountLimitRequestModel = None
    ) -> SetAccountLimit200ResponseModel:
        """
        Set Wallet Account Limit
        Parameters:
        ----------
            wallet_id: str
                ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_
        """

        if isinstance(request_input, dict):
            request_input = SetAccountLimitRequestModel(**request_input)
        url_endpoint = "/v1/ewallets/{wallet_id}/account/limits"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not wallet_id:
            raise ValueError(
                "Parameter wallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{wallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, wallet_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return SetAccountLimit200ResponseModel._unmap(res)
        return res

    def remove_account_limit(
        self, wallet_id: str, request_input: RemoveAccountLimitRequestModel = None
    ) -> RemoveAccountLimit200ResponseModel:
        """
        Delete a coupon from the Rapyd platform
        Parameters:
        ----------
            wallet_id: str
                ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_
        """

        if isinstance(request_input, dict):
            request_input = RemoveAccountLimitRequestModel(**request_input)
        url_endpoint = "/v1/ewallets/{wallet_id}/account/limits"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not wallet_id:
            raise ValueError(
                "Parameter wallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{wallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, wallet_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return RemoveAccountLimit200ResponseModel._unmap(res)
        return res

    def get_user_accounts(self, wallet_id: str) -> GetUserAccounts200ResponseModel:
        """
        Retrieve Wallet Balances
        Parameters:
        ----------
            wallet_id: str
                ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_
        """

        url_endpoint = "/v1/ewallets/{wallet_id}/accounts"
        headers = {}
        self._add_required_headers(headers)
        if not wallet_id:
            raise ValueError(
                "Parameter wallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{wallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, wallet_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetUserAccounts200ResponseModel._unmap(res)
        return res

    def get_user_transactions(
        self,
        wallet_id: str,
        balance: float = None,
        currency: str = None,
        end_date: str = None,
        ending_before: str = None,
        page_number: str = None,
        page_size: str = None,
        start_date: str = None,
        starting_after: str = None,
        type_: str = None,
    ) -> GetUserTransactions200ResponseModel:
        """
        List Wallet Transactions
        Parameters:
        ----------
            wallet_id: str
                ID of the wallet. String starting with ewallet_.
            balance: float
                The updated wallet balance after successful completion of the transaction.
            currency: str
                Three-letter ISO 4217 code for the currency of the transactions. Uppercase.
            end_date: str
                Timestamp of the last transaction or later, in Unix time.
            ending_before: str
                The ID of the wallet transaction created after the last wallet transaction you want to retrieve. String starting with wt_.
            page_number: str
                Page number to retrieve.
            page_size: str
                Number of results per page.
            start_date: str
                Timestamp of the first transaction or earlier, in Unix time.
            starting_after: str
                The ID of the wallet transaction created before the first wallet transaction you want to retrieve. String starting with wt_
            type_: str
                Type of transaction.
        """

        url_endpoint = "/v1/ewallets/{wallet_id}/transactions"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not wallet_id:
            raise ValueError(
                "Parameter wallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{wallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, wallet_id, None))
            ),
        )
        if balance:
            query_params.append(
                query_serializer.serialize_query("form", False, "balance", balance)
            )
        if currency:
            query_params.append(
                query_serializer.serialize_query("form", False, "currency", currency)
            )
        if end_date:
            query_params.append(
                query_serializer.serialize_query("form", False, "end_date", end_date)
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
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
        if start_date:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "start_date", start_date
                )
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        if type_:
            query_params.append(
                query_serializer.serialize_query("form", False, "type", type_)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetUserTransactions200ResponseModel._unmap(res)
        return res

    def get_user_transaction_details(
        self, transaction_id: str, wallet_id: str
    ) -> GetUserTransactionDetails200ResponseModel:
        """
        Get Details of Wallet Transaction
        Parameters:
        ----------
            wallet_id: str
                ID of the wallet. String starting with ewallet_.
            transaction_id: str
                ID of the transaction, from the response to List Wallet Transactions. String starting with wt_.
        """

        url_endpoint = "/v1/ewallets/{wallet_id}/transactions/{transaction_id}"
        headers = {}
        self._add_required_headers(headers)
        if not wallet_id:
            raise ValueError(
                "Parameter wallet_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{wallet_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, wallet_id, None))
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
            return GetUserTransactionDetails200ResponseModel._unmap(res)
        return res
