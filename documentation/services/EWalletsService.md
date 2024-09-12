# EWalletsService

A list of all methods in the `EWalletsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                                                                                                                                              |
| :------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [funds_transfer](#funds_transfer)                                               | Transfer funds between Rapyd Wallets.                                                                                                                                                    |
| [set_funds_transfer_response](#set_funds_transfer_response)                     | Respond to a funds transfer between wallets. The transferee uses this method to accept or decline the transfer.                                                                          |
| [get_ewallet_contacts](#get_ewallet_contacts)                                   | Retrieve all contacts for a wallet.                                                                                                                                                      |
| [create_ewallet_contact](#create_ewallet_contact)                               | Add a personal contact to a company wallet or client wallet.                                                                                                                             |
| [get_ewallet_contact](#get_ewallet_contact)                                     | Retrieve a contact for an existing Rapyd Wallet.                                                                                                                                         |
| [update_ewallet_contact](#update_ewallet_contact)                               | Update a contact for a Rapyd Wallet.                                                                                                                                                     |
| [delete_ewallet_contact](#delete_ewallet_contact)                               | Delete a personal contact from a company wallet or client wallet.                                                                                                                        |
| [get_ewallet_contact_compliance_levels](#get_ewallet_contact_compliance_levels) | Verify the compliance status of a personal contact.                                                                                                                                      |
| [get_users](#get_users)                                                         | Retrieve a list of Rapyd Wallets. You can filter the list with query parameters.                                                                                                         |
| [create_user](#create_user)                                                     | Create a Rapyd Wallet.                                                                                                                                                                   |
| [get_user](#get_user)                                                           | Retrieve the details of a Rapyd Wallet.                                                                                                                                                  |
| [updated_user](#updated_user)                                                   | Change or modify a Rapyd Wallet.                                                                                                                                                         |
| [delete_user](#delete_user)                                                     | Delete a Rapyd Wallet. Use this method when the wallet has never been used. This method triggers the Wallet Deleted webhook. This webhook contains the same information as the response. |
| [update_ewallet_status](#update_ewallet_status)                                 | Change Wallet Status                                                                                                                                                                     |
| [set_account_limit](#set_account_limit)                                         | Set the maximum balance limit or the minimum balance threshold for an existing wallet account.                                                                                           |
| [remove_account_limit](#remove_account_limit)                                   | Delete a limit on a wallet account.                                                                                                                                                      |
| [get_user_accounts](#get_user_accounts)                                         | Retrieve details of the balances in a Rapyd Wallet.                                                                                                                                      |
| [get_user_transactions](#get_user_transactions)                                 | Retrieve a list of all transactions related to a wallet.                                                                                                                                 |
| [get_user_transaction_details](#get_user_transaction_details)                   | Retrieve the details of a wallet transaction.                                                                                                                                            |

## funds_transfer

Transfer funds between Rapyd Wallets.

- HTTP Method: `POST`
- Endpoint: `/v1/account/transfer`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | `[AccountTransferBody](../models/AccountTransferBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import AccountTransferBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AccountTransferBody(
    amount=8.08,
    currency="currency",
    destination_ewallet="destination_ewallet",
    expiration="expiration",
    metadata={},
    source_ewallet="source_ewallet"
)

result = sdk.e_wallets.funds_transfer(request_body=request_body)

print(result)
```

## set_funds_transfer_response

Respond to a funds transfer between wallets. The transferee uses this method to accept or decline the transfer.

- HTTP Method: `POST`
- Endpoint: `/v1/account/transfer/response`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | `[TransferResponseBody](../models/TransferResponseBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import TransferResponseBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = TransferResponseBody(
    id_="id",
    metadata={},
    status="status"
)

result = sdk.e_wallets.set_funds_transfer_response(request_body=request_body)

print(result)
```

## get_ewallet_contacts

Retrieve all contacts for a wallet.

- HTTP Method: `GET`
- Endpoint: `/v1/ewallets/{ewalletId}/contacts`

**Parameters**

| Name       | Type  | Required | Description                                                                                  |
| :--------- | :---- | :------- | :------------------------------------------------------------------------------------------- |
| ewallet_id | `str` | ✅       | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet\_. |

**Return Type**

`InlineResponse200_1`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_ewallet_contacts(ewallet_id="ewalletId")

print(result)
```

## create_ewallet_contact

Add a personal contact to a company wallet or client wallet.

- HTTP Method: `POST`
- Endpoint: `/v1/ewallets/{ewalletId}/contacts`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                  |
| :----------- | :------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------- |
| request_body | `[EwalletIdContactsBody](../models/EwalletIdContactsBody.md)` | ✅       | The request body.                                                                            |
| ewallet_id   | `str`                                                         | ✅       | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet\_. |

**Return Type**

`InlineResponse200_2`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import EwalletIdContactsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = EwalletIdContactsBody(
    address={
        "canton": "canton",
        "city": "city",
        "country": "GB",
        "created_at": 3.34,
        "district": "district",
        "id_": "id",
        "line_1": "line_1",
        "line_2": "line_2",
        "line_3": "line_3",
        "metadata": {},
        "name": "name",
        "phone_number": "phone_number",
        "state": "state",
        "zip": "zip"
    },
    contact_type="contact_type",
    country="country",
    date_of_birth="date_of_birth",
    email="email",
    first_name="first_name",
    last_name="last_name",
    gender="gender",
    house_type="house_type",
    identification_number="identification_number",
    identification_type="identification_type",
    marital_status="marital_status",
    metadata="metadata",
    middle_name="middle_name",
    mothers_name="mothers_name",
    nationality="nationality",
    phone_number="phone_number",
    second_last_name="second_last_name",
    send_notifications=False,
    contact_reference_id="contact_reference_id"
)

result = sdk.e_wallets.create_ewallet_contact(
    request_body=request_body,
    ewallet_id="ewalletId"
)

print(result)
```

## get_ewallet_contact

Retrieve a contact for an existing Rapyd Wallet.

- HTTP Method: `GET`
- Endpoint: `/v1/ewallets/{ewalletId}/contacts/{contactId}`

**Parameters**

| Name       | Type  | Required | Description                                                                                                   |
| :--------- | :---- | :------- | :------------------------------------------------------------------------------------------------------------ |
| ewallet_id | `str` | ✅       | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet\_.                  |
| contact_id | `str` | ✅       | One of two values. either ID of the contact - String starting with the prefix cont\_ or Contact reference ID. |

**Return Type**

`InlineResponse200_2`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_ewallet_contact(
    ewallet_id="ewalletId",
    contact_id="contactId"
)

print(result)
```

## update_ewallet_contact

Update a contact for a Rapyd Wallet.

- HTTP Method: `POST`
- Endpoint: `/v1/ewallets/{ewalletId}/contacts/{contactId}`

**Parameters**

| Name         | Type                              | Required | Description                                                                                  |
| :----------- | :-------------------------------- | :------- | :------------------------------------------------------------------------------------------- |
| request_body | `[Contact](../models/Contact.md)` | ✅       | The request body.                                                                            |
| ewallet_id   | `str`                             | ✅       | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet\_. |
| contact_id   | `str`                             | ✅       | ID of the contact. String starting with the prefix cont\_.                                   |

**Return Type**

`InlineResponse200_2`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Contact

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = Contact(
    address={
        "canton": "canton",
        "city": "city",
        "country": "GB",
        "created_at": 3.34,
        "district": "district",
        "id_": "id",
        "line_1": "line_1",
        "line_2": "line_2",
        "line_3": "line_3",
        "metadata": {},
        "name": "name",
        "phone_number": "phone_number",
        "state": "state",
        "zip": "zip"
    },
    business_details={
        "address": {
            "canton": "canton",
            "city": "city",
            "country": "GB",
            "created_at": 3.34,
            "district": "district",
            "id_": "id",
            "line_1": "line_1",
            "line_2": "line_2",
            "line_3": "line_3",
            "metadata": {},
            "name": "name",
            "phone_number": "phone_number",
            "state": "state",
            "zip": "zip"
        },
        "annual_revenue": 6.14,
        "cnae_code": "cnae_code",
        "created_at": 6.84,
        "entity_type": "sole_prop",
        "establishment_date": "2813-47-84",
        "id_": "id",
        "industry_category": "2PLX8Nv1Se",
        "industry_sub_category": "industry_sub_category",
        "legal_entity_type": "legal_entity_type",
        "name": "name",
        "registration_number": "registration_number"
    },
    compliance_profile=0.4,
    contact_type="personal",
    country="GB",
    created_at=8.94,
    date_of_birth="date_of_birth",
    email="phL8Es@GB.oMq",
    ewallet="ewallet",
    first_name="first_name",
    gender="male",
    house_type="lease",
    id_="id",
    identification_number="identification_number",
    identification_type="identification_type",
    issued_card_data={},
    last_name="last_name",
    marital_status="married",
    metadata={},
    middle_name="middle_name",
    mothers_name="mothers_name",
    nationality="GB",
    phone_number="phone_number",
    second_last_name="second_last_name",
    send_notifications=False,
    verification_status="not verified",
    contact_reference_id="contact_reference_id"
)

result = sdk.e_wallets.update_ewallet_contact(
    request_body=request_body,
    ewallet_id="ewalletId",
    contact_id="contactId"
)

print(result)
```

## delete_ewallet_contact

Delete a personal contact from a company wallet or client wallet.

- HTTP Method: `DELETE`
- Endpoint: `/v1/ewallets/{ewalletId}/contacts/{contactId}`

**Parameters**

| Name       | Type  | Required | Description                                                                                  |
| :--------- | :---- | :------- | :------------------------------------------------------------------------------------------- |
| ewallet_id | `str` | ✅       | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet\_. |
| contact_id | `str` | ✅       | ID of the contact. String starting with the prefix cont\_.                                   |

**Return Type**

`InlineResponse200_3`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.delete_ewallet_contact(
    ewallet_id="ewalletId",
    contact_id="contactId"
)

print(result)
```

## get_ewallet_contact_compliance_levels

Verify the compliance status of a personal contact.

- HTTP Method: `GET`
- Endpoint: `/v1/ewallets/{ewalletId}/contacts/{contactId}/compliance_levels`

**Parameters**

| Name       | Type  | Required | Description                                                                                  |
| :--------- | :---- | :------- | :------------------------------------------------------------------------------------------- |
| ewallet_id | `str` | ✅       | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet\_. |
| contact_id | `str` | ✅       | ID of the contact. String starting with cont\_.                                              |

**Return Type**

`InlineResponse200_4`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_ewallet_contact_compliance_levels(
    ewallet_id="ewalletId",
    contact_id="contactId"
)

print(result)
```

## get_users

Retrieve a list of Rapyd Wallets. You can filter the list with query parameters.

- HTTP Method: `GET`
- Endpoint: `/v1/ewallets`

**Parameters**

| Name                 | Type    | Required | Description                                                                    |
| :------------------- | :------ | :------- | :----------------------------------------------------------------------------- |
| phone_number         | `str`   | ❌       | Phone number of the Rapyd Wallet in E.164 format.                              |
| email                | `str`   | ❌       | Email address of the wallet owner.                                             |
| ewallet_reference_id | `str`   | ❌       | Wallet ID defined by the customer or end user.                                 |
| page_number          | `float` | ❌       | Page number to retrieve. If page_number is not specified, page 1 is retrieved. |
| page_size            | `float` | ❌       | Number of results per page.                                                    |
| type\_               | `str`   | ❌       | Type of wallet - company, person, client.                                      |
| min_balance          | `float` | ❌       |                                                                                |
| currency             | `str`   | ❌       |                                                                                |

**Return Type**

`InlineResponse200_20`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_users(
    phone_number="phone_number",
    email="email",
    ewallet_reference_id="ewallet_reference_id",
    page_number=1.1,
    page_size=8.92,
    type_="type",
    min_balance=1.17,
    currency="currency"
)

print(result)
```

## create_user

Create a Rapyd Wallet.

- HTTP Method: `POST`
- Endpoint: `/v1/ewallets`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | `[V1EwalletsBody](../models/V1EwalletsBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_21`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1EwalletsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1EwalletsBody(
    contact={
        "data": [
            {
                "address": {
                    "canton": "canton",
                    "city": "city",
                    "country": "GB",
                    "created_at": 3.34,
                    "district": "district",
                    "id_": "id",
                    "line_1": "line_1",
                    "line_2": "line_2",
                    "line_3": "line_3",
                    "metadata": {},
                    "name": "name",
                    "phone_number": "phone_number",
                    "state": "state",
                    "zip": "zip"
                },
                "business_details": {
                    "address": {
                        "canton": "canton",
                        "city": "city",
                        "country": "GB",
                        "created_at": 3.34,
                        "district": "district",
                        "id_": "id",
                        "line_1": "line_1",
                        "line_2": "line_2",
                        "line_3": "line_3",
                        "metadata": {},
                        "name": "name",
                        "phone_number": "phone_number",
                        "state": "state",
                        "zip": "zip"
                    },
                    "annual_revenue": 6.14,
                    "cnae_code": "cnae_code",
                    "created_at": 6.84,
                    "entity_type": "sole_prop",
                    "establishment_date": "2813-47-84",
                    "id_": "id",
                    "industry_category": "2PLX8Nv1Se",
                    "industry_sub_category": "industry_sub_category",
                    "legal_entity_type": "legal_entity_type",
                    "name": "name",
                    "registration_number": "registration_number"
                },
                "compliance_profile": 0.4,
                "contact_type": "personal",
                "country": "GB",
                "created_at": 8.94,
                "date_of_birth": "date_of_birth",
                "email": "phL8Es@GB.oMq",
                "ewallet": "ewallet",
                "first_name": "first_name",
                "gender": "male",
                "house_type": "lease",
                "id_": "id",
                "identification_number": "identification_number",
                "identification_type": "identification_type",
                "issued_card_data": {},
                "last_name": "last_name",
                "marital_status": "married",
                "metadata": {},
                "middle_name": "middle_name",
                "mothers_name": "mothers_name",
                "nationality": "GB",
                "phone_number": "phone_number",
                "second_last_name": "second_last_name",
                "send_notifications": False,
                "verification_status": "not verified",
                "contact_reference_id": "contact_reference_id"
            }
        ],
        "total_count": 3.99,
        "has_more": False,
        "url": "url"
    },
    ewallet_reference_id="ewallet_reference_id",
    first_name="first_name",
    last_name="last_name",
    metadata={},
    type_="type"
)

result = sdk.e_wallets.create_user(request_body=request_body)

print(result)
```

## get_user

Retrieve the details of a Rapyd Wallet.

- HTTP Method: `GET`
- Endpoint: `/v1/ewallets/{ewalletToken}`

**Parameters**

| Name          | Type  | Required | Description                                       |
| :------------ | :---- | :------- | :------------------------------------------------ |
| ewallet_token | `str` | ✅       | ID of the wallet. String starting with ewallet\_. |

**Return Type**

`InlineResponse200_21`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_user(ewallet_token="ewalletToken")

print(result)
```

## updated_user

Change or modify a Rapyd Wallet.

- HTTP Method: `POST`
- Endpoint: `/v1/ewallets/{ewalletToken}`

**Parameters**

| Name          | Type                                                                | Required | Description                                       |
| :------------ | :------------------------------------------------------------------ | :------- | :------------------------------------------------ |
| request_body  | `[EwalletsEwalletTokenBody](../models/EwalletsEwalletTokenBody.md)` | ✅       | The request body.                                 |
| ewallet_token | `str`                                                               | ✅       | ID of the wallet. String starting with ewallet\_. |

**Return Type**

`InlineResponse200_21`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import EwalletsEwalletTokenBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = EwalletsEwalletTokenBody(
    ewallet_reference_id="ewallet_reference_id",
    first_name="first_name",
    last_name="last_name",
    metadata={}
)

result = sdk.e_wallets.updated_user(
    request_body=request_body,
    ewallet_token="ewalletToken"
)

print(result)
```

## delete_user

Delete a Rapyd Wallet. Use this method when the wallet has never been used. This method triggers the Wallet Deleted webhook. This webhook contains the same information as the response.

- HTTP Method: `DELETE`
- Endpoint: `/v1/ewallets/{ewalletToken}`

**Parameters**

| Name          | Type  | Required | Description                                       |
| :------------ | :---- | :------- | :------------------------------------------------ |
| ewallet_token | `str` | ✅       | ID of the wallet. String starting with ewallet\_. |

**Return Type**

`InlineResponse200_22`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.delete_user(ewallet_token="ewalletToken")

print(result)
```

## update_ewallet_status

Change Wallet Status

- HTTP Method: `POST`
- Endpoint: `/v1/ewallets/{ewalletToken}/statuses/{status}`

**Parameters**

| Name          | Type                                                                  | Required | Description                                                                                                                                                                                                          |
| :------------ | :-------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ewallet_token | `str`                                                                 | ✅       | ID of the Rapyd Wallet. String starting with ewallet\_. Required when phone number is not used.                                                                                                                      |
| status        | `[UpdateEwalletStatusStatus](../models/UpdateEwalletStatusStatus.md)` | ✅       | Status of the wallet. One of the following: enable, disable, close. disable - Change to disabled status (DIS). close - Close the wallet. Changes the status to closed (CLO). enable - Change to active status (ACT). |

**Return Type**

`InlineResponse200_22`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import UpdateEwalletStatusStatus

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.update_ewallet_status(
    ewallet_token="ewalletToken",
    status="enable"
)

print(result)
```

## set_account_limit

Set the maximum balance limit or the minimum balance threshold for an existing wallet account.

- HTTP Method: `POST`
- Endpoint: `/v1/ewallets/{walletId}/account/limits`

**Parameters**

| Name         | Type                                                  | Required | Description                                                                                 |
| :----------- | :---------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------ |
| request_body | `[AccountLimitsBody](../models/AccountLimitsBody.md)` | ❌       | The request body.                                                                           |
| wallet_id    | `str`                                                 | ✅       | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet\_ |

**Return Type**

`InlineResponse200_23`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import AccountLimitsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AccountLimitsBody(
    account_id="account_id",
    amount="amount",
    currency="currency",
    type_="type"
)

result = sdk.e_wallets.set_account_limit(
    request_body=request_body,
    wallet_id="walletId"
)

print(result)
```

## remove_account_limit

Delete a limit on a wallet account.

- HTTP Method: `DELETE`
- Endpoint: `/v1/ewallets/{walletId}/account/limits`

**Parameters**

| Name      | Type  | Required | Description                                                                                 |
| :-------- | :---- | :------- | :------------------------------------------------------------------------------------------ |
| wallet_id | `str` | ✅       | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet\_ |

**Return Type**

`InlineResponse200_24`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.remove_account_limit(wallet_id="walletId")

print(result)
```

## get_user_accounts

Retrieve details of the balances in a Rapyd Wallet.

- HTTP Method: `GET`
- Endpoint: `/v1/ewallets/{walletId}/accounts`

**Parameters**

| Name      | Type  | Required | Description                                                                                 |
| :-------- | :---- | :------- | :------------------------------------------------------------------------------------------ |
| wallet_id | `str` | ✅       | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet\_ |

**Return Type**

`InlineResponse200_23`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_user_accounts(wallet_id="walletId")

print(result)
```

## get_user_transactions

Retrieve a list of all transactions related to a wallet.

- HTTP Method: `GET`
- Endpoint: `/v1/ewallets/{walletId}/transactions`

**Parameters**

| Name           | Type    | Required | Description                                                                                                                  |
| :------------- | :------ | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| wallet_id      | `str`   | ✅       | ID of the wallet. String starting with ewallet\_.                                                                            |
| balance        | `float` | ❌       | The updated wallet balance after successful completion of the transaction.                                                   |
| currency       | `str`   | ❌       | Three-letter ISO 4217 code for the currency of the transactions. Uppercase.                                                  |
| end_date       | `str`   | ❌       | Timestamp of the last transaction or later, in Unix time.                                                                    |
| ending_before  | `str`   | ❌       | The ID of the wallet transaction created after the last wallet transaction you want to retrieve. String starting with wt\_.  |
| page_number    | `str`   | ❌       | Page number to retrieve.                                                                                                     |
| page_size      | `str`   | ❌       | Number of results per page.                                                                                                  |
| start_date     | `str`   | ❌       | Timestamp of the first transaction or earlier, in Unix time.                                                                 |
| starting_after | `str`   | ❌       | The ID of the wallet transaction created before the first wallet transaction you want to retrieve. String starting with wt\_ |
| type\_         | `str`   | ❌       | Type of transaction.                                                                                                         |

**Return Type**

`InlineResponse200_25`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_user_transactions(
    wallet_id="walletId",
    balance=0.31,
    currency="currency",
    end_date="end_date",
    ending_before="ending_before",
    page_number="page_number",
    page_size="page_size",
    start_date="start_date",
    starting_after="starting_after",
    type_="type"
)

print(result)
```

## get_user_transaction_details

Retrieve the details of a wallet transaction.

- HTTP Method: `GET`
- Endpoint: `/v1/ewallets/{walletId}/transactions/{transactionId}`

**Parameters**

| Name           | Type  | Required | Description                                                                                      |
| :------------- | :---- | :------- | :----------------------------------------------------------------------------------------------- |
| wallet_id      | `str` | ✅       | ID of the wallet. String starting with ewallet\_.                                                |
| transaction_id | `str` | ✅       | ID of the transaction, from the response to List Wallet Transactions. String starting with wt\_. |

**Return Type**

`InlineResponse200_26`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_user_transaction_details(
    wallet_id="walletId",
    transaction_id="transactionId"
)

print(result)
```
