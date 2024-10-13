```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import SubscriptionItemsSubscriptionItemIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SubscriptionItemsSubscriptionItemIdBody(
    metadata={},
    prorate=True,
    proration_date=8.99,
    quantity=8.22
)

result = sdk.subscription_subscription_item.update_subscription_item(
    request_body=request_body,
    subscription_item_id="subscriptionItemId"
)

print(result)

```
