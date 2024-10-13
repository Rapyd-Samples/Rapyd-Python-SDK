# OrderService

A list of all methods in the `OrderService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                                       |
| :-------------------------------- | :---------------------------------------------------------------- |
| [list_order](#list_order)         | Retrieve a list of all orders.                                    |
| [create_order](#create_order)     | Create an order for goods. For services, see Create Subscription. |
| [retrieve_order](#retrieve_order) | Retrieve the details of an order.                                 |
| [update_order](#update_order)     | Change or modify an order.                                        |
| [pay_order](#pay_order)           | Pay an order.                                                     |

## list_order

Retrieve a list of all orders.

- HTTP Method: `GET`
- Endpoint: `/v1/orders`

**Parameters**

| Name           | Type | Required | Description                                                              |
| :------------- | :--- | :------- | :----------------------------------------------------------------------- |
| limit          | str  | ❌       | The maximum number of orders to return. Range - 1-100. Default is 10.    |
| ending_before  | str  | ❌       | The ID of the order created after the last order you want to retrieve.   |
| starting_after | str  | ❌       | The ID of the order created before the first order you want to retrieve. |

**Return Type**

`InlineResponse200_54`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.order.list_order(
    limit="limit",
    ending_before="ending_before",
    starting_after="starting_after"
)

print(result)
```

## create_order

Create an order for goods. For services, see Create Subscription.

- HTTP Method: `POST`
- Endpoint: `/v1/orders`

**Parameters**

| Name         | Type                                      | Required | Description       |
| :----------- | :---------------------------------------- | :------- | :---------------- |
| request_body | [V1OrdersBody](../models/V1OrdersBody.md) | ❌       | The request body. |

**Return Type**

`InlineResponse200_55`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1OrdersBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1OrdersBody(
    coupon="coupon",
    customer="customer",
    currency="currency",
    email="email",
    items=[
        {
            "amount": "amount",
            "currency": "GBP",
            "description": "description",
            "parent": "parent",
            "type_": "shipping",
            "quantity": 2.7
        }
    ],
    metadata={},
    shipping_address={
        "canton": "canton",
        "city": "city",
        "country": "GB",
        "created_at": 8.2,
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
    tax_percent=2.68,
    upstream_id="upstream_id"
)

result = sdk.order.create_order(request_body=request_body)

print(result)
```

## retrieve_order

Retrieve the details of an order.

- HTTP Method: `GET`
- Endpoint: `/v1/orders/{orderId}`

**Parameters**

| Name     | Type | Required | Description                                        |
| :------- | :--- | :------- | :------------------------------------------------- |
| order_id | str  | ✅       | ID of the order. String starting with **order\_**. |

**Return Type**

`InlineResponse200_55`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.order.retrieve_order(order_id="orderId")

print(result)
```

## update_order

Change or modify an order.

- HTTP Method: `POST`
- Endpoint: `/v1/orders/{orderId}`

**Parameters**

| Name         | Type                                                | Required | Description                                        |
| :----------- | :-------------------------------------------------- | :------- | :------------------------------------------------- |
| request_body | [OrdersOrderIdBody](../models/OrdersOrderIdBody.md) | ✅       | The request body.                                  |
| order_id     | str                                                 | ✅       | ID of the order. String starting with **order\_**. |

**Return Type**

`InlineResponse200_55`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import OrdersOrderIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = OrdersOrderIdBody(
    coupon="coupon",
    metadata={},
    tax_percent=2.48,
    status="paid"
)

result = sdk.order.update_order(
    request_body=request_body,
    order_id="orderId"
)

print(result)
```

## pay_order

Pay an order.

- HTTP Method: `POST`
- Endpoint: `/v1/orders/{orderId}/pay`

**Parameters**

| Name         | Type                                          | Required | Description                                        |
| :----------- | :-------------------------------------------- | :------- | :------------------------------------------------- |
| request_body | [OrderIdPayBody](../models/OrderIdPayBody.md) | ✅       | The request body.                                  |
| order_id     | str                                           | ✅       | ID of the order. String starting with **order\_**. |

**Return Type**

`InlineResponse200_55`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import OrderIdPayBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = OrderIdPayBody(
    metadata={},
    payment_method="payment_method",
    customer="customer"
)

result = sdk.order.pay_order(
    request_body=request_body,
    order_id="orderId"
)

print(result)
```
