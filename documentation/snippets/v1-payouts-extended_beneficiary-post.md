```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PayoutsExtendedBeneficiaryBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PayoutsExtendedBeneficiaryBody(
    address="123 East 32nd street",
    city="anytown",
    category="bank",
    company_name="All Star Limousine Service",
    country="ipsum",
    country_of_incorporation="IT",
    currency="HUF",
    date_of_birth="05/03/1967",
    date_of_incorporation="05/03/1967",
    default_payout_method_type="us_general_bank",
    entity_type="company",
    first_name="John",
    gender="male",
    identification_type="drivers_license",
    identification_value="ABNHDLK354665",
    last_name="John",
    merchant_reference_id="GHY-0YU-HUJ-POI",
    nationality="SG"
)

result = sdk.disburse.create_extended_beneficiary(request_body=request_body)

print(result)

```
