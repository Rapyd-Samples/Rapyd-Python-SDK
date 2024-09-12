```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PayoutsSenderBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PayoutsSenderBody(
    company_name="ABC",
    country="GB",
    currency="GBP",
    entity_type="company",
    first_name="Scott",
    identification_type="drivers_license",
    identification_value="ANDSFS8974562",
    last_name="Williams"
)

result = sdk.disburse.create_sender(request_body=request_body)

print(result)

```
