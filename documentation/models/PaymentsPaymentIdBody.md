# PaymentsPaymentIdBody

**Properties**

| Name                | Type     | Required | Description                                                                                                                                                |
| :------------------ | :------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| address             | Address1 | ❌       | address associated with this specific Rapyd entity Payment/Customer etc...                                                                                 |
| description         | str      | ❌       | Description of the payment.                                                                                                                                |
| escrow              | bool     | ❌       | To release escrow funds immediately, set to false. If there are multiple sellers, the funds are released to all of them. Relevant to payments with escrow. |
| escrow_release_days | int      | ❌       | Defines the number of days after the creation of the payment that the funds are automatically released. Relevant when escrow is true.                      |
| initiation_type     | str      | ❌       | Category of transaction initiation type.                                                                                                                   |
| metadata            | dict     | ❌       | A JSON object defined by the client.                                                                                                                       |
| receipt_email       | str      | ❌       | Email address that the receipt for this transaction is sent to.                                                                                            |
