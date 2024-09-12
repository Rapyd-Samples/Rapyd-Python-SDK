```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import SubscriptionItemIdUsageRecordsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SubscriptionItemIdUsageRecordsBody(
    action="action",
    metadata={},
    quantity=0.99,
    timestamp=7.16
)

result = sdk.subscription_subscription_item.create_subscription_item_usage_record(
    request_body=request_body,
    subscription_item_id="subscriptionItemId"
)

print(result)

```
