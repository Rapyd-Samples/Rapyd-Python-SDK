# ApplicationsHostedBody

**Properties**

| Name                | Type | Required | Description                                                                                                                                                                |
| :------------------ | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| country             | str  | ✅       | The country where the company is domiciled. Two-letter ISO 3166-1 ALPHA-2 code. The hosted application displays the country as the default setting.                        |
| rapyd_entity_token  | str  | ✅       | The ID of the Rapyd wallet of the company. String starting with ewallet\_.                                                                                                 |
| phone_number        | str  | ✅       | The phone number of the applicant. This is the phone number where an authentication code is sent. Must have a leading plus sign (+).                                       |
| application_type    | str  | ❌       | Code for the type of application.                                                                                                                                          |
| metadata            | dict | ❌       | A JSON object defined by the client.                                                                                                                                       |
| client_reference_id | str  | ❌       | ID defined by the client. Limited to 255 characters.                                                                                                                       |
| cancel_url          | str  | ❌       | URL where the customer is redirected after pressing Back to Website to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs. |
| complete_url        | str  | ❌       | URL where the customer is redirected after pressing Close to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs.           |
