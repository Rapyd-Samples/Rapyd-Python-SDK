```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import BankaccountsVirtualAccountIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = BankaccountsVirtualAccountIdBody(
    requesting_currency="TTD"
)

result = sdk.issuing.update_receiving_currency(
    request_body=request_body,
    virtual_account_id="virtualAccountId"
)

print(result)

```
