```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Address

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = Address(
    canton="canton",
    city="city",
    country="dolore u",
    created_at=2.12,
    district="district",
    id_="id",
    line_1="line_1",
    line_2="line_2",
    line_3="line_3",
    metadata={},
    name="name",
    phone_number="phone_number",
    state="state",
    zip="zip"
)

result = sdk.payment_address.create_address(request_body=request_body)

print(result)

```
