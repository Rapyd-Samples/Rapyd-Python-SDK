```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.issuing.retrieve_issuing_by_rapyd_token(virtual_account_id="virtualAccountId")

print(result)

```
