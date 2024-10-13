```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CustomerRequest

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CustomerRequest(
    addresses=[
        {
            "canton": "canton",
            "city": "city",
            "country": "GB",
            "created_at": 8.2,
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
    payment_method={
        "fields": [
            {
                "code": "code",
                "is_required": False,
                "is_updatable": True,
                "instructions": "instructions",
                "name": "name",
                "numeric_code": "numeric_code",
                "required_fields": [
                    {
                        "code": "code",
                        "is_required": False,
                        "is_updatable": True,
                        "instructions": "instructions",
                        "name": "name",
                        "numeric_code": "numeric_code",
                        "type_": "boolean",
                        "regex": "regex",
                        "conditions": [
                            {
                                "description": "description",
                                "element_name": "element_name",
                                "operator": "operator",
                                "threshold_value": "reprehenderit "
                            }
                        ],
                        "description": "description"
                    }
                ],
                "type_": "boolean",
                "regex": "regex",
                "conditions": [
                    {
                        "description": "description",
                        "element_name": "element_name",
                        "operator": "operator",
                        "threshold_value": "reprehenderit "
                    }
                ],
                "description": "description"
            }
        ],
        "type_": "type"
    },
    description="description",
    email="email",
    ewallet="ewallet",
    invoice_prefix="invoice_prefix",
    metadata={},
    name="name",
    phone_number="phone_number"
)

result = sdk.customer.update_customer(
    request_body=request_body,
    customer_id="customerId"
)

print(result)

```
