```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PaymentsGroupPaymentsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PaymentsGroupPaymentsBody(
    description="description",
    merchant_reference_id="merchant_reference_id",
    metadata={},
    payments={}
)

result = sdk.group_payment.create_group_payment(request_body=request_body)

print(result)

```
