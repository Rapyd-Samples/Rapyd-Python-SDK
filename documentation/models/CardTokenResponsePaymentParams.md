# CardTokenResponsePaymentParams

Contains the following fields. When these fields do not include values, the user is redirected to the hosted page, and a related status message appears at the top of the page.

**Properties**

| Name                 | Type | Required | Description                                                                                                                                                      |
| :------------------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| complete_payment_url | str  | ❌       | URL where the customer is redirected when payment is successful, after returning from an external page such as a 3DS page. Does not support localhost URLs.      |
| error_payment_url    | str  | ❌       | URL where the customer is redirected when payment is not successful, after returning from an external page, such as a 3DS page. Does not support localhost URLs. |
