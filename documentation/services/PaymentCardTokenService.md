# PaymentCardTokenService

A list of all methods in the `PaymentCardTokenService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                                                                                                                                                 |
| :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_card_token](#create_card_token) | Create a hosted page for a customer to save card details and manage cards. Prerequisite: [Create Customer](https://docs.rapyd.net/en/create-customer.html). |

## create_card_token

Create a hosted page for a customer to save card details and manage cards. Prerequisite: [Create Customer](https://docs.rapyd.net/en/create-customer.html).

- HTTP Method: `POST`
- Endpoint: `/v1/hosted/collect/card/`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [CollectCardBody](../models/CollectCardBody.md) | ❌       | The request body. |

**Return Type**

`InlineResponse200_61`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CollectCardBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CollectCardBody(
    billing_address_collect=False,
    cancel_url="cancel_url",
    card_fields={
        "recurrence_type": "unscheduled"
    },
    complete_url="complete_url",
    complete_payment_url="complete_payment_url",
    country="country",
    currency="currency",
    customer="customer",
    error_payment_url="error_payment_url",
    language="en",
    page_expiration="page_expiration",
    payment_method_type="payment_method_type"
)

result = sdk.payment_card_token.create_card_token(request_body=request_body)

print(result)
```
