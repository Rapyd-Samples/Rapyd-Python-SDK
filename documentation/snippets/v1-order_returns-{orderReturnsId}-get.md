```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.order_return.retrieve_order_return(order_returns_id="orderReturnsId")

print(result)

```
