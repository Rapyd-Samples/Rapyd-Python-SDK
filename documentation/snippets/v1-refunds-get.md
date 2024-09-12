```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.refund.all_refunds(
    ending_before="ending_before",
    limit="limit",
    starting_after="starting_after"
)

print(result)

```
