# VirtualAccountIssuing

**Properties**

| Name                  | Type                                      | Required | Description                                                                                                                                                                                            |
| :-------------------- | :---------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_                  | `str`                                     | ❌       | ID of the virtual account number object. String starting with issuing\_.                                                                                                                               |
| merchant_reference_id | `str`                                     | ❌       | Identifier defined by the client for reference purposes. Limit - 45 characters.                                                                                                                        |
| ewallet               | `str`                                     | ❌       | ID of the Rapyd Wallet that the virtual account is attached to. String starting with ewallet\_.                                                                                                        |
| bank_account          | `dict`                                    | ❌       | Details about the virtual account.                                                                                                                                                                     |
| metadata              | `dict`                                    | ❌       | A JSON object defined by the client.                                                                                                                                                                   |
| status                | `VirtualAccountIssuingStatus`             | ❌       | Indicates the status of the virtual account. _ ACT (Active) _ CLO (Closed) _ ERR (Error) _ PEN (Pending) _ REJ (REjected) _ DIS \* ENA                                                                 |
| description           | `str`                                     | ❌       | Description of the transaction, as defined by the client.                                                                                                                                              |
| funding_instructions  | `dict`                                    | ❌       | Issuied virtual account funding instructions.                                                                                                                                                          |
| currency              | `str`                                     | ❌       |                                                                                                                                                                                                        |
| requested_currency    | `str`                                     | ❌       | Currency received by the virtual account after conversion. One of the following: AUD - Australian Dollar EUR - Euro GBP - Pound Sterling HKD - Hong Kong Dollar SGD - Singapore Dollar USD - US Dollar |
| transactions          | `List[VirtualAccountTransactionResponse]` | ❌       | Issuied virtual account transactions.                                                                                                                                                                  |

# VirtualAccountIssuingStatus

Indicates the status of the virtual account. _ ACT (Active) _ CLO (Closed) _ ERR (Error) _ PEN (Pending) _ REJ (REjected) _ DIS \* ENA

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| ACT  | `str` | ✅       | "ACT"       |
| CLO  | `str` | ✅       | "CLO"       |
| ERR  | `str` | ✅       | "ERR"       |
| PEN  | `str` | ✅       | "PEN"       |
| REJ  | `str` | ✅       | "REJ"       |
| DIS  | `str` | ✅       | "DIS"       |
| ENA  | `str` | ✅       | "ENA"       |
