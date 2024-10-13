# EwalletTransactionDetails

**Properties**

| Name         | Type                                 | Required | Description                                                                                                                                                                              |
| :----------- | :----------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| action_data  | dict                                 | ❌       |                                                                                                                                                                                          |
| metadata     | dict                                 | ❌       |                                                                                                                                                                                          |
| amount       | float                                | ❌       | Amount of the transaction, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 4217:2015. |
| balance      | float                                | ❌       | The updated wallet balance after successful completion of the transaction.                                                                                                               |
| balance_type | EwalletTransactionDetailsBalanceType | ❌       | Balance type affected by the transaction. One of the following                                                                                                                           |
| created_at   | float                                | ❌       | Time the transaction was made, in Unix time.                                                                                                                                             |
| currency     | str                                  | ❌       | Three-letter ISO 4217 code for the currency used in the amount field.                                                                                                                    |
| ewallet_id   | str                                  | ❌       | ID of the wallet. String starting with **ewallet\_**.                                                                                                                                    |
| id\_         | str                                  | ❌       | ID of the transaction. String starting with **wt\_** or UUID.                                                                                                                            |
| reason       | str                                  | ❌       | Unique identifier of the wallet object. String starting with **ewallet\_**.                                                                                                              |
| status       | str                                  | ❌       | Status of the transaction.                                                                                                                                                               |
| type\_       | str                                  | ❌       | Type of transaction                                                                                                                                                                      |
| subtype      | str                                  | ❌       | Sub type of the transaction                                                                                                                                                              |

# EwalletTransactionDetailsBalanceType

Balance type affected by the transaction. One of the following

**Properties**

| Name             | Type | Required | Description         |
| :--------------- | :--- | :------- | :------------------ |
| AVAILABLEBALANCE | str  | ✅       | "available_balance" |
| ONHOLDBALANCE    | str  | ✅       | "on_hold_balance"   |
| RECEIVEDBALANCE  | str  | ✅       | "received_balance"  |
| RESERVEBALANCE   | str  | ✅       | "reserve_balance"   |
