```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CollectPaymentsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CollectPaymentsBody(
    amount="amount",
    amount_is_editable=False,
    checkout={},
    country="country",
    currency="currency",
    customer="customer",
    fixed_side="buy",
    language="en",
    max_payments=7,
    merchant_reference_id="merchant_reference_id",
    requested_currency="requested_currency"
)

result = sdk.payment_link.create_payment_link(request_body=request_body)

print(result)

```
