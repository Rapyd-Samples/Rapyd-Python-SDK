```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1IdentitiesBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1IdentitiesBody(
    back_side_image="back_side_image",
    back_side_image_mime_type="back_side_image_mime_type",
    contact="contact",
    country="GB",
    document_type="document_type",
    ewallet="ewallet",
    face_image="face_image",
    face_image_mime_type="face_image_mime_type",
    front_side_image="front_side_image",
    front_side_image_mime_type="front_side_image_mime_type",
    reference_id="reference_id",
    request_type="request_type",
    send_callback="send_callback"
)

result = sdk.verify.create_v1_identities(request_body=request_body)

print(result)

```
