```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer.list_customer(
    starting_after="starting_after",
    ending_before="ending_before",
    limit="5"
)

print(result)

```
