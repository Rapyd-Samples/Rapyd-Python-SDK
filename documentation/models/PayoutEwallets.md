# PayoutEwallets

**Properties**

| Name       | Type  | Required | Description                                                                                                                                                                                                                                   |
| :--------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| amount     | float | ❌       | The amount of the payment to the wallet, in units of the currency defined in currency. Decimal. If the total amount of the payment is not fully accounted for, the balance appears in the client wallet. Relevant when percentage is not set. |
| ewallet_id | str   | ❌       | ID of the wallet. String starting with **ewallet\_**. Read-only.                                                                                                                                                                              |
| percent    | float | ❌       | The percentage that is paid to the wallet out of the total payment. Read-only.                                                                                                                                                                |
