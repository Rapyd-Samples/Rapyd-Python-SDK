```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_ewallet_contact_compliance_levels(
    ewallet_id="ewalletId",
    contact_id="contactId"
)

print(result)

```
