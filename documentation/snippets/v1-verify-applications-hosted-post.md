```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import ApplicationsHostedBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ApplicationsHostedBody(
    application_type="application_type",
    country="country",
    rapyd_entity_token="ewallet_ef84c580177dbfc4293b1cf73c73fc77",
    phone_number="phone_number",
    metadata={},
    client_reference_id="client_reference_id",
    cancel_url="cancel_url",
    complete_url="complete_url"
)

result = sdk.verify.create_hosted_application_token(request_body=request_body)

print(result)

```
