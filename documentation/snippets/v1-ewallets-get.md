```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.e_wallets.get_users(
    phone_number="phone_number",
    email="email",
    ewallet_reference_id="ewallet_reference_id",
    page_number=1.1,
    page_size=8.92,
    type_="type",
    min_balance=1.17,
    currency="currency"
)

print(result)

```
