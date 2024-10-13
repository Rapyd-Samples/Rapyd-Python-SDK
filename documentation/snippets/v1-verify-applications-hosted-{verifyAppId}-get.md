```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.verify.get_hosted_application_by_token(verify_app_id="verifyAppId")

print(result)

```
