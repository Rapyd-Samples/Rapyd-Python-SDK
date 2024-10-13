# V1ewalletsContact

**Properties**

| Name                 | Type          | Required | Description                                                          |
| :------------------- | :------------ | :------- | :------------------------------------------------------------------- |
| data                 | List[Contact] | ❌       |                                                                      |
| total_count          | float         | ❌       |                                                                      |
| has_more             | bool          | ❌       |                                                                      |
| url                  | str           | ❌       |                                                                      |
| ewallet_reference_id | str           | ❌       | Rapyd Wallet ID defined by the customer or end user. Must be unique. |
| first_name           | str           | ❌       | First name of the Rapyd Wallet owner.                                |
| last_name            | str           | ❌       | Last name of the Rapyd Wallet owner.                                 |
| metadata             | dict          | ❌       | A JSON object defined by the client.                                 |
| type\_               | str           | ❌       | Type of wallet, company or person. Default is person.                |
| phone_number         | str           | ❌       | Phone number of the Rapyd Wallet owner.                              |
