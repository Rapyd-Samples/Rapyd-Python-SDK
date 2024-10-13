# PayoutRequiredFields

**Properties**

| Name           | Type                     | Required | Description                                                                                                                                                                                                |
| :------------- | :----------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| allowed_values | str                      | ❌       | List out the allowed values                                                                                                                                                                                |
| description    | str                      | ❌       | Description of the field                                                                                                                                                                                   |
| is_required    | bool                     | ❌       | Indicates whether the field is always required for using the payout method                                                                                                                                 |
| name           | str                      | ❌       | Name of the field                                                                                                                                                                                          |
| regex          | str                      | ❌       | A regular expression that defines the format when type is string. Note: Rapyd uses a unique variant of the regex standard. See note in "https://docs.rapyd.net/en/get-payment-method-required-fields.html" |
| transfer_type  | str                      | ❌       | Indicates transfer type of the payout                                                                                                                                                                      |
| type\_         | PayoutRequiredFieldsType | ❌       | Indicates datatype of the field                                                                                                                                                                            |

# PayoutRequiredFieldsType

Indicates datatype of the field

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| BOOLEAN | str  | ✅       | "boolean"   |
| NUMBER  | str  | ✅       | "number"    |
| STRING  | str  | ✅       | "string"    |
