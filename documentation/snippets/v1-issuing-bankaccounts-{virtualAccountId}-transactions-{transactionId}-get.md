```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.issuing.retrieve_issuing_transaction(
    virtual_account_id="virtualAccountId",
    transaction_id="transactionId"
)

print(result)

```
