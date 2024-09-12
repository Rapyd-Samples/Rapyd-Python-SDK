```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.order.list_order(
    limit="limit",
    ending_before="ending_before",
    starting_after="starting_after"
)

print(result)

```
