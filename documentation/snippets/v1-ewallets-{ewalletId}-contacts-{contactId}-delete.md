```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.delete_ewallet_contact(
    ewallet_id="ewalletId",
    contact_id="contactId"
)

print(result)

```
