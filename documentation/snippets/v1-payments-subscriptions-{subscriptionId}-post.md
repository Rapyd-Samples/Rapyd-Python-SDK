```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import SubscriptionsSubscriptionIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SubscriptionsSubscriptionIdBody(
    billing="billing",
    billing_cycle_anchor="billing_cycle_anchor",
    cancel_at_period_end=True,
    coupon="coupon",
    days_until_due=6.04,
    metadata={},
    payment_fields={
        "address": {
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
        },
        "amount_range_per_currency": [
            {
                "maximum_amount": 4.53,
                "minimum_amount": 0.65,
                "currency": "GBP"
            }
        ],
        "bin_details": {
            "brand": "brand",
            "bin_number": "bin_number",
            "type_": "type",
            "issuer": "issuer",
            "country": "GB",
            "level": "level"
        },
        "category": "bank",
        "conditions": [
            {
                "description": "description",
                "element_name": "element_name",
                "operator": "operator",
                "threshold_value": "quis sed u"
            }
        ],
        "country": "GB",
        "currencies": [
            "GBP"
        ],
        "customer": {
            "addresses": [
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
            "business_vat_id": "business_vat_id",
            "created_at": 3,
            "default_payment_method": "default_payment_method",
            "delinquent": False,
            "description": "description",
            "discount": {
                "coupon": {
                    "amount_off": 6.55,
                    "created": 1671697165,
                    "currency": "GBP",
                    "description": "Sample Coupon 1",
                    "discount_duration_in_uses": 2,
                    "discount_valid_until": 0.57,
                    "discount_validity_in_months": 2,
                    "duration": "forever",
                    "duration_in_months": 3,
                    "id_": "coupon_c1194a18a9972ca7f9804826f00c9eb8",
                    "max_redemptions": 2,
                    "metadata": {},
                    "percent_off": 10,
                    "redeem_by": 0.14,
                    "times_redeemed": 2.17,
                    "valid": True
                },
                "customer": "cus_3f4ed3168413d863671602dfbe839aa2",
                "end": 1679473563,
                "id_": "dis_ab0445dee00fdcdd83811760ffe90e3b",
                "number_of_uses": 5.55,
                "start": 1679473563,
                "subscription": "sub_199e8c92ec0ec2bcbe56740042639d6e",
                "valid": True
            },
            "email": "email",
            "ewallet": "ewallet",
            "id_": "id",
            "invoice_prefix": "invoice_prefix",
            "metadata": {},
            "name": "name",
            "payment_methods": {
                "data": [
                    {
                        "category": "bank",
                        "fingerprint_token": "fingerprint_token",
                        "id_": "id",
                        "image": "image",
                        "last4": "6326",
                        "metadata": {},
                        "name": "name",
                        "network_reference_id": "network_reference_id",
                        "next_action": "3d_verification",
                        "redirect_url": "redirect_url",
                        "supporting_documentation": "supporting_documentation",
                        "token": "token",
                        "type_": "type",
                        "webhook_url": "webhook_url"
                    }
                ],
                "has_more": False,
                "total_count": 3,
                "url": "url"
            },
            "phone_number": "phone_number",
            "subscriptions": [
                {
                    "billing": "pay_automatically",
                    "billing_cycle_anchor": "now",
                    "cancel_at_period_end": True,
                    "canceled_at": 4,
                    "created_at": 1592379647,
                    "current_period_end": 1594971647,
                    "current_period_start": 1592379647,
                    "customer_token": "cus_3f4ed3168413d863671602dfbe839aa2",
                    "days_until_due": 30,
                    "discount": {
                        "coupon": {
                            "amount_off": 6.55,
                            "created": 1671697165,
                            "currency": "GBP",
                            "description": "Sample Coupon 1",
                            "discount_duration_in_uses": 2,
                            "discount_valid_until": 0.57,
                            "discount_validity_in_months": 2,
                            "duration": "forever",
                            "duration_in_months": 3,
                            "id_": "coupon_c1194a18a9972ca7f9804826f00c9eb8",
                            "max_redemptions": 2,
                            "metadata": {},
                            "percent_off": 10,
                            "redeem_by": 0.14,
                            "times_redeemed": 2.17,
                            "valid": True
                        },
                        "customer": "cus_3f4ed3168413d863671602dfbe839aa2",
                        "end": 1679473563,
                        "id_": "dis_ab0445dee00fdcdd83811760ffe90e3b",
                        "number_of_uses": 5.55,
                        "start": 1679473563,
                        "subscription": "sub_199e8c92ec0ec2bcbe56740042639d6e",
                        "valid": True
                    },
                    "ended_at": 4.95,
                    "id_": "sub_04fd8fbd78d7dd7e0e6323810a69275c",
                    "metadata": {},
                    "payment_fields": {},
                    "payment_method": "card_320dcb1879fbc41f13a81e690636f3c2",
                    "payout_fields": {},
                    "simultaneous_invoice": True,
                    "status": "active",
                    "subscription_items": {
                        "data": [
                            {
                                "created": 1.1,
                                "id_": "subi_e5dbbf84c68e5bb7db761625158d4262",
                                "metadata": "{\"merchant_defined\": True }",
                                "plan": {
                                    "active": True,
                                    "aggregate_usage": "max",
                                    "amount": 1.34,
                                    "billing_scheme": "per_unit",
                                    "created_at": 1592311574,
                                    "currency": "GBP",
                                    "id_": "plan_51788cf4ed1b672cb0a2a97773887f5b",
                                    "interval": "month",
                                    "interval_count": 2,
                                    "metadata": {},
                                    "nickname": "Basic Parking",
                                    "product": {
                                        "active": True,
                                        "attributes": [
                                            "attributes"
                                        ],
                                        "created_at": 1592299157,
                                        "description": "The ultimate in comfort for the dedicated gamer",
                                        "id_": "product_0d9dc6be69c769560fe913f3b086d8ca",
                                        "images": [
                                            "images"
                                        ],
                                        "metadata": {},
                                        "name": "Gamer's Red Chair",
                                        "package_dimensions": {
                                            "height": 10,
                                            "length": 20,
                                            "weight": 100,
                                            "width": 40
                                        },
                                        "shippable": True,
                                        "skus": [
                                            {
                                                "active": True,
                                                "attributes": {
                                                    "color": "green"
                                                },
                                                "created_at": 1546353713,
                                                "currency": "GBP",
                                                "id_": "sku_a6d86bdc6f3a7ef6cb51de5a5678493f",
                                                "image": "image",
                                                "inventory": {},
                                                "metadata": {},
                                                "package_dimensions": {
                                                    "height": 1,
                                                    "length": 2,
                                                    "weight": 3,
                                                    "width": 4
                                                },
                                                "price": 10.99,
                                                "product": "product_f383d03c34fb499eb3ada4e3c574002a",
                                                "updated_at": 1546354288
                                            }
                                        ],
                                        "statement_descriptor": "statement_descriptor",
                                        "type_": "goods",
                                        "unit_label": "unit_label",
                                        "updated_at": 1592300812
                                    },
                                    "tiers": [
                                        {
                                            "amount": 15,
                                            "flat_amount": 4.6,
                                            "up_to": "inf"
                                        }
                                    ],
                                    "tiers_mode": "graduated",
                                    "transform_usage": {
                                        "divide_by": 1,
                                        "round": "round"
                                    },
                                    "trial_period_days": 4.85,
                                    "usage_type": "metered"
                                },
                                "quantity": 1.01,
                                "subscription_id": "sub_0de9c79c1e2beee09499dc8220493d5"
                            }
                        ],
                        "has_more": False,
                        "total_count": 1,
                        "url": "/v1/subscription_items?subscription=sub_324ee75f8c26f1df94bc8cc693f3c729"
                    },
                    "tax_percent": 10.5,
                    "trial_end": 4.72,
                    "trial_start": 1.39,
                    "type_": "payout"
                }
            ]
        },
        "fingerprint": "fingerprint",
        "image": "image",
        "instructions": "instructions",
        "is_cancelable": True,
        "is_expirable": False,
        "is_online": True,
        "is_refundable": False,
        "is_required": False,
        "is_tokenizable": True,
        "is_virtual": False,
        "last4": "6546",
        "maximum_expiration_seconds": 5,
        "minimum_expiration_seconds": 10,
        "multiple_overage_allowed": True,
        "name": "name",
        "payment_flow_type": "direct"
    },
    payment_method="id ipsum et dol",
    simultaneous_invoice=False,
    subscription_items=[
        "subscription_items"
    ],
    tax_percent=8.25,
    trial_end=9.65,
    trial_from_plan=True,
    trial_period_days=0.56
)

result = sdk.subscription.update_subscription(
    request_body=request_body,
    subscription_id="subscriptionId"
)

print(result)

```
