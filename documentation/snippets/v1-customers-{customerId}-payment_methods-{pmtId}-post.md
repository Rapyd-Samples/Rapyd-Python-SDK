```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import CustomerPaymentMethod

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CustomerPaymentMethod(
    category="bank",
    fingerprint_token="fingerprint_token",
    id_="id",
    image="image",
    last4="4487",
    metadata={},
    name="name",
    network_reference_id="network_reference_id",
    next_action="3d_verification",
    redirect_url="redirect_url",
    supporting_documentation="supporting_documentation",
    token="token",
    type_="type",
    webhook_url="webhook_url"
)

result = sdk.customer_payment_method.update_customer_payment_method(
    request_body=request_body,
    customer_id="customerId",
    pmt_id="pmtId"
)

print(result)

```
