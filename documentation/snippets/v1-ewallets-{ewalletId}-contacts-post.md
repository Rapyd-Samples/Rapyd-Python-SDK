```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import EwalletIdContactsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = EwalletIdContactsBody(
    address={
        "canton": "canton",
        "city": "city",
        "country": "dolore u",
        "created_at": 2.12,
        "district": "district",
        "id_": "id",
        "line_1": "line_1",
        "line_2": "line_2",
        "line_3": "line_3",
        "metadata": {},
        "name": "name",
        "phone_number": "phone_number",
        "state": "state",
        "zip": "zip"
    },
    contact_type="contact_type",
    country="country",
    date_of_birth="date_of_birth",
    email="email",
    first_name="first_name",
    last_name="last_name",
    gender="gender",
    house_type="house_type",
    identification_number="identification_number",
    identification_type="identification_type",
    marital_status="marital_status",
    metadata="metadata",
    middle_name="middle_name",
    mothers_name="mothers_name",
    nationality="nationality",
    phone_number="phone_number",
    second_last_name="second_last_name",
    send_notifications=False,
    contact_reference_id="contact_reference_id"
)

result = sdk.e_wallets.create_ewallet_contact(
    request_body=request_body,
    ewallet_id="ewalletId"
)

print(result)

```
