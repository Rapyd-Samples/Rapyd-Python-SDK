# V1ordersorderIdreturnsItems

**Properties**

| Name        | Type                            | Required | Description |
| :---------- | :------------------------------ | :------- | :---------- |
| description | str                             | ❌       |             |
| parent      | str                             | ❌       |             |
| type\_      | V1ordersorderIdreturnsItemsType | ❌       |             |
| quantity    | float                           | ❌       |             |
| currency    | str                             | ❌       |             |
| amount      | float                           | ❌       |             |
| order_id    | str                             | ❌       |             |

# V1ordersorderIdreturnsItemsType

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| SKU      | str  | ✅       | "sku"       |
| SHIPPING | str  | ✅       | "shipping"  |
| TAX      | str  | ✅       | "tax"       |
