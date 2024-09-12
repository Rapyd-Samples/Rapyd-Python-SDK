```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PlansPlanIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PlansPlanIdBody(
    metadata={},
    nickname="nickname"
)

result = sdk.subscription_plan.update_plan(
    request_body=request_body,
    plan_id="plan_id"
)

print(result)

```
