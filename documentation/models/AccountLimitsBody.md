# AccountLimitsBody

**Properties**

| Name       | Type  | Required | Description                                                         |
| :--------- | :---- | :------- | :------------------------------------------------------------------ |
| amount     | `str` | ✅       | The amount of the limit.                                            |
| currency   | `str` | ✅       | Three-letter ISO 4217 code for the currency of an existing account. |
| type\_     | `str` | ✅       | The limit type.                                                     |
| account_id | `str` | ❌       | The ID of the account within the wallet.                            |
