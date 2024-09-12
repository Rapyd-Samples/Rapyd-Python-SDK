```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_subscription_item.get_subscription_discount_by_id(discount_id="discountId")

print(result)

```
