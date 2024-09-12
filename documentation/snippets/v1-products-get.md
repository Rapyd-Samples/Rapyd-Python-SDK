```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_product.get_products_list(
    ending_before=2.82,
    limit=9.32,
    starting_after="starting_after"
)

print(result)

```
