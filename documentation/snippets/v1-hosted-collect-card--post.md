```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CollectCardBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CollectCardBody(
    billing_address_collect=False,
    cancel_url="cancel_url",
    card_fields={
        "recurrence_type": "unscheduled"
    },
    complete_url="complete_url",
    complete_payment_url="complete_payment_url",
    country="country",
    currency="currency",
    customer="customer",
    error_payment_url="error_payment_url",
    language="en",
    page_expiration="page_expiration",
    payment_method_type="payment_method_type"
)

result = sdk.payment_card_token.create_card_token(request_body=request_body)

print(result)

```
