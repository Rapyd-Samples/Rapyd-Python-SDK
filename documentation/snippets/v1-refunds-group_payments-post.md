```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import RefundsGroupPaymentsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RefundsGroupPaymentsBody(
    amount=1.08,
    group_payment="group_payment"
)

result = sdk.refund.refund_group_payment(request_body=request_body)

print(result)

```
