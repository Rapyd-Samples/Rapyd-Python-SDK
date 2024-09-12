# CustomerPaymentMethods

An object containing the following fields - _ data - A list of up to three payment methods. For more information, see Customer Payment Method Object. _ has_more - Indicates whether there are more than three payment methods for this customer. _ total_count - Total number of payment methods for this customer. _ url - URL for requesting all of the payment methods for this customer..

**Properties**

| Name        | Type                          | Required | Description |
| :---------- | :---------------------------- | :------- | :---------- |
| data        | `List[CustomerPaymentMethod]` | ❌       |             |
| has_more    | `bool`                        | ❌       |             |
| total_count | `int`                         | ❌       |             |
| url         | `str`                         | ❌       |             |
