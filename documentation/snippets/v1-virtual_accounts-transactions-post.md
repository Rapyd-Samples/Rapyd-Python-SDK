```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import VirtualAccountsTransactionsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = VirtualAccountsTransactionsBody(
    amount="amount",
    currency="currency",
    issued_bank_account="issued_bank_account"
)

result = sdk.virtual_accounts.simulate_complete_bank_account_issuing_transaction(request_body=request_body)

print(result)

```
