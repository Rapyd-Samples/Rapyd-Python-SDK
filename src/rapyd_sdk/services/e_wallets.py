from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_ewallets_body import V1EwalletsBody
from ..models.utils.cast_models import cast_models
from ..models.update_ewallet_status_status import UpdateEwalletStatusStatus
from ..models.transfer_response_body import TransferResponseBody
from ..models.inline_response_200_4 import InlineResponse200_4
from ..models.inline_response_200_3 import InlineResponse200_3
from ..models.inline_response_200_26 import InlineResponse200_26
from ..models.inline_response_200_25 import InlineResponse200_25
from ..models.inline_response_200_24 import InlineResponse200_24
from ..models.inline_response_200_23 import InlineResponse200_23
from ..models.inline_response_200_22 import InlineResponse200_22
from ..models.inline_response_200_21 import InlineResponse200_21
from ..models.inline_response_200_20 import InlineResponse200_20
from ..models.inline_response_200_2 import InlineResponse200_2
from ..models.inline_response_200_1 import InlineResponse200_1
from ..models.inline_response_200 import InlineResponse200
from ..models.ewallets_ewallet_token_body import EwalletsEwalletTokenBody
from ..models.ewallet_id_contacts_body import EwalletIdContactsBody
from ..models.contact import Contact
from ..models.account_transfer_body import AccountTransferBody
from ..models.account_limits_body import AccountLimitsBody


class EWalletsService(BaseService):

    @cast_models
    def funds_transfer(self, request_body: AccountTransferBody) -> InlineResponse200:
        """Transfer funds between Rapyd Wallets.

        :param request_body: The request body.
        :type request_body: AccountTransferBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Transaction properties
        :rtype: InlineResponse200
        """

        Validator(AccountTransferBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/account/transfer", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200._unmap(response)

    @cast_models
    def set_funds_transfer_response(
        self, request_body: TransferResponseBody
    ) -> InlineResponse200:
        """Respond to a funds transfer between wallets. The transferee uses this method to accept or decline the transfer.

        :param request_body: The request body.
        :type request_body: TransferResponseBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Transacton properties
        :rtype: InlineResponse200
        """

        Validator(TransferResponseBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/account/transfer/response",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200._unmap(response)

    @cast_models
    def get_ewallet_contacts(self, ewallet_id: str) -> InlineResponse200_1:
        """Retrieve all contacts for a wallet.

        :param ewallet_id: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
        :type ewallet_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet,
        :rtype: InlineResponse200_1
        """

        Validator(str).validate(ewallet_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletId}}/contacts",
                self.get_default_headers(),
            )
            .add_path("ewalletId", ewallet_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_1._unmap(response)

    @cast_models
    def create_ewallet_contact(
        self, request_body: EwalletIdContactsBody, ewallet_id: str
    ) -> InlineResponse200_2:
        """Add a personal contact to a company wallet or client wallet.

        :param request_body: The request body.
        :type request_body: EwalletIdContactsBody
        :param ewallet_id: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
        :type ewallet_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet,
        :rtype: InlineResponse200_2
        """

        Validator(EwalletIdContactsBody).validate(request_body)
        Validator(str).validate(ewallet_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletId}}/contacts",
                self.get_default_headers(),
            )
            .add_path("ewalletId", ewallet_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_2._unmap(response)

    @cast_models
    def get_ewallet_contact(
        self, ewallet_id: str, contact_id: str
    ) -> InlineResponse200_2:
        """Retrieve a contact for an existing Rapyd Wallet.

        :param ewallet_id: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
        :type ewallet_id: str
        :param contact_id: One of two values. either ID of the contact - String starting with the prefix cont_ or Contact reference ID.
        :type contact_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieve a contact for an existing Rapyd Wallet.
        :rtype: InlineResponse200_2
        """

        Validator(str).validate(ewallet_id)
        Validator(str).validate(contact_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletId}}/contacts/{{contactId}}",
                self.get_default_headers(),
            )
            .add_path("ewalletId", ewallet_id)
            .add_path("contactId", contact_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_2._unmap(response)

    @cast_models
    def update_ewallet_contact(
        self, request_body: Contact, ewallet_id: str, contact_id: str
    ) -> InlineResponse200_2:
        """Update a contact for a Rapyd Wallet.

        :param request_body: The request body.
        :type request_body: Contact
        :param ewallet_id: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
        :type ewallet_id: str
        :param contact_id: ID of the contact. String starting with the prefix cont_.
        :type contact_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieve a contact for an existing Rapyd Wallet.
        :rtype: InlineResponse200_2
        """

        Validator(Contact).validate(request_body)
        Validator(str).validate(ewallet_id)
        Validator(str).validate(contact_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletId}}/contacts/{{contactId}}",
                self.get_default_headers(),
            )
            .add_path("ewalletId", ewallet_id)
            .add_path("contactId", contact_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_2._unmap(response)

    @cast_models
    def delete_ewallet_contact(
        self, ewallet_id: str, contact_id: str
    ) -> InlineResponse200_3:
        """Delete a personal contact from a company wallet or client wallet.

        :param ewallet_id: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
        :type ewallet_id: str
        :param contact_id: ID of the contact. String starting with the prefix cont_.
        :type contact_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieve a contact for an existing Rapyd Wallet.
        :rtype: InlineResponse200_3
        """

        Validator(str).validate(ewallet_id)
        Validator(str).validate(contact_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletId}}/contacts/{{contactId}}",
                self.get_default_headers(),
            )
            .add_path("ewalletId", ewallet_id)
            .add_path("contactId", contact_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_3._unmap(response)

    @cast_models
    def get_ewallet_contact_compliance_levels(
        self, ewallet_id: str, contact_id: str
    ) -> InlineResponse200_4:
        """Verify the compliance status of a personal contact.

        :param ewallet_id: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_.
        :type ewallet_id: str
        :param contact_id: ID of the contact. String starting with cont_.
        :type contact_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Verify the compliance status of a personal contact.
        :rtype: InlineResponse200_4
        """

        Validator(str).validate(ewallet_id)
        Validator(str).validate(contact_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletId}}/contacts/{{contactId}}/compliance_levels",
                self.get_default_headers(),
            )
            .add_path("ewalletId", ewallet_id)
            .add_path("contactId", contact_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_4._unmap(response)

    @cast_models
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
    ) -> InlineResponse200_20:
        """Retrieve a list of Rapyd Wallets. You can filter the list with query parameters.

        :param phone_number: Phone number of the Rapyd Wallet in E.164 format., defaults to None
        :type phone_number: str, optional
        :param email: Email address of the wallet owner., defaults to None
        :type email: str, optional
        :param ewallet_reference_id: Wallet ID defined by the customer or end user., defaults to None
        :type ewallet_reference_id: str, optional
        :param page_number: Page number to retrieve. If page_number is not specified, page 1 is retrieved., defaults to None
        :type page_number: float, optional
        :param page_size: Number of results per page., defaults to None
        :type page_size: float, optional
        :param type_: Type of wallet - company, person, client., defaults to None
        :type type_: str, optional
        :param min_balance: min_balance, defaults to None
        :type min_balance: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of eWallets,
        :rtype: InlineResponse200_20
        """

        Validator(str).is_optional().validate(phone_number)
        Validator(str).is_optional().validate(email)
        Validator(str).is_optional().validate(ewallet_reference_id)
        Validator(float).is_optional().validate(page_number)
        Validator(float).is_optional().validate(page_size)
        Validator(str).is_optional().validate(type_)
        Validator(float).is_optional().validate(min_balance)
        Validator(str).is_optional().validate(currency)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/ewallets", self.get_default_headers())
            .add_query("phone_number", phone_number, explode=False)
            .add_query("email", email, explode=False)
            .add_query("ewallet_reference_id", ewallet_reference_id, explode=False)
            .add_query("page_number", page_number, explode=False)
            .add_query("page_size", page_size, explode=False)
            .add_query("type", type_, explode=False)
            .add_query("min_balance", min_balance, explode=False)
            .add_query("currency", currency, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_20._unmap(response)

    @cast_models
    def create_user(self, request_body: V1EwalletsBody) -> InlineResponse200_21:
        """Create a Rapyd Wallet.

        :param request_body: The request body.
        :type request_body: V1EwalletsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created Rapyd Wallet
        :rtype: InlineResponse200_21
        """

        Validator(V1EwalletsBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/ewallets", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_21._unmap(response)

    @cast_models
    def get_user(self, ewallet_token: str) -> InlineResponse200_21:
        """Retrieve the details of a Rapyd Wallet.

        :param ewallet_token: ID of the wallet. String starting with ewallet_.
        :type ewallet_token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieve the details of a Rapyd Wallet.
        :rtype: InlineResponse200_21
        """

        Validator(str).validate(ewallet_token)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletToken}}",
                self.get_default_headers(),
            )
            .add_path("ewalletToken", ewallet_token)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_21._unmap(response)

    @cast_models
    def updated_user(
        self, request_body: EwalletsEwalletTokenBody, ewallet_token: str
    ) -> InlineResponse200_21:
        """Change or modify a Rapyd Wallet.

        :param request_body: The request body.
        :type request_body: EwalletsEwalletTokenBody
        :param ewallet_token: ID of the wallet. String starting with ewallet_.
        :type ewallet_token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created Rapyd Wallet
        :rtype: InlineResponse200_21
        """

        Validator(EwalletsEwalletTokenBody).validate(request_body)
        Validator(str).validate(ewallet_token)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletToken}}",
                self.get_default_headers(),
            )
            .add_path("ewalletToken", ewallet_token)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_21._unmap(response)

    @cast_models
    def delete_user(self, ewallet_token: str) -> InlineResponse200_22:
        """Delete a Rapyd Wallet. Use this method when the wallet has never been used. This method triggers the Wallet Deleted webhook. This webhook contains the same information as the response.

        :param ewallet_token: ID of the wallet. String starting with ewallet_.
        :type ewallet_token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Wallet was deleted
        :rtype: InlineResponse200_22
        """

        Validator(str).validate(ewallet_token)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletToken}}",
                self.get_default_headers(),
            )
            .add_path("ewalletToken", ewallet_token)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_22._unmap(response)

    @cast_models
    def update_ewallet_status(
        self, ewallet_token: str, status: UpdateEwalletStatusStatus
    ) -> InlineResponse200_22:
        """Change Wallet Status

        :param ewallet_token: ID of the Rapyd Wallet. String starting with ewallet_. Required when phone number is not used.
        :type ewallet_token: str
        :param status: Status of the wallet. One of the following: enable, disable, close. disable - Change to disabled status (DIS). close - Close the wallet. Changes the status to closed (CLO). enable - Change to active status (ACT).
        :type status: UpdateEwalletStatusStatus
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Operations status
        :rtype: InlineResponse200_22
        """

        Validator(str).validate(ewallet_token)
        Validator(UpdateEwalletStatusStatus).validate(status)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{ewalletToken}}/statuses/{{status}}",
                self.get_default_headers(),
            )
            .add_path("ewalletToken", ewallet_token)
            .add_path("status", status)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_22._unmap(response)

    @cast_models
    def set_account_limit(
        self, wallet_id: str, request_body: AccountLimitsBody = None
    ) -> InlineResponse200_23:
        """Set the maximum balance limit or the minimum balance threshold for an existing wallet account.

        :param request_body: The request body., defaults to None
        :type request_body: AccountLimitsBody, optional
        :param wallet_id: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_
        :type wallet_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List Contacts for a Rapyd Wallet Accounts
        :rtype: InlineResponse200_23
        """

        Validator(AccountLimitsBody).is_optional().validate(request_body)
        Validator(str).validate(wallet_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{walletId}}/account/limits",
                self.get_default_headers(),
            )
            .add_path("walletId", wallet_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_23._unmap(response)

    @cast_models
    def remove_account_limit(self, wallet_id: str) -> InlineResponse200_24:
        """Delete a limit on a wallet account.

        :param wallet_id: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_
        :type wallet_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: limit was deleted
        :rtype: InlineResponse200_24
        """

        Validator(str).validate(wallet_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{walletId}}/account/limits",
                self.get_default_headers(),
            )
            .add_path("walletId", wallet_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_24._unmap(response)

    @cast_models
    def get_user_accounts(self, wallet_id: str) -> InlineResponse200_23:
        """Retrieve details of the balances in a Rapyd Wallet.

        :param wallet_id: ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet_
        :type wallet_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List accounts related to the Rapyd Wallet
        :rtype: InlineResponse200_23
        """

        Validator(str).validate(wallet_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{walletId}}/accounts",
                self.get_default_headers(),
            )
            .add_path("walletId", wallet_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_23._unmap(response)

    @cast_models
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
    ) -> InlineResponse200_25:
        """Retrieve a list of all transactions related to a wallet.

        :param wallet_id: ID of the wallet. String starting with ewallet_.
        :type wallet_id: str
        :param balance: The updated wallet balance after successful completion of the transaction., defaults to None
        :type balance: float, optional
        :param currency: Three-letter ISO 4217 code for the currency of the transactions. Uppercase., defaults to None
        :type currency: str, optional
        :param end_date: Timestamp of the last transaction or later, in Unix time., defaults to None
        :type end_date: str, optional
        :param ending_before: The ID of the wallet transaction created after the last wallet transaction you want to retrieve. String starting with wt_., defaults to None
        :type ending_before: str, optional
        :param page_number: Page number to retrieve., defaults to None
        :type page_number: str, optional
        :param page_size: Number of results per page., defaults to None
        :type page_size: str, optional
        :param start_date: Timestamp of the first transaction or earlier, in Unix time., defaults to None
        :type start_date: str, optional
        :param starting_after: The ID of the wallet transaction created before the first wallet transaction you want to retrieve. String starting with wt_, defaults to None
        :type starting_after: str, optional
        :param type_: Type of transaction., defaults to None
        :type type_: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of all transactions related to a wallet
        :rtype: InlineResponse200_25
        """

        Validator(str).validate(wallet_id)
        Validator(float).is_optional().validate(balance)
        Validator(str).is_optional().validate(currency)
        Validator(str).is_optional().validate(end_date)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(page_number)
        Validator(str).is_optional().validate(page_size)
        Validator(str).is_optional().validate(start_date)
        Validator(str).is_optional().validate(starting_after)
        Validator(str).is_optional().validate(type_)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{walletId}}/transactions",
                self.get_default_headers(),
            )
            .add_path("walletId", wallet_id)
            .add_query("balance", balance, explode=False)
            .add_query("currency", currency, explode=False)
            .add_query("end_date", end_date, explode=False)
            .add_query("ending_before", ending_before, explode=False)
            .add_query("page_number", page_number, explode=False)
            .add_query("page_size", page_size, explode=False)
            .add_query("start_date", start_date, explode=False)
            .add_query("starting_after", starting_after, explode=False)
            .add_query("type", type_, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_25._unmap(response)

    @cast_models
    def get_user_transaction_details(
        self, wallet_id: str, transaction_id: str
    ) -> InlineResponse200_26:
        """Retrieve the details of a wallet transaction.

        :param wallet_id: ID of the wallet. String starting with ewallet_.
        :type wallet_id: str
        :param transaction_id: ID of the transaction, from the response to List Wallet Transactions. String starting with wt_.
        :type transaction_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieve the details of a wallet transaction
        :rtype: InlineResponse200_26
        """

        Validator(str).validate(wallet_id)
        Validator(str).validate(transaction_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/ewallets/{{walletId}}/transactions/{{transactionId}}",
                self.get_default_headers(),
            )
            .add_path("walletId", wallet_id)
            .add_path("transactionId", transaction_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_26._unmap(response)
