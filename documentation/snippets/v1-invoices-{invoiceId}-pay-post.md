```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import InvoiceIdPayBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = InvoiceIdPayBody(
    payment_method="payment_method"
)

result = sdk.subscription_invoice.pay_invoice(
    request_body=request_body,
    invoice_id="invoiceId"
)

print(result)

```
