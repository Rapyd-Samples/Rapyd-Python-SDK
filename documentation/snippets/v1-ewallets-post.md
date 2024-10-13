```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1EwalletsBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1EwalletsBody(
    contact={
        "data": [
            {
                "address": {
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
                "business_details": {
                    "address": {
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
                    "annual_revenue": 0.61,
                    "cnae_code": "cnae_code",
                    "created_at": 2.4,
                    "entity_type": "sole_prop",
                    "establishment_date": "3393-35-87",
                    "id_": "id",
                    "industry_category": "z0Z4di9",
                    "industry_sub_category": "industry_sub_category",
                    "legal_entity_type": "legal_entity_type",
                    "name": "name",
                    "registration_number": "registration_number"
                },
                "compliance_profile": 9.54,
                "contact_type": "personal",
                "country": "ad laborum",
                "created_at": 6.53,
                "date_of_birth": "date_of_birth",
                "email": "98+v8hnTp@gOQLw-.QqIWCjgtSG",
                "ewallet": "ewallet",
                "first_name": "first_name",
                "gender": "male",
                "house_type": "lease",
                "id_": "id",
                "identification_number": "identification_number",
                "identification_type": "identification_type",
                "issued_card_data": {},
                "last_name": "last_name",
                "marital_status": "married",
                "metadata": {},
                "middle_name": "middle_name",
                "mothers_name": "mothers_name",
                "nationality": "Excepteur c",
                "phone_number": "phone_number",
                "second_last_name": "second_last_name",
                "send_notifications": True,
                "verification_status": "not verified",
                "contact_reference_id": "contact_reference_id"
            }
        ],
        "total_count": 4.95,
        "has_more": True,
        "url": "url",
        "ewallet_reference_id": "ewallet_reference_id",
        "first_name": "first_name",
        "last_name": "last_name",
        "metadata": {},
        "type_": "type",
        "phone_number": "phone_number"
    },
    ewallet_reference_id="ewallet_reference_id",
    first_name="first_name",
    last_name="last_name",
    metadata={},
    type_="type"
)

result = sdk.e_wallets.create_user(request_body=request_body)

print(result)

```
