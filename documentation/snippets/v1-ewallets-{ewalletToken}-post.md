```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import EwalletsEwalletTokenBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = EwalletsEwalletTokenBody(
    ewallet_reference_id="ewallet_reference_id",
    first_name="first_name",
    last_name="last_name",
    metadata={}
)

result = sdk.e_wallets.updated_user(
    request_body=request_body,
    ewallet_token="ewalletToken"
)

print(result)

```
