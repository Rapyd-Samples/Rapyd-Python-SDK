```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import EscrowEscrowReleasesBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = EscrowEscrowReleasesBody(
    ewallets={
        "ewallet": "ewallet",
        "amount": 2.94,
        "percentage": 0.49
    }
)

result = sdk.escrow.release_funds_from_escrow(
    request_body=request_body,
    payment="payment",
    escrow="escrow"
)

print(result)

```
