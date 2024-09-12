# DisburseService

A list of all methods in the `DisburseService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_payout_method_types_details](#get_payout_method_types_details) | Retrieve the fields required to use a payout method type. The fields are returned as an array of objects. The name of each field appears in the name field of each object. Use this information for Create Payout, Create Beneficiary and Create Sender. Note: The fields returned by this method are required when you create a payout. If you create a payout with a sender or beneficiary that was created previously, you are responsible for choosing a sender and beneficiary that have all the fields required by the payout method.                                                                                                                                                  |
| [list_payouts](#list_payouts)                                       | Retrieve a list of payouts that you created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [create_payout](#create_payout)                                     | Create a payout (disbursement). This method triggers the Payout Created webhook. This webhook contains the same information as the response. If the action of a third party is not required, the Payout Completed webhook is also triggered.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [create_beneficiary](#create_beneficiary)                           | Create a beneficiary for use in payouts. The response provides a unique beneficiary ID, which you can use in place of the Beneficiary object for Create Payout. This method triggers the Beneficiary Created webhook. This webhook contains the same information as the response. Note: In addition to the required fields documented below, you must include all other beneficiary fields listed in the response to Get Payout Required Fields, and you must conform to the regex provided. To create a beneficiary that you can use with multiple payout methods, include all fields that are required by each payout method. The client is responsible for including all required fields. |
| [validate_beneficiary](#validate_beneficiary)                       | Validate the format of the details for a payout beneficiary. You can validate a beneficiary multiple times for different payout methods. You can enter a Beneficiary object or a previously created beneficiary ID. Note: In addition to the required fields for Create Beneficiary, the Beneficiary object must include all required fields for the beneficiary listed in the response to Get Payout Required Fields. The examples include additional fields for the 'us_ach_bank' payout method.                                                                                                                                                                                           |
| [get_beneficiary](#get_beneficiary)                                 | Retrieve details of a payout beneficiary. Note: The 'Retrieve Beneficiary - individual' response includes additional fields for the 'ca_general_bank' payout method. The 'Retrieve Beneficiary - company' response includes additional fields for the 'us_ach_bank' payout method.                                                                                                                                                                                                                                                                                                                                                                                                           |
| [delete_beneficiary](#delete_beneficiary)                           | Delete a payout beneficiary from the Rapyd platform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [simulate_complete_payout](#simulate_complete_payout)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [confirm_payout](#confirm_payout)                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [create_sender](#create_sender)                                     | Create a sender for use in payouts. The response provides a unique sender ID, which you can use in place of the sender object for Create Payout. Note: In addition to the required fields documented below, you must include all other sender fields listed in the response to Get Payout Required Fields, and you must conform to the regex provided. To create a sender that you can use with multiple payout methods, include all fields that are required by each payout method. The client is responsible for including all required fields.                                                                                                                                            |
| [get_payer](#get_payer)                                             | Note: The Retrieve Sender - individual response includes additional fields for the ca_general_bank payout method. The Retrieve Sender - company response includes an additional field for the us_ach_bank payout method.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [delete_payer](#delete_payer)                                       | Delete a payout sender from the Rapyd platform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [get_payout_method_types](#get_payout_method_types)                 | Retrieve a list of payout method types that you can use when creating a payout. The response contains a list of objects. Each object includes a payout method type and its attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [get_payout](#get_payout)                                           | Retrieve the details of a payout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [update_payout](#update_payout)                                     | Change or modify a payout. This method triggers the Payout Updated webhook. This webhook contains the same information as the response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [cancel_payout](#cancel_payout)                                     | The payout can be canceled unless its status is confirmation or completed. This method triggers the Payout Canceled webhook. This webhook contains the same information as the response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## get_payout_method_types_details

Retrieve the fields required to use a payout method type. The fields are returned as an array of objects. The name of each field appears in the name field of each object. Use this information for Create Payout, Create Beneficiary and Create Sender. Note: The fields returned by this method are required when you create a payout. If you create a payout with a sender or beneficiary that was created previously, you are responsible for choosing a sender and beneficiary that have all the fields required by the payout method.

- HTTP Method: `GET`
- Endpoint: `/v1/payout_methods/{pomt}/required_fields`

**Parameters**

| Name                    | Type    | Required | Description                                                                                                                                                                          |
| :---------------------- | :------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pomt                    | `str`   | ✅       | The type of the payout method. Set to the name of a payout method listed in the response to List Payout Method Types. The two-letter prefix must match the beneficiary country code. |
| beneficiary_country     | `str`   | ✅       | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.                                                                                                           |
| beneficiary_entity_type | `str`   | ✅       | Type of entity for the beneficiary. One of the following, individual, company                                                                                                        |
| payout_amount           | `float` | ✅       | Amount of the payout, in units of the currency that the beneficiary is receiving. Decimal.                                                                                           |
| payout_currency         | `str`   | ✅       | Currency received by the beneficiary. Three-letter ISO 4217 code. Uppercase.                                                                                                         |
| sender_country          | `str`   | ✅       | Country of the sender. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.                                                                                                                |
| sender_currency         | `str`   | ✅       | Currency that the sender is paying with. Three-letter ISO 4217 code. Uppercase.                                                                                                      |
| sender_entity_type      | `str`   | ✅       | Type of entity for the sender. One of the following: individual, company                                                                                                             |

**Return Type**

`InlineResponse200_10`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.get_payout_method_types_details(
    pomt="pomt",
    beneficiary_country="beneficiary_country",
    beneficiary_entity_type="beneficiary_entity_type",
    payout_amount=5.58,
    payout_currency="payout_currency",
    sender_country="sender_country",
    sender_currency="sender_currency",
    sender_entity_type="sender_entity_type"
)

print(result)
```

## list_payouts

Retrieve a list of payouts that you created.

- HTTP Method: `GET`
- Endpoint: `/v1/payouts`

**Parameters**

| Name                  | Type  | Required | Description                                                                                                                                                                                                                                             |
| :-------------------- | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| beneficiary           | `str` | ❌       | Filters according to the beneficiary ID. String starting with beneficiary\_.                                                                                                                                                                            |
| created_after         | `str` | ❌       | The ID of the payout created before the first payout you want to retrieve. String starting with payout\_.                                                                                                                                               |
| created_before        | `str` | ❌       | The ID of the payout created after the last payout you want to retrieve. String starting with payout\_.                                                                                                                                                 |
| ending_before         | `str` | ❌       | The ID of a payout in the list. The list ends with the payout that was created before the payout with this ID. Use this filter to get the previous page of results. String starting with payout\_. Deprecated.                                          |
| ewallet               | `str` | ❌       | Filters according to the wallet ID. String starting with ewallet\_.                                                                                                                                                                                     |
| limit                 | `str` | ❌       | The maximum number of payouts to return. Range: 1-100. Default is 10.                                                                                                                                                                                   |
| merchant_reference_id | `str` | ❌       | Filters according to the merchant reference ID.                                                                                                                                                                                                         |
| payout_method_type    | `str` | ❌       | Filters according to the type of payout method. The two-letter prefix must match the beneficiary country code.                                                                                                                                          |
| sender                | `str` | ❌       | Filters according to the sender ID. String starting with sender\_.                                                                                                                                                                                      |
| sender_country        | `str` | ❌       | Filters according to the country of the sender. Two-letter ISO 3166-1 ALPHA-2 code.                                                                                                                                                                     |
| sender_currency       | `str` | ❌       | Filters according to the currency that the sender is paying with. Three-letter ISO 4217 code.                                                                                                                                                           |
| starting_after        | `str` | ❌       | The ID of a payout in the list. The list begins with the payout that was created next after the payout with this ID. Use this filter to get the next page of results. Relevant when ending*before is not used. String starting with payout*. Deprecated |

**Return Type**

`InlineResponse200_11`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.list_payouts(
    beneficiary="beneficiary",
    created_after="created_after",
    created_before="created_before",
    ending_before="ending_before",
    ewallet="ewallet",
    limit="limit",
    merchant_reference_id="merchant_reference_id",
    payout_method_type="payout_method_type",
    sender="sender",
    sender_country="GB",
    sender_currency="GBP",
    starting_after="starting_after"
)

print(result)
```

## create_payout

Create a payout (disbursement). This method triggers the Payout Created webhook. This webhook contains the same information as the response. If the action of a third party is not required, the Payout Completed webhook is also triggered.

- HTTP Method: `POST`
- Endpoint: `/v1/payouts`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | `[V1PayoutsBody](../models/V1PayoutsBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_12`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models.v1_payouts_body import V1PayoutsBody1

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1PayoutsBody1(
    beneficiary="mollit u",
    beneficiary_country="US",
    beneficiary_entity_type="individual",
    confirm_automatically=True,
    converstion_rate=1,
    description="description",
    ewallet="ewallet_4f1757749b8858160274e6db49f78ff3",
    expiration="1607941348",
    location="location",
    merchant_reference_id="GHY-0YU-HUJ-POI",
    metadata={},
    payout_amount=110,
    payout_currency="GBP",
    payout_method_type="us_general_bank",
    payout_options={},
    sender="irure nulla",
    sender_country="GB",
    sender_currency="GBP",
    sender_entity_type="company",
    statement_descriptor="statement_descriptor"
)

result = sdk.disburse.create_payout(request_body=request_body)

print(result)
```

## create_beneficiary

Create a beneficiary for use in payouts. The response provides a unique beneficiary ID, which you can use in place of the Beneficiary object for Create Payout. This method triggers the Beneficiary Created webhook. This webhook contains the same information as the response. Note: In addition to the required fields documented below, you must include all other beneficiary fields listed in the response to Get Payout Required Fields, and you must conform to the regex provided. To create a beneficiary that you can use with multiple payout methods, include all fields that are required by each payout method. The client is responsible for including all required fields.

- HTTP Method: `POST`
- Endpoint: `/v1/payouts/beneficiary`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | `[PayoutsBeneficiaryBody](../models/PayoutsBeneficiaryBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_13`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PayoutsBeneficiaryBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PayoutsBeneficiaryBody(
    category="bank",
    company_name="ABC",
    country="GB",
    currency="GBP",
    default_payout_method_type="us_general_bank",
    entity_type="company",
    first_name="John",
    identification_type="drivers_license",
    identification_value="ABNHDLK354665",
    last_name="John",
    merchant_reference_id="GHY-0YU-HUJ-POI"
)

result = sdk.disburse.create_beneficiary(request_body=request_body)

print(result)
```

## validate_beneficiary

Validate the format of the details for a payout beneficiary. You can validate a beneficiary multiple times for different payout methods. You can enter a Beneficiary object or a previously created beneficiary ID. Note: In addition to the required fields for Create Beneficiary, the Beneficiary object must include all required fields for the beneficiary listed in the response to Get Payout Required Fields. The examples include additional fields for the 'us_ach_bank' payout method.

- HTTP Method: `POST`
- Endpoint: `/v1/payouts/beneficiary/validate`

**Parameters**

| Name         | Type                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------- | :------- | :---------------- |
| request_body | `[BeneficiaryValidateBody](../models/BeneficiaryValidateBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_14`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import BeneficiaryValidateBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = BeneficiaryValidateBody(
    amount=4.29,
    beneficiary="Duis c",
    identifier_type="identifier_type",
    identifier_value="identifier_value",
    payout_method_type="us_general_bank",
    sender_country="GB",
    sender_currency="GBP",
    sender_entity_type="company"
)

result = sdk.disburse.validate_beneficiary(request_body=request_body)

print(result)
```

## get_beneficiary

Retrieve details of a payout beneficiary. Note: The 'Retrieve Beneficiary - individual' response includes additional fields for the 'ca_general_bank' payout method. The 'Retrieve Beneficiary - company' response includes additional fields for the 'us_ach_bank' payout method.

- HTTP Method: `GET`
- Endpoint: `/v1/payouts/beneficiary/{beneficiaryId}`

**Parameters**

| Name           | Type  | Required | Description                                                         |
| :------------- | :---- | :------- | :------------------------------------------------------------------ |
| beneficiary_id | `str` | ✅       | ID of the 'beneficiary' object. String starting with beneficiary\_. |

**Return Type**

`InlineResponse200_13`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.get_beneficiary(beneficiary_id="beneficiaryId")

print(result)
```

## delete_beneficiary

Delete a payout beneficiary from the Rapyd platform.

- HTTP Method: `DELETE`
- Endpoint: `/v1/payouts/beneficiary/{beneficiaryId}`

**Parameters**

| Name           | Type  | Required | Description                                                         |
| :------------- | :---- | :------- | :------------------------------------------------------------------ |
| beneficiary_id | `str` | ✅       | ID of the 'beneficiary' object. String starting with beneficiary\_. |

**Return Type**

`InlineResponse200_15`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.delete_beneficiary(beneficiary_id="beneficiaryId")

print(result)
```

## simulate_complete_payout

- HTTP Method: `POST`
- Endpoint: `/v1/payouts/complete/{payoutToken}/{amount}`

**Parameters**

| Name         | Type  | Required | Description                                                                                                                        |
| :----------- | :---- | :------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| payout_token | `str` | ✅       | ID of the payout. String starting with 'payout\_'.                                                                                 |
| amount       | `str` | ✅       | The payout amount. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. |

**Return Type**

`InlineResponse200_12`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.simulate_complete_payout(
    payout_token="payoutToken",
    amount="amount"
)

print(result)
```

## confirm_payout

- HTTP Method: `POST`
- Endpoint: `/v1/payouts/confirm/{payoutToken}`

**Parameters**

| Name         | Type  | Required | Description                                        |
| :----------- | :---- | :------- | :------------------------------------------------- |
| payout_token | `str` | ✅       | ID of the payout. String starting with 'payout\_'. |

**Return Type**

`InlineResponse200_12`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.confirm_payout(payout_token="payoutToken")

print(result)
```

## create_sender

Create a sender for use in payouts. The response provides a unique sender ID, which you can use in place of the sender object for Create Payout. Note: In addition to the required fields documented below, you must include all other sender fields listed in the response to Get Payout Required Fields, and you must conform to the regex provided. To create a sender that you can use with multiple payout methods, include all fields that are required by each payout method. The client is responsible for including all required fields.

- HTTP Method: `POST`
- Endpoint: `/v1/payouts/sender`

**Parameters**

| Name         | Type                                                  | Required | Description       |
| :----------- | :---------------------------------------------------- | :------- | :---------------- |
| request_body | `[PayoutsSenderBody](../models/PayoutsSenderBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_16`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PayoutsSenderBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PayoutsSenderBody(
    company_name="ABC",
    country="GB",
    currency="GBP",
    entity_type="company",
    first_name="Scott",
    identification_type="drivers_license",
    identification_value="ANDSFS8974562",
    last_name="Williams"
)

result = sdk.disburse.create_sender(request_body=request_body)

print(result)
```

## get_payer

Note: The Retrieve Sender - individual response includes additional fields for the ca_general_bank payout method. The Retrieve Sender - company response includes an additional field for the us_ach_bank payout method.

- HTTP Method: `GET`
- Endpoint: `/v1/payouts/sender/{senderId}`

**Parameters**

| Name      | Type  | Required | Description                                               |
| :-------- | :---- | :------- | :-------------------------------------------------------- |
| sender_id | `str` | ✅       | ID of the Sender object. String starting with 'sender\_'. |

**Return Type**

`InlineResponse200_16`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.get_payer(sender_id="senderId")

print(result)
```

## delete_payer

Delete a payout sender from the Rapyd platform.

- HTTP Method: `DELETE`
- Endpoint: `/v1/payouts/sender/{senderId}`

**Parameters**

| Name      | Type  | Required | Description                                               |
| :-------- | :---- | :------- | :-------------------------------------------------------- |
| sender_id | `str` | ✅       | ID of the 'sender' object. String starting with sender\_. |

**Return Type**

`InlineResponse200_17`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.delete_payer(sender_id="senderId")

print(result)
```

## get_payout_method_types

Retrieve a list of payout method types that you can use when creating a payout. The response contains a list of objects. Each object includes a payout method type and its attributes.

- HTTP Method: `GET`
- Endpoint: `/v1/payout_methods`

**Parameters**

| Name                    | Type   | Required | Description                                                                                                                                                                                                                        |
| :---------------------- | :----- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sender_entity_type      | `str`  | ❌       | Filters the type of entity for the payer. One of the following: individual, company                                                                                                                                                |
| beneficiary_country     | `str`  | ❌       | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code.                                                                                                                                                                    |
| payout_currency         | `str`  | ❌       | Currency received by the beneficiary. Three-letter ISO 4217 code.                                                                                                                                                                  |
| sender_currency         | `str`  | ❌       | Currency that the sender is paying with. Three-letter ISO 4217 code.                                                                                                                                                               |
| sender_country          | `str`  | ❌       | Country of the sender. Two-letter ISO 3166-1 ALPHA-2 code. Note: This field does not appear in the response.                                                                                                                       |
| beneficiary_entity_type | `str`  | ❌       | Filters the type of entity for the beneficiary. One of the following: individual, company                                                                                                                                          |
| category                | `str`  | ❌       | The category of payout method. One of the following: bank, card, cash, rapyd_ewallet, ewallet                                                                                                                                      |
| is_cancelable           | `bool` | ❌       | Indicates whether the payout can be canceled. Relevant when category is cash.                                                                                                                                                      |
| is_location_specific    | `bool` | ❌       | Indicates whether the payout must be made at a specific physical location. Relevant when category is cash.                                                                                                                         |
| is_expirable            | `bool` | ❌       | Indicates whether the payout expires if not completed. Relevant when category is cash.                                                                                                                                             |
| starting_after          | `str`  | ❌       | The name of a payout method in the list. The list begins with the record that was created next after the record with this payout method. Use this filter to get the next page of results. Relevant when ending_before is not used. |
| ending_before           | `str`  | ❌       | The name of a payout method in the list. The list ends with the last record that was created before the record with this payout method. Use this filter to get the previous page of results.                                       |
| limit                   | `str`  | ❌       | The maximum number of payout methods to return. Range: 1-100. Default is 10.                                                                                                                                                       |

**Return Type**

`InlineResponse200_18`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.get_payout_method_types(
    sender_entity_type="sender_entity_type",
    beneficiary_country="beneficiary_country",
    payout_currency="payout_currency",
    sender_currency="sender_currency",
    sender_country="sender_country",
    beneficiary_entity_type="beneficiary_entity_type",
    category="category",
    is_cancelable=True,
    is_location_specific=True,
    is_expirable=False,
    starting_after="starting_after",
    ending_before="ending_before",
    limit="limit"
)

print(result)
```

## get_payout

Retrieve the details of a payout.

- HTTP Method: `GET`
- Endpoint: `/v1/payouts/{payoutId}`

**Parameters**

| Name      | Type  | Required | Description                                        |
| :-------- | :---- | :------- | :------------------------------------------------- |
| payout_id | `str` | ✅       | ID of the payout. String starting with 'payout\_'. |

**Return Type**

`InlineResponse200_12`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.get_payout(payout_id="payoutId")

print(result)
```

## update_payout

Change or modify a payout. This method triggers the Payout Updated webhook. This webhook contains the same information as the response.

- HTTP Method: `POST`
- Endpoint: `/v1/payouts/{payoutId}`

**Parameters**

| Name         | Type                                                      | Required | Description                                      |
| :----------- | :-------------------------------------------------------- | :------- | :----------------------------------------------- |
| request_body | `[PayoutsPayoutIdBody](../models/PayoutsPayoutIdBody.md)` | ✅       | The request body.                                |
| payout_id    | `str`                                                     | ✅       | ID of the payout. String starting with payout\_. |

**Return Type**

`InlineResponse200_12`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PayoutsPayoutIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PayoutsPayoutIdBody(
    description="description",
    metadata={}
)

result = sdk.disburse.update_payout(
    request_body=request_body,
    payout_id="payoutId"
)

print(result)
```

## cancel_payout

The payout can be canceled unless its status is confirmation or completed. This method triggers the Payout Canceled webhook. This webhook contains the same information as the response.

- HTTP Method: `DELETE`
- Endpoint: `/v1/payouts/{payoutId}`

**Parameters**

| Name      | Type  | Required | Description                                      |
| :-------- | :---- | :------- | :----------------------------------------------- |
| payout_id | `str` | ✅       | ID of the payout. String starting with payout\_. |

**Return Type**

`InlineResponse200_12`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.cancel_payout(payout_id="payoutId")

print(result)
```
