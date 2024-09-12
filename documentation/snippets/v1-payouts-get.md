```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.list_payouts(
    beneficiary="beneficiary",
    created_after="created_after",
    created_before="created_before",
    ending_before="ending_before",
    ewallet="ewallet",
    limit="limit",
    merchant_reference_id="merchant_reference_id",
    payout_method_type="payout_method_type",
    sender="sender",
    sender_country="GB",
    sender_currency="GBP",
    starting_after="starting_after"
)

print(result)

```
