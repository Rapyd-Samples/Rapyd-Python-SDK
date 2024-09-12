```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.checkout_page.get_hosted_page_payment(checkout_token="checkout_token")

print(result)

```
