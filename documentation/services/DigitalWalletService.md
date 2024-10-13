# DigitalWalletService

A list of all methods in the `DigitalWalletService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                                                                                                                                                                 |
| :---------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_apple_pay_session](#get_apple_pay_session) | Retrieve the details of an Apple Pay payment session. Each payment that uses Apple Pay has a unique session. [Activating Apple Pay](https://docs.rapyd.net/en/activating-apple-pay.html) is a prerequisite. |

## get_apple_pay_session

Retrieve the details of an Apple Pay payment session. Each payment that uses Apple Pay has a unique session. [Activating Apple Pay](https://docs.rapyd.net/en/activating-apple-pay.html) is a prerequisite.

- HTTP Method: `POST`
- Endpoint: `/v1/digital_wallets/session/apple_pay`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [ApplePayObject](../models/ApplePayObject.md) | ✅       | The request body. |

**Return Type**

`InlineResponse200_46`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import ApplePayObject

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ApplePayObject(
    display_name="display_name",
    initiative_context="initiative_context"
)

result = sdk.digital_wallet.get_apple_pay_session(request_body=request_body)

print(result)
```
