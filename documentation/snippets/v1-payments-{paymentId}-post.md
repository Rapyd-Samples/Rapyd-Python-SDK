```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PaymentsPaymentIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PaymentsPaymentIdBody(
    address={
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
    },
    description="description",
    escrow=True,
    escrow_release_days="/3/",
    initiation_type="initiation_type",
    metadata={},
    receipt_email="receipt_email"
)

result = sdk.payment.update_payment(
    request_body=request_body,
    payment_id="paymentId"
)

print(result)

```
