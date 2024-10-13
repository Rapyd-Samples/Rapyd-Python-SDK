```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import GetDisputesListByOrgIdStatus

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.dispute.get_disputes_list_by_org_id(
    starting_after="starting_after",
    ending_before="ending_before",
    limit="9",
    status="ACT",
    payment="payment"
)

print(result)

```
