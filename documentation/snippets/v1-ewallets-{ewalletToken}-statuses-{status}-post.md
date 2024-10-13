```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import UpdateEwalletStatusStatus

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.update_ewallet_status(
    ewallet_token="ewalletToken",
    status="ACT"
)

print(result)

```
