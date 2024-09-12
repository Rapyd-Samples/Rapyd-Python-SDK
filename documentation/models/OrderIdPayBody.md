# OrderIdPayBody

**Properties**

| Name           | Type   | Required | Description                                                                                                                                         |
| :------------- | :----- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| metadata       | `dict` | ❌       | A JSON object defined by the client.                                                                                                                |
| payment_method | `str`  | ❌       | ID of the payment method. String starting with card* or other*. If not specified, the payment method is the default_payment_method of the customer. |
| customer       | `str`  | ❌       | ID of a customer. String starting with cus\_. The order is paid with the customer's default payment method.                                         |
