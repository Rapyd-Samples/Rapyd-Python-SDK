```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.sku.list_sku(
    active=False,
    starting_after=9.68,
    ending_before=5.31,
    limit=1.17
)

print(result)

```
