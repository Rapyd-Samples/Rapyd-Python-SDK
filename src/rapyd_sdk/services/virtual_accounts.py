from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.virtual_accounts_virtual_account_id_body import (
    VirtualAccountsVirtualAccountIdBody,
)
from ..models.virtual_accounts_transactions_body import VirtualAccountsTransactionsBody
from ..models.v1_virtual_accounts_body import V1VirtualAccountsBody
from ..models.utils.cast_models import cast_models
from ..models.inline_response_200_9 import InlineResponse200_9
from ..models.inline_response_200_8 import InlineResponse200_8
from ..models.inline_response_200_7 import InlineResponse200_7
from ..models.inline_response_200_6 import InlineResponse200_6
from ..models.inline_response_200_5 import InlineResponse200_5


class VirtualAccountsService(BaseService):

    @cast_models
    def create_issuing(
        self, request_body: V1VirtualAccountsBody
    ) -> InlineResponse200_5:
        """Issue a virtual account number to an existing wallet.

        :param request_body: The request body.
        :type request_body: V1VirtualAccountsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Virtual Accounts
        :rtype: InlineResponse200_5
        """

        Validator(V1VirtualAccountsBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/virtual_accounts", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_5._unmap(response)

    @cast_models
    def simulate_complete_bank_account_issuing_transaction(
        self, request_body: VirtualAccountsTransactionsBody
    ) -> InlineResponse200_6:
        """Simulate a deposit to a virtual account number that was issued to a wallet. This method is relevant only for testing in the sandbox. The currency of the transfer must be supported by the specific virtual account. This method triggers the Deposit Completed webhook.

        :param request_body: The request body.
        :type request_body: VirtualAccountsTransactionsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet,
        :rtype: InlineResponse200_6
        """

        Validator(VirtualAccountsTransactionsBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/virtual_accounts/transactions",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_6._unmap(response)

    @cast_models
    def retrieve_issuing_by_rapyd_token(
        self, virtual_account_id: str
    ) -> InlineResponse200_7:
        """Retrieve a Virtual Account Number object for a wallet.

        :param virtual_account_id: ID of the Virtual Account Number object. String starting with issuing_.
        :type virtual_account_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Virtual Accounts
        :rtype: InlineResponse200_7
        """

        Validator(str).validate(virtual_account_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/virtual_accounts/{{virtualAccountId}}",
                self.get_default_headers(),
            )
            .add_path("virtualAccountId", virtual_account_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_7._unmap(response)

    @cast_models
    def update_issuing_by_rapyd_token(
        self, request_body: VirtualAccountsVirtualAccountIdBody, virtual_account_id: str
    ) -> InlineResponse200_7:
        """Update Receiving Currency

        :param request_body: The request body.
        :type request_body: VirtualAccountsVirtualAccountIdBody
        :param virtual_account_id: ID of the Virtual Account Number object. String starting with issuing_.
        :type virtual_account_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet,
        :rtype: InlineResponse200_7
        """

        Validator(VirtualAccountsVirtualAccountIdBody).validate(request_body)
        Validator(str).validate(virtual_account_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/virtual_accounts/{{virtualAccountId}}",
                self.get_default_headers(),
            )
            .add_path("virtualAccountId", virtual_account_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_7._unmap(response)

    @cast_models
    def close_issuing(self, virtual_account_id: str) -> InlineResponse200_8:
        """Delete a virtual account number of an existing wallet. In order to close a virtual account its status must be ACT.

        :param virtual_account_id: ID of the virtual account. String starting with issuing_.
        :type virtual_account_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Virtual Account
        :rtype: InlineResponse200_8
        """

        Validator(str).validate(virtual_account_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/virtual_accounts/{{virtualAccountId}}",
                self.get_default_headers(),
            )
            .add_path("virtualAccountId", virtual_account_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_8._unmap(response)

    @cast_models
    def retrieve_issuing_transaction(
        self, virtual_account_id: str, transaction_id: str
    ) -> InlineResponse200_9:
        """Retrieve a virtual account transaction.

        :param virtual_account_id: ID of the Virtual Account Number object. String starting with issuing_.
        :type virtual_account_id: str
        :param transaction_id: ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'.
        :type transaction_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet
        :rtype: InlineResponse200_9
        """

        Validator(str).validate(virtual_account_id)
        Validator(str).validate(transaction_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/virtual_accounts/{{virtualAccountId}}/transactions/{{transactionId}}",
                self.get_default_headers(),
            )
            .add_path("virtualAccountId", virtual_account_id)
            .add_path("transactionId", transaction_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_9._unmap(response)
