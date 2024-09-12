```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_subscription_item.usage_record_summaries(
    subscription_item_id="subscriptionItemId",
    limit=4.1,
    ending_before=9.52,
    starting_after=0.05
)

print(result)

```
