```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import AccountTransferBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AccountTransferBody(
    amount=8.08,
    currency="currency",
    destination_ewallet="destination_ewallet",
    expiration="expiration",
    metadata={},
    source_ewallet="source_ewallet"
)

result = sdk.e_wallets.funds_transfer(request_body=request_body)

print(result)

```
