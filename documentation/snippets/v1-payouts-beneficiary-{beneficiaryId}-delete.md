```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.delete_beneficiary(beneficiary_id="beneficiaryId")

print(result)

```
