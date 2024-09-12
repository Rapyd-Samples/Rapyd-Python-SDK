# PayoutsSenderBody

**Properties**

| Name                 | Type         | Required | Description                                                             |
| :------------------- | :----------- | :------- | :---------------------------------------------------------------------- |
| country              | `str`        | ✅       |                                                                         |
| currency             | `str`        | ✅       |                                                                         |
| entity_type          | `EntityType` | ✅       |                                                                         |
| company_name         | `str`        | ❌       | Name of the sender company. Relevant when entity_type is company.       |
| first_name           | `str`        | ❌       | First name of the sebder. Relevant when entity_type is individual.      |
| identification_type  | `str`        | ❌       | Type of identification document for the sender.                         |
| identification_value | `str`        | ❌       | Identification number on the document mentioned in identification_type. |
| last_name            | `str`        | ❌       | Last name of the sender. Relevant when entity_type is individual.       |
