```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_user_transactions(
    wallet_id="walletId",
    balance=8.85,
    page_size="page_size",
    currency="currency",
    end_date="end_date",
    ending_before="ending_before",
    page_number="page_number",
    start_date="start_date",
    starting_after="starting_after",
    type_="type"
)

print(result)

```
