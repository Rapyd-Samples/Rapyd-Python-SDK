# ContactBusiness

**Properties**

| Name                  | Type                        | Required | Description                                                                                                                                                       |
| :-------------------- | :-------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| address               | `Address`                   | ❌       | address associated with this specific Rapyd entity Payment/Customer etc...                                                                                        |
| annual_revenue        | `float`                     | ❌       | Annual revenue of the business in US dollars. Maximum value 100000000000000. Decimal.                                                                             |
| cnae_code             | `str`                       | ❌       | Business activity code of the business, according to the ClassificaÃ§Ã£o Nacional de Atividades EconÃ´micas of Brazil. Alphanumeric string. Maximum 7 characters. |
| created_at            | `float`                     | ❌       | Time of creation of the business_details object, in Unix time. Response only.                                                                                     |
| entity_type           | `ContactBusinessEntityType` | ❌       | Type of business entity                                                                                                                                           |
| establishment_date    | `str`                       | ❌       | Date that the business was established. Format YYYY-MM-DD                                                                                                         |
| id\_                  | `str`                       | ❌       | ID of the business*details object. String starting with busi*.                                                                                                    |
| industry_category     | `str`                       | ❌       | Name of the industry that this business belongs to. Required. Alphanumeric string with no special characters.                                                     |
| industry_sub_category | `str`                       | ❌       | Subcategory of the industry that this business belongs to.                                                                                                        |
| legal_entity_type     | `str`                       | ❌       | Type of legal entity. Alphanumeric string.                                                                                                                        |
| name                  | `str`                       | ❌       | Business name.                                                                                                                                                    |
| registration_number   | `str`                       | ❌       | Registration number.                                                                                                                                              |

# ContactBusinessEntityType

Type of business entity

**Properties**

| Name        | Type  | Required | Description   |
| :---------- | :---- | :------- | :------------ |
| SOLEPROP    | `str` | ✅       | "sole_prop"   |
| PARTNERSHIP | `str` | ✅       | "partnership" |
| COMPANY     | `str` | ✅       | "company"     |
| GOVERNMENT  | `str` | ✅       | "government"  |
| CHARITY     | `str` | ✅       | "charity"     |
| NPO         | `str` | ✅       | "NPO"         |
| ASSOCIATION | `str` | ✅       | "association" |
| TRUST       | `str` | ✅       | "trust"       |
