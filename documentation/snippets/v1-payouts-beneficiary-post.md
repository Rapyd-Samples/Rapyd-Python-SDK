```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PayoutsBeneficiaryBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PayoutsBeneficiaryBody(
    category="bank",
    company_name="ABC",
    country="GB",
    currency="GBP",
    default_payout_method_type="us_general_bank",
    entity_type="company",
    first_name="John",
    identification_type="drivers_license",
    identification_value="ABNHDLK354665",
    last_name="John",
    merchant_reference_id="GHY-0YU-HUJ-POI"
)

result = sdk.disburse.create_beneficiary(request_body=request_body)

print(result)

```
