# Fee

**Properties**

| Name                | Type           | Required | Description                                                                                                     |
| :------------------ | :------------- | :------- | :-------------------------------------------------------------------------------------------------------------- |
| fx_fee              | FxFee          | ❌       | Describes the fees for processing the currency exchange. Relevant to payouts with FX.                           |
| gross_fees          | float          | ❌       | The total gross fees for the transaction, in units defined by currency_code. Relevant to responses.             |
| net_fees            | float          | ❌       | The total net fees for the transaction, in units defined by merchant_requested_currency. Relevant to responses. |
| transaction_fee     | TransactionFee | ❌       | Describes the fee for processing the transaction.                                                               |
| total_merchant_fees | float          | ❌       |                                                                                                                 |
