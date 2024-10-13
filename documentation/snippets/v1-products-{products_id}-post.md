```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import SubscriptionProductUpdateProductRequest2

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SubscriptionProductUpdateProductRequest2(
    active=True,
    attributes=[
        "attributes"
    ],
    metadata={},
    name="name",
    package_dimensions={
        "height": 8.98,
        "length": 1.11,
        "weight": 6.53,
        "width": 2.25
    },
    statement_descriptor="statement_descriptor",
    unit_label="unit_label"
)

result = sdk.subscription_product.update_product(
    request_body=request_body,
    products_id_1="products_id"
)

print(result)

```
