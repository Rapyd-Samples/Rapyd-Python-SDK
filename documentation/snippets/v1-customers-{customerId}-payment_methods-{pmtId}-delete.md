```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer_payment_method.delete_customer_payment_method(
    customer_id="customerId",
    pmt_id="pmtId"
)

print(result)

```
