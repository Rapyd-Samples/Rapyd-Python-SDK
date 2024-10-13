# Contact

**Properties**

| Name                  | Type               | Required | Description                                                                                                                                              |
| :-------------------- | :----------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| address               | Address            | ❌       | address associated with this specific Rapyd entity Payment/Customer etc...                                                                               |
| business_details      | ContactBusiness    | ❌       |                                                                                                                                                          |
| compliance_profile    | float              | ❌       | Indicates the degree to which this contact can use the wallet.                                                                                           |
| contact_type          | ContactType        | ❌       | Type of contact.                                                                                                                                         |
| country               | str                | ❌       | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code. |
| created_at            | float              | ❌       |                                                                                                                                                          |
| date_of_birth         | str                | ❌       | Date of birth of the individua                                                                                                                           |
| email                 | str                | ❌       | Email address of the contact                                                                                                                             |
| ewallet               | str                | ❌       | ID of the Rapyd Wallet that this contact is associated with. String starting with **ewallet\_**.                                                         |
| first_name            | str                | ❌       | First name of the personal contact or primary person associated with the business contact.                                                               |
| gender                | ContactGender      | ❌       | Gender of the personal contact or primary person associated with the business contact                                                                    |
| house_type            | HouseType          | ❌       | Description of the type of residency at the contact's residence.                                                                                         |
| id\_                  | str                | ❌       | ID of the contact object. String starting with cont\_.                                                                                                   |
| identification_number | str                | ❌       | ID number as shown by the ID document.                                                                                                                   |
| identification_type   | str                | ❌       | Type of the identification document associated with the contact. Uppercase.                                                                              |
| issued_card_data      | dict               | ❌       | Describes additional information about the business contact for a company wallet.                                                                        |
| last_name             | str                | ❌       | Family name of the personal contact or primary person associated with the business contact. Required for issuing a card to a personal contact.           |
| marital_status        | MaritalStatus      | ❌       | Marital status of the personal contact or primary person associated with the business contact.                                                           |
| metadata              | dict               | ❌       | A JSON object defined by the client.                                                                                                                     |
| middle_name           | str                | ❌       | Middle name of the personal contact or primary person associated with the business contact.                                                              |
| mothers_name          | str                | ❌       | Name of the contact's mother                                                                                                                             |
| nationality           | str                | ❌       | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code. |
| phone_number          | str                | ❌       | Phone number of the contact in E.164 format.                                                                                                             |
| second_last_name      | str                | ❌       | Second last name of the personal contact or primary person associated with the business contact.                                                         |
| send_notifications    | bool               | ❌       | Determines whether Rapyd sends notifications to the contact. Default is false.                                                                           |
| verification_status   | VerificationStatus | ❌       | Result of the verification check.                                                                                                                        |
| contact_reference_id  | str                | ❌       | Reference ID for the contact. Limited to 45 characters. Should be unique per merchant per e-wallet.                                                      |

# ContactType

Type of contact.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| PERSONAL | str  | ✅       | "personal"  |
| BUSINESS | str  | ✅       | "business"  |

# ContactGender

Gender of the personal contact or primary person associated with the business contact

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| MALE          | str  | ✅       | "male"           |
| FEMALE        | str  | ✅       | "female"         |
| OTHER         | str  | ✅       | "other"          |
| NOTAPPLICABLE | str  | ✅       | "not_applicable" |

# HouseType

Description of the type of residency at the contact's residence.

**Properties**

| Name           | Type | Required | Description        |
| :------------- | :--- | :------- | :----------------- |
| LEASE          | str  | ✅       | "lease"            |
| LIVEWITHFAMILY | str  | ✅       | "live_with_family" |
| OWN            | str  | ✅       | "own"              |
| OWNER          | str  | ✅       | "owner"            |
| MONTHTOMONTH   | str  | ✅       | "month_to_month"   |
| HOUSINGPROJECT | str  | ✅       | "housing_project"  |

# MaritalStatus

Marital status of the personal contact or primary person associated with the business contact.

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| MARRIED       | str  | ✅       | "married"        |
| SINGLE        | str  | ✅       | "single"         |
| DIVORCED      | str  | ✅       | "divorced"       |
| WIDOWED       | str  | ✅       | "widowed"        |
| COHABITING    | str  | ✅       | "cohabiting"     |
| NOTAPPLICABLE | str  | ✅       | "not_applicable" |

# VerificationStatus

Result of the verification check.

**Properties**

| Name        | Type | Required | Description    |
| :---------- | :--- | :------- | :------------- |
| NOTVERIFIED | str  | ✅       | "not verified" |
| KYCD        | str  | ✅       | "KYCd"         |
