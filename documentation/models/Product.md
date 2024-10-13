# Product

**Properties**

| Name                 | Type                     | Required | Description                                                                                                                                                                                                                                                                     |
| :------------------- | :----------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| active               | bool                     | ❌       | Indicates whether the product is currently available for purchase.                                                                                                                                                                                                              |
| attributes           | List[str]                | ❌       | Up to 5 unique alphanumeric strings defined by the merchant. Cannot contain spaces. For example: [ > "size", > "color"] Each string defines the key in a key-value pair in the 'attributes' object in the corresponding 'sku' objects.                                          |
| created_at           | float                    | ❌       | Time of creation of this product, in Unix time. Response only.                                                                                                                                                                                                                  |
| description          | str                      | ❌       | Full text description of the product.                                                                                                                                                                                                                                           |
| id\_                 | str                      | ❌       | Unique string for identification of the product. Legal input includes alphanumeric characters and the underscore () character. If the merchant does not define an ID, Rapyd generates it with a string that starts with **product**.                                            |
| images               | List[str]                | ❌       | Images associated with the product.                                                                                                                                                                                                                                             |
| metadata             | dict                     | ❌       | A JSON object defined by the client.                                                                                                                                                                                                                                            |
| name                 | str                      | ❌       | The name of the product or service that appears in the line items in invoices.                                                                                                                                                                                                  |
| package_dimensions   | ProductPackageDimensions | ❌       | Describes the physical size and weight of the product. Contains the following fields: _ height _ length _ weight _ width These fields are represented as numbers, but it is the responsibility of the merchant to define and interpret the relevant units of length and weight. |
| shippable            | bool                     | ❌       | Indicates whether the product can be shipped.                                                                                                                                                                                                                                   |
| skus                 | List[Sku]                | ❌       |                                                                                                                                                                                                                                                                                 |
| statement_descriptor | str                      | ❌       | Description that is suitable for a customer's statement. Limited to 22 characters. Relevant when type is service. Must be null when type is goods.                                                                                                                              |
| type\_               | ProductType              | ❌       | One of the following: _ services - Relevant to subscriptions and plans. _ goods - Relevant to orders and SKUs.                                                                                                                                                                  |
| unit_label           | str                      | ❌       | Determines what one unit of this product is called on customersâ€™ receipts and invoices, such as minutes, viewings, kilometers or packages. Relevant when type is service. Must be null when type is goods.                                                                   |
| updated_at           | float                    | ❌       | Time that this product was last updated, in Unix time. Response only.                                                                                                                                                                                                           |

# ProductType

One of the following: _ services - Relevant to subscriptions and plans. _ goods - Relevant to orders and SKUs.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| GOODS    | str  | ✅       | "goods"     |
| SERVICES | str  | ✅       | "services"  |
