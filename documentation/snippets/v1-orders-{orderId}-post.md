```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import OrdersOrderIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = OrdersOrderIdBody(
    coupon="coupon",
    metadata={},
    tax_percent=6.19,
    status="paid"
)

result = sdk.order.update_order(
    request_body=request_body,
    order_id="orderId"
)

print(result)

```
