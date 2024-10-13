```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_plan.delete_plan(plan_id_1="plan_id")

print(result)

```
