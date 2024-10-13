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
