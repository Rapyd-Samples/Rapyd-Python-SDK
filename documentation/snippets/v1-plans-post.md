```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1PlansBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1PlansBody(
    aggregate_usage="aggregate_usage",
    amount=0.54,
    billing_scheme="billing_scheme",
    currency="currency",
    id_="id",
    interval="interval",
    interval_count=5.88,
    metadata={},
    nickname="nickname",
    product="product",
    tiers="tiers",
    tiers_mode="tiers_mode",
    transform_usage={},
    trial_period_days=2.83,
    usage_type="usage_type"
)

result = sdk.subscription_plan.create_plan(request_body=request_body)

print(result)

```
