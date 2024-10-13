# ProductsProductsIdBody

**Properties**

| Name                 | Type                        | Required | Description                                                                                                                                                                   |
| :------------------- | :-------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                 | str                         | ✅       | The name of the product or service that is displayed to the customer.                                                                                                         |
| active               | bool                        | ❌       | Indicates whether the product is currently available for purchase. Default is true.                                                                                           |
| attributes           | List[str]                   | ❌       | Array of up to 5 alphanumeric strings defined by the merchant. Each string defines the key in a key-value pair in the 'attributes' object in the corresponding 'sku' objects. |
| metadata             | dict                        | ❌       | A JSON object defined by the client.                                                                                                                                          |
| package_dimensions   | V1productsPackageDimensions | ❌       | Describes the physical size and weight of the product. Relevant when type is goods.                                                                                           |
| statement_descriptor | str                         | ❌       | A text description that appears in the customer's invoice. Limited to 22 characters. Relevant when type is service.                                                           |
| unit_label           | str                         | ❌       | A label that represents units of this product, such as seats, on customersâ€™                                                                                                |
