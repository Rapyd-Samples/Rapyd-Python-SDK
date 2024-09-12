```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1RefundsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1RefundsBody(
    amount=1.28,
    currency="currency",
    ewallets=[
        "ewallets"
    ],
    merchant_reference_id="merchant_reference_id",
    metadata={},
    payment="payment",
    reason="reason"
)

result = sdk.refund.request_total_create_refund(request_body=request_body)

print(result)

```
