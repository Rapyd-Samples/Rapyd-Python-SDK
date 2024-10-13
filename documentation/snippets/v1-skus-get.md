```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.sku.list_sku(
    active=False,
    starting_after=9.83,
    ending_before=3.58,
    limit=3.06
)

print(result)

```
