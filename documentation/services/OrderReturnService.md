# OrderReturnService

A list of all methods in the `OrderReturnService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                                                 |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------ |
| [returns_order](#returns_order)                 | Make a return against an order. The maximum amount of the return is the amount of the order |
| [list_order_return](#list_order_return)         | Retrieve a list of all order returns.                                                       |
| [retrieve_order_return](#retrieve_order_return) | Retrieve the details of a return.                                                           |

## returns_order

Make a return against an order. The maximum amount of the return is the amount of the order

- HTTP Method: `POST`
- Endpoint: `/v1/orders/{orderId}/returns`

**Parameters**

| Name         | Type                                                  | Required | Description                                    |
| :----------- | :---------------------------------------------------- | :------- | :--------------------------------------------- |
| request_body | [OrderIdReturnsBody](../models/OrderIdReturnsBody.md) | ✅       | The request body.                              |
| order_id     | str                                                   | ✅       | ID of the order. String starting with order\_. |

**Return Type**

`InlineResponse200_56`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import OrderIdReturnsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = OrderIdReturnsBody(
    order_id="order_id",
    items=[
        {
            "description": "description",
            "parent": "parent",
            "type_": "sku",
            "quantity": 8.5,
            "currency": "currency",
            "amount": 0.51,
            "order_id": "order_id"
        }
    ]
)

result = sdk.order_return.returns_order(
    request_body=request_body,
    order_id="orderId"
)

print(result)
```

## list_order_return

Retrieve a list of all order returns.

- HTTP Method: `GET`
- Endpoint: `/v1/order_returns`

**Parameters**

| Name           | Type      | Required | Description                                                                            |
| :------------- | :-------- | :------- | :------------------------------------------------------------------------------------- |
| limit          | str       | ❌       | The maximum number of returns to list. Range - 1-100. Default is 10.                   |
| ending_before  | str       | ❌       | The ID of the order created after the last order you want to retrieve a return from.   |
| starting_after | str       | ❌       | The ID of the order created before the first order you want to retrieve a return from. |
| tokens         | List[str] | ❌       | Filters the list for orders related to the specified order.                            |

**Return Type**

`InlineResponse200_57`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tokens=[
    "tokens"
]

result = sdk.order_return.list_order_return(
    limit="limit",
    ending_before="ending_before",
    starting_after="starting_after",
    tokens=tokens
)

print(result)
```

## retrieve_order_return

Retrieve the details of a return.

- HTTP Method: `GET`
- Endpoint: `/v1/order_returns/{orderReturnsId}`

**Parameters**

| Name             | Type | Required | Description                                        |
| :--------------- | :--- | :------- | :------------------------------------------------- |
| order_returns_id | str  | ✅       | ID of the return. String starting with **orre\_**. |

**Return Type**

`InlineResponse200_56`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.order_return.retrieve_order_return(order_returns_id="orderReturnsId")

print(result)
```
