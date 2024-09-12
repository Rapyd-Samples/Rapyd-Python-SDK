# CheckoutPageService

A list of all methods in the `CheckoutPageService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                  |
| :------------------------------------------------------------ | :------------------------------------------- |
| [get_hosted_page_payment](#get_hosted_page_payment)           | Retrieve a checkout page                     |
| [generate_hosted_page_payment](#generate_hosted_page_payment) | Create a checkout page that makes a payment. |

## get_hosted_page_payment

Retrieve a checkout page

- HTTP Method: `GET`
- Endpoint: `/v1/checkout/{checkout_token}`

**Parameters**

| Name           | Type  | Required | Description                                               |
| :------------- | :---- | :------- | :-------------------------------------------------------- |
| checkout_token | `str` | ✅       | ID of the checkout page. String starting with checkout\_. |

**Return Type**

`InlineResponse200_27`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.checkout_page.get_hosted_page_payment(checkout_token="checkout_token")

print(result)
```

## generate_hosted_page_payment

Create a checkout page that makes a payment.

- HTTP Method: `POST`
- Endpoint: `/v1/checkout`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | `[V1CheckoutBody](../models/V1CheckoutBody.md)` | ❌       | The request body. |

**Return Type**

`InlineResponse200_28`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1CheckoutBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1CheckoutBody(
    account_funding_transaction={},
    amount=7.66,
    cart_items={
        "amount": 9.14,
        "name": "name",
        "quantity": 7.59,
        "image": "image"
    },
    country="GB",
    currency="GBP",
    customer="customer",
    escrow=True,
    escrow_release_days=7.22,
    id_="id",
    merchant_main_button="merchant_main_button",
    merchant_privacy_policy="merchant_privacy_policy",
    merchant_terms="merchant_terms",
    merchant_website="merchant_website",
    custom_elements={
        "save_card_default": False,
        "payment_fees_display": True,
        "billing_address_collect": True,
        "display_description": True,
        "merchant_currency_only": False,
        "cardholder_name": "cardholder_name",
        "cardholder_preferred_currency": "cardholder_preferred_currency",
        "dynamic_currency_conversion": False
    },
    page_expiration=8.45
)

result = sdk.checkout_page.generate_hosted_page_payment(request_body=request_body)

print(result)
```
