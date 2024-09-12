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
            "quantity": 9.55,
            "currency": "currency",
            "amount": 7.78,
            "order_id": "order_id"
        }
    ]
)

result = sdk.order.returns_order(
    request_body=request_body,
    order_id="orderId"
)

print(result)

```
