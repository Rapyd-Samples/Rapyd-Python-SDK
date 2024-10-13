```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer.get_customer_discount_by_id(discount_id="discountId")

print(result)

```
