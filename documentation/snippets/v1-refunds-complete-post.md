```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import RefundsCompleteBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RefundsCompleteBody(
    token="token"
)

result = sdk.refund.simulate_complete_refund(request_body=request_body)

print(result)

```
