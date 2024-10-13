# EwalletTransaction

**Properties**

| Name                     | Type                          | Required | Description                                                                                                                                                                              |
| :----------------------- | :---------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| metadata                 | dict                          | ❌       |                                                                                                                                                                                          |
| amount                   | float                         | ❌       | Amount of the transaction, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 4217:2015. |
| balance                  | float                         | ❌       | The updated wallet balance after successful completion of the transaction.                                                                                                               |
| balance_type             | EwalletTransactionBalanceType | ❌       | Balance type affected by the transaction. One of the following                                                                                                                           |
| created_at               | float                         | ❌       | Time the transaction was made, in Unix time.                                                                                                                                             |
| currency                 | str                           | ❌       | Three-letter ISO 4217 code for the currency used in the amount field.                                                                                                                    |
| destination_balance_type | DestinationBalanceType        | ❌       | The destination balance type when funds are transferred from one balance to another within the wallet.                                                                                   |
| destination_ewallet_id   | str                           | ❌       | ID of the wallet receiving the money. String starting with **ewallet\_**. Response only.                                                                                                 |
| ewallet_id               | str                           | ❌       | ID of the wallet. String starting with **ewallet\_**.                                                                                                                                    |
| id\_                     | str                           | ❌       | ID of the transaction. String starting with wt\_ or UUID.                                                                                                                                |
| reason                   | str                           | ❌       | Unique identifier of the wallet object. String starting with **ewallet\_**.                                                                                                              |
| source_balance_type      | SourceBalanceType             | ❌       | The source balance type when funds are transferred from one balance to another within the wallet                                                                                         |
| source_ewallet_id        | str                           | ❌       | ID of the wallet sending the money. String starting with **ewallet\_**.                                                                                                                  |
| status                   | str                           | ❌       | Status of the transaction.                                                                                                                                                               |
| type\_                   | str                           | ❌       | Type of transaction                                                                                                                                                                      |
| subtype                  | float                         | ❌       | Subtype of the transaction.                                                                                                                                                              |
| action_data              | dict                          | ❌       |                                                                                                                                                                                          |

# EwalletTransactionBalanceType

Balance type affected by the transaction. One of the following

**Properties**

| Name             | Type | Required | Description         |
| :--------------- | :--- | :------- | :------------------ |
| AVAILABLEBALANCE | str  | ✅       | "available_balance" |
| ONHOLDBALANCE    | str  | ✅       | "on_hold_balance"   |
| RECEIVEDBALANCE  | str  | ✅       | "received_balance"  |
| RESERVEBALANCE   | str  | ✅       | "reserve_balance"   |

# DestinationBalanceType

The destination balance type when funds are transferred from one balance to another within the wallet.

**Properties**

| Name             | Type | Required | Description         |
| :--------------- | :--- | :------- | :------------------ |
| AVAILABLEBALANCE | str  | ✅       | "available_balance" |
| ONHOLDBALANCE    | str  | ✅       | "on_hold_balance"   |
| RECEIVEDBALANCE  | str  | ✅       | "received_balance"  |
| RESERVEBALANCE   | str  | ✅       | "reserve_balance"   |

# SourceBalanceType

The source balance type when funds are transferred from one balance to another within the wallet

**Properties**

| Name             | Type | Required | Description         |
| :--------------- | :--- | :------- | :------------------ |
| AVAILABLEBALANCE | str  | ✅       | "available_balance" |
| ONHOLDBALANCE    | str  | ✅       | "on_hold_balance"   |
| RECEIVEDBALANCE  | str  | ✅       | "received_balance"  |
| RESERVEBALANCE   | str  | ✅       | "reserve_balance"   |
