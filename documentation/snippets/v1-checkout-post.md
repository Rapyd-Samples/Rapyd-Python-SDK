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
