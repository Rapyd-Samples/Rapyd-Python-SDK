# VirtualAccountsService

A list of all methods in the `VirtualAccountsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                   | Description                                                                                                                                                                                                                                                              |
| :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_issuing](#create_issuing)                                                                         | Issue a virtual account number to an existing wallet.                                                                                                                                                                                                                    |
| [simulate_complete_bank_account_issuing_transaction](#simulate_complete_bank_account_issuing_transaction) | Simulate a deposit to a virtual account number that was issued to a wallet. This method is relevant only for testing in the sandbox. The currency of the transfer must be supported by the specific virtual account. This method triggers the Deposit Completed webhook. |
| [retrieve_issuing_by_rapyd_token](#retrieve_issuing_by_rapyd_token)                                       | Retrieve a Virtual Account Number object for a wallet.                                                                                                                                                                                                                   |
| [update_issuing_by_rapyd_token](#update_issuing_by_rapyd_token)                                           | Update Receiving Currency                                                                                                                                                                                                                                                |
| [close_issuing](#close_issuing)                                                                           | Delete a virtual account number of an existing wallet. In order to close a virtual account its status must be ACT.                                                                                                                                                       |
| [retrieve_issuing_transaction](#retrieve_issuing_transaction)                                             | Retrieve a virtual account transaction.                                                                                                                                                                                                                                  |

## create_issuing

Issue a virtual account number to an existing wallet.

- HTTP Method: `POST`
- Endpoint: `/v1/virtual_accounts`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | `[V1VirtualAccountsBody](../models/V1VirtualAccountsBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_5`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1VirtualAccountsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1VirtualAccountsBody(
    country="country",
    currency="currency",
    description="description",
    ewallet="ewallet",
    merchant_reference_id="merchant_reference_id",
    metadata={},
    requested_currency="requested_currency"
)

result = sdk.virtual_accounts.create_issuing(request_body=request_body)

print(result)
```

## simulate_complete_bank_account_issuing_transaction

Simulate a deposit to a virtual account number that was issued to a wallet. This method is relevant only for testing in the sandbox. The currency of the transfer must be supported by the specific virtual account. This method triggers the Deposit Completed webhook.

- HTTP Method: `POST`
- Endpoint: `/v1/virtual_accounts/transactions`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | `[VirtualAccountsTransactionsBody](../models/VirtualAccountsTransactionsBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_6`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import VirtualAccountsTransactionsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = VirtualAccountsTransactionsBody(
    amount="amount",
    currency="currency",
    issued_bank_account="issued_bank_account"
)

result = sdk.virtual_accounts.simulate_complete_bank_account_issuing_transaction(request_body=request_body)

print(result)
```

## retrieve_issuing_by_rapyd_token

Retrieve a Virtual Account Number object for a wallet.

- HTTP Method: `GET`
- Endpoint: `/v1/virtual_accounts/{virtualAccountId}`

**Parameters**

| Name               | Type  | Required | Description                                                              |
| :----------------- | :---- | :------- | :----------------------------------------------------------------------- |
| virtual_account_id | `str` | ✅       | ID of the Virtual Account Number object. String starting with issuing\_. |

**Return Type**

`InlineResponse200_7`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.virtual_accounts.retrieve_issuing_by_rapyd_token(virtual_account_id="virtualAccountId")

print(result)
```

## update_issuing_by_rapyd_token

Update Receiving Currency

- HTTP Method: `POST`
- Endpoint: `/v1/virtual_accounts/{virtualAccountId}`

**Parameters**

| Name               | Type                                                                                      | Required | Description                                                              |
| :----------------- | :---------------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------- |
| request_body       | `[VirtualAccountsVirtualAccountIdBody](../models/VirtualAccountsVirtualAccountIdBody.md)` | ✅       | The request body.                                                        |
| virtual_account_id | `str`                                                                                     | ✅       | ID of the Virtual Account Number object. String starting with issuing\_. |

**Return Type**

`InlineResponse200_7`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import VirtualAccountsVirtualAccountIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = VirtualAccountsVirtualAccountIdBody(
    requesting_currency="GBP"
)

result = sdk.virtual_accounts.update_issuing_by_rapyd_token(
    request_body=request_body,
    virtual_account_id="virtualAccountId"
)

print(result)
```

## close_issuing

Delete a virtual account number of an existing wallet. In order to close a virtual account its status must be ACT.

- HTTP Method: `DELETE`
- Endpoint: `/v1/virtual_accounts/{virtualAccountId}`

**Parameters**

| Name               | Type  | Required | Description                                                |
| :----------------- | :---- | :------- | :--------------------------------------------------------- |
| virtual_account_id | `str` | ✅       | ID of the virtual account. String starting with issuing\_. |

**Return Type**

`InlineResponse200_8`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.virtual_accounts.close_issuing(virtual_account_id="virtualAccountId")

print(result)
```

## retrieve_issuing_transaction

Retrieve a virtual account transaction.

- HTTP Method: `GET`
- Endpoint: `/v1/virtual_accounts/{virtualAccountId}/transactions/{transactionId}`

**Parameters**

| Name               | Type  | Required | Description                                                                                                           |
| :----------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------- |
| virtual_account_id | `str` | ✅       | ID of the Virtual Account Number object. String starting with issuing\_.                                              |
| transaction_id     | `str` | ✅       | ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'. |

**Return Type**

`InlineResponse200_9`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.virtual_accounts.retrieve_issuing_transaction(
    virtual_account_id="virtualAccountId",
    transaction_id="transactionId"
)

print(result)
```
