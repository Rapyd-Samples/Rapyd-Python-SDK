# CouponService

A list of all methods in the `CouponService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description                                                                                                                                                                                           |
| :---------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_coupon](#list_coupon)         | Retrieve a list of all coupons                                                                                                                                                                        |
| [create_coupon](#create_coupon)     | create a coupon                                                                                                                                                                                       |
| [retrieve_coupon](#retrieve_coupon) | Retrieve a coupon                                                                                                                                                                                     |
| [update_coupon](#update_coupon)     | Modify the metadata of a coupon with coupon Id in Path                                                                                                                                                |
| [delete_coupon](#delete_coupon)     | Delete a coupon from the Rapyd platform. Deleting a coupon removes it from all customers and subscriptions, but does not affect invoices and payment authorizations that have already been calculated |

## list_coupon

Retrieve a list of all coupons

- HTTP Method: `GET`
- Endpoint: `/v1/coupons`

**Parameters**

| Name           | Type  | Required | Description                                                               |
| :------------- | :---- | :------- | :------------------------------------------------------------------------ |
| starting_after | `str` | ❌       | The ID of the coupon created before the first coupon you want to retrieve |
| ending_before  | `str` | ❌       | The ID of the coupon created after the last coupon you want to retrieve   |
| limit          | `str` | ❌       | The maximum number of coupons to return. Range is 1-100. Default is 10    |

**Return Type**

`InlineResponse200_29`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.coupon.list_coupon(
    starting_after="starting_after",
    ending_before="ending_before",
    limit="1"
)

print(result)
```

## create_coupon

create a coupon

- HTTP Method: `POST`
- Endpoint: `/v1/coupons`

**Parameters**

| Name         | Type                            | Required | Description       |
| :----------- | :------------------------------ | :------- | :---------------- |
| request_body | `[Coupon](../models/Coupon.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_30`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Coupon

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = Coupon(
    amount_off=0.13,
    created=1671697165,
    currency="GBP",
    description="Sample Coupon 1",
    discount_duration_in_uses=2,
    discount_valid_until=7.67,
    discount_validity_in_months=2,
    duration="forever",
    duration_in_months=3,
    id_="coupon_c1194a18a9972ca7f9804826f00c9eb8",
    max_redemptions=2,
    metadata={},
    percent_off=10,
    redeem_by=0.44,
    times_redeemed=6.69,
    valid=True
)

result = sdk.coupon.create_coupon(request_body=request_body)

print(result)
```

## retrieve_coupon

Retrieve a coupon

- HTTP Method: `GET`
- Endpoint: `/v1/coupons/{couponId}`

**Parameters**

| Name      | Type  | Required | Description                               |
| :-------- | :---- | :------- | :---------------------------------------- |
| coupon_id | `str` | ✅       | coupon Id. String starting with coupon\_. |

**Return Type**

`InlineResponse200_31`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.coupon.retrieve_coupon(coupon_id="couponId")

print(result)
```

## update_coupon

Modify the metadata of a coupon with coupon Id in Path

- HTTP Method: `POST`
- Endpoint: `/v1/coupons/{couponId}`

**Parameters**

| Name         | Type                            | Required | Description                               |
| :----------- | :------------------------------ | :------- | :---------------------------------------- |
| request_body | `[Coupon](../models/Coupon.md)` | ✅       | The request body.                         |
| coupon_id    | `str`                           | ✅       | coupon Id. String starting with coupon\_. |

**Return Type**

`InlineResponse200_31`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Coupon

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = Coupon(
    amount_off=0.13,
    created=1671697165,
    currency="GBP",
    description="Sample Coupon 1",
    discount_duration_in_uses=2,
    discount_valid_until=7.67,
    discount_validity_in_months=2,
    duration="forever",
    duration_in_months=3,
    id_="coupon_c1194a18a9972ca7f9804826f00c9eb8",
    max_redemptions=2,
    metadata={},
    percent_off=10,
    redeem_by=0.44,
    times_redeemed=6.69,
    valid=True
)

result = sdk.coupon.update_coupon(
    request_body=request_body,
    coupon_id="couponId"
)

print(result)
```

## delete_coupon

Delete a coupon from the Rapyd platform. Deleting a coupon removes it from all customers and subscriptions, but does not affect invoices and payment authorizations that have already been calculated

- HTTP Method: `DELETE`
- Endpoint: `/v1/coupons/{couponId}`

**Parameters**

| Name      | Type  | Required | Description                               |
| :-------- | :---- | :------- | :---------------------------------------- |
| coupon_id | `str` | ✅       | coupon Id. String starting with coupon\_. |

**Return Type**

`InlineResponse200_32`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.coupon.delete_coupon(coupon_id="couponId")

print(result)
```
