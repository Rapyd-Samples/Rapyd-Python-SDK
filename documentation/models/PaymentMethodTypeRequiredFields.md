# PaymentMethodTypeRequiredFields

Payment Method Type required fields - this is the response of GET required fields for Payment_Method_Type

**Properties**

| Name                       | Type         | Required | Description                                                                                                            |
| :------------------------- | :----------- | :------- | :--------------------------------------------------------------------------------------------------------------------- |
| fields                     | List[Field1] | ❌       | Payment Method Type required field                                                                                     |
| maximum_expiration_seconds | float        | ❌       | The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true |
| minimum_expiration_seconds | float        | ❌       | The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true |
| payment_method_options     | List[Field1] | ❌       | payment method option                                                                                                  |
| payment_options            | List[Field1] | ❌       |                                                                                                                        |
| type\_                     | str          | ❌       |                                                                                                                        |
