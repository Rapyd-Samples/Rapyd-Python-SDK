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
                    "country": "GB",
                    "created_at": 3.34,
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
                        "country": "GB",
                        "created_at": 3.34,
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
                    "annual_revenue": 6.14,
                    "cnae_code": "cnae_code",
                    "created_at": 6.84,
                    "entity_type": "sole_prop",
                    "establishment_date": "2813-47-84",
                    "id_": "id",
                    "industry_category": "2PLX8Nv1Se",
                    "industry_sub_category": "industry_sub_category",
                    "legal_entity_type": "legal_entity_type",
                    "name": "name",
                    "registration_number": "registration_number"
                },
                "compliance_profile": 0.4,
                "contact_type": "personal",
                "country": "GB",
                "created_at": 8.94,
                "date_of_birth": "date_of_birth",
                "email": "phL8Es@GB.oMq",
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
                "nationality": "GB",
                "phone_number": "phone_number",
                "second_last_name": "second_last_name",
                "send_notifications": False,
                "verification_status": "not verified",
                "contact_reference_id": "contact_reference_id"
            }
        ],
        "total_count": 3.99,
        "has_more": False,
        "url": "url"
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
