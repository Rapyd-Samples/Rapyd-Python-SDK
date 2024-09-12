# FxService

A list of all methods in the `FxService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                                                                                                                                                                           |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_daily_rate](#get_daily_rate) | Retrieve a daily rate for conversion of currencies in payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees. |

## get_daily_rate

Retrieve a daily rate for conversion of currencies in payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees.

- HTTP Method: `GET`
- Endpoint: `/v1/rates/daily`

**Parameters**

| Name          | Type    | Required | Description                                                                                                                      |
| :------------ | :------ | :------- | :------------------------------------------------------------------------------------------------------------------------------- |
| action_type   | `str`   | ✅       | Determines the type of transaction that the currency exchange applies to. One of the following - payment, payout                 |
| buy_currency  | `str`   | ✅       | Defines the currency purchased in the currency exchange transaction. Three-letter ISO 4217 code in Uppercase.                    |
| sell_currency | `str`   | ✅       | Defines the currency sold in the currency exchange transaction. Three-letter ISO 4217 code in Uppercase.                         |
| amount        | `float` | ❌       | Amount of the currency exchange transaction, in units of the fixed-side currency in Decimal.                                     |
| date\_        | `str`   | ❌       | The date when the rate is applicable. Today or earlier. Format YYYY-MM-DD                                                        |
| fixed_side    | `str`   | ❌       | Indicates whether the rate is fixed for the currency defined by buy_currency or sell_currency. One of the following - buy, sell. |

**Return Type**

`InlineResponse200_19`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.fx.get_daily_rate(
    action_type="action_type",
    buy_currency="buy_currency",
    sell_currency="sell_currency",
    amount=9.91,
    date_="date",
    fixed_side="fixed_side"
)

print(result)
```
