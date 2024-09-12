```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1PaymentsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1PaymentsBody(
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
    amount=5.04,
    capture=True,
    client_details={
        "ip_address": "ip_address",
        "java_enabled": False,
        "java_script_enabled": False,
        "language": "language",
        "screen_color_depth": 1,
        "screen_height": 4,
        "screen_width": 8,
        "time_zone_offset": 5
    },
    complete_payment_url="complete_payment_url",
    currency="GBP",
    customer="customer",
    description="description",
    error_payment_url="error_payment_url",
    escrow=True,
    escrow_release_days="/6/",
    ewallet="ewallet",
    ewallets="",
    expiration=3.35,
    fixed_side="fixed_side",
    group_payment="group_payment",
    initiation_type="customer_present",
    merchant_reference_id="merchant_reference_id",
    metadata={},
    payment_fees={
        "fx_fee": {
            "calc_type": "gross",
            "value": 2.5
        },
        "gross_fees": 4.23,
        "net_fees": 2.4,
        "transaction_fee": {
            "calc_type": "gross",
            "fee_type": "absolute",
            "value": 2
        },
        "total_merchant_fees": 3.19
    },
    payment_method="uteli",
    payment_method_options={},
    receipt_email="receipt_email",
    requested_currency="requested_currency",
    statement_descriptor="statement_descriptor"
)

result = sdk.payment.create_payment(request_body=request_body)

print(result)

```
