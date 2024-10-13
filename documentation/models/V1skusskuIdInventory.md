# V1skusskuIdInventory

inventory object {quantity, type, value}

**Properties**

| Name     | Type                     | Required | Description |
| :------- | :----------------------- | :------- | :---------- |
| type\_   | V1skusskuIdInventoryType | ❌       |             |
| quantity | int                      | ❌       |             |
| value    | Value                    | ❌       |             |

# V1skusskuIdInventoryType

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| FINITE   | str  | ✅       | "finite"    |
| INFINITE | str  | ✅       | "infinite"  |
| BUCKET   | str  | ✅       | "bucket"    |

# Value

**Properties**

| Name       | Type | Required | Description    |
| :--------- | :--- | :------- | :------------- |
| INSTOCK    | str  | ✅       | "in_stock"     |
| LIMITED    | str  | ✅       | "limited"      |
| OUTOFSTOCK | str  | ✅       | "out_of_stock" |
