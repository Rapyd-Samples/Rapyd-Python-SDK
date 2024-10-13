```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import SkusSkuIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SkusSkuIdBody(
    currency="GBP",
    inventory={
        "type_": "finite",
        "quantity": 5,
        "value": "in_stock"
    },
    price=3.69,
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

result = sdk.sku.update_sku(
    request_body=request_body,
    sku_id="skuId"
)

print(result)

```
