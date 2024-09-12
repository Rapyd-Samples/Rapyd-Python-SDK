```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Customer

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
customer=Customer(
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
    created_at=7,
    default_payment_method="default_payment_method",
    delinquent=False,
    description="description",
    discount={
        "coupon": {
            "amount_off": 0.13,
            "created": 1671697165,
            "currency": "GBP",
            "description": "Sample Coupon 1",
            "discount_duration_in_uses": 2,
            "discount_valid_until": 7.67,
            "discount_validity_in_months": 2,
            "duration": "forever",
            "duration_in_months": 3,
            "id_": "coupon_c1194a18a9972ca7f9804826f00c9eb8",
            "max_redemptions": 2,
            "metadata": {},
            "percent_off": 10,
            "redeem_by": 0.44,
            "times_redeemed": 6.69,
            "valid": True
        },
        "customer": "cus_3f4ed3168413d863671602dfbe839aa2",
        "end": 1679473563,
        "id_": "dis_ab0445dee00fdcdd83811760ffe90e3b",
        "number_of_uses": 2.89,
        "start": 1679473563,
        "subscription": "sub_199e8c92ec0ec2bcbe56740042639d6e",
        "valid": True
    },
    email="email",
    ewallet="ewallet",
    id_="id",
    invoice_prefix="invoice_prefix",
    metadata={},
    name="name",
    payment_methods={
        "data": [
            {
                "category": "bank",
                "fingerprint_token": "fingerprint_token",
                "id_": "id",
                "image": "image",
                "last4": "4487",
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
        "has_more": True,
        "total_count": 7,
        "url": "url"
    },
    phone_number="phone_number",
    subscriptions=[
        {
            "billing": "pay_automatically",
            "billing_cycle_anchor": "now",
            "cancel_at_period_end": True,
            "canceled_at": 5.63,
            "created_at": 1592379647,
            "current_period_end": 1594971647,
            "current_period_start": 1592379647,
            "customer_token": "cus_3f4ed3168413d863671602dfbe839aa2",
            "days_until_due": 30,
            "discount": {
                "coupon": {
                    "amount_off": 0.13,
                    "created": 1671697165,
                    "currency": "GBP",
                    "description": "Sample Coupon 1",
                    "discount_duration_in_uses": 2,
                    "discount_valid_until": 7.67,
                    "discount_validity_in_months": 2,
                    "duration": "forever",
                    "duration_in_months": 3,
                    "id_": "coupon_c1194a18a9972ca7f9804826f00c9eb8",
                    "max_redemptions": 2,
                    "metadata": {},
                    "percent_off": 10,
                    "redeem_by": 0.44,
                    "times_redeemed": 6.69,
                    "valid": True
                },
                "customer": "cus_3f4ed3168413d863671602dfbe839aa2",
                "end": 1679473563,
                "id_": "dis_ab0445dee00fdcdd83811760ffe90e3b",
                "number_of_uses": 2.89,
                "start": 1679473563,
                "subscription": "sub_199e8c92ec0ec2bcbe56740042639d6e",
                "valid": True
            },
            "ended_at": 7.3,
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
                        "created": 1.05,
                        "id_": "subi_e5dbbf84c68e5bb7db761625158d4262",
                        "metadata": "{\"merchant_defined\": True }",
                        "plan": {
                            "aggregate_usage": "max",
                            "amount": 5.37,
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
                                    "flat_amount": 6.45,
                                    "up_to": "inf"
                                }
                            ],
                            "tiers_mode": "graduated",
                            "transform_usage": {
                                "divide_by": 1,
                                "round": "round"
                            },
                            "trial_period_days": 9.42,
                            "usage_type": "metered"
                        },
                        "quantity": 4.27,
                        "subscription_id": "sub_0de9c79c1e2beee09499dc8220493d5"
                    }
                ],
                "has_more": True,
                "total_count": 1,
                "url": "/v1/subscription_items?subscription=sub_324ee75f8c26f1df94bc8cc693f3c729"
            },
            "tax_percent": 10.5,
            "trial_end": 9.98,
            "trial_start": 3.73,
            "type_": "payout"
        }
    ]
)

result = sdk.subscription_invoice.list_invoices(
    customer=customer,
    date_="date",
    due_date="due_date",
    ending_before="ending_before",
    limit="limit",
    starting_after="starting_after",
    subscription=True
)

print(result)

```
