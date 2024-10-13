# PayoutsExtendedBeneficiaryBody

**Properties**

| Name                       | Type               | Required | Description                                                                                                                                                                                       |
| :------------------------- | :----------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| address                    | str                | ✅       | Beneficiary's street address including the build number.                                                                                                                                          |
| city                       | str                | ✅       | City of the beneficiary.                                                                                                                                                                          |
| category                   | Category           | ✅       |                                                                                                                                                                                                   |
| country                    | str                | ✅       | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code.                                          |
| currency                   | str                | ✅       |                                                                                                                                                                                                   |
| entity_type                | EntityType         | ✅       |                                                                                                                                                                                                   |
| identification_type        | IdentificationType | ✅       | Type of identification document for the beneficiary. When `entity_type` is **company**, this field must be**company_registered_number**. When `entity_type` is **individual**:                    |
| identification_value       | str                | ✅       | Identification number on the document mentioned in `identification_type`.                                                                                                                         |
| company_name               | str                | ❌       | Name of the beneficiary company. Required when `entity_type` is **company**.                                                                                                                      |
| country_of_incorporation   | str                | ❌       | The country where the company was registered. Two-letter ISO 3166-1 ALPHA-2 code. Required when `entity_type` is **company**.                                                                     |
| date_of_birth              | str                | ❌       | Date of birth of the individual. Format: DD/MM/YYYY. Required when `entity_type` is **individual**.                                                                                               |
| date_of_incorporation      | str                | ❌       | The date when the company was registered. Format: DD/MM/YYYY. Required when `entity_type` is **company**.                                                                                         |
| default_payout_method_type | str                | ❌       | The type of payout method for the beneficiary. The two-letter prefix must match the beneficiary country code.                                                                                     |
| first_name                 | str                | ❌       | First name of the beneficiary. Required when `entity_type` is **individual**.                                                                                                                     |
| gender                     | Gender             | ❌       | Gender of the individual. Required when `entity_type` is **individual**.                                                                                                                          |
| last_name                  | str                | ❌       | Family name of the beneficiary. Required when `entity_type` is **individual**. Required when `entity_type` is **individual**.                                                                     |
| merchant_reference_id      | str                | ❌       | ID defined by the client.                                                                                                                                                                         |
| nationality                | str                | ❌       | The citizenship of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code for the country. To determine the code for a country, see 'List Countries'. Required when `entity_type` is **individual**. |

# IdentificationType

Type of identification document for the beneficiary. When `entity_type` is **company**, this field must be**company_registered_number**. When `entity_type` is **individual**:

**Properties**

| Name                  | Type | Required | Description              |
| :-------------------- | :--- | :------- | :----------------------- |
| DRIVERSLICENSE        | str  | ✅       | "drivers_license"        |
| IDENTIFICATIONID      | str  | ✅       | "identification_id"      |
| INTERNATIONALPASSPORT | str  | ✅       | "international_passport" |
| RESIDENCEPERMIT       | str  | ✅       | "residence_permit"       |
| SOCIALSECURITY        | str  | ✅       | "social_security"        |
| WORKPERMIT            | str  | ✅       | "work_permit"            |
