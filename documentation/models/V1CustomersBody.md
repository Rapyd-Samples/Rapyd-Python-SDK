# V1CustomersBody

**Properties**

| Name                   | Type            | Required | Description                                                                                                                   |
| :--------------------- | :-------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------- |
| name                   | `str`           | ✅       | The name of the individual customer or the business name                                                                      |
| addresses              | `List[Address]` | ❌       | Array of address objects associated with this customer. For more information                                                  |
| business_vat_id        | `str`           | ❌       | The tax ID number of the customer                                                                                             |
| coupon                 | `str`           | ❌       | The ID of a coupon that is assigned to this customer                                                                          |
| default_payment_method | `str`           | ❌       | The payment method that is used when the transaction does not specify a payment method. String starting with card* or other*. |
| description            | `str`           | ❌       | A text description of the customer                                                                                            |
| email                  | `str`           | ❌       | Customer's email address                                                                                                      |
| ewallet                | `str`           | ❌       | ID of the wallet that is linked to the customer. String starting with ewallet\_                                               |
| invoice_prefix         | `str`           | ❌       | A custom string that is prefixed to all invoices for this customer                                                            |
| metadata               | `dict`          | ❌       | A JSON object defined by the Rapyd partner                                                                                    |
| phone_number           | `str`           | ❌       | Customer's primary phone number in E.164 format                                                                               |
