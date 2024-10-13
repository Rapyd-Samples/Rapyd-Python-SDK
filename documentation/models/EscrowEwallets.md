# EscrowEwallets

Describes the wallets and the releases from escrow.

**Properties**

| Name       | Type  | Required | Description                                                                                                                                                                                           |
| :--------- | :---- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ewallet    | str   | ❌       | ID of the wallet, a string starting with **ewallet\_**.                                                                                                                                               |
| amount     | float | ❌       | The amount to release to this wallet. Relevant when `percentage` is not set.                                                                                                                          |
| percentage | float | ❌       | The percentage of this escrow to release to this wallet. Relevant when `amount` is not set. On a partial release after the first, this refers to the percentage of the original amount of the escrow. |
