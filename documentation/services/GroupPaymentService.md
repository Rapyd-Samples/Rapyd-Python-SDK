# GroupPaymentService

A list of all methods in the `GroupPaymentService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                          |
| :------------------------------------------------------ | :----------------------------------- |
| [create_group_payment](#create_group_payment)           | Create a group payment.              |
| [retrieve_group_payment_id](#retrieve_group_payment_id) | Retrieve details of a group payment. |
| [deletegroup_payment_id](#deletegroup_payment_id)       | Cancel a group payment.              |

## create_group_payment

Create a group payment.

- HTTP Method: `POST`
- Endpoint: `/v1/payments/group_payments`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [PaymentsGroupPaymentsBody](../models/PaymentsGroupPaymentsBody.md) | ✅       | The request body. |

**Return Type**

`InlineResponse200_51`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PaymentsGroupPaymentsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PaymentsGroupPaymentsBody(
    description="description",
    merchant_reference_id="merchant_reference_id",
    metadata={},
    payments={}
)

result = sdk.group_payment.create_group_payment(request_body=request_body)

print(result)
```

## retrieve_group_payment_id

Retrieve details of a group payment.

- HTTP Method: `GET`
- Endpoint: `/v1/payments/group_payments/{groupPaymentId}`

**Parameters**

| Name             | Type | Required | Description                                            |
| :--------------- | :--- | :------- | :----------------------------------------------------- |
| group_payment_id | str  | ✅       | ID of the group payment. String starting with **gp\_** |

**Return Type**

`InlineResponse200_51`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.group_payment.retrieve_group_payment_id(group_payment_id="groupPaymentId")

print(result)
```

## deletegroup_payment_id

Cancel a group payment.

- HTTP Method: `DELETE`
- Endpoint: `/v1/payments/group_payments/{groupPaymentId}`

**Parameters**

| Name             | Type | Required | Description                                            |
| :--------------- | :--- | :------- | :----------------------------------------------------- |
| group_payment_id | str  | ✅       | ID of the group payment. String starting with **gp\_** |

**Return Type**

`InlineResponse200_51`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.group_payment.deletegroup_payment_id(group_payment_id="groupPaymentId")

print(result)
```
