```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1VirtualAccountsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1VirtualAccountsBody(
    country="country",
    currency="currency",
    description="description",
    ewallet="ewallet",
    merchant_reference_id="merchant_reference_id",
    metadata={},
    requested_currency="requested_currency"
)

result = sdk.virtual_accounts.create_virtual_account(request_body=request_body)

print(result)

```
