# CardTransaction

**Properties**

| Name                       | Type           | Required | Description                                                                                                                                                                             |
| :------------------------- | :------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| amount                     | `float`        | ❌       | Amount of the transaction, in units defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. Response only. |
| auth_code                  | `str`          | ❌       | Authorization code sent to the merchant. Relevant to authorizations approved by Rapyd. Response only.                                                                                   |
| authorization_approved_by  | `str`          | ❌       | Approver of the transaction when remote authorization is used. See Remote Authorization.                                                                                                |
| bin                        | `str`          | ❌       | The first 6 digits of the card number. Response only.                                                                                                                                   |
| card_authorization         | `str`          | ❌       |                                                                                                                                                                                         |
| card_id                    | `str`          | ❌       | ID of the card. String starting with card\_. Response only.                                                                                                                             |
| card_program               | `str`          | ❌       | ID of the card program that the card is issued from. String starting with cardprog\_. Response only.                                                                                    |
| created_at                 | `float`        | ❌       | Time of creation of the transaction object, in Unix time. Response only.                                                                                                                |
| currency                   | `str`          | ❌       |                                                                                                                                                                                         |
| fx_rate                    | `float`        | ❌       | The exchange rate. Response only.                                                                                                                                                       |
| id\_                       | `str`          | ❌       | ID of the issued card transaction object. String starting with cit\_.                                                                                                                   |
| issuing_txn_type           | `str`          | ❌       | Type of the transaction.                                                                                                                                                                |
| last4                      | `str`          | ❌       | The last 4 digits of the card number. Response only.                                                                                                                                    |
| merchant_category_code     | `str`          | ❌       | Four-digit merchant category code (MCC) of the initiator of the transaction, as defined in ISO 18245. Response only.                                                                    |
| merchant_name_location     | `str`          | ❌       | Name and location of the merchant. Maximum 40 characters. Response only.                                                                                                                |
| original_transaction_id    | `str`          | ❌       | ID of the original card transaction. Response only.                                                                                                                                     |
| original_txn_amount        | `float`        | ❌       | Original amount for FX transactions, when currency is different from original_txn_currency. Response only.                                                                              |
| original_txn_currency      | `str`          | ❌       | Original currency in FX transaction. Three-letter ISO 4217 code. Response only.                                                                                                         |
| pos_entry_mode             | `PosEntryMode` | ❌       | The mode of the POS entry. One of the following                                                                                                                                         |
| retrieval_reference_number | `str`          | ❌       | Reserved.                                                                                                                                                                               |
| systems_trace_audit_number | `str`          | ❌       | Reserved                                                                                                                                                                                |
| wallet_transaction_id      | `str`          | ❌       | ID of the wallet transaction. String starting with wt\_. Response only.                                                                                                                 |

# PosEntryMode

The mode of the POS entry. One of the following

**Properties**

| Name           | Type  | Required | Description      |
| :------------- | :---- | :------- | :--------------- |
| MAGSTRIPE      | `str` | ✅       | "magstripe"      |
| MANUALENTERED  | `str` | ✅       | "manual_entered" |
| EMV            | `str` | ✅       | "emv"            |
| EMVSTANDIN     | `str` | ✅       | "emv_standin"    |
| NFC            | `str` | ✅       | "nfc"            |
| NETWORKTOKEN   | `str` | ✅       | "network_token"  |
| ECOMMERCE      | `str` | ✅       | "ecommerce"      |
| \_3DSECOMMERCE | `str` | ✅       | "3ds_ecommerce"  |
| ADJUSTMENT     | `str` | ✅       | "adjustment"     |
