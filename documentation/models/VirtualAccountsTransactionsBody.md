# VirtualAccountsTransactionsBody

**Properties**

| Name                | Type | Required | Description                                                                                                                                                                                                                                                     |
| :------------------ | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| amount              | str  | ✅       | The amount of the transaction, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal. |
| currency            | str  | ✅       | Currency of the transaction. Three-letter ISO 4217 code. Must be the same as the currency of the virtual account.                                                                                                                                               |
| issued_bank_account | str  | ✅       | ID of the Virtual Account Number object. String starting with issuing\_                                                                                                                                                                                         |
