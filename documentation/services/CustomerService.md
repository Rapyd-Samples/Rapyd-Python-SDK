# CustomerService

A list of all methods in the `CustomerService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                                                       |
| :---------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_customer](#list_customer)                       | Retrieve a list of all customers                                                                                                                                                                                  |
| [create_customer](#create_customer)                   | Adds a customer to merchant                                                                                                                                                                                       |
| [retrieve_customer](#retrieve_customer)               | Retrieve a customer                                                                                                                                                                                               |
| [update_customer](#update_customer)                   | Update a customer with customer Id in Path                                                                                                                                                                        |
| [delete_customer](#delete_customer)                   | This method triggers the Customer Deleted webhook. This webhook contains the same information as the response                                                                                                     |
| [delete_customer_discount](#delete_customer_discount) | Delete the discount that has been assigned to a customer through a coupon. This action does not affect the coupon that the discount was derived from. This method triggers the Customer Discount Deleted webhook. |

## list_customer

Retrieve a list of all customers

- HTTP Method: `GET`
- Endpoint: `/v1/customers`

**Parameters**

| Name           | Type  | Required | Description                                                                   |
| :------------- | :---- | :------- | :---------------------------------------------------------------------------- |
| starting_after | `str` | ❌       | The ID of the customer created before the first customer you want to retrieve |
| ending_before  | `str` | ❌       | The ID of the customer created after the last customer you want to retrieve   |
| limit          | `str` | ❌       | The maximum number of customers to return. Range is 1-100. Default is 10      |

**Return Type**

`InlineResponse200_33`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer.list_customer(
    starting_after="starting_after",
    ending_before="ending_before",
    limit="100"
)

print(result)
```

## create_customer

Adds a customer to merchant

- HTTP Method: `POST`
- Endpoint: `/v1/customers`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | `[V1CustomersBody](../models/V1CustomersBody.md)` | ✅       | The request body. |

**Return Type**

`InlineResponse200_34`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1CustomersBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1CustomersBody(
    addresses=[
        {
            "canton": "canton",
            "city": "city",
            "country": "GB",
            "created_at": 3.34,
            "district": "district",
            "id_": "id",
            "line_1": "line_1",
            "line_2": "line_2",
            "line_3": "line_3",
            "metadata": {},
            "name": "name",
            "phone_number": "phone_number",
            "state": "state",
            "zip": "zip"
        }
    ],
    business_vat_id="business_vat_id",
    coupon="coupon",
    default_payment_method="default_payment_method",
    description="description",
    email="email",
    ewallet="ewallet",
    invoice_prefix="invoice_prefix",
    metadata={},
    name="name",
    phone_number="phone_number"
)

result = sdk.customer.create_customer(request_body=request_body)

print(result)
```

## retrieve_customer

Retrieve a customer

- HTTP Method: `GET`
- Endpoint: `/v1/customers/{customerId}`

**Parameters**

| Name        | Type  | Required | Description |
| :---------- | :---- | :------- | :---------- |
| customer_id | `str` | ✅       | customer Id |

**Return Type**

`InlineResponse200_35`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer.retrieve_customer(customer_id="customerId")

print(result)
```

## update_customer

Update a customer with customer Id in Path

- HTTP Method: `POST`
- Endpoint: `/v1/customers/{customerId}`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | `[CustomerRequest](../models/CustomerRequest.md)` | ❌       | The request body. |
| customer_id  | `str`                                             | ✅       | customer Id       |

**Return Type**

`InlineResponse200_35`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CustomerRequest

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CustomerRequest(
    addresses=[
        {
            "canton": "canton",
            "city": "city",
            "country": "GB",
            "created_at": 3.34,
            "district": "district",
            "id_": "id",
            "line_1": "line_1",
            "line_2": "line_2",
            "line_3": "line_3",
            "metadata": {},
            "name": "name",
            "phone_number": "phone_number",
            "state": "state",
            "zip": "zip"
        }
    ],
    business_vat_id="business_vat_id",
    coupon="coupon",
    default_payment_method="default_payment_method",
    description="description",
    email="email",
    ewallet="ewallet",
    invoice_prefix="invoice_prefix",
    metadata={},
    name="name",
    phone_number="phone_number"
)

result = sdk.customer.update_customer(
    request_body=request_body,
    customer_id="customerId"
)

print(result)
```

## delete_customer

This method triggers the Customer Deleted webhook. This webhook contains the same information as the response

- HTTP Method: `DELETE`
- Endpoint: `/v1/customers/{customerId}`

**Parameters**

| Name        | Type  | Required | Description |
| :---------- | :---- | :------- | :---------- |
| customer_id | `str` | ✅       | customer Id |

**Return Type**

`InlineResponse200_36`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer.delete_customer(customer_id="customerId")

print(result)
```

## delete_customer_discount

Delete the discount that has been assigned to a customer through a coupon. This action does not affect the coupon that the discount was derived from. This method triggers the Customer Discount Deleted webhook.

- HTTP Method: `DELETE`
- Endpoint: `/v1/customers/{customerId}/discount`

**Parameters**

| Name        | Type  | Required | Description |
| :---------- | :---- | :------- | :---------- |
| customer_id | `str` | ✅       | customer Id |

**Return Type**

`InlineResponse200_36`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer.delete_customer_discount(customer_id="customerId")

print(result)
```
