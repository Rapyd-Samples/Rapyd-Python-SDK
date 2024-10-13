# PaymentsGroupPaymentsBody

**Properties**

| Name                  | Type | Required | Description                                                                                                                                            |
| :-------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| payments              | dict | ✅       | Array of 'payment' objects. For details about the fields in the 'payment' object, see [Create Payment](https://docs.rapyd.net/en/create-payment.html). |
| description           | str  | ❌       | Description of the group payment                                                                                                                       |
| merchant_reference_id | str  | ❌       | ID defined by the client. Limited to 255 characters.                                                                                                   |
| metadata              | dict | ❌       | A JSON object defined by the client.                                                                                                                   |
