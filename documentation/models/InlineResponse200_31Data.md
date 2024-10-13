# InlineResponse_200_31Data

**Properties**

| Name                   | Type  | Required | Description                                                                                                                      |
| :--------------------- | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------- |
| account_name           | str   | ❌       | Name of the bank account holder.                                                                                                 |
| account_number         | str   | ❌       | Number of the bank account.                                                                                                      |
| amount                 | str   | ❌       | The amount of the transaction, in units of the currency defined in currency.                                                     |
| bank_code              | str   | ❌       | Bank identifier code, such as SWIFT, BIC, ABA, or other local identifier.                                                        |
| bank_name              | str   | ❌       | Name of the bank.                                                                                                                |
| country                | str   | ❌       | The country that the account number will be associated with. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.                      |
| created_at             | float | ❌       | Time of creation of the transaction, in Unix time. Response only.                                                                |
| currency               | str   | ❌       | Currency of the account. Three-letter ISO 4217 code.                                                                             |
| iban                   | str   | ❌       | IBAN of the virtual bank account.                                                                                                |
| id\_                   | str   | ❌       | ID that is assigned by the remitter                                                                                              |
| partner_transaction_id | str   | ❌       | ID that is assigned by the client to the transaction.                                                                            |
| receiving_iban         | str   | ❌       | IBAN that was assigned to the Rapyd Wallet.                                                                                      |
| remitter_reference     | str   | ❌       | Optional information that the remitter adds to the transaction, intended for the beneficiary. Supported by some payment methods. |
| sort_code              | str   | ❌       |                                                                                                                                  |
| status                 | str   | ❌       | Indicates the status of the transfer.                                                                                            |
| updated_at             | float | ❌       | Time of update of the virtual account, in Unix time. Response only.                                                              |
| created_at_gw          | str   | ❌       | Time of creation of the transaction, in Unix time. Response only.                                                                |
| original_currency      | str   | ❌       | This field will display the currency in which the transaction was originally made.                                               |
| original_amount        | str   | ❌       | This field will show the initial transaction amount before conversion.                                                           |
| fx_rate                | str   | ❌       | This field will indicate the exchange rate applied for the currency conversion                                                   |
