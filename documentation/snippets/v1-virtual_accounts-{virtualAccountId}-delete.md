```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.virtual_accounts.close_issuing(virtual_account_id="virtualAccountId")

print(result)

```
