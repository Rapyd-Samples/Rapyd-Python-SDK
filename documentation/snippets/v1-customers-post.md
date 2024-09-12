```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1CustomersBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1CustomersBody(
    addresses=[
        {
            "canton": "canton",
            "city": "city",
            "country": "GB",
            "created_at": 3.34,
            "district": "district",
            "id_": "id",
            "line_1": "line_1",
            "line_2": "line_2",
            "line_3": "line_3",
            "metadata": {},
            "name": "name",
            "phone_number": "phone_number",
            "state": "state",
            "zip": "zip"
        }
    ],
    business_vat_id="business_vat_id",
    coupon="coupon",
    default_payment_method="default_payment_method",
    description="description",
    email="email",
    ewallet="ewallet",
    invoice_prefix="invoice_prefix",
    metadata={},
    name="name",
    phone_number="phone_number"
)

result = sdk.customer.create_customer(request_body=request_body)

print(result)

```
