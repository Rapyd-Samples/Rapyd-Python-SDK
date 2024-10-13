```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1PayoutsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1PayoutsBody(
    beneficiary="proident id ",
    beneficiary_country="US",
    beneficiary_entity_type="individual",
    confirm_automatically=True,
    converstion_rate=1,
    description="description",
    ewallet="ewallet_4f1757749b8858160274e6db49f78ff3",
    expiration="1607941348",
    location="location",
    merchant_reference_id="GHY-0YU-HUJ-POI",
    metadata={},
    payout_amount=110,
    payout_currency="DZD",
    payout_method_type="us_general_bank",
    payout_options={},
    sender="incididunt sed",
    sender_country="commodo sint ",
    sender_currency="LRD",
    sender_entity_type="company",
    statement_descriptor="statement_descriptor"
)

result = sdk.disburse.create_payout(request_body=request_body)

print(result)

```
