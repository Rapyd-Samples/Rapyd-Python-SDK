# TransferResponseBody

**Properties**

| Name     | Type   | Required | Description                                                                                                     |
| :------- | :----- | :------- | :-------------------------------------------------------------------------------------------------------------- |
| id\_     | `str`  | ✅       | ID of the transfer transaction, from the `id` field in the `data` object of the response. 32-digit hexadecimal. |
| status   | `str`  | ✅       | Determines how to handle the transfer. One of the following values - accept, decline, cancel                    |
| metadata | `dict` | ❌       | A JSON object defined by the client.                                                                            |
