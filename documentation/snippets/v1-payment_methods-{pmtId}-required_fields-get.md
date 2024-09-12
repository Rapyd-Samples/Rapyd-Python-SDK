```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.payment_method_type.get_payment_method_type_required_fields(pmt_id="pmtId")

print(result)

```
