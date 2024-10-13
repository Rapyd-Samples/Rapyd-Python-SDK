```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription.get_subscription_list(
    billing="billing",
    customer="customer",
    status="status",
    product="product",
    starting_after="starting_after",
    ending_before="ending_before",
    limit="limit"
)

print(result)

```
