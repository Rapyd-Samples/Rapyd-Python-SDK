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
        "height": 1.62,
        "length": 4.73,
        "weight": 6.81,
        "width": 0.63
    },
    statement_descriptor="statement_descriptor",
    unit_label="unit_label"
)

result = sdk.subscription_product.update_product(
    request_body=request_body,
    products_id="productsId"
)

print(result)

```
