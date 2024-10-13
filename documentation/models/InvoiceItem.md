# InvoiceItem

Invoice item

**Properties**

| Name              | Type              | Required | Description                                                                                 |
| :---------------- | :---------------- | :------- | :------------------------------------------------------------------------------------------ |
| id\_              | str               | ❌       | line item id                                                                                |
| amount            | float             | ❌       | amount                                                                                      |
| currency          | str               | ❌       |                                                                                             |
| description       | str               | ❌       | item description                                                                            |
| discountable      | bool              | ❌       |                                                                                             |
| invoice_item      | str               | ❌       | invoice item id                                                                             |
| metadata          | dict              | ❌       | A JSON object defined by the client.                                                        |
| period            | InvoiceItemPeriod | ❌       |                                                                                             |
| proration         | bool              | ❌       |                                                                                             |
| quantity          | float             | ❌       |                                                                                             |
| plan              | Plan              | ❌       |                                                                                             |
| subscription      | str               | ❌       | ID of the subscription that generates charges to this customer. String starting with sub\_. |
| subscription_item | str               | ❌       | ID of the subscription item that generates charges to this customer.                        |
| type\_            | str               | ❌       |                                                                                             |
