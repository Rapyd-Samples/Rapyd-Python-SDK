```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1SubscriptionItemsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1SubscriptionItemsBody(
    metadata={},
    plan="plan",
    prorate=False,
    proration_date=9.19,
    quantity=6.81,
    subscription="subscription"
)

result = sdk.subscription_subscription_item.create_subscription_item(request_body=request_body)

print(result)

```
