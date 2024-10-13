# CustomerPaymentMethodService

A list of all methods in the `CustomerPaymentMethodService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                                                   |
| :---------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| [get_customer_payment_methods](#get_customer_payment_methods)     | Retrieve payment methods for a customer                                                                                       |
| [create_customer_payment_method](#create_customer_payment_method) | Add a payment method to a customer profile                                                                                    |
| [get_customer_payment_method](#get_customer_payment_method)       | Retrieve a payment method for a specific customer                                                                             |
| [update_customer_payment_method](#update_customer_payment_method) | Change or modify a payment method that was stored in a customer profile                                                       |
| [delete_customer_payment_method](#delete_customer_payment_method) | This method triggers the Webhook - Payment Method Canceled webhook. This webhook contains more information than the response. |

## get_customer_payment_methods

Retrieve payment methods for a customer

- HTTP Method: `GET`
- Endpoint: `/v1/customers/{customerId}/payment_methods`

**Parameters**

| Name           | Type                              | Required | Description                                                               |
| :------------- | :-------------------------------- | :------- | :------------------------------------------------------------------------ |
| customer_id    | str                               | ✅       | customer Id                                                               |
| category       | [Category](../models/Category.md) | ❌       |                                                                           |
| starting_after | str                               | ❌       | The ID of the coupon created before the first coupon you want to retrieve |
| ending_before  | str                               | ❌       | The ID of the coupon created after the last coupon you want to retrieve   |
| limit          | str                               | ❌       | The maximum number of coupons to return. Range is 1-100. Default is 10    |
| type\_         | str                               | ❌       | The type of payment method to find.                                       |

**Return Type**

`InlineResponse200_43`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Category

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer_payment_method.get_customer_payment_methods(
    customer_id="customerId",
    category="bank",
    starting_after="starting_after",
    ending_before="ending_before",
    limit="limit",
    type_="type"
)

print(result)
```

## create_customer_payment_method

Add a payment method to a customer profile

- HTTP Method: `POST`
- Endpoint: `/v1/customers/{customerId}/payment_methods`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [CustomerIdPaymentMethodsBody](../models/CustomerIdPaymentMethodsBody.md) | ✅       | The request body. |
| customer_id  | str                                                                       | ✅       | customer Id       |

**Return Type**

`InlineResponse200_44`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CustomerIdPaymentMethodsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CustomerIdPaymentMethodsBody(
    data={
        "amount_range_per_currency": [
            {
                "maximum_amount": 4.53,
                "minimum_amount": 0.65,
                "currency": "GBP"
            }
        ],
        "category": "bank",
        "country": "GB",
        "currencies": [
            "GBP"
        ],
        "fields": [
            {
                "code": "code",
                "is_required": False,
                "is_updatable": True,
                "instructions": "instructions",
                "name": "name",
                "numeric_code": "numeric_code",
                "required_fields": [
                    {
                        "code": "code",
                        "is_required": False,
                        "is_updatable": True,
                        "instructions": "instructions",
                        "name": "name",
                        "numeric_code": "numeric_code",
                        "type_": "boolean",
                        "regex": "regex",
                        "conditions": [
                            {
                                "description": "description",
                                "element_name": "element_name",
                                "operator": "operator",
                                "threshold_value": "reprehenderit "
                            }
                        ],
                        "description": "description"
                    }
                ],
                "type_": "boolean",
                "regex": "regex",
                "conditions": [
                    {
                        "description": "description",
                        "element_name": "element_name",
                        "operator": "operator",
                        "threshold_value": "reprehenderit "
                    }
                ],
                "description": "description"
            }
        ],
        "image": "image",
        "is_cancelable": True,
        "is_expirable": False,
        "is_online": True,
        "is_refundable": False,
        "is_tokenizable": False,
        "is_virtual": True,
        "maximum_expiration_seconds": 1.03,
        "minimum_expiration_seconds": 6.1,
        "multiple_overage_allowed": False,
        "name": "name",
        "payment_flow_type": "direct",
        "payment_options": [
            {
                "code": "code",
                "is_required": False,
                "is_updatable": True,
                "instructions": "instructions",
                "name": "name",
                "numeric_code": "numeric_code",
                "required_fields": [
                    {
                        "code": "code",
                        "is_required": False,
                        "is_updatable": True,
                        "instructions": "instructions",
                        "name": "name",
                        "numeric_code": "numeric_code",
                        "type_": "boolean",
                        "regex": "regex",
                        "conditions": [
                            {
                                "description": "description",
                                "element_name": "element_name",
                                "operator": "operator",
                                "threshold_value": "reprehenderit "
                            }
                        ],
                        "description": "description"
                    }
                ],
                "type_": "boolean",
                "regex": "regex",
                "conditions": [
                    {
                        "description": "description",
                        "element_name": "element_name",
                        "operator": "operator",
                        "threshold_value": "reprehenderit "
                    }
                ],
                "description": "description"
            }
        ],
        "status": "status",
        "supported_digital_wallet_providers": [
            "supported_digital_wallet_providers"
        ],
        "type_": "type",
        "virtual_payment_method_type": "virtual_payment_method_type",
        "is_restricted": True,
        "supports_subscription": False
    }
)

result = sdk.customer_payment_method.create_customer_payment_method(
    request_body=request_body,
    customer_id="customerId"
)

print(result)
```

## get_customer_payment_method

Retrieve a payment method for a specific customer

- HTTP Method: `GET`
- Endpoint: `/v1/customers/{customerId}/payment_methods/{pmtId}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| customer_id | str  | ✅       | customer Id |
| pmt_id      | str  | ✅       | Pmt Id      |

**Return Type**

`InlineResponse200_44`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer_payment_method.get_customer_payment_method(
    customer_id="customerId",
    pmt_id="pmtId"
)

print(result)
```

## update_customer_payment_method

Change or modify a payment method that was stored in a customer profile

- HTTP Method: `POST`
- Endpoint: `/v1/customers/{customerId}/payment_methods/{pmtId}`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [CustomerPaymentMethod](../models/CustomerPaymentMethod.md) | ✅       | The request body. |
| customer_id  | str                                                         | ✅       | customer Id       |
| pmt_id       | str                                                         | ✅       | Pmt Id            |

**Return Type**

`InlineResponse200_44`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CustomerPaymentMethod

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CustomerPaymentMethod(
    category="bank",
    fingerprint_token="fingerprint_token",
    id_="id",
    image="image",
    last4="6326",
    metadata={},
    name="name",
    network_reference_id="network_reference_id",
    next_action="3d_verification",
    redirect_url="redirect_url",
    supporting_documentation="supporting_documentation",
    token="token",
    type_="type",
    webhook_url="webhook_url"
)

result = sdk.customer_payment_method.update_customer_payment_method(
    request_body=request_body,
    customer_id="customerId",
    pmt_id="pmtId"
)

print(result)
```

## delete_customer_payment_method

This method triggers the Webhook - Payment Method Canceled webhook. This webhook contains more information than the response.

- HTTP Method: `DELETE`
- Endpoint: `/v1/customers/{customerId}/payment_methods/{pmtId}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| customer_id | str  | ✅       | customer Id |
| pmt_id      | str  | ✅       | Pmt Id      |

**Return Type**

`InlineResponse200_45`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.customer_payment_method.delete_customer_payment_method(
    customer_id="customerId",
    pmt_id="pmtId"
)

print(result)
```
