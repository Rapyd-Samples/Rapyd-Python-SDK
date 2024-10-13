# Field_1

Field Object

**Properties**

| Name            | Type                  | Required | Description                                                                                                                                                                                        |
| :-------------- | :-------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code            | str                   | ❌       | Three-letter alphabetic ISO 4217 code for the official currency used in the country.                                                                                                               |
| is_required     | bool                  | ❌       | Whether the field is always required for using the payment method                                                                                                                                  |
| is_updatable    | bool                  | ❌       | Indicates whether the field can be updated with Update Payment Method                                                                                                                              |
| instructions    | str                   | ❌       |                                                                                                                                                                                                    |
| name            | str                   | ❌       | Name of the currency in English.                                                                                                                                                                   |
| numeric_code    | str                   | ❌       | Three-letter ISO numeric 4217 code for the currency.                                                                                                                                               |
| required_fields | List[Field1]          | ❌       |                                                                                                                                                                                                    |
| type\_          | Field1Type            | ❌       |                                                                                                                                                                                                    |
| regex           | str                   | ❌       | A regular expression that defines the format when type is string.                                                                                                                                  |
| conditions      | List[FieldConditions] | ❌       | Defines specific conditions when a field is required for a payment method. When the conditions defined by conditions are met, the field is required even though the value of is_required is false. |
| description     | str                   | ❌       | Description of the field.                                                                                                                                                                          |

# Field_1Type

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| BOOLEAN | str  | ✅       | "boolean"   |
| NUMBER  | str  | ✅       | "number"    |
| STRING  | str  | ✅       | "string"    |
| OBJECT  | str  | ✅       | "object"    |
