# InlineResponse_200_33Data

**Properties**

| Name            | Type  | Required | Description                                                                                         |
| :-------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------- |
| account_id      | str   | ❌       | ID of the virtual bank account.                                                                     |
| account_id_type | str   | ❌       | Type of the virtual account number.                                                                 |
| amount          | float | ❌       | Amount of the transaction, in units defined in currency.                                            |
| created_at      | int   | ❌       | Timestamp for the transaction, in Unix time                                                         |
| currency        | str   | ❌       | Currency of the account. Three-letter ISO 4217 code.                                                |
| ewallet         | str   | ❌       | ID of the Rapyd Wallet that is attached to the virtual account. String starting with **ewallet\_**. |
| id\_            | str   | ❌       | ID of the transaction. String starting with **isutran\_**.                                          |
