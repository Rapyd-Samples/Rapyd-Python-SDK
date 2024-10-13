```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import ApplePayObject

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ApplePayObject(
    display_name="display_name",
    initiative_context="initiative_context"
)

result = sdk.digital_wallet.get_apple_pay_session(request_body=request_body)

print(result)

```
