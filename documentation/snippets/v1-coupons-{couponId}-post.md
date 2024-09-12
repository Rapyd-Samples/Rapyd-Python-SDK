```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import Coupon

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = Coupon(
    amount_off=0.13,
    created=1671697165,
    currency="GBP",
    description="Sample Coupon 1",
    discount_duration_in_uses=2,
    discount_valid_until=7.67,
    discount_validity_in_months=2,
    duration="forever",
    duration_in_months=3,
    id_="coupon_c1194a18a9972ca7f9804826f00c9eb8",
    max_redemptions=2,
    metadata={},
    percent_off=10,
    redeem_by=0.44,
    times_redeemed=6.69,
    valid=True
)

result = sdk.coupon.update_coupon(
    request_body=request_body,
    coupon_id="couponId"
)

print(result)

```
