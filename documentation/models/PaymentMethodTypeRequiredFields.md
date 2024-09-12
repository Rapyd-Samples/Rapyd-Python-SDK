# PaymentMethodTypeRequiredFields

Payment Method Type required fields

**Properties**

| Name                       | Type          | Required | Description                                                                                                            |
| :------------------------- | :------------ | :------- | :--------------------------------------------------------------------------------------------------------------------- |
| fields                     | `List[Field]` | ❌       | Payment Method Type required field                                                                                     |
| maximum_expiration_seconds | `float`       | ❌       | The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true |
| minimum_expiration_seconds | `float`       | ❌       | The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true |
| payment_method_options     | `List[Field]` | ❌       | payment method option                                                                                                  |
| payment_options            | `List[Field]` | ❌       |                                                                                                                        |
| type\_                     | `str`         | ❌       |                                                                                                                        |
