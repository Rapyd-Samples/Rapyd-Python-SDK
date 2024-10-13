# Account

**Properties**

| Name             | Type        | Required | Description                                                 |
| :--------------- | :---------- | :------- | :---------------------------------------------------------- |
| alias            | str         | ❌       | Three-letter ISO 4217 code for the currency of the account. |
| balance          | float       | ❌       | Available funds in the account.                             |
| currency         | str         | ❌       |                                                             |
| id\_             | str         | ❌       | ID of the account. UUID                                     |
| limit            | str         | ❌       |                                                             |
| limits           | List[Limit] | ❌       |                                                             |
| on_hold_balance  | float       | ❌       | Amount in the on-hold balance of the account.               |
| received_balance | float       | ❌       | Amount of escrow funds in the account.                      |
| reserve_balance  | float       | ❌       | Amount in the reserve balance of the account.               |
