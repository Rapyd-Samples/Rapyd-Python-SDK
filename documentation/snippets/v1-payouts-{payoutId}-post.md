```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PayoutsPayoutIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PayoutsPayoutIdBody(
    description="description",
    metadata={}
)

result = sdk.disburse.update_payout(
    request_body=request_body,
    payout_id="payoutId"
)

print(result)

```
