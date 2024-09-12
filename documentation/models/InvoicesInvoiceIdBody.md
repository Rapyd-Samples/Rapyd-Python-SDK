# InvoicesInvoiceIdBody

**Properties**

| Name                 | Type    | Required | Description                                                                                                                                                                                    |
| :------------------- | :------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| days_until_due       | `float` | ❌       | The number of days until the due date.                                                                                                                                                         |
| description          | `str`   | ❌       | Description of the invoice.                                                                                                                                                                    |
| due_date             | `str`   | ❌       | The date payment is due on this invoice. This value is calculated from the date the invoice is created, plus the number of days specified in the days_until_due field. Format is in Unix time. |
| metadata             | `dict`  | ❌       | A JSON object defined by the client.                                                                                                                                                           |
| payment_fields       | `dict`  | ❌       | Object containing additional payment_options fields.                                                                                                                                           |
| statement_descriptor | `str`   | ❌       | Description of the invoice for the customer's credit card statement. Limited to 22 characters.                                                                                                 |
| tax_percent          | `float` | ❌       | The tax rate, defined as a percentage.                                                                                                                                                         |
