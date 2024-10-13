# SubscriptionInvoiceService

A list of all methods in the `SubscriptionInvoiceService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_invoices](#list_invoices)       | Retrieve the basic data of an invoice, with individual invoice lines.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [retrieve_invoice](#retrieve_invoice) | Retrieve the basic data of an invoice, with individual invoice lines.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [update_invoice](#update_invoice)     | Change or modify an invoice. You can modify the invoice when its status is draft.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [delete_invoice](#delete_invoice)     | Delete an invoice. You can delete an invoice when status is draft.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [finalize_invoice](#finalize_invoice) | Finalize an invoice.Invoices are initially created with a draft status, and this is the only state in which an invoice can be finalized. When an invoice is ready to be paid, finalize it. This sets its status to open. Subscriptions automatically create draft invoices during each billing cycle, which are then automatically finalized. When an invoice is finalized, it can no longer be deleted and its final status can be one of the following - Paid Uncollectible\* Void. An invoice can be finalized only one time. |
| [pay_invoice](#pay_invoice)           | Make a payment against an invoice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## list_invoices

Retrieve the basic data of an invoice, with individual invoice lines.

- HTTP Method: `GET`
- Endpoint: `/v1/invoices`

**Parameters**

| Name           | Type                              | Required | Description                                                                                                                                                                                    |
| :------------- | :-------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| customer       | [Customer](../models/Customer.md) | ❌       | ID of the customer. String starting with **cus\_**.                                                                                                                                            |
| date\_         | str                               | ❌       | Date that the invoice was created.                                                                                                                                                             |
| due_date       | str                               | ❌       | The date payment is due on this invoice. This value is calculated from the date the invoice is created, plus the number of days specified in the days_until_due field. Format is in Unix time. |
| ending_before  | str                               | ❌       | The ID of the invoice created after the last invoice you want to retrieve. card.                                                                                                               |
| limit          | str                               | ❌       | The maximum number of invoices to return. Range 1-100. Default is 10.                                                                                                                          |
| starting_after | str                               | ❌       | The ID of the invoice created before the first invoice you want to retrieve.                                                                                                                   |
| subscription   | str                               | ❌       | ID of the subscription. String starting with sub\_.                                                                                                                                            |

**Return Type**

`InlineResponse200_52`

**Example Usage Code Snippet**

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
    created_at=3,
    default_payment_method="default_payment_method",
    delinquent=False,
    description="description",
    discount={
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
    phone_number="phone_number",
    subscriptions=[
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
)

result = sdk.subscription_invoice.list_invoices(
    customer=customer,
    date_="date",
    due_date="due_date",
    ending_before="ending_before",
    limit="limit",
    starting_after="starting_after",
    subscription="subscription"
)

print(result)
```

## retrieve_invoice

Retrieve the basic data of an invoice, with individual invoice lines.

- HTTP Method: `GET`
- Endpoint: `/v1/invoices/{invoiceId}`

**Parameters**

| Name       | Type | Required | Description                                      |
| :--------- | :--- | :------- | :----------------------------------------------- |
| invoice_id | str  | ✅       | The ID of the invoice that you want to retrieve. |

**Return Type**

`InlineResponse200_53`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_invoice.retrieve_invoice(invoice_id="invoiceId")

print(result)
```

## update_invoice

Change or modify an invoice. You can modify the invoice when its status is draft.

- HTTP Method: `POST`
- Endpoint: `/v1/invoices/{invoiceId}`

**Parameters**

| Name         | Type                                                        | Required | Description                                     |
| :----------- | :---------------------------------------------------------- | :------- | :---------------------------------------------- |
| request_body | [InvoicesInvoiceIdBody](../models/InvoicesInvoiceIdBody.md) | ❌       | The request body.                               |
| invoice_id   | str                                                         | ✅       | The ID of the invoice that you want to updated. |

**Return Type**

`InlineResponse200_53`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import InvoicesInvoiceIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = InvoicesInvoiceIdBody(
    days_until_due=1.38,
    description="description",
    due_date="due_date",
    metadata={},
    payment_fields={},
    statement_descriptor="statement_descriptor",
    tax_percent=0.05
)

result = sdk.subscription_invoice.update_invoice(
    request_body=request_body,
    invoice_id="invoiceId"
)

print(result)
```

## delete_invoice

Delete an invoice. You can delete an invoice when status is draft.

- HTTP Method: `DELETE`
- Endpoint: `/v1/invoices/{invoiceId}`

**Parameters**

| Name       | Type | Required | Description                                    |
| :--------- | :--- | :------- | :--------------------------------------------- |
| invoice_id | str  | ✅       | The ID of the invoice that you want to delete. |

**Return Type**

`InlineResponse200_40`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_invoice.delete_invoice(invoice_id="invoiceId")

print(result)
```

## finalize_invoice

Finalize an invoice.Invoices are initially created with a draft status, and this is the only state in which an invoice can be finalized. When an invoice is ready to be paid, finalize it. This sets its status to open. Subscriptions automatically create draft invoices during each billing cycle, which are then automatically finalized. When an invoice is finalized, it can no longer be deleted and its final status can be one of the following - Paid Uncollectible\* Void. An invoice can be finalized only one time.

- HTTP Method: `POST`
- Endpoint: `/v1/invoices/{invoiceId}/finalize`

**Parameters**

| Name       | Type | Required | Description                        |
| :--------- | :--- | :------- | :--------------------------------- |
| invoice_id | str  | ✅       | ID of the invoice you want to pay. |

**Return Type**

`InlineResponse200_53`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_invoice.finalize_invoice(invoice_id="invoiceId")

print(result)
```

## pay_invoice

Make a payment against an invoice.

- HTTP Method: `POST`
- Endpoint: `/v1/invoices/{invoiceId}/pay`

**Parameters**

| Name         | Type                                              | Required | Description                        |
| :----------- | :------------------------------------------------ | :------- | :--------------------------------- |
| request_body | [InvoiceIdPayBody](../models/InvoiceIdPayBody.md) | ❌       | The request body.                  |
| invoice_id   | str                                               | ✅       | ID of the invoice you want to pay. |

**Return Type**

`InlineResponse200_53`

**Example Usage Code Snippet**

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
