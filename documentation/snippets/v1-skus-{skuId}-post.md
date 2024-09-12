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
        "quantity": 9,
        "value": "in_stock"
    },
    price=3.63,
    product="product",
    active=True,
    attributes=[
        "attributes"
    ],
    image="image",
    metadata={},
    package_dimensions={
        "length": 3.17,
        "height": 6.46,
        "weight": 2.6,
        "width": 2.52
    }
)

result = sdk.sku.update_sku(
    request_body=request_body,
    sku_id="skuId"
)

print(result)

```
