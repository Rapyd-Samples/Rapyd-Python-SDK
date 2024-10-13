# Ewallet

**Properties**

| Name                 | Type            | Required | Description                                                                  |
| :------------------- | :-------------- | :------- | :--------------------------------------------------------------------------- |
| accounts             | List[Account]   | ❌       |                                                                              |
| category             | EwalletCategory | ❌       | Indicates the type of client wallet                                          |
| contacts             | EwalletContacts | ❌       |                                                                              |
| email                | str             | ❌       | Email address of the wallet owner. Response only. Deprecated.                |
| ewallet_reference_id | str             | ❌       | Wallet ID defined by the customer or end user. Must be unique.               |
| first_name           | str             | ❌       | First name of the wallet owner.                                              |
| id\_                 | str             | ❌       | Unique identifier of the wallet object. String starting with **ewallet\_**.  |
| last_name            | str             | ❌       | Last name of the wallet owner.                                               |
| metadata             | dict            | ❌       | A JSON object defined by the client.                                         |
| phone_number         | str             | ❌       | Phone number of the wallet owner in E.164 format. Response only. Deprecated. |
| status               | EwalletStatus   | ❌       | Status of the wallet                                                         |
| type\_               | EwalletType     | ❌       | Type of wallet.                                                              |
| verification_status  | str             | ❌       | Result of the verification check.                                            |

# EwalletCategory

Indicates the type of client wallet

**Properties**

| Name              | Type | Required | Description          |
| :---------------- | :--- | :------- | :------------------- |
| COLLECT           | str  | ✅       | "collect"            |
| DISBURSE          | str  | ✅       | "disburse"           |
| CARDAUTHORIZATION | str  | ✅       | "card_authorization" |
| GENERAL           | str  | ✅       | "general"            |

# EwalletStatus

Status of the wallet

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| ACT  | str  | ✅       | "ACT"       |
| DIS  | str  | ✅       | "DIS"       |

# EwalletType

Type of wallet.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| COMPANY | str  | ✅       | "company"   |
| PERSON  | str  | ✅       | "person"    |
| CLIENT  | str  | ✅       | "client"    |
