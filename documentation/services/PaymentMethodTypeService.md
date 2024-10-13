# PaymentMethodTypeService

A list of all methods in the `PaymentMethodTypeService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                                                                                                    |
| :---------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| [get_payment_methods_types_by_country](#get_payment_methods_types_by_country)       | You can filter the results by specifying the currency query parameter                                          |
| [get_payment_method_type_required_fields](#get_payment_method_type_required_fields) | The fields are returned as a list of objects. The name of each field appears in the name field of the response |

## get_payment_methods_types_by_country

You can filter the results by specifying the currency query parameter

- HTTP Method: `GET`
- Endpoint: `/v1/payment_methods/countries/{countryId}`

**Parameters**

| Name       | Type | Required | Description                                                    |
| :--------- | :--- | :------- | :------------------------------------------------------------- |
| country_id | str  | ✅       | Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. |
| currency   | str  | ❌       | currency                                                       |

**Return Type**

`InlineResponse200_58`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.payment_method_type.get_payment_methods_types_by_country(
    country_id="GB",
    currency="GBP"
)

print(result)
```

## get_payment_method_type_required_fields

The fields are returned as a list of objects. The name of each field appears in the name field of the response

- HTTP Method: `GET`
- Endpoint: `/v1/payment_methods/{pmtId}/required_fields`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| pmt_id | str  | ✅       | discount Id |

**Return Type**

`InlineResponse200_59`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.payment_method_type.get_payment_method_type_required_fields(pmt_id="pmtId")

print(result)
```
