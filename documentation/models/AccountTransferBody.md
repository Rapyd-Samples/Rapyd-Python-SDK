# AccountTransferBody

**Properties**

| Name                | Type  | Required | Description                                                                                                                                                                                                                            |
| :------------------ | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| amount              | float | ✅       | Amount of the transfer. Decimal.                                                                                                                                                                                                       |
| currency            | str   | ✅       | Three-letter ISO 4217 code for the currency used in the amount field. Uppercase.                                                                                                                                                       |
| destination_ewallet | str   | ✅       | ID of the wallet receiving the money. String starting with **ewallet\_**.                                                                                                                                                              |
| source_ewallet      | str   | ✅       | ID of the wallet sending the money. String starting with **ewallet\_**.                                                                                                                                                                |
| expiration          | str   | ❌       | Determines the day the ewallet funds transfer expires, in Unix time. Acceptance of the ewallet transfer must be completed before the start of this day. The default setting is 14 days from the date the ewallet transfer was created. |
| metadata            | dict  | ❌       | A JSON object defined by the client.                                                                                                                                                                                                   |
