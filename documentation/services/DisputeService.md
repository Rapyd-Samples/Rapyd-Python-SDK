# DisputeService

A list of all methods in the `DisputeService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                    |
| :---------------------------------------------------------- | :--------------------------------------------- |
| [get_disputes_list_by_org_id](#get_disputes_list_by_org_id) | Retrieve a detailed list of 'dispute' objects. |
| [get_dispute](#get_dispute)                                 | Retrieve the details of a dispute.             |

## get_disputes_list_by_org_id

Retrieve a detailed list of 'dispute' objects.

- HTTP Method: `GET`
- Endpoint: `/v1/disputes`

**Parameters**

| Name           | Type                                                                        | Required | Description                                                                                                  |
| :------------- | :-------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------- |
| starting_after | `str`                                                                       | ❌       | The ID of the dispute created before the first dispute you want to retrieve. String starting with dispute\_. |
| ending_before  | `str`                                                                       | ❌       | The ID of the dispute created after the last dispute you want to retrieve. String starting with dispute\_.   |
| limit          | `str`                                                                       | ❌       | The maximum number of disputes to return. Range is 1-100. Default is 10.                                     |
| status         | `[GetDisputesListByOrgIdStatus](../models/GetDisputesListByOrgIdStatus.md)` | ❌       | Filters the list for disputes with the specified dispute status.                                             |
| payment        | `str`                                                                       | ❌       | The ID of the payment that is linked to the dispute. String starting with payment\_.                         |

**Return Type**

`InlineResponse200_41`

**Example Usage Code Snippet**

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
    limit="6",
    status="ACT",
    payment="payment"
)

print(result)
```

## get_dispute

Retrieve the details of a dispute.

- HTTP Method: `GET`
- Endpoint: `/v1/disputes/{disputeId}`

**Parameters**

| Name       | Type  | Required | Description                                                             |
| :--------- | :---- | :------- | :---------------------------------------------------------------------- |
| dispute_id | `str` | ✅       | ID of the dispute you want to retrieve. String starting with dispute\_. |

**Return Type**

`InlineResponse200_42`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.dispute.get_dispute(dispute_id="disputeId")

print(result)
```
