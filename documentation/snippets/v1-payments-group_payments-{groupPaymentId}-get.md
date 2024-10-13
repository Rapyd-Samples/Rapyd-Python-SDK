```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.group_payment.retrieve_group_payment_id(group_payment_id="groupPaymentId")

print(result)

```
