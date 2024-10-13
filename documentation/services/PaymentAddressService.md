# PaymentAddressService

A list of all methods in the `PaymentAddressService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                                                    |
| :-------------------------------- | :----------------------------------------------------------------------------- |
| [create_address](#create_address) | Create an address.                                                             |
| [get_address](#get_address)       | Retrieve an address.                                                           |
| [update_address](#update_address) | Change or modify an address. To clear a field, set it to an empty string.      |
| [delete_address](#delete_address) | Remove an address that is linked to a customer or is not linked to any object. |

## create_address

Create an address.

- HTTP Method: `POST`
- Endpoint: `/v1/addresses`

**Parameters**

| Name         | Type                            | Required | Description       |
| :----------- | :------------------------------ | :------- | :---------------- |
| request_body | [Address](../models/Address.md) | ❌       | The request body. |

**Return Type**

`InlineResponse200_64`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Address

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = Address(
    canton="canton",
    city="city",
    country="dolore u",
    created_at=2.12,
    district="district",
    id_="id",
    line_1="line_1",
    line_2="line_2",
    line_3="line_3",
    metadata={},
    name="name",
    phone_number="phone_number",
    state="state",
    zip="zip"
)

result = sdk.payment_address.create_address(request_body=request_body)

print(result)
```

## get_address

Retrieve an address.

- HTTP Method: `GET`
- Endpoint: `/v1/addresses{addressId}`

**Parameters**

| Name       | Type | Required | Description                                                   |
| :--------- | :--- | :------- | :------------------------------------------------------------ |
| address_id | str  | ✅       | ID of the address object. String starting with **address\_**. |

**Return Type**

`InlineResponse200_64`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.payment_address.get_address(address_id="addressId")

print(result)
```

## update_address

Change or modify an address. To clear a field, set it to an empty string.

- HTTP Method: `POST`
- Endpoint: `/v1/addresses{addressId}`

**Parameters**

| Name         | Type                            | Required | Description                                                   |
| :----------- | :------------------------------ | :------- | :------------------------------------------------------------ |
| request_body | [Address](../models/Address.md) | ✅       | The request body.                                             |
| address_id   | str                             | ✅       | ID of the address object. String starting with **address\_**. |

**Return Type**

`InlineResponse200_64`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Address

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = Address(
    canton="canton",
    city="city",
    country="dolore u",
    created_at=2.12,
    district="district",
    id_="id",
    line_1="line_1",
    line_2="line_2",
    line_3="line_3",
    metadata={},
    name="name",
    phone_number="phone_number",
    state="state",
    zip="zip"
)

result = sdk.payment_address.update_address(
    request_body=request_body,
    address_id="addressId"
)

print(result)
```

## delete_address

Remove an address that is linked to a customer or is not linked to any object.

- HTTP Method: `DELETE`
- Endpoint: `/v1/addresses{addressId}`

**Parameters**

| Name       | Type | Required | Description                                                   |
| :--------- | :--- | :------- | :------------------------------------------------------------ |
| address_id | str  | ✅       | ID of the address object. String starting with **address\_**. |

**Return Type**

`InlineResponse200_64`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.payment_address.delete_address(address_id="addressId")

print(result)
```
