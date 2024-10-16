```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CustomerIdPaymentMethodsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CustomerIdPaymentMethodsBody(
    data={
        "amount_range_per_currency": [
            {
                "maximum_amount": 4.53,
                "minimum_amount": 0.65,
                "currency": "GBP"
            }
        ],
        "category": "bank",
        "country": "GB",
        "currencies": [
            "GBP"
        ],
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
        "image": "image",
        "is_cancelable": True,
        "is_expirable": False,
        "is_online": True,
        "is_refundable": False,
        "is_tokenizable": False,
        "is_virtual": True,
        "maximum_expiration_seconds": 1.03,
        "minimum_expiration_seconds": 6.1,
        "multiple_overage_allowed": False,
        "name": "name",
        "payment_flow_type": "direct",
        "payment_options": [
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
        "status": "status",
        "supported_digital_wallet_providers": [
            "supported_digital_wallet_providers"
        ],
        "type_": "type",
        "virtual_payment_method_type": "virtual_payment_method_type",
        "is_restricted": True,
        "supports_subscription": False
    }
)

result = sdk.customer_payment_method.create_customer_payment_method(
    request_body=request_body,
    customer_id="customerId"
)

print(result)

```
