# V1RefundsBody

**Properties**

| Name                  | Type      | Required | Description                                                                                      |
| :-------------------- | :-------- | :------- | :----------------------------------------------------------------------------------------------- |
| payment               | str       | ✅       | ID of the Payment object that the refund is charged against. String starting with **payment\_**. |
| amount                | float     | ❌       | The amount of the refund. Decimal.                                                               |
| currency              | str       | ❌       | The currency of the amount received by the original payment source. Three-letter ISO 4217 code.  |
| ewallets              | List[str] | ❌       | ID of the wallet contact that the card is assigned to. String starting with **cont\_**.          |
| merchant_reference_id | str       | ❌       | ID defined by the client. Limited to 255 characters.                                             |
| metadata              | dict      | ❌       | A JSON object defined by the client.                                                             |
| reason                | str       | ❌       | Description of the reason for the refund.                                                        |
