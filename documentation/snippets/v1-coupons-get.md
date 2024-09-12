```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.coupon.list_coupon(
    starting_after="starting_after",
    ending_before="ending_before",
    limit="1"
)

print(result)

```
