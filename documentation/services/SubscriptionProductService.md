# SubscriptionProductService

A list of all methods in the `SubscriptionProductService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                                                                                         |
| :-------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| [get_products_list](#get_products_list) | Retrieve a list of all products.                                                                    |
| [create_product](#create_product)       | Create goods or services.                                                                           |
| [get_product](#get_product)             | Retrieve details of a product or service.                                                           |
| [update_product](#update_product)       | Change or modify a product or service.                                                              |
| [delete_product](#delete_product)       | Delete a product or service from the Rapyd platform. This action also deletes all associated plans. |

## get_products_list

Retrieve a list of all products.

- HTTP Method: `GET`
- Endpoint: `/v1/products`

**Parameters**

| Name           | Type | Required | Description                                                                   |
| :------------- | :--- | :------- | :---------------------------------------------------------------------------- |
| ending_before  | str  | ❌       | The ID of the products created after the last product you want to retrieve.   |
| limit          | str  | ❌       | The maximum number of products to return. Range 1-100. Default is 10.         |
| starting_after | str  | ❌       | The ID of the product created before the first products you want to retrieve. |

**Return Type**

`InlineResponse200_72`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_product.get_products_list(
    ending_before="ending_before",
    limit="limit",
    starting_after="starting_after"
)

print(result)
```

## create_product

Create goods or services.

- HTTP Method: `POST`
- Endpoint: `/v1/products`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [V1ProductsBody](../models/V1ProductsBody.md) | ✅       | The request body. |

**Return Type**

`InlineResponse200_73`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1ProductsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1ProductsBody(
    active=True,
    attributes=[
        "attributes"
    ],
    description="description",
    id_="id",
    images=[
        "images"
    ],
    metadata={},
    name="name",
    package_dimensions={
        "height": 1.62,
        "length": 4.73,
        "weight": 6.81,
        "width": 0.63
    },
    shippable=False,
    statement_descriptor="statement_descriptor",
    type_="services",
    unit_label="unit_label"
)

result = sdk.subscription_product.create_product(request_body=request_body)

print(result)
```

## get_product

Retrieve details of a product or service.

- HTTP Method: `GET`
- Endpoint: `/v1/products/{productsId}`

**Parameters**

| Name        | Type | Required | Description        |
| :---------- | :--- | :------- | :----------------- |
| products_id | str  | ✅       | ID of the product. |

**Return Type**

`InlineResponse200_73`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_product.get_product(products_id="productsId")

print(result)
```

## update_product

Change or modify a product or service.

- HTTP Method: `POST`
- Endpoint: `/v1/products/{productsId}`

**Parameters**

| Name         | Type                                                          | Required | Description        |
| :----------- | :------------------------------------------------------------ | :------- | :----------------- |
| request_body | [ProductsProductsIdBody](../models/ProductsProductsIdBody.md) | ❌       | The request body.  |
| products_id  | str                                                           | ✅       | ID of the product. |

**Return Type**

`InlineResponse200_73`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import ProductsProductsIdBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ProductsProductsIdBody(
    active=False,
    attributes=[
        "attributes"
    ],
    metadata={},
    name="name",
    package_dimensions={
        "height": 1.62,
        "length": 4.73,
        "weight": 6.81,
        "width": 0.63
    },
    statement_descriptor="statement_descriptor",
    unit_label="unit_label"
)

result = sdk.subscription_product.update_product(
    request_body=request_body,
    products_id="productsId"
)

print(result)
```

## delete_product

Delete a product or service from the Rapyd platform. This action also deletes all associated plans.

- HTTP Method: `DELETE`
- Endpoint: `/v1/products/{productsId}`

**Parameters**

| Name        | Type | Required | Description        |
| :---------- | :--- | :------- | :----------------- |
| products_id | str  | ✅       | ID of the product. |

**Return Type**

`InlineResponse200_71`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.subscription_product.delete_product(products_id="productsId")

print(result)
```
