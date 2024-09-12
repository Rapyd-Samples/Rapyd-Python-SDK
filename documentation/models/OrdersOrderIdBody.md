# OrdersOrderIdBody

**Properties**

| Name        | Type                      | Required | Description                                                                                                                                                                                                                    |
| :---------- | :------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| coupon      | `str`                     | ❌       | ID of a coupon that is applied against this order. String starting with coupon\_. The duration field of the coupon must be set to repeating, and the duration_in_months and discount_duration_in_uses fields must be set to 1. |
| metadata    | `dict`                    | ❌       | A JSON object defined by the client.                                                                                                                                                                                           |
| tax_percent | `float`                   | ❌       | Percentage of tax to charge. Decimal.                                                                                                                                                                                          |
| status      | `OrdersOrderIdBodyStatus` | ❌       | Indicates the status of the order. Can be changed when status is pending, paid or fulfilled                                                                                                                                    |

# OrdersOrderIdBodyStatus

Indicates the status of the order. Can be changed when status is pending, paid or fulfilled

**Properties**

| Name      | Type  | Required | Description |
| :-------- | :---- | :------- | :---------- |
| PAID      | `str` | ✅       | "paid"      |
| PENDING   | `str` | ✅       | "pending"   |
| CANCELED  | `str` | ✅       | "canceled"  |
| FULFILLED | `str` | ✅       | "fulfilled" |
| RETURNED  | `str` | ✅       | "returned"  |
| PARTIAL   | `str` | ✅       | "partial"   |
