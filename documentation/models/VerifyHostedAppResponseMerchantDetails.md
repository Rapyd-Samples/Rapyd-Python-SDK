# VerifyHostedAppResponseMerchantDetails

Object containing information about the merchant.

**Properties**

| Name                      | Type                                                          | Required | Description                                                                                                                                |
| :------------------------ | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| merchant_alias            | str                                                           | ❌       | The name that appears on the hosted page when merchant_logo is not specified. To change this value, contact Client Support. Response only. |
| merchant_language         | str                                                           | ❌       | Determines the default language of the application page. The values are documented in List Hosted Page Supported Languages.                |
| merchant_logo             | str                                                           | ❌       | URL for the image of the client's logo. Response only. To configure this feature, use the Client Portal.                                   |
| merchant_website          | str                                                           | ❌       | The URL where the customer is redirected after exiting the hosted page.                                                                    |
| merchant_color            | str                                                           | ❌       |                                                                                                                                            |
| merchant_design           | str                                                           | ❌       |                                                                                                                                            |
| merchant_customer_support | VerifyHostedAppResponseMerchantDetailsMerchantCustomerSupport | ❌       |                                                                                                                                            |
| merchant_terms            | str                                                           | ❌       |                                                                                                                                            |
| merchant_privacy_policy   | str                                                           | ❌       |                                                                                                                                            |
