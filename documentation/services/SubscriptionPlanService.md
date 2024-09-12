# SubscriptionPlanService

A list of all methods in the `SubscriptionPlanService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description                                                                                                                                                                                     |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_plans](#list_plans)       | Retrieve a list of all plans. Use the optional query parameters to filter the results. You can filter the results further by specifying one or more Plan fields as additional query parameters. |
| [create_plan](#create_plan)     | Create a pricing plan for services.                                                                                                                                                             |
| [retrieve_plan](#retrieve_plan) | Retrieve the details of a pricing plan for services.                                                                                                                                            |
| [update_plan](#update_plan)     | Change or modify a pricing plan for services. You can update a plan's nickname or metadata.                                                                                                     |
| [delete_plan](#delete_plan)     | Delete a pricing plan for services.                                                                                                                                                             |

## list_plans

Retrieve a list of all plans. Use the optional query parameters to filter the results. You can filter the results further by specifying one or more Plan fields as additional query parameters.

- HTTP Method: `GET`
- Endpoint: `/v1/plans`

**Parameters**

| Name           | Type    | Required | Description                                                            |
| :------------- | :------ | :------- | :--------------------------------------------------------------------- |
| ending_before  | `float` | ❌       | The ID of the plan created after the last plan you want to retrieve.   |
| limit          | `float` | ❌       | The maximum number of plans to return. Range 1-100. Default is 10.     |
| starting_after | `str`   | ❌       | The ID of the plan created before the first plan you want to retrieve. |

**Return Type**

`InlineResponse200_58`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_plan.list_plans(
    ending_before=8.11,
    limit=4.41,
    starting_after="starting_after"
)

print(result)
```

## create_plan

Create a pricing plan for services.

- HTTP Method: `POST`
- Endpoint: `/v1/plans`

**Parameters**

| Name         | Type                                      | Required | Description       |
| :----------- | :---------------------------------------- | :------- | :---------------- |
| request_body | `[V1PlansBody](../models/V1PlansBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_59`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1PlansBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1PlansBody(
    aggregate_usage="aggregate_usage",
    amount=2.52,
    billing_scheme="billing_scheme",
    currency="currency",
    id_="id",
    interval="interval",
    interval_count=0.75,
    metadata={},
    nickname="nickname",
    product="product",
    tiers="tiers",
    tiers_mode="tiers_mode",
    transform_usage={},
    trial_period_days=7.87,
    usage_type="usage_type"
)

result = sdk.subscription_plan.create_plan(request_body=request_body)

print(result)
```

## retrieve_plan

Retrieve the details of a pricing plan for services.

- HTTP Method: `GET`
- Endpoint: `/v1/plans/{plan_id}`

**Parameters**

| Name    | Type  | Required | Description     |
| :------ | :---- | :------- | :-------------- |
| plan_id | `str` | ✅       | ID of the plan. |

**Return Type**

`InlineResponse200_59`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_plan.retrieve_plan(plan_id="plan_id")

print(result)
```

## update_plan

Change or modify a pricing plan for services. You can update a plan's nickname or metadata.

- HTTP Method: `POST`
- Endpoint: `/v1/plans/{plan_id}`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | `[PlansPlanIdBody](../models/PlansPlanIdBody.md)` | ✅       | The request body. |
| plan_id      | `str`                                             | ✅       | ID of the plan.   |

**Return Type**

`InlineResponse200_59`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import PlansPlanIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PlansPlanIdBody(
    metadata={},
    nickname="nickname"
)

result = sdk.subscription_plan.update_plan(
    request_body=request_body,
    plan_id="plan_id"
)

print(result)
```

## delete_plan

Delete a pricing plan for services.

- HTTP Method: `DELETE`
- Endpoint: `/v1/plans/{plan_id}`

**Parameters**

| Name    | Type  | Required | Description     |
| :------ | :---- | :------- | :-------------- |
| plan_id | `str` | ✅       | ID of the plan. |

**Return Type**

`InlineResponse200_60`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_plan.delete_plan(plan_id="plan_id")

print(result)
```
