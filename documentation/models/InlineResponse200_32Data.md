# InlineResponse_200_32Data

**Properties**

| Name                  | Type                                       | Required | Description                                                                                |
| :-------------------- | :----------------------------------------- | :------- | :----------------------------------------------------------------------------------------- |
| id\_                  | str                                        | ❌       | ID of the issued card transaction object. String starting with **cit\_**.                  |
| merchant_reference_id | str                                        | ❌       | ID of this account, as provided by the merchant. Limited to 45 characters.                 |
| ewallet               | str                                        | ❌       | ID of the wallet the bank account number is issued to. String starting with **ewallet\_**. |
| bank_account          | dict                                       | ❌       | Issued virtual account.                                                                    |
| metadata              | dict                                       | ❌       | A JSON object defined by the client.                                                       |
| status                | str                                        | ❌       | Issued virtual account statuts.                                                            |
| description           | str                                        | ❌       | Description of the account.                                                                |
| funding_instructions  | dict                                       | ❌       | Issued virtual account funding instructions.                                               |
| currency              | str                                        | ❌       | Currency of the transaction. Three-letter ISO 4217.                                        |
| transactions          | List[InlineResponse200_30DataTransactions] | ❌       | Issued virtual account transactions.                                                       |
