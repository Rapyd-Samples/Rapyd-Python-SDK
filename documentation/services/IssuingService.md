# IssuingService

A list of all methods in the `IssuingService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                   | Description                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_issuing](#create_issuing)                                                                         | Issue a virtual account number to an existing wallet.                                                                                                                                                                                                                   |
| [simulate_complete_bank_account_issuing_transaction](#simulate_complete_bank_account_issuing_transaction) | Imulate a deposit to a virtual account number that was issued to a wallet. This method is relevant only for testing in the sandbox. The currency of the transfer must be supported by the specific virtual account. This method triggers the Deposit Completed webhook. |
| [get_remitter_details](#get_remitter_details)                                                             | Retrieve the details of the remitter of a transfer to a virtual bank account.                                                                                                                                                                                           |
| [retrieve_issuing_by_rapyd_token](#retrieve_issuing_by_rapyd_token)                                       | Retrieve a Virtual Account Number object for a wallet.                                                                                                                                                                                                                  |
| [update_receiving_currency](#update_receiving_currency)                                                   | Update Receiving Currency                                                                                                                                                                                                                                               |
| [retrieve_issuing_transaction](#retrieve_issuing_transaction)                                             | Retrieve a virtual account transaction.                                                                                                                                                                                                                                 |

## create_issuing

Issue a virtual account number to an existing wallet.

- HTTP Method: `POST`
- Endpoint: `/v1/issuing/bankaccounts`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [IssuingBankaccountsBody](../models/IssuingBankaccountsBody.md) | ✅       | The request body. |

**Return Type**

`InlineResponse200_29`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import IssuingBankaccountsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = IssuingBankaccountsBody(
    country="country",
    currency="currency",
    description="description",
    ewallet="ewallet",
    merchant_reference_id="merchant_reference_id",
    metadata={},
    requested_currency="requested_currency"
)

result = sdk.issuing.create_issuing(request_body=request_body)

print(result)
```

## simulate_complete_bank_account_issuing_transaction

Imulate a deposit to a virtual account number that was issued to a wallet. This method is relevant only for testing in the sandbox. The currency of the transfer must be supported by the specific virtual account. This method triggers the Deposit Completed webhook.

- HTTP Method: `POST`
- Endpoint: `/v1/issuing/bankaccounts/bankaccounttransfertobankaccount`

**Parameters**

| Name         | Type                                                                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [BankaccountsBankaccounttransfertobankaccountBody](../models/BankaccountsBankaccounttransfertobankaccountBody.md) | ✅       | The request body. |

**Return Type**

`InlineResponse200_30`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import BankaccountsBankaccounttransfertobankaccountBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = BankaccountsBankaccounttransfertobankaccountBody(
    amount="amount",
    currency="currency",
    issued_bank_account="issued_bank_account"
)

result = sdk.issuing.simulate_complete_bank_account_issuing_transaction(request_body=request_body)

print(result)
```

## get_remitter_details

Retrieve the details of the remitter of a transfer to a virtual bank account.

- HTTP Method: `GET`
- Endpoint: `/v1/issuing/bankaccounts/remitters/{virtualAccountId}/transactions/{transaction_id}`

**Parameters**

| Name               | Type | Required | Description                                                                                                           |
| :----------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------- |
| virtual_account_id | str  | ✅       | ID of the Virtual Account Number object. String starting with **issuing\_**.                                          |
| transaction_id     | str  | ✅       | ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'. |

**Return Type**

`InlineResponse200_31`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.issuing.get_remitter_details(
    virtual_account_id="virtualAccountId",
    transaction_id="transaction_id"
)

print(result)
```

## retrieve_issuing_by_rapyd_token

Retrieve a Virtual Account Number object for a wallet.

- HTTP Method: `GET`
- Endpoint: `/v1/issuing/bankaccounts/{virtualAccountId}`

**Parameters**

| Name               | Type | Required | Description                                                                  |
| :----------------- | :--- | :------- | :--------------------------------------------------------------------------- |
| virtual_account_id | str  | ✅       | ID of the Virtual Account Number object. String starting with **issuing\_**. |

**Return Type**

`InlineResponse200_30`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.issuing.retrieve_issuing_by_rapyd_token(virtual_account_id="virtualAccountId")

print(result)
```

## update_receiving_currency

Update Receiving Currency

- HTTP Method: `POST`
- Endpoint: `/v1/issuing/bankaccounts/{virtualAccountId}`

**Parameters**

| Name               | Type                                                                              | Required | Description                                                                  |
| :----------------- | :-------------------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------- |
| request_body       | [BankaccountsVirtualAccountIdBody](../models/BankaccountsVirtualAccountIdBody.md) | ❌       | The request body.                                                            |
| virtual_account_id | str                                                                               | ✅       | ID of the Virtual Account Number object. String starting with **issuing\_**. |

**Return Type**

`InlineResponse200_32`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import BankaccountsVirtualAccountIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = BankaccountsVirtualAccountIdBody(
    requesting_currency="TTD"
)

result = sdk.issuing.update_receiving_currency(
    request_body=request_body,
    virtual_account_id="virtualAccountId"
)

print(result)
```

## retrieve_issuing_transaction

Retrieve a virtual account transaction.

- HTTP Method: `GET`
- Endpoint: `/v1/issuing/bankaccounts/{virtualAccountId}/transactions/{transactionId}`

**Parameters**

| Name               | Type | Required | Description                                                                                                           |
| :----------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------- |
| virtual_account_id | str  | ✅       | ID of the Virtual Account Number object. String starting with **issuing\_**.                                          |
| transaction_id     | str  | ✅       | ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'. |

**Return Type**

`InlineResponse200_33`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.issuing.retrieve_issuing_transaction(
    virtual_account_id="virtualAccountId",
    transaction_id="transactionId"
)

print(result)
```
