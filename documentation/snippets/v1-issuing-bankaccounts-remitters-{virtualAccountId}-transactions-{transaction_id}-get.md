```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.issuing.get_remitter_details(
    virtual_account_id="virtualAccountId",
    transaction_id="transaction_id"
)

print(result)

```
