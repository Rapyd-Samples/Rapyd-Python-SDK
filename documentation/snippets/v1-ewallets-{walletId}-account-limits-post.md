```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import AccountLimitsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AccountLimitsBody(
    account_id="account_id",
    amount="amount",
    currency="currency",
    type_="type"
)

result = sdk.e_wallets.set_account_limit(
    request_body=request_body,
    wallet_id="walletId"
)

print(result)

```
