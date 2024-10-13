# V1SkusBody

**Properties**

| Name               | Type                         | Required | Description                                                                                                                                                 |
| :----------------- | :--------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| currency           | str                          | ✅       |                                                                                                                                                             |
| inventory          | V1skusskuIdInventory         | ✅       | inventory object {quantity, type, value}                                                                                                                    |
| price              | float                        | ✅       | The amount of the price. Decimal.                                                                                                                           |
| product            | str                          | ✅       | ID of the product that this SKU relates to. The type field of the product must be set to goods.                                                             |
| active             | bool                         | ❌       | Indicates whether the product is currently available for purchase.                                                                                          |
| attributes         | List[str]                    | ❌       | Array of alphanumeric key-value pairs defined by the merchant. Each key must match a string in the "attributes" list of the corresponding "product" object. |
| image              | str                          | ❌       | URL of image associated with the product.                                                                                                                   |
| metadata           | dict                         | ❌       | A JSON object defined by the client.                                                                                                                        |
| package_dimensions | V1skusskuIdPackageDimensions | ❌       | Physical attributes of the SKU item. Object containing the following fields - height, length, weight, width                                                 |
