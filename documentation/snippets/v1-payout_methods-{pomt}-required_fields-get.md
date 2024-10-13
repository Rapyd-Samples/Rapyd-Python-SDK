```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.get_payout_method_types_details(
    pomt="pomt",
    beneficiary_country="beneficiary_country",
    beneficiary_entity_type="beneficiary_entity_type",
    payout_amount=0.8,
    payout_currency="payout_currency",
    sender_country="sender_country",
    sender_currency="sender_currency",
    sender_entity_type="sender_entity_type"
)

print(result)

```
