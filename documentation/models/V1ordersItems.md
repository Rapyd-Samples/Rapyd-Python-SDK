# V1ordersItems

**Properties**

| Name        | Type                | Required | Description                                                                                                                                                                                                           |
| :---------- | :------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| amount      | `str`               | ❌       | Price of one SKU unit, in the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015.                                           |
| currency    | `str`               | ❌       |                                                                                                                                                                                                                       |
| description | `str`               | ❌       | Description of the item.                                                                                                                                                                                              |
| parent      | `str`               | ❌       | ID of the SKU object that represents the product. String starting with sku\_. Each SKU can appear in this list only one time, for items of type 'sku'. Required when type is sku. Must be null when type is shipping. |
| type\_      | `V1ordersItemsType` | ❌       | Type of line item.                                                                                                                                                                                                    |
| quantity    | `float`             | ❌       | Quantity of the product in the line item. Integer. Required when type is sku.                                                                                                                                         |

# V1ordersItemsType

Type of line item.

**Properties**

| Name     | Type  | Required | Description |
| :------- | :---- | :------- | :---------- |
| SHIPPING | `str` | ✅       | "shipping"  |
| SKU      | `str` | ✅       | "sku"       |
