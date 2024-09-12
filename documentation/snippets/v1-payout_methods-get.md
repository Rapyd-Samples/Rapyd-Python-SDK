```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.disburse.get_payout_method_types(
    sender_entity_type="sender_entity_type",
    beneficiary_country="beneficiary_country",
    payout_currency="payout_currency",
    sender_currency="sender_currency",
    sender_country="sender_country",
    beneficiary_entity_type="beneficiary_entity_type",
    category="category",
    is_cancelable=True,
    is_location_specific=True,
    is_expirable=False,
    starting_after="starting_after",
    ending_before="ending_before",
    limit="limit"
)

print(result)

```
