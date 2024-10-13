# PaymentLinkService

A list of all methods in the `PaymentLinkService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                                                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [payment_link](#payment_link)               | Retrieve details of a payment link.                                                                                                                                                                                                                                                                                                                                                     |
| [create_payment_link](#create_payment_link) | Creates a reusable link for a hosted payment page. <BR> A customer can use the link and the hosted payment page multiple times. After providing required information, the customer is redirected seamlessly to a Rapyd Checkout page to complete the payment.You can create the link for everyone or for a specific customer. You can make the payment amount fixed, editable, or open. |

## payment_link

Retrieve details of a payment link.

- HTTP Method: `GET`
- Endpoint: `/v1/hosted/collect/payments/{paymentLink}`

**Parameters**

| Name         | Type | Required | Description                                                 |
| :----------- | :--- | :------- | :---------------------------------------------------------- |
| payment_link | str  | ✅       | ID of the payment link. String starting with **hp*reuse***. |

**Return Type**

`InlineResponse200_60`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.payment_link.payment_link(payment_link="paymentLink")

print(result)
```

## create_payment_link

Creates a reusable link for a hosted payment page. <BR> A customer can use the link and the hosted payment page multiple times. After providing required information, the customer is redirected seamlessly to a Rapyd Checkout page to complete the payment.You can create the link for everyone or for a specific customer. You can make the payment amount fixed, editable, or open.

- HTTP Method: `POST`
- Endpoint: `/v1/hosted/collect/payments/`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [CollectPaymentsBody](../models/CollectPaymentsBody.md) | ❌       | The request body. |

**Return Type**

`InlineResponse200_60`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CollectPaymentsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CollectPaymentsBody(
    amount="amount",
    amount_is_editable=False,
    checkout={},
    country="country",
    currency="currency",
    customer="customer",
    fixed_side="buy",
    language="en",
    max_payments=7,
    merchant_reference_id="merchant_reference_id",
    requested_currency="requested_currency"
)

result = sdk.payment_link.create_payment_link(request_body=request_body)

print(result)
```
