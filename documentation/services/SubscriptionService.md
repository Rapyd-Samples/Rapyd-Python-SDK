# SubscriptionService

A list of all methods in the `SubscriptionService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                                                                |
| :------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_subscription_list](#get_subscription_list)               | Retrieve a list of subscriptions. You can filter the list with query parameters.                                                                           |
| [create_subscription](#create_subscription)                   | Create a subscription for regular, automatic payments.                                                                                                     |
| [get_subscription](#get_subscription)                         | Retrieve the details of a subscription.                                                                                                                    |
| [update_subscription](#update_subscription)                   | Update the details of a subscription.                                                                                                                      |
| [cancel_subscription](#cancel_subscription)                   | Cancel a subscription.                                                                                                                                     |
| [delete_subscription_discount](#delete_subscription_discount) | Delete the discount that was assigned to a subscription. This method does not affect the coupon that the discount was derived from.                        |
| [complete_subscription_cycle](#complete_subscription_cycle)   | Cancel the subscription and create an invoice. This method is for testing purposes and runs only in the sandbox.                                           |
| [simulate_start_new_cycle](#simulate_start_new_cycle)         | End a subscription cycle, create an invoice and move the subscription to the next cycle. This method is for testing purposes and runs only in the sandbox. |

## get_subscription_list

Retrieve a list of subscriptions. You can filter the list with query parameters.

- HTTP Method: `GET`
- Endpoint: `/v1/payments/subscriptions`

**Parameters**

| Name           | Type  | Required | Description                                                                                                                                                                                                    |
| :------------- | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| starting_after | `str` | ✅       | The ID of a record in the list. The list begins with the record that was created next after the record with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used. |
| billing        | `str` | ❌       | Method of billing. One of the following, pay_automatically, send_invoice.                                                                                                                                      |
| customer       | `str` | ❌       | ID of the customer. String starting with cus\_                                                                                                                                                                 |
| status         | `str` | ❌       | Status of the subscription. One of the following, active, canceled, trialing                                                                                                                                   |
| product        | `str` | ❌       | ID of a 'product' object. The product must have type set to service. String starting with product\_. Filter for one product at a time.                                                                         |
| ending_before  | `str` | ❌       | The ID of a record in the list. The list ends with the last record that was created before the record with this ID. Use this filter to get the previous page of results.                                       |
| limit          | `str` | ❌       | The maximum number of subscriptions to return. Range, 1-100. Default is 10.                                                                                                                                    |

**Return Type**

`InlineResponse200_55`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription.get_subscription_list(
    starting_after="starting_after",
    billing="billing",
    customer="customer",
    status="status",
    product="product",
    ending_before="ending_before",
    limit="limit"
)

print(result)
```

## create_subscription

Create a subscription for regular, automatic payments.

- HTTP Method: `POST`
- Endpoint: `/v1/payments/subscriptions`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | `[PaymentsSubscriptionsBody](../models/PaymentsSubscriptionsBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_56`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PaymentsSubscriptionsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PaymentsSubscriptionsBody(
    billing="billing",
    billing_cycle_anchor=2.91,
    cancel_at_period_end=True,
    coupon="coupon",
    customer="customer",
    days_until_due=4.17,
    metadata={},
    payment_fields={
        "address": {
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
        "amount": 3.28,
        "auth_code": "auth_code",
        "cancel_reason": "cancel_reason",
        "captured": True,
        "complete_payment_url": "complete_payment_url",
        "country_code": "GB",
        "created_at": 3,
        "currency_code": "GBP",
        "customer_token": "customer_token",
        "description": "description",
        "dispute": {
            "id_": "id",
            "token": "dispute_6bd95ecec6bee6a505d39b56dbded2ec",
            "status": "ACT",
            "amount": 6.69,
            "currency": "currency",
            "dispute_category": "dispute_category",
            "dispute_reason_description": "dispute_reason_description",
            "original_transaction_currency": "GBP",
            "original_transaction_amount": 5.78,
            "original_dispute_amount": 9.23,
            "original_dispute_currency": "GBP",
            "original_transaction_id": "payment_ce936f36d93bc9307a3db9ebfd3deaaa",
            "ewallet_id": "ewallet_id",
            "central_processing_date": 0.59,
            "created_at": 0.69,
            "updated_at": 9.59,
            "due_date": 6.87,
            "payment_method": "card_39d8aee398dfa5492fc2a0ea2822958f\"",
            "payment_method_data": {},
            "rate": 8.99,
            "evidence": "evidence",
            "evidence_reason_code": "evidence_reason_code",
            "pre_dispute": False,
            "arn": "arn"
        },
        "error_code": "error_code",
        "error_payment_url": "error_payment_url",
        "escrow": {},
        "ewallet_id": "ewallet_id",
        "ewallets": [
            {
                "ewallet_id": "ewallet_id",
                "amount": 8.57,
                "percent": 5.39,
                "refunded_amount": 4.4
            }
        ],
        "expiration": 2.42,
        "failure_code": "failure_code",
        "failure_message": "failure_message",
        "fixed_side": "fixed_side",
        "flow_type": "flow_type",
        "fx_rate": 1,
        "group_payment": "group_payment",
        "id_": "id",
        "initiation_type": "initiation_type",
        "instructions": [
            {
                "name": "name",
                "steps": [
                    {
                        "step": "step"
                    }
                ]
            }
        ],
        "invoice": "invoice",
        "is_partial": True,
        "merchant_reference_id": "merchant_reference_id",
        "merchant_requested_amount": "merchant_requested_amount",
        "merchant_requested_currency": "merchant_requested_currency",
        "metadata": {},
        "mid": "mid",
        "next_action": "3d_verification",
        "order": "order",
        "original_amount": 7.95,
        "outcome": {
            "network_status": "approved_by_network",
            "payment_flow_type": "direct",
            "payment_options": {
                "address": {
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
                "amount_range_per_currency": [
                    {
                        "maximum_amount": 8.96,
                        "minimum_amount": 8.01,
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
                        "threshold_value": "estadi"
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
                    "business_vat_id": "business_vat_id",
                    "created_at": 7,
                    "default_payment_method": "default_payment_method",
                    "delinquent": False,
                    "description": "description",
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
                    "phone_number": "phone_number",
                    "subscriptions": [
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
                },
                "fingerprint": "fingerprint",
                "image": "image",
                "instructions": "instructions",
                "is_cancelable": False,
                "is_expirable": True,
                "is_online": True,
                "is_refundable": True,
                "is_required": False,
                "is_tokenizable": False,
                "is_virtual": False,
                "last4": "0117",
                "maximum_expiration_seconds": 10,
                "minimum_expiration_seconds": 0,
                "multiple_overage_allowed": False,
                "name": "name",
                "payment_flow_type": "direct"
            },
            "status": "status",
            "risk_level": "normal",
            "seller_message": "seller_message"
        },
        "paid": False,
        "paid_at": 3.25,
        "payment_fees": {
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
        "payment_method": "payment_method",
        "payment_method_data": {},
        "payment_method_options": {},
        "payment_method_type": "payment_method_type",
        "payment_method_type_category": "bank_transfer",
        "receipt_email": "receipt_email",
        "receipt_number": "receipt_number",
        "redirect_url": "redirect_url",
        "refunded": True,
        "refunded_amount": 4.58,
        "refunds": {
            "data": [
                "data"
            ],
            "has_more": True,
            "total_count": 2,
            "url": "url"
        },
        "remitter_information": {},
        "save_payment_method": False,
        "statement_descriptor": "statement_descriptor",
        "status": "ACT",
        "textual_codes": {},
        "transaction_id": "transaction_id",
        "visual_codes": {}
    },
    payment_method="estminim adipis",
    simultaneous_invoice=True,
    subscription_items=[
        {
            "plan": "plan",
            "quantity": 8.42
        }
    ],
    tax_percent=3.39,
    trial_end=7.11,
    trial_from_plan=True,
    trial_period_days=2.81
)

result = sdk.subscription.create_subscription(request_body=request_body)

print(result)
```

## get_subscription

Retrieve the details of a subscription.

- HTTP Method: `GET`
- Endpoint: `/v1/payments/subscriptions/{subscriptionId}`

**Parameters**

| Name            | Type  | Required | Description                                         |
| :-------------- | :---- | :------- | :-------------------------------------------------- |
| subscription_id | `str` | ✅       | ID of the subscription. String starting with sub\_. |

**Return Type**

`InlineResponse200_56`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription.get_subscription(subscription_id="subscriptionId")

print(result)
```

## update_subscription

Update the details of a subscription.

- HTTP Method: `POST`
- Endpoint: `/v1/payments/subscriptions/{subscriptionId}`

**Parameters**

| Name            | Type                                                                              | Required | Description                                         |
| :-------------- | :-------------------------------------------------------------------------------- | :------- | :-------------------------------------------------- |
| request_body    | `[SubscriptionsSubscriptionIdBody](../models/SubscriptionsSubscriptionIdBody.md)` | ✅       | The request body.                                   |
| subscription_id | `str`                                                                             | ✅       | ID of the subscription. String starting with sub\_. |

**Return Type**

`InlineResponse200_56`

**Example Usage Code Snippet**

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
    cancel_at_period_end=False,
    coupon="coupon",
    days_until_due=1.94,
    metadata={},
    payment_fields={
        "address": {
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
        "amount_range_per_currency": [
            {
                "maximum_amount": 8.96,
                "minimum_amount": 8.01,
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
                "threshold_value": "estadi"
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
            "business_vat_id": "business_vat_id",
            "created_at": 7,
            "default_payment_method": "default_payment_method",
            "delinquent": False,
            "description": "description",
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
            "phone_number": "phone_number",
            "subscriptions": [
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
        },
        "fingerprint": "fingerprint",
        "image": "image",
        "instructions": "instructions",
        "is_cancelable": False,
        "is_expirable": True,
        "is_online": True,
        "is_refundable": True,
        "is_required": False,
        "is_tokenizable": False,
        "is_virtual": False,
        "last4": "0117",
        "maximum_expiration_seconds": 10,
        "minimum_expiration_seconds": 0,
        "multiple_overage_allowed": False,
        "name": "name",
        "payment_flow_type": "direct"
    },
    payment_method="pariatur",
    simultaneous_invoice=True,
    subscription_items=[
        "subscription_items"
    ],
    tax_percent=3.25,
    trial_end=1.6,
    trial_from_plan=False,
    trial_period_days=4.21
)

result = sdk.subscription.update_subscription(
    request_body=request_body,
    subscription_id="subscriptionId"
)

print(result)
```

## cancel_subscription

Cancel a subscription.

- HTTP Method: `DELETE`
- Endpoint: `/v1/payments/subscriptions/{subscriptionId}`

**Parameters**

| Name            | Type  | Required | Description                                         |
| :-------------- | :---- | :------- | :-------------------------------------------------- |
| subscription_id | `str` | ✅       | ID of the subscription. String starting with sub\_. |

**Return Type**

`InlineResponse200_56`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription.cancel_subscription(subscription_id="subscriptionId")

print(result)
```

## delete_subscription_discount

Delete the discount that was assigned to a subscription. This method does not affect the coupon that the discount was derived from.

- HTTP Method: `DELETE`
- Endpoint: `/v1/payments/subscriptions/{subscriptionId}/discount`

**Parameters**

| Name            | Type  | Required | Description                                        |
| :-------------- | :---- | :------- | :------------------------------------------------- |
| subscription_id | `str` | ✅       | ID of the subscription. String starting with sub\_ |

**Return Type**

`InlineResponse200_57`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription.delete_subscription_discount(subscription_id="subscriptionId")

print(result)
```

## complete_subscription_cycle

Cancel the subscription and create an invoice. This method is for testing purposes and runs only in the sandbox.

- HTTP Method: `POST`
- Endpoint: `/v1/payments/subscriptions/{subscriptionId}/complete_cycle`

**Parameters**

| Name            | Type  | Required | Description                                         |
| :-------------- | :---- | :------- | :-------------------------------------------------- |
| subscription_id | `str` | ✅       | ID of the subscription. String starting with sub\_. |

**Return Type**

`InlineResponse200_56`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription.complete_subscription_cycle(subscription_id="subscriptionId")

print(result)
```

## simulate_start_new_cycle

End a subscription cycle, create an invoice and move the subscription to the next cycle. This method is for testing purposes and runs only in the sandbox.

- HTTP Method: `POST`
- Endpoint: `/v1/payments/subscriptions/{subscriptionId}/start_new_cycle`

**Parameters**

| Name            | Type  | Required | Description                                         |
| :-------------- | :---- | :------- | :-------------------------------------------------- |
| subscription_id | `str` | ✅       | ID of the subscription. String starting with sub\_. |

**Return Type**

`InlineResponse200_56`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription.simulate_start_new_cycle(subscription_id="subscriptionId")

print(result)
```
