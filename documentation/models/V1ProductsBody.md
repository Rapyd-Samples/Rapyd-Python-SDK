# V1ProductsBody

**Properties**

| Name                 | Type                        | Required | Description                                                                                                                                                                                                                                       |
| :------------------- | :-------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name                 | str                         | ✅       | The name of the product or service that is displayed to the customer.                                                                                                                                                                             |
| type\_               | V1ProductsBodyType          | ✅       | One of the following - services, goods                                                                                                                                                                                                            |
| active               | bool                        | ❌       | Indicates whether the product is currently available for purchase. Default is true.                                                                                                                                                               |
| attributes           | List[str]                   | ❌       | Array of up to 5 alphanumeric strings defined by the merchant. Each string defines the key in a key-value pair in the 'attributes' object in the corresponding 'sku' objects.                                                                     |
| description          | str                         | ❌       | Full text description of the product.                                                                                                                                                                                                             |
| id\_                 | str                         | ❌       | Unique string for identification of the product. Legal input includes all the English alphanumeric characters and the underscore (_) character. If the merchant does not define an ID, Rapyd generates it with a string that starts with product_ |
| images               | List[str]                   | ❌       | An array of images. Each image is a string in Base64 encoding.                                                                                                                                                                                    |
| metadata             | dict                        | ❌       | A JSON object defined by the client.                                                                                                                                                                                                              |
| package_dimensions   | V1productsPackageDimensions | ❌       | Describes the physical size and weight of the product. Relevant when type is goods.                                                                                                                                                               |
| shippable            | bool                        | ❌       | Indicates whether the product is physically shipped to the customer. Relevant when type is goods. Default is false.                                                                                                                               |
| statement_descriptor | str                         | ❌       | A text description that appears in the customer's invoice. Limited to 22 characters. Relevant when type is service.                                                                                                                               |
| unit_label           | str                         | ❌       | A label that represents units of this product, such as seats, on customers’ invoices. Relevant when type is service.                                                                                                                              |

# V1ProductsBodyType

One of the following - services, goods

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| SERVICES | str  | ✅       | "services"  |
| GOODS    | str  | ✅       | "goods"     |
