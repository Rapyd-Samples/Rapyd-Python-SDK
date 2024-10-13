```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1SkusBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1SkusBody(
    currency="GBP",
    inventory={
        "type_": "finite",
        "quantity": 5,
        "value": "in_stock"
    },
    price=2.67,
    product="product",
    active=False,
    attributes=[
        "attributes"
    ],
    image="image",
    metadata={},
    package_dimensions={
        "length": 4.84,
        "height": 8.35,
        "weight": 1.01,
        "width": 7.9
    }
)

result = sdk.sku.create_sku(request_body=request_body)

print(result)

```
