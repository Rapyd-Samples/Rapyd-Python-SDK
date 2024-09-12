```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import ProductsProductsIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ProductsProductsIdBody(
    active=False,
    attributes=[
        "attributes"
    ],
    metadata={},
    name="name",
    package_dimensions={
        "height": 5.88,
        "length": 3.28,
        "weight": 1.4,
        "width": 7.3
    },
    statement_descriptor="statement_descriptor",
    unit_label="unit_label"
)

result = sdk.subscription_product.update_product(
    request_body=request_body,
    products_id="products_id"
)

print(result)

```
