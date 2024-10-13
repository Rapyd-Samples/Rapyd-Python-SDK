# DailyRate

Describes currency conversion for payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees.

**Properties**

| Name          | Type  | Required | Description                                                                                                                                                                                                    |
| :------------ | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| action_type   | str   | ❌       | The type of transaction that the currency exchange applies to. One of the following - payment, payout                                                                                                          |
| buy_amount    | float | ❌       | If fixed_side is buy, the value of amount. If fixed_side is sell, the value of buy_currency following the currency exchange transaction. Relevant when amount and `fixed_side` are specified.                  |
| buy_currency  | str   | ❌       | The currency purchased in the currency exchange transaction. Three-letter ISO 4217 code. Uppercase.                                                                                                            |
| date\_        | str   | ❌       | The date when the rate is applicable. Today or earlier. Format is YYYY-MM-DD. Default is today.                                                                                                                |
| fixed_side    | str   | ❌       | Indicates which currency the rate is fixed for. One of the following : _ buy - The currency defined by buy_currency. _ sell : The currency defined by sell_currency.                                           |
| rate          | float | ❌       | The exchange rate. Includes FX markup fees.                                                                                                                                                                    |
| sell_amount   | float | ❌       | If `fixed_side` is **sell**, the value of amount. If `fixed_side` is **buy**, the value of `sell_currency` following the currency exchange transaction. Relevant when `amount` and `fixed_side` are specified. |
| sell_currency | str   | ❌       | Selling currency                                                                                                                                                                                               |
