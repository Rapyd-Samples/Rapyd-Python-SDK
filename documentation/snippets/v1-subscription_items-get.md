```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_subscription_item.list_subscription_item(
    ending_before=0.01,
    limit=0.09,
    starting_after="starting_after",
    subscription="subscription"
)

print(result)

```
