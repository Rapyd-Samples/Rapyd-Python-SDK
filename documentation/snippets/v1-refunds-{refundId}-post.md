```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import RefundsRefundIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RefundsRefundIdBody(
    metadata=""
)

result = sdk.refund.update_refund(
    request_body=request_body,
    refund_id="refundId"
)

print(result)

```
