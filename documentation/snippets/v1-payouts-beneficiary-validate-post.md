```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import BeneficiaryValidateBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = BeneficiaryValidateBody(
    amount=3.71,
    beneficiary="ut in",
    identifier_type="identifier_type",
    identifier_value="identifier_value",
    payout_method_type="us_general_bank",
    sender_country="repre",
    sender_currency="HRK",
    sender_entity_type="company"
)

result = sdk.disburse.validate_beneficiary(request_body=request_body)

print(result)

```
