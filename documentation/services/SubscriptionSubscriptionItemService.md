# SubscriptionSubscriptionItemService

A list of all methods in the `SubscriptionSubscriptionItemService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                                                                                         |
| :------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------- |
| [list_subscription_item](#list_subscription_item)                               | Retrieve a list of all subscription items for a subscription.                                                                       |
| [create_subscription_item](#create_subscription_item)                           | Create a subscription item and add it to an existing subscription for recurring payment.                                            |
| [retrieve_subscription_item](#retrieve_subscription_item)                       | Retrieve the details of a subscription item.                                                                                        |
| [update_subscription_item](#update_subscription_item)                           | Change or modify a subscription item.                                                                                               |
| [delete_subscription_item](#delete_subscription_item)                           | Delete a subscription item from the Rapyd platform.                                                                                 |
| [usage_record_summaries](#usage_record_summaries)                               | Retrieve a list of usage records for a subscription item                                                                            |
| [create_subscription_item_usage_record](#create_subscription_item_usage_record) | Create a usage record or update an existing usage record where its unique identifier is composed of timestamp and subscription_item |

## list_subscription_item

Retrieve a list of all subscription items for a subscription.

- HTTP Method: `GET`
- Endpoint: `/v1/subscription_items`

**Parameters**

| Name           | Type  | Required | Description                                                                                      |
| :------------- | :---- | :------- | :----------------------------------------------------------------------------------------------- |
| ending_before  | float | ❌       | The ID of the subscription item created after the last subscription item you want to retrieve.   |
| limit          | float | ❌       | The maximum number of subscription items to return. Range 1-100. Default is 10.                  |
| starting_after | str   | ❌       | The ID of the subscription item created before the first subscription item you want to retrieve. |
| subscription   | str   | ❌       | ID of the subscription.                                                                          |

**Return Type**

`InlineResponse200_77`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_subscription_item.list_subscription_item(
    ending_before=0.05,
    limit=7.77,
    starting_after="starting_after",
    subscription="subscription"
)

print(result)
```

## create_subscription_item

Create a subscription item and add it to an existing subscription for recurring payment.

- HTTP Method: `POST`
- Endpoint: `/v1/subscription_items`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [V1SubscriptionItemsBody](../models/V1SubscriptionItemsBody.md) | ✅       | The request body. |

**Return Type**

`InlineResponse200_78`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1SubscriptionItemsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1SubscriptionItemsBody(
    metadata={},
    plan="plan",
    prorate=False,
    proration_date=8.16,
    quantity=2.99,
    subscription="subscription"
)

result = sdk.subscription_subscription_item.create_subscription_item(request_body=request_body)

print(result)
```

## retrieve_subscription_item

Retrieve the details of a subscription item.

- HTTP Method: `GET`
- Endpoint: `/v1/subscription_items/{subscriptionItemId}`

**Parameters**

| Name                 | Type | Required | Description                                                   |
| :------------------- | :--- | :------- | :------------------------------------------------------------ |
| subscription_item_id | str  | ✅       | ID of the subscription item. String starting with **subi\_**. |

**Return Type**

`InlineResponse200_78`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_subscription_item.retrieve_subscription_item(subscription_item_id="subscriptionItemId")

print(result)
```

## update_subscription_item

Change or modify a subscription item.

- HTTP Method: `POST`
- Endpoint: `/v1/subscription_items/{subscriptionItemId}`

**Parameters**

| Name                 | Type                                                                                            | Required | Description                                                   |
| :------------------- | :---------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------ |
| request_body         | [SubscriptionItemsSubscriptionItemIdBody](../models/SubscriptionItemsSubscriptionItemIdBody.md) | ✅       | The request body.                                             |
| subscription_item_id | str                                                                                             | ✅       | ID of the subscription item. String starting with **subi\_**. |

**Return Type**

`InlineResponse200_78`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import SubscriptionItemsSubscriptionItemIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SubscriptionItemsSubscriptionItemIdBody(
    metadata={},
    prorate=True,
    proration_date=8.99,
    quantity=8.22
)

result = sdk.subscription_subscription_item.update_subscription_item(
    request_body=request_body,
    subscription_item_id="subscriptionItemId"
)

print(result)
```

## delete_subscription_item

Delete a subscription item from the Rapyd platform.

- HTTP Method: `DELETE`
- Endpoint: `/v1/subscription_items/{subscriptionItemId}`

**Parameters**

| Name                 | Type | Required | Description                                                   |
| :------------------- | :--- | :------- | :------------------------------------------------------------ |
| subscription_item_id | str  | ✅       | ID of the subscription item. String starting with **subi\_**. |

**Return Type**

`InlineResponse200_79`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_subscription_item.delete_subscription_item(subscription_item_id="subscriptionItemId")

print(result)
```

## usage_record_summaries

Retrieve a list of usage records for a subscription item

- HTTP Method: `GET`
- Endpoint: `/v1/subscription_items/{subscriptionItemId}/usage_record_summaries`

**Parameters**

| Name                 | Type  | Required | Description                                                                           |
| :------------------- | :---- | :------- | :------------------------------------------------------------------------------------ |
| subscription_item_id | str   | ✅       | ID of the subscription item. String starting with **subi\_**.                         |
| limit                | float | ❌       | The maximum number of usage records that are returned. Range is 1-100. Default is 10. |
| ending_before        | float | ❌       | The latest date and time of the returned usage records. Format is in Unix time.       |
| starting_after       | float | ❌       | The earliest date and time of the returned usage records. Format is in Unix time.     |

**Return Type**

`InlineResponse200_80`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_subscription_item.usage_record_summaries(
    subscription_item_id="subscriptionItemId",
    limit=3.23,
    ending_before=6.55,
    starting_after=4.66
)

print(result)
```

## create_subscription_item_usage_record

Create a usage record or update an existing usage record where its unique identifier is composed of timestamp and subscription_item

- HTTP Method: `POST`
- Endpoint: `/v1/subscription_items/{subscriptionItemId}/usage_records`

**Parameters**

| Name                 | Type                                                                                  | Required | Description                                                   |
| :------------------- | :------------------------------------------------------------------------------------ | :------- | :------------------------------------------------------------ |
| request_body         | [SubscriptionItemIdUsageRecordsBody](../models/SubscriptionItemIdUsageRecordsBody.md) | ✅       | The request body.                                             |
| subscription_item_id | str                                                                                   | ✅       | ID of the subscription item. String starting with **subi\_**. |

**Return Type**

`InlineResponse200_81`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import SubscriptionItemIdUsageRecordsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SubscriptionItemIdUsageRecordsBody(
    action="action",
    metadata={},
    quantity=5.56,
    timestamp=1.86
)

result = sdk.subscription_subscription_item.create_subscription_item_usage_record(
    request_body=request_body,
    subscription_item_id="subscriptionItemId"
)

print(result)
```
