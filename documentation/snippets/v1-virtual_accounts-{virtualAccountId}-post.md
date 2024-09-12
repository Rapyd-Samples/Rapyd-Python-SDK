```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import VirtualAccountsVirtualAccountIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = VirtualAccountsVirtualAccountIdBody(
    requesting_currency="GBP"
)

result = sdk.virtual_accounts.update_issuing_by_rapyd_token(
    request_body=request_body,
    virtual_account_id="virtualAccountId"
)

print(result)

```
