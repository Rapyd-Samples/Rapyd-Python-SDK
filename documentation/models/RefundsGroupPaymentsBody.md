# RefundsGroupPaymentsBody

**Properties**

| Name          | Type  | Required | Description                                                                                                                                  |
| :------------ | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| group_payment | str   | ✅       | ID of the group payment that the refund is charged against. String starting with **gp\_**.                                                   |
| amount        | float | ❌       | The amount of the refund, in the currency of the group payment. Decimal. If this parameter is omitted, the entire group payment is refunded. |
