# V1PayoutsBody

**Properties**

| Name                    | Type                     | Required | Description                                                                                                                                                         |
| :---------------------- | :----------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| beneficiary             | V1PayoutsBodyBeneficiary | ✅       | String starting with **beneficiary\_** or the object describing the beneficiary.                                                                                    |
| beneficiary_entity_type | BeneficiaryEntityType    | ✅       | Type of entity for the beneficiary. One of the following: **individual** \| **company**                                                                             |
| payout_amount           | float                    | ✅       | Amount of the payout, in units of the currency defined in `payout_currency`. Mandatory when `sender_amount` is not used. Decimal.                                   |
| payout_currency         | str                      | ✅       |                                                                                                                                                                     |
| sender                  | V1PayoutsBodySender      | ✅       | String starting with **sender\_** or the object describing the sender.                                                                                              |
| sender_country          | str                      | ✅       | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code.            |
| sender_currency         | str                      | ✅       |                                                                                                                                                                     |
| sender_entity_type      | EntityType               | ✅       |                                                                                                                                                                     |
| beneficiary_country     | str                      | ❌       | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.                                                                                          |
| confirm_automatically   | bool                     | ❌       | Determines whether completion of the payout requires confirmation of the FX rate. Relevant to payouts with foreign exchange. Default is false.                      |
| converstion_rate        | float                    | ❌       | conversion rate                                                                                                                                                     |
| description             | str                      | ❌       | Description of the payout transaction.                                                                                                                              |
| ewallet                 | str                      | ❌       | ID of the wallet that the money is transferred from. String starting with **ewallet\_**.                                                                            |
| expiration              | str                      | ❌       | Determines the day the payout expires, in Unix time. The payout must be completed before the start of this day. Relevant to cash payouts.                           |
| location                | str                      | ❌       | Location of the payout transaction.                                                                                                                                 |
| merchant_reference_id   | str                      | ❌       | ID defined by the client. Limited to 255 characters.                                                                                                                |
| metadata                | dict                     | ❌       | A JSON object defined by the client.                                                                                                                                |
| payout_method_type      | str                      | ❌       | The type of payout method. The two-letter prefix must match the beneficiary country code. Required when the beneficiary does not have a default payout method type. |
| payout_options          | dict                     | ❌       | Payout options                                                                                                                                                      |
| statement_descriptor    | str                      | ❌       | A statement that includes the reason for the payout. Limited to 35 characters.                                                                                      |

# V1PayoutsBodyBeneficiary

String starting with **beneficiary\_** or the object describing the beneficiary.

# BeneficiaryEntityType

Type of entity for the beneficiary. One of the following: **individual** \| **company**

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| INDIVIDUAL | str  | ✅       | "individual" |
| COMPANY    | str  | ✅       | "company"    |

# V1PayoutsBodySender

String starting with **sender\_** or the object describing the sender.
