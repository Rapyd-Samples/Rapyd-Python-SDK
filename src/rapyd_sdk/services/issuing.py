from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    BankaccountsBankaccounttransfertobankaccountBody,
    BankaccountsVirtualAccountIdBody,
    InlineResponse200_29,
    InlineResponse200_30,
    InlineResponse200_31,
    InlineResponse200_32,
    InlineResponse200_33,
    IssuingBankaccountsBody,
)


class IssuingService(BaseService):

    @cast_models
    def create_issuing(
        self, request_body: IssuingBankaccountsBody
    ) -> InlineResponse200_29:
        """Issue a virtual account number to an existing wallet.

        :param request_body: The request body.
        :type request_body: IssuingBankaccountsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Virtual Account,
        :rtype: InlineResponse200_29
        """

        Validator(IssuingBankaccountsBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/issuing/bankaccounts", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_29._unmap(response)

    @cast_models
    def simulate_complete_bank_account_issuing_transaction(
        self, request_body: BankaccountsBankaccounttransfertobankaccountBody
    ) -> InlineResponse200_30:
        """Imulate a deposit to a virtual account number that was issued to a wallet. This method is relevant only for testing in the sandbox. The currency of the transfer must be supported by the specific virtual account. This method triggers the Deposit Completed webhook.

        :param request_body: The request body.
        :type request_body: BankaccountsBankaccounttransfertobankaccountBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet,
        :rtype: InlineResponse200_30
        """

        Validator(BankaccountsBankaccounttransfertobankaccountBody).validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/issuing/bankaccounts/bankaccounttransfertobankaccount",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_30._unmap(response)

    @cast_models
    def get_remitter_details(
        self, virtual_account_id: str, transaction_id: str
    ) -> InlineResponse200_31:
        """Retrieve the details of the remitter of a transfer to a virtual bank account.

        :param virtual_account_id: ID of the Virtual Account Number object. String starting with **issuing_**.
        :type virtual_account_id: str
        :param transaction_id: ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'.
        :type transaction_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet,
        :rtype: InlineResponse200_31
        """

        Validator(str).validate(virtual_account_id)
        Validator(str).validate(transaction_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/issuing/bankaccounts/remitters/{{virtualAccountId}}/transactions/{{transaction_id}}",
                self.get_default_headers(),
            )
            .add_path("virtualAccountId", virtual_account_id)
            .add_path("transaction_id", transaction_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_31._unmap(response)

    @cast_models
    def retrieve_issuing_by_rapyd_token(
        self, virtual_account_id: str
    ) -> InlineResponse200_30:
        """Retrieve a Virtual Account Number object for a wallet.

        :param virtual_account_id: ID of the Virtual Account Number object. String starting with **issuing_**.
        :type virtual_account_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Virtual Account,
        :rtype: InlineResponse200_30
        """

        Validator(str).validate(virtual_account_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/issuing/bankaccounts/{{virtualAccountId}}",
                self.get_default_headers(),
            )
            .add_path("virtualAccountId", virtual_account_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_30._unmap(response)

    @cast_models
    def update_receiving_currency(
        self,
        virtual_account_id: str,
        request_body: BankaccountsVirtualAccountIdBody = None,
    ) -> InlineResponse200_32:
        """Update Receiving Currency

        :param request_body: The request body., defaults to None
        :type request_body: BankaccountsVirtualAccountIdBody, optional
        :param virtual_account_id: ID of the Virtual Account Number object. String starting with **issuing_**.
        :type virtual_account_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet,
        :rtype: InlineResponse200_32
        """

        Validator(BankaccountsVirtualAccountIdBody).is_optional().validate(request_body)
        Validator(str).validate(virtual_account_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/issuing/bankaccounts/{{virtualAccountId}}",
                self.get_default_headers(),
            )
            .add_path("virtualAccountId", virtual_account_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_32._unmap(response)

    @cast_models
    def retrieve_issuing_transaction(
        self, virtual_account_id: str, transaction_id: str
    ) -> InlineResponse200_33:
        """Retrieve a virtual account transaction.

        :param virtual_account_id: ID of the Virtual Account Number object. String starting with **issuing_**.
        :type virtual_account_id: str
        :param transaction_id: ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'.
        :type transaction_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet,
        :rtype: InlineResponse200_33
        """

        Validator(str).validate(virtual_account_id)
        Validator(str).validate(transaction_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/issuing/bankaccounts/{{virtualAccountId}}/transactions/{{transactionId}}",
                self.get_default_headers(),
            )
            .add_path("virtualAccountId", virtual_account_id)
            .add_path("transactionId", transaction_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_33._unmap(response)
