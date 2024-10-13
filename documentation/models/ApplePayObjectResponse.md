# ApplePayObjectResponse

**Properties**

| Name                        | Type  | Required | Description                                                                                                              |
| :-------------------------- | :---- | :------- | :----------------------------------------------------------------------------------------------------------------------- |
| display_name                | str   | ❌       | The canonical name for the client's business, suitable for display. 64 or fewer UTF-8 characters. Relevant to Apple Pay. |
| domain_name                 | str   | ❌       | The domain name of the client's ecommerce site.                                                                          |
| epoch_timestamp             | float | ❌       | Time of creation of the Apple Pay session, in Unix time.                                                                 |
| expires_at                  | float | ❌       | Time of expiration of the Apple Pay session, in Unix time.                                                               |
| merchant_identifier         | str   | ❌       | Your Apple Pay merchant ID.                                                                                              |
| merchant_session_identifier | str   | ❌       | Your Apple Pay session ID.                                                                                               |
| nonce                       | str   | ❌       | A string that uniquely identifies each call to Apple Pay.                                                                |
| retries                     | float | ❌       | The number of previous attempts to get an Apple Pay Session object.                                                      |
| signature                   | str   | ❌       | Digital signature that validates the authenticity and integrity of a digital wallet payment.                             |
