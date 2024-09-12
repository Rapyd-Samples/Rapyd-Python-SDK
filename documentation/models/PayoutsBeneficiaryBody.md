# PayoutsBeneficiaryBody

**Properties**

| Name                       | Type         | Required | Description                                                                                                   |
| :------------------------- | :----------- | :------- | :------------------------------------------------------------------------------------------------------------ |
| category                   | `Category`   | ✅       |                                                                                                               |
| country                    | `str`        | ✅       |                                                                                                               |
| currency                   | `str`        | ✅       |                                                                                                               |
| entity_type                | `EntityType` | ✅       |                                                                                                               |
| company_name               | `str`        | ❌       | Name of the beneficiary company. Relevant when entity_type is company.                                        |
| default_payout_method_type | `str`        | ❌       | The type of payout method for the beneficiary. The two-letter prefix must match the beneficiary country code. |
| first_name                 | `str`        | ❌       | First name of the beneficiary. Relevant when entity_type is individual.                                       |
| identification_type        | `str`        | ❌       | Type of identification document for the beneficiary.                                                          |
| identification_value       | `str`        | ❌       | Identification number on the document mentioned in identification_type.                                       |
| last_name                  | `str`        | ❌       | Family name of the beneficiary. Relevant when entity_type is individual.                                      |
| merchant_reference_id      | `str`        | ❌       | ID defined by the client.                                                                                     |
