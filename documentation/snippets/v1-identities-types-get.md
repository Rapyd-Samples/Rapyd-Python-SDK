```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.verify.get_kyc_id_verification_supported_doc_types(country="GB")

print(result)

```
