# EscrowService

A list of all methods in the `EscrowService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                       |
| :------------------------------------------------------ | :---------------------------------------------------------------- |
| [list_escrow_releases](#list_escrow_releases)           | Retrieve a list of all releases of funds from a specified escrow. |
| [release_funds_from_escrow](#release_funds_from_escrow) | Retrieve a list of all releases of funds from a specified escrow. |
| [get_escrow](#get_escrow)                               | Retrieve details of the escrow for a payment.                     |

## list_escrow_releases

Retrieve a list of all releases of funds from a specified escrow.

- HTTP Method: `GET`
- Endpoint: `/v1/payments/{payment}/escrows/{escrow}/escrow_releases`

**Parameters**

| Name    | Type | Required | Description                                            |
| :------ | :--- | :------- | :----------------------------------------------------- |
| payment | str  | ✅       | ID of the payment. String starting with **payment\_**. |
| escrow  | str  | ✅       | ID of the escrow. String starting with **escrow\_**.   |

**Return Type**

`InlineResponse200_49`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.escrow.list_escrow_releases(
    payment="payment",
    escrow="escrow"
)

print(result)
```

## release_funds_from_escrow

Retrieve a list of all releases of funds from a specified escrow.

- HTTP Method: `POST`
- Endpoint: `/v1/payments/{payment}/escrows/{escrow}/escrow_releases`

**Parameters**

| Name         | Type                                                              | Required | Description                                            |
| :----------- | :---------------------------------------------------------------- | :------- | :----------------------------------------------------- |
| request_body | [EscrowEscrowReleasesBody](../models/EscrowEscrowReleasesBody.md) | ❌       | The request body.                                      |
| payment      | str                                                               | ✅       | ID of the payment. String starting with **payment\_**. |
| escrow       | str                                                               | ✅       | ID of the escrow. String starting with **escrow\_**.   |

**Return Type**

`InlineResponse200_50`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import EscrowEscrowReleasesBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = EscrowEscrowReleasesBody(
    ewallets={
        "ewallet": "ewallet",
        "amount": 2.94,
        "percentage": 0.49
    }
)

result = sdk.escrow.release_funds_from_escrow(
    request_body=request_body,
    payment="payment",
    escrow="escrow"
)

print(result)
```

## get_escrow

Retrieve details of the escrow for a payment.

- HTTP Method: `GET`
- Endpoint: `/v1/payments/{payment}/escrows/{escrow}`

**Parameters**

| Name    | Type | Required | Description                                            |
| :------ | :--- | :------- | :----------------------------------------------------- |
| payment | str  | ✅       | ID of the payment. String starting with **payment\_**. |
| escrow  | str  | ✅       | ID of the escrow. String starting with **escrow\_**.   |

**Return Type**

`InlineResponse200_49`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.escrow.get_escrow(
    payment="payment",
    escrow="escrow"
)

print(result)
```
