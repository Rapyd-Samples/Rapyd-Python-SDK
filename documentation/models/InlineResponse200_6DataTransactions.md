# InlineResponse_200_6DataTransactions

**Properties**

| Name              | Type    | Required | Description                                                                            |
| :---------------- | :------ | :------- | :------------------------------------------------------------------------------------- |
| id\_              | `str`   | ❌       | ID of the issued card transaction object. String starting with cit\_.                  |
| ewallet           | `str`   | ❌       | ID of the wallet the bank account number is issued to. String starting with ewallet\_. |
| account_id        | `str`   | ❌       | ID of the virtual bank account.                                                        |
| account_id_type   | `str`   | ❌       | Type of the virtual account number.                                                    |
| amount            | `float` | ❌       | Amount of the transaction.                                                             |
| currency          | `str`   | ❌       | Currency of the transaction. Three-letter ISO 4217.                                    |
| created_at        | `float` | ❌       | Time of creation of the transaction, in Unix time. Response only.                      |
| original_amount   | `float` | ❌       | This field will show the initial transaction amount before conversion.                 |
| original_currency | `str`   | ❌       |                                                                                        |
| fx_rate           | `float` | ❌       | This field will indicate the exchange rate applied for the currency conversion         |
