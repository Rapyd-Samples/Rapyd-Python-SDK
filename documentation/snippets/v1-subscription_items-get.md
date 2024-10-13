```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_subscription_item.list_subscription_item(
    ending_before=0.05,
    limit=7.77,
    starting_after="starting_after",
    subscription="subscription"
)

print(result)

```
