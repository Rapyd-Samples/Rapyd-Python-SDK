# V1EwalletsBody

**Properties**

| Name                 | Type              | Required | Description                                                          |
| :------------------- | :---------------- | :------- | :------------------------------------------------------------------- |
| contact              | V1ewalletsContact | ✅       |                                                                      |
| ewallet_reference_id | str               | ❌       | Rapyd Wallet ID defined by the customer or end user. Must be unique. |
| first_name           | str               | ❌       | First name of the Rapyd Wallet owner.                                |
| last_name            | str               | ❌       | Last name of the Rapyd Wallet owner.                                 |
| metadata             | dict              | ❌       | A JSON object defined by the client.                                 |
| type\_               | str               | ❌       | Type of wallet, company or person. Default is person.                |
