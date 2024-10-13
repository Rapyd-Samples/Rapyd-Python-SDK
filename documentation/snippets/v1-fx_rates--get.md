```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_fx_rate(
    action_type="action_type",
    buy_currency="buy_currency",
    sell_currency="sell_currency",
    amount=8.15,
    date_="date",
    fixed_side="fixed_side"
)

print(result)

```
