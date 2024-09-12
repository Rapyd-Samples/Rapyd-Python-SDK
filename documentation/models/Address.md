# Address

address associated with this specific Rapyd entity Payment/Customer etc...

**Properties**

| Name         | Type    | Required | Description                                                                                 |
| :----------- | :------ | :------- | :------------------------------------------------------------------------------------------ |
| canton       | `str`   | ❌       | Name of the canton administrative subdivision, as used in banking                           |
| city         | `str`   | ❌       | City name portion of the address. Required for issuance of a card to an eWallet contact     |
| country      | `str`   | ❌       |                                                                                             |
| created_at   | `float` | ❌       | Time of creation of the payment, in Unix time. Response only.                               |
| district     | `str`   | ❌       | Name of the district administrative subdivision, as used in banking                         |
| id\_         | `str`   | ❌       | ID of the Address object. String starting with address\_                                    |
| line_1       | `str`   | ❌       | Line 1 of the address, such as a building number and street name                            |
| line_2       | `str`   | ❌       | Line 2 of the address, such as a suite or apartment number, or the name of a named building |
| line_3       | `str`   | ❌       | Line 3 of the address                                                                       |
| metadata     | `dict`  | ❌       | A JSON object defined by the client                                                         |
| name         | `str`   | ❌       | The name of a contact person or an `in care of` person at this address                      |
| phone_number | `str`   | ❌       | Phone number associated with this specific address in E.164 format. Must be unique          |
| state        | `str`   | ❌       |                                                                                             |
| zip          | `str`   | ❌       | Postal code portion of the address                                                          |
