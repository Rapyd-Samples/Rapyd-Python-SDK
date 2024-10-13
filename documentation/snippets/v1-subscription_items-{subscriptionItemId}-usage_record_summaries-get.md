```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_subscription_item.usage_record_summaries(
    subscription_item_id="subscriptionItemId",
    limit=3.23,
    ending_before=6.55,
    starting_after=4.66
)

print(result)

```
