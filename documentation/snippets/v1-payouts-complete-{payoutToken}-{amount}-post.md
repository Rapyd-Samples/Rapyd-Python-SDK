```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.simulate_complete_payout(
    payout_token="payoutToken",
    amount="amount"
)

print(result)

```
