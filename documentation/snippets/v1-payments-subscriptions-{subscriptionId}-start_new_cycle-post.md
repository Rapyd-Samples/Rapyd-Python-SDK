```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription.simulate_start_new_cycle(subscription_id="subscriptionId")

print(result)

```
