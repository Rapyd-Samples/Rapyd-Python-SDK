```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import TransferResponseBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = TransferResponseBody(
    id_="id",
    metadata={},
    status="status"
)

result = sdk.e_wallets.set_funds_transfer_response(request_body=request_body)

print(result)

```
