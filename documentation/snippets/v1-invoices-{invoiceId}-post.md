```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import InvoicesInvoiceIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = InvoicesInvoiceIdBody(
    days_until_due=0.55,
    description="description",
    due_date="due_date",
    metadata={},
    payment_fields={},
    statement_descriptor="statement_descriptor",
    tax_percent=2.05
)

result = sdk.subscription_invoice.update_invoice(
    request_body=request_body,
    invoice_id="invoiceId"
)

print(result)

```
