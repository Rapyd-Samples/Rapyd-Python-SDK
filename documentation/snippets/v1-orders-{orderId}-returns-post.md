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
