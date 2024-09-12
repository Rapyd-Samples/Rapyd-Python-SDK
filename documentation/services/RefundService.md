# RefundService

A list of all methods in the `RefundService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                                                                                                                                                                                                                                                                                                                                     |
| :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [all_refunds](#all_refunds)                                 | Retrieve a list of all refunds.                                                                                                                                                                                                                                                                                                                                                 |
| [request_total_create_refund](#request_total_create_refund) | Refund of a payment. The refund is credited against a specific payment. The money is returned to the payment method that was used for the payment, and the currency is the same as what was used in the payment. If the action of a third party is not required, this method triggers the Refund Completed webhook. This webhook contains the same information as the response. |
| [simulate_complete_refund](#simulate_complete_refund)       | Simulate the action of a third party that is required for completing the refund process. Relevant to sandbox. Use this method when a payment was made with a payment method such as cash, bank redirect or bank transfer, and the payment was completed by an action taken by the customer.                                                                                     |
| [refund_group_payment](#refund_group_payment)               | Refund a group payment when the status of the group payment is closed. The refund is credited against a specific group payment. The money is returned to the payment methods that were used for the payment. If the action of a third party is not required, this method triggers the Refund Completed webhook for each payment method.                                         |
| [refund_by_token](#refund_by_token)                         | Retrieve the details of a refund object.                                                                                                                                                                                                                                                                                                                                        |
| [update_refund](#update_refund)                             | Change or modify the metadata in a refund object.                                                                                                                                                                                                                                                                                                                               |

## all_refunds

Retrieve a list of all refunds.

- HTTP Method: `GET`
- Endpoint: `/v1/refunds`

**Parameters**

| Name           | Type  | Required | Description                                                                                               |
| :------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------- |
| ending_before  | `str` | ❌       | The ID of the refund created after the last refund you want to retrieve. String starting with refund\_.   |
| limit          | `str` | ❌       | The maximum number of refunds to return. Range, 1-100. Default is 10.                                     |
| starting_after | `str` | ❌       | The ID of the refund created before the first refund you want to retrieve. String starting with refund\_. |

**Return Type**

`InlineResponse200_63`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.refund.all_refunds(
    ending_before="ending_before",
    limit="limit",
    starting_after="starting_after"
)

print(result)
```

## request_total_create_refund

Refund of a payment. The refund is credited against a specific payment. The money is returned to the payment method that was used for the payment, and the currency is the same as what was used in the payment. If the action of a third party is not required, this method triggers the Refund Completed webhook. This webhook contains the same information as the response.

- HTTP Method: `POST`
- Endpoint: `/v1/refunds`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | `[V1RefundsBody](../models/V1RefundsBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_64`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1RefundsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1RefundsBody(
    amount=1.28,
    currency="currency",
    ewallets=[
        "ewallets"
    ],
    merchant_reference_id="merchant_reference_id",
    metadata={},
    payment="payment",
    reason="reason"
)

result = sdk.refund.request_total_create_refund(request_body=request_body)

print(result)
```

## simulate_complete_refund

Simulate the action of a third party that is required for completing the refund process. Relevant to sandbox. Use this method when a payment was made with a payment method such as cash, bank redirect or bank transfer, and the payment was completed by an action taken by the customer.

- HTTP Method: `POST`
- Endpoint: `/v1/refunds/complete`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | `[RefundsCompleteBody](../models/RefundsCompleteBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_64`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import RefundsCompleteBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RefundsCompleteBody(
    token="token"
)

result = sdk.refund.simulate_complete_refund(request_body=request_body)

print(result)
```

## refund_group_payment

Refund a group payment when the status of the group payment is closed. The refund is credited against a specific group payment. The money is returned to the payment methods that were used for the payment. If the action of a third party is not required, this method triggers the Refund Completed webhook for each payment method.

- HTTP Method: `POST`
- Endpoint: `/v1/refunds/group_payments`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | `[RefundsGroupPaymentsBody](../models/RefundsGroupPaymentsBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_65`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import RefundsGroupPaymentsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RefundsGroupPaymentsBody(
    amount=3.98,
    group_payment="group_payment"
)

result = sdk.refund.refund_group_payment(request_body=request_body)

print(result)
```

## refund_by_token

Retrieve the details of a refund object.

- HTTP Method: `GET`
- Endpoint: `/v1/refunds/{refundId}`

**Parameters**

| Name      | Type  | Required | Description                                                                    |
| :-------- | :---- | :------- | :----------------------------------------------------------------------------- |
| refund_id | `str` | ✅       | ID of the 'refund' object you want to retrieve. String starting with refund\_. |

**Return Type**

`InlineResponse200_64`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.refund.refund_by_token(refund_id="refundId")

print(result)
```

## update_refund

Change or modify the metadata in a refund object.

- HTTP Method: `POST`
- Endpoint: `/v1/refunds/{refundId}`

**Parameters**

| Name         | Type                                                      | Required | Description                                                                    |
| :----------- | :-------------------------------------------------------- | :------- | :----------------------------------------------------------------------------- |
| request_body | `[RefundsRefundIdBody](../models/RefundsRefundIdBody.md)` | ✅       | The request body.                                                              |
| refund_id    | `str`                                                     | ✅       | ID of the 'refund' object you want to retrieve. String starting with refund\_. |

**Return Type**

`InlineResponse200_64`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import RefundsRefundIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RefundsRefundIdBody(
    metadata=""
)

result = sdk.refund.update_refund(
    request_body=request_body,
    refund_id="refundId"
)

print(result)
```
