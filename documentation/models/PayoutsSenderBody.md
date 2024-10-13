# PayoutsSenderBody

**Properties**

| Name                 | Type       | Required | Description                                                                                                                                              |
| :------------------- | :--------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| country              | str        | ✅       | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code. |
| currency             | str        | ✅       |                                                                                                                                                          |
| entity_type          | EntityType | ✅       |                                                                                                                                                          |
| company_name         | str        | ❌       | Name of the sender company. Relevant when `entity_type` is **company**.                                                                                  |
| first_name           | str        | ❌       | First name of the sebder. Relevant when entity_type is individual.                                                                                       |
| identification_type  | str        | ❌       | Type of identification document for the sender.                                                                                                          |
| identification_value | str        | ❌       | Identification number on the document mentioned in identification_type.                                                                                  |
| last_name            | str        | ❌       | Last name of the sender. Relevant when `entity_type` is **individual**.                                                                                  |
