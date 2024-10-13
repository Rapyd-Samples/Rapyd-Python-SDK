# AddressResponse

**Properties**

| Name         | Type  | Required | Description                                                                                                                                                                           |
| :----------- | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| canton       | str   | ❌       | Name of the canton administrative subdivision, as used in banking.                                                                                                                    |
| city         | str   | ❌       | City portion of the address.                                                                                                                                                          |
| country      | str   | ❌       | The two-letter ISO 3166-1 ALPHA-2 code for the country.                                                                                                                               |
| created_at   | float | ❌       | Time of creation of the object, in Unix time.                                                                                                                                         |
| district     | str   | ❌       | Name of the district administrative subdivision, as used in banking.                                                                                                                  |
| id\_         | str   | ❌       | ID of the `address` object.                                                                                                                                                           |
| line_1       | str   | ❌       | Line 1 of the address, such as a building number and street name.                                                                                                                     |
| line_2       | str   | ❌       | Line 2 of the address, such as a suite or apartment number, or the name of a named building.                                                                                          |
| line_3       | str   | ❌       | Line 2 of the address, such as a suite or apartment number, or the name of a named building.                                                                                          |
| metadata     | any   | ❌       | A JSON object defined by the client.                                                                                                                                                  |
| name         | str   | ❌       | The name of a contact person or an 'in care of' person at this address. For a **personal** wallet contact type, alphabetic characters and spaces.A JSON object defined by the client. |
| phone_number | str   | ❌       | Phone number associated with this specific address in E.164 format. Must be unique.                                                                                                   |
| state        | str   | ❌       | State or province portion of the address.                                                                                                                                             |
| zip          | str   | ❌       | Postal code portion of the address.                                                                                                                                                   |
