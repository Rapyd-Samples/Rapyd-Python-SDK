# VerifyHostedAppResponse

**Properties**

| Name                  | Type                                   | Required | Description                                                                                                                                                                |
| :-------------------- | :------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| token                 | str                                    | ❌       | Identifier of the hosted application. String starting with happ\_.                                                                                                         |
| rapyd_entity_token    | str                                    | ❌       | The ID of the Rapyd wallet of the company. String starting with ewallet\_. Must be a company type wallet.                                                                  |
| cancel_url            | str                                    | ❌       | URL where the customer is redirected after pressing Back to Website to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs. |
| complete_url          | str                                    | ❌       | URL where the customer is redirected after pressing Close to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs.           |
| client_reference_id   | str                                    | ❌       | ID defined by the client. Limited to 255 characters.                                                                                                                       |
| application_token     | str                                    | ❌       | Identifier of the application. String starting with app\_.                                                                                                                 |
| phone_number          | str                                    | ❌       | The phone number of the applicant. This is the phone number where an authentication code is sent. Must have a leading plus sign (+).                                       |
| merchant_details      | VerifyHostedAppResponseMerchantDetails | ❌       | Object containing information about the merchant.                                                                                                                          |
| redirect_url          | str                                    | ❌       | URL of the hosted page that is shown to the customer.                                                                                                                      |
| metadata              | dict                                   | ❌       | A JSON object defined by the client                                                                                                                                        |
| authorized_user_email | str                                    | ❌       |                                                                                                                                                                            |
