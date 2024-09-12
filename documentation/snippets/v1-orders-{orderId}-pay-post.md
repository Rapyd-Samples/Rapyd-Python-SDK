```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import OrderIdPayBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = OrderIdPayBody(
    metadata={},
    payment_method="payment_method",
    customer="customer"
)

result = sdk.order.pay_order(
    request_body=request_body,
    order_id="orderId"
)

print(result)

```
