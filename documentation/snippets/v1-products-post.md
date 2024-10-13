```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1ProductsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1ProductsBody(
    active=True,
    attributes=[
        "attributes"
    ],
    description="description",
    id_="id",
    images=[
        "images"
    ],
    metadata={},
    name="name",
    package_dimensions={
        "height": 1.62,
        "length": 4.73,
        "weight": 6.81,
        "width": 0.63
    },
    shippable=False,
    statement_descriptor="statement_descriptor",
    type_="services",
    unit_label="unit_label"
)

result = sdk.subscription_product.create_product(request_body=request_body)

print(result)

```
