```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Category

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer_payment_method.get_customer_payment_methods(
    customer_id="customerId",
    category="bank",
    starting_after="starting_after",
    ending_before="ending_before",
    limit="limit",
    type_="type"
)

print(result)

```
