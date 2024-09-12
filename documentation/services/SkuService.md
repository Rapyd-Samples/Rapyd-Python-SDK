# SkuService

A list of all methods in the `SkuService` service. Click on the method name to view detailed information about that method.

| Methods                       | Description                               |
| :---------------------------- | :---------------------------------------- |
| [retrieve_sku](#retrieve_sku) | Retrieve the details of an SKU.           |
| [update_sku](#update_sku)     | Change or modify an SKU.                  |
| [delete_sku](#delete_sku)     | Delete an SKU from the Rapyd platform.    |
| [list_sku](#list_sku)         | Retrieve a list of all SKUs.              |
| [create_sku](#create_sku)     | Create an SKU and attach it to a product. |

## retrieve_sku

Retrieve the details of an SKU.

- HTTP Method: `GET`
- Endpoint: `/v1/skus/{skuId}`

**Parameters**

| Name   | Type  | Required | Description                                         |
| :----- | :---- | :------- | :-------------------------------------------------- |
| sku_id | `str` | ✅       | ID of the 'sku' object. String starting with sku\_. |

**Return Type**

`InlineResponse200_72`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.sku.retrieve_sku(sku_id="skuId")

print(result)
```

## update_sku

Change or modify an SKU.

- HTTP Method: `POST`
- Endpoint: `/v1/skus/{skuId}`

**Parameters**

| Name         | Type                                          | Required | Description                                         |
| :----------- | :-------------------------------------------- | :------- | :-------------------------------------------------- |
| request_body | `[SkusSkuIdBody](../models/SkusSkuIdBody.md)` | ❌       | The request body.                                   |
| sku_id       | `str`                                         | ✅       | ID of the 'sku' object. String starting with sku\_. |

**Return Type**

`InlineResponse200_72`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import SkusSkuIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SkusSkuIdBody(
    currency="GBP",
    inventory={
        "type_": "finite",
        "quantity": 9,
        "value": "in_stock"
    },
    price=3.63,
    product="product",
    active=True,
    attributes=[
        "attributes"
    ],
    image="image",
    metadata={},
    package_dimensions={
        "length": 3.17,
        "height": 6.46,
        "weight": 2.6,
        "width": 2.52
    }
)

result = sdk.sku.update_sku(
    request_body=request_body,
    sku_id="skuId"
)

print(result)
```

## delete_sku

Delete an SKU from the Rapyd platform.

- HTTP Method: `DELETE`
- Endpoint: `/v1/skus/{skuId}`

**Parameters**

| Name   | Type  | Required | Description                                         |
| :----- | :---- | :------- | :-------------------------------------------------- |
| sku_id | `str` | ✅       | ID of the 'sku' object. String starting with sku\_. |

**Return Type**

`InlineResponse200_73`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.sku.delete_sku(sku_id="skuId")

print(result)
```

## list_sku

Retrieve a list of all SKUs.

- HTTP Method: `GET`
- Endpoint: `/v1/skus`

**Parameters**

| Name           | Type    | Required | Description                                                                         |
| :------------- | :------ | :------- | :---------------------------------------------------------------------------------- |
| active         | `bool`  | ❌       | Determines whether the query returns active SKUs or inactive SKUs. Default is true. |
| starting_after | `float` | ❌       | The ID of the SKU created before the first SKU you want to retrieve.                |
| ending_before  | `float` | ❌       | The ID of the SKU created after the last SKU you want to retrieve.                  |
| limit          | `float` | ❌       | The maximum number of SKUs to return. Range 1-100. Default is 10.                   |

**Return Type**

`InlineResponse200_74`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.sku.list_sku(
    active=False,
    starting_after=9.68,
    ending_before=5.31,
    limit=1.17
)

print(result)
```

## create_sku

Create an SKU and attach it to a product.

- HTTP Method: `POST`
- Endpoint: `/v1/skus`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | `[V1SkusBody](../models/V1SkusBody.md)` | ❌       | The request body. |

**Return Type**

`InlineResponse200_72`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1SkusBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1SkusBody(
    currency="GBP",
    inventory={
        "type_": "finite",
        "quantity": 9,
        "value": "in_stock"
    },
    price=1.08,
    product="product",
    active=False,
    attributes=[
        "attributes"
    ],
    image="image",
    metadata={},
    package_dimensions={
        "length": 3.17,
        "height": 6.46,
        "weight": 2.6,
        "width": 2.52
    }
)

result = sdk.sku.create_sku(request_body=request_body)

print(result)
```
