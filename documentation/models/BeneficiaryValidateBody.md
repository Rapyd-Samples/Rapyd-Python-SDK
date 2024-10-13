# BeneficiaryValidateBody

**Properties**

| Name               | Type                               | Required | Description                                                                                                                                                        |
| :----------------- | :--------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| amount             | float                              | ✅       | Maximum payout amount to validate, in units of the currency defined in `sender_currency`. Decimal.                                                                 |
| beneficiary        | BeneficiaryValidateBodyBeneficiary | ✅       | String starting with **beneficiary\_** or the object describing the beneficiary.                                                                                   |
| payout_method_type | str                                | ✅       | The type of the payout method. Set to a value included in the response to List Payout Method Types. The two-letter prefix must match the beneficiary country code. |
| sender_country     | str                                | ✅       | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code.           |
| sender_currency    | str                                | ✅       |                                                                                                                                                                    |
| sender_entity_type | EntityType                         | ✅       |                                                                                                                                                                    |
| identifier_type    | str                                | ❌       | Identifier type of beneficiary                                                                                                                                     |
| identifier_value   | str                                | ❌       | Identifier value to filter with                                                                                                                                    |

# BeneficiaryValidateBodyBeneficiary

String starting with **beneficiary\_** or the object describing the beneficiary.
