# Rapydsdk Python SDK 1.0.5

A Python SDK for Rapydsdk.

This is Rapyd OpenAPI

- API version: 1.0.5
- SDK version: 1.0.5

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
  - [Dependencies](#dependencies)
- [Environment Variables](#environment-variables)
- [API Endpoint Services](#api-endpoint-services)
- [API Models](#api-models)
- [Testing](#testing)
- [Configuration](#configuration)
- [Sample Usage](#sample-usage)
- [Environments](#environments)
- [Rapydsdk Services](#rapydsdk-services)
- [License](#license)

## Installation

```bash
pip install rapydsdk
```

### Dependencies

This SDK uses the following dependencies:

- requests 2.28.1
- http-exceptions 0.2.10
- pytest 7.1.2
- responses 0.21.0

## Environment Variables

You will need the following environment variables in order to access all the features of this SDK:

| Name       | Description          |
| :--------- | :------------------- |
| ACCESS_KEY | Access Key parameter |
| SECRET_KEY | Secret Key parameter |

You can set these environment variables on the command line or you can use
whatever tooling your project has in place to manage environment variables. If
you are using a `.env` file, we have provided a template with the variable names
in the `.env.example` file in the same directory as this readme.

## API Endpoint Services

All URIs are relative to https://api.rapyd.net.

Click the service name for a full list of the service methods.

| Service                                                   |
| :-------------------------------------------------------- |
| [EWallets](./services/README.md#ewallets)                 |
| [Collect](./services/README.md#collect)                   |
| [GeneralResources](./services/README.md#generalresources) |
| [Hosted](./services/README.md#hosted)                     |
| [Verify](./services/README.md#verify)                     |
| [Issuing](./services/README.md#issuing)                   |
| [Disburse](./services/README.md#disburse)                 |

## API Models

[A list documenting all API models for this SDK](./models/README.md#rapydsdk-models).

## Testing

Run unit tests with this command:

```sh
python -m unittest discover -p "test*.py"
```

## Sample Usage

```py
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk

sdk = Rapydsdk()

results = sdk.collect.list_coupon()

pprint(vars(results))
```

## Environments

Here is the list of all available environments:

```py
DEFAULT = 'https://api.rapyd.net'
SANDBOX = 'https://sandboxapi.rapyd.net'
PRODUCTION = 'https://api.rapyd.net'
```

How to set the environment:

```py
from rapydsdk import Rapydsdk, Environment

sdk = Rapydsdk(environment=Environment.DEFAULT)
```

# Rapydsdk Services

A list of all services and services methods.

- Services

  - [EWallets](#ewallets)

  - [Collect](#collect)

  - [GeneralResources](#generalresources)

  - [Hosted](#hosted)

  - [Verify](#verify)

  - [Issuing](#issuing)

  - [Disburse](#disburse)

- [All Methods](#all-methods)

## EWallets

| Method                                                                          | Description                                      |
| :------------------------------------------------------------------------------ | :----------------------------------------------- |
| [funds_transfer](#funds_transfer)                                               | Transfer Funds Between Wallets                   |
| [set_funds_transfer_response](#set_funds_transfer_response)                     | Set Transfer Response                            |
| [create_ewallet_contact](#create_ewallet_contact)                               | Add Contact to Wallet                            |
| [get_ewallet_contacts](#get_ewallet_contacts)                                   | List Contacts for a Rapyd Wallet                 |
| [update_ewallet_contact](#update_ewallet_contact)                               | Update Wallet Contact                            |
| [get_ewallet_contact](#get_ewallet_contact)                                     | Retrieve Wallet Contact.                         |
| [delete_ewallet_contact](#delete_ewallet_contact)                               | Delete Wallet Contact                            |
| [get_ewallet_contact_compliance_levels](#get_ewallet_contact_compliance_levels) | Get the compliance status of a personal contact. |
| [create_user](#create_user)                                                     | Create Wallet                                    |
| [get_users](#get_users)                                                         | List eWallets.                                   |
| [updated_user](#updated_user)                                                   | Update Wallet                                    |
| [get_user](#get_user)                                                           | Retrieve Wallet                                  |
| [delete_user](#delete_user)                                                     | Delete a Wallet.                                 |
| [update_ewallet_status](#update_ewallet_status)                                 | Change Wallet status                             |
| [set_account_limit](#set_account_limit)                                         | Set Wallet Account Limit                         |
| [remove_account_limit](#remove_account_limit)                                   | Delete a coupon from the Rapyd platform          |
| [get_user_accounts](#get_user_accounts)                                         | Retrieve Wallet Balances                         |
| [get_user_transactions](#get_user_transactions)                                 | List Wallet Transactions                         |
| [get_user_transaction_details](#get_user_transaction_details)                   | Get Details of Wallet Transaction                |

## Collect

| Method                                                                              | Description                                                    |
| :---------------------------------------------------------------------------------- | :------------------------------------------------------------- |
| [create_address](#create_address)                                                   | Create an address                                              |
| [update_address](#update_address)                                                   | Update an address                                              |
| [retrieve_address](#retrieve_address)                                               | Retrieve an address                                            |
| [create_coupon](#create_coupon)                                                     | Create new coupon                                              |
| [list_coupon](#list_coupon)                                                         | Retrieve list of coupons                                       |
| [update_coupon](#update_coupon)                                                     | Update a coupon                                                |
| [retrieve_coupon](#retrieve_coupon)                                                 | Retrieve an coupon                                             |
| [delete_coupon](#delete_coupon)                                                     | Delete a coupon from the Rapyd platform                        |
| [get_hosted_page_payment](#get_hosted_page_payment)                                 | Retrieve a checkout page.                                      |
| [generate_hosted_page_payment](#generate_hosted_page_payment)                       | Create checkout page                                           |
| [create_customer](#create_customer)                                                 | Create a customer                                              |
| [list_customer](#list_customer)                                                     | Retrieve list of customers                                     |
| [update_customer](#update_customer)                                                 | Update customer                                                |
| [retrieve_customer](#retrieve_customer)                                             | Retrieve a customer details                                    |
| [delete_customer](#delete_customer)                                                 | Delete a customer from the Rapyd platform                      |
| [delete_customer_discount](#delete_customer_discount)                               | Delete the discount that has been assigned to a customer       |
| [create_customer_payment_method](#create_customer_payment_method)                   | Add a payment method to a customer profile                     |
| [get_customer_payment_methods](#get_customer_payment_methods)                       | Retrieve payment methods for a customer                        |
| [update_customer_payment_method](#update_customer_payment_method)                   | Update payment method for customer                             |
| [get_customer_payment_method](#get_customer_payment_method)                         | Retrieve a payment method for a specific customer              |
| [delete_customer_payment_method](#delete_customer_payment_method)                   | Delete a payment method type from customer                     |
| [get_disputes_list_by_org_id](#get_disputes_list_by_org_id)                         | Retrieve list of disputes                                      |
| [get_dispute](#get_dispute)                                                         | Retrieve an dispute.                                           |
| [list_invoices](#list_invoices)                                                     | List Invoices                                                  |
| [update_invoice](#update_invoice)                                                   | Update Invoice                                                 |
| [retrieve_invoice](#retrieve_invoice)                                               | Retrieve Invoice                                               |
| [delete_invoice](#delete_invoice)                                                   | Delete Invoice                                                 |
| [finalize_invoice](#finalize_invoice)                                               | Finalize Invoice                                               |
| [pay_invoice](#pay_invoice)                                                         | payInvoice                                                     |
| [create_order](#create_order)                                                       | Create an Order                                                |
| [list_order](#list_order)                                                           | List Orders                                                    |
| [update_order](#update_order)                                                       | Update an Order                                                |
| [retrieve_order](#retrieve_order)                                                   | Retrieve an Order                                              |
| [returns_order](#returns_order)                                                     | Create a Return Against an Order                               |
| [pay_order](#pay_order)                                                             | Pay an order.                                                  |
| [list_order_return](#list_order_return)                                             | List Returns                                                   |
| [retrieve_order_return](#retrieve_order_return)                                     | Retrieve a Return                                              |
| [get_payment_methods_types_by_country](#get_payment_methods_types_by_country)       | Retrieve a list of all payment methods available for a country |
| [get_payment_method_type_required_fields](#get_payment_method_type_required_fields) | Retrieve the required fields for a payment method              |
| [create_payment](#create_payment)                                                   | Create a payment                                               |
| [list_payments](#list_payments)                                                     | List Payments                                                  |
| [update_payment](#update_payment)                                                   | Update Payment                                                 |
| [retrieve_payment](#retrieve_payment)                                               | Retrieve Payment                                               |
| [cancel_payment](#cancel_payment)                                                   | Cancel Payment                                                 |
| [create_subscription](#create_subscription)                                         | Create Subscription                                            |
| [get_subscription_list](#get_subscription_list)                                     | List Subscriptions                                             |
| [update_subscription](#update_subscription)                                         | Update Subscription                                            |
| [get_subscription](#get_subscription)                                               | Retrieve Subscription                                          |
| [cancel_subscription](#cancel_subscription)                                         | Cancel Subscription                                            |
| [delete_subscription_discount](#delete_subscription_discount)                       | Delete Discount from Subscription                              |
| [create_plan](#create_plan)                                                         | Create Plan Item                                               |
| [list_plans](#list_plans)                                                           | List Plans                                                     |
| [update_plan](#update_plan)                                                         | Update Plan                                                    |
| [retrieve_plan](#retrieve_plan)                                                     | Retrieve plan                                                  |
| [delete_plan](#delete_plan)                                                         | Delete Plan                                                    |
| [create_product](#create_product)                                                   | Create Product                                                 |
| [get_products_list](#get_products_list)                                             | List Products                                                  |
| [update_product](#update_product)                                                   | Update Product                                                 |
| [get_product](#get_product)                                                         | Retrieve Product                                               |
| [delete_product](#delete_product)                                                   | Delete Product                                                 |
| [request_total_create_refund](#request_total_create_refund)                         | Create Refund                                                  |
| [all_refunds](#all_refunds)                                                         | List Refunds                                                   |
| [simulate_complete_refund](#simulate_complete_refund)                               | Complete Refund                                                |
| [refund_group_payment](#refund_group_payment)                                       | Create Group Refund                                            |
| [update_refund](#update_refund)                                                     | Update Refund                                                  |
| [refund_by_token](#refund_by_token)                                                 | Retrieve Refund                                                |
| [create_subscription_item](#create_subscription_item)                               | Create Subscription Item                                       |
| [list_subscription_item](#list_subscription_item)                                   | List Subscription Items                                        |
| [update_subscription_item](#update_subscription_item)                               | Update Subscription Item                                       |
| [retrieve_subscription_item](#retrieve_subscription_item)                           | Retrieve Subscription Item                                     |
| [delete_subscription_item](#delete_subscription_item)                               | Delete Subscription Item                                       |
| [usage_record_summaries](#usage_record_summaries)                                   | Create Usage Record                                            |
| [create_subscription_item_usage_record](#create_subscription_item_usage_record)     | Create Usage Record                                            |
| [get_subscription_discount_by_id](#get_subscription_discount_by_id)                 | Retrieve an discount                                           |
| [update_sku](#update_sku)                                                           | Retrieve SKU.                                                  |
| [retrieve_sku](#retrieve_sku)                                                       | Retrieve SKU.                                                  |
| [delete_sku](#delete_sku)                                                           | Delete SKU.                                                    |
| [create_sku](#create_sku)                                                           | Create SKU                                                     |
| [list_sku](#list_sku)                                                               | List SKUs.                                                     |

## GeneralResources

| Method                                              | Description                                                                                    |
| :-------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| [get_countries](#get_countries)                     | List Countries                                                                                 |
| [get_currencies](#get_currencies)                   | List Currencies                                                                                |
| [get_daily_rate](#get_daily_rate)                   | Resource Methods                                                                               |
| [get_webhooks](#get_webhooks)                       | List Webhooks.                                                                                 |
| [resend_webhook_by_token](#resend_webhook_by_token) | Use List Webhooks to find the IDs of webhooks. You can resend a webhook that is in status ERR. |
| [get_webhook_by_token](#get_webhook_by_token)       | Use List Webhooks to find the IDs of webhooks.                                                 |

## Hosted

| Method                                                              | Description                                                                                     |
| :------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------- |
| [generate_card_tokenization_page](#generate_card_tokenization_page) | Create a hosted page for a customer to save card details and manage cards.                      |
| [generate_idv_page](#generate_idv_page)                             | Create Identity Verification Page                                                               |
| [generate_card_issuing_page](#generate_card_issuing_page)           | Generate a hosted page that displays details of a virtual issued card directly to the customer. |

## Verify

| Method                                                                                      | Description                                                                       |
| :------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------- |
| [perform_identity_verification](#perform_identity_verification)                             | Verify the identity of an individual or a personal contact for a 'person' wallet. |
| [get_kyc_id_verification_supported_doc_types](#get_kyc_id_verification_supported_doc_types) | Retrieve a list of the types of official identification documents for a country.  |
| [get_application_types_by_country](#get_application_types_by_country)                       | List Rapyd Verify Application Types.                                              |
| [get_application_status](#get_application_status)                                           | Retrieve Status of Rapyd Verify Application                                       |
| [create_hosted_application_token](#create_hosted_application_token)                         | Create Rapyd Verify Application                                                   |
| [get_hosted_application_by_token](#get_hosted_application_by_token)                         | Create Rapyd Verify Application                                                   |

## Issuing

| Method                                                                                                    | Description                              |
| :-------------------------------------------------------------------------------------------------------- | :--------------------------------------- |
| [create_issuing](#create_issuing)                                                                         | Issue Virtual Account Number to Wallet   |
| [simulate_complete_bank_account_issuing_transaction](#simulate_complete_bank_account_issuing_transaction) | Simulate a Bank Transfer to a Wallet     |
| [update_receiving_currency](#update_receiving_currency)                                                   |                                          |
| [retrieve_issuing_by_rapyd_token](#retrieve_issuing_by_rapyd_token)                                       | Retrieve Virtual Account History         |
| [close_issuing](#close_issuing)                                                                           | Close VA                                 |
| [retrieve_issuing_transaction](#retrieve_issuing_transaction)                                             | Retrieve Virtual Account Transaction     |
| [issue_card](#issue_card)                                                                                 | Issue Card                               |
| [get_card_issuing_list](#get_card_issuing_list)                                                           | List issuing cards.                      |
| [get_card_issuing_details](#get_card_issuing_details)                                                     | Card details.                            |
| [activate_card](#activate_card)                                                                           | Activate Issued Card Using API           |
| [modify_card](#modify_card)                                                                               | Personalize Bulk-Issued Card             |
| [update_card_status](#update_card_status)                                                                 | Update Card Status                       |
| [get_card_issuing_transactions](#get_card_issuing_transactions)                                           | List Issued Card Transactions            |
| [get_card_issuing_transaction](#get_card_issuing_transaction)                                             | Retrieve Issued Card Transaction Details |

## Disburse

| Method                                                              | Description                                   |
| :------------------------------------------------------------------ | :-------------------------------------------- |
| [get_payout_method_types_details](#get_payout_method_types_details) | Get Payout Required Fields                    |
| [create_payout](#create_payout)                                     | Create Payout                                 |
| [list_payouts](#list_payouts)                                       | List Payouts                                  |
| [create_beneficiary](#create_beneficiary)                           | Create Beneficiary                            |
| [validate_beneficiary](#validate_beneficiary)                       | Validate Beneficiary                          |
| [get_beneficiary](#get_beneficiary)                                 | Retrieve Beneficiary                          |
| [delete_beneficiary](#delete_beneficiary)                           | Delete Beneficiary                            |
| [simulate_complete_payout](#simulate_complete_payout)               | Complete the Payout                           |
| [confirm_payout](#confirm_payout)                                   | Confirm Payout that involves foreign exchange |
| [create_sender](#create_sender)                                     | Create Sender                                 |
| [get_payer](#get_payer)                                             | Retrieve details of a payout sender.          |
| [delete_payer](#delete_payer)                                       | Delete Sender                                 |
| [get_payout_method_types](#get_payout_method_types)                 | List Payout Method Types                      |
| [update_payout](#update_payout)                                     | Update Payout                                 |
| [get_payout](#get_payout)                                           | Retrieve Payout                               |
| [cancel_payout](#cancel_payout)                                     | Cancel Payout                                 |

## All Methods

### **funds_transfer**

Transfer Funds Between Wallets

- HTTP Method: POST
- Endpoint: /v1/account/transfer

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [FundsTransferRequest](/src/rapydsdk/models/README.md#fundstransferrequest) | Required | Request body. |

**Return Type**

[FundsTransfer200Response](/src/rapydsdk/models/README.md#fundstransfer200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'amount': 63823937.80818334,
	'currency': 'currency',
	'destination_ewallet': 'destination_ewallet',
	'expiration': 'expiration',
	'metadata': {},
	'source_ewallet': 'source_ewallet'
}
results = sdk.e_wallets.funds_transfer(request_input = request_body)

pprint(vars(results))

```

### **set_funds_transfer_response**

Set Transfer Response

- HTTP Method: POST
- Endpoint: /v1/account/transfer/response

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [SetFundsTransferResponseRequest](/src/rapydsdk/models/README.md#setfundstransferresponserequest) | Required | Request body. |

**Return Type**

[SetFundsTransferResponse200Response](/src/rapydsdk/models/README.md#setfundstransferresponse200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'id': 'id',
	'metadata': {},
	'status': 'status'
}
results = sdk.e_wallets.set_funds_transfer_response(request_input = request_body)

pprint(vars(results))

```

### **create_ewallet_contact**

Add Contact to Wallet

- HTTP Method: POST
- Endpoint: /v1/ewallets/{ewalletId}/contacts

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*id | str | Required | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet*. |
| request_input | [CreateEwalletContactRequest](/src/rapydsdk/models/README.md#createewalletcontactrequest) | Required | Request body. |

**Return Type**

[CreateEwalletContact200Response](/src/rapydsdk/models/README.md#createewalletcontact200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {}
results = sdk.e_wallets.create_ewallet_contact(
	request_input = request_body,
	ewallet_id = 'ewalletId'
)

pprint(vars(results))

```

### **get_ewallet_contacts**

List Contacts for a Rapyd Wallet

- HTTP Method: GET
- Endpoint: /v1/ewallets/{ewalletId}/contacts

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*id | str | Required | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet*. |

**Return Type**

[GetEwalletContacts200Response](/src/rapydsdk/models/README.md#getewalletcontacts200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.get_ewallet_contacts(ewallet_id = 'ewalletId')

pprint(vars(results))

```

### **update_ewallet_contact**

Update Wallet Contact

- HTTP Method: POST
- Endpoint: /v1/ewallets/{ewalletId}/contacts/{contactId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*id | str | Required | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet*. |
| contact*id | str | Required | ID of the contact. String starting with the prefix cont*. |
| request_input | [Contact](/src/rapydsdk/models/README.md#contact) | Required | Request body. |

**Return Type**

[UpdateEwalletContact200Response](/src/rapydsdk/models/README.md#updateewalletcontact200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {}
results = sdk.e_wallets.update_ewallet_contact(
	request_input = request_body,
	ewallet_id = 'ewalletId',
	contact_id = 'contactId'
)

pprint(vars(results))

```

### **get_ewallet_contact**

Retrieve Wallet Contact.

- HTTP Method: GET
- Endpoint: /v1/ewallets/{ewalletId}/contacts/{contactId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*id | str | Required | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet*. |
| contact*id | str | Required | One of two values. either ID of the contact - String starting with the prefix cont* or Contact reference ID. |

**Return Type**

[GetEwalletContact200Response](/src/rapydsdk/models/README.md#getewalletcontact200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.get_ewallet_contact(
	ewallet_id = 'ewalletId',
	contact_id = 'contactId'
)

pprint(vars(results))

```

### **delete_ewallet_contact**

Delete Wallet Contact

- HTTP Method: DELETE
- Endpoint: /v1/ewallets/{ewalletId}/contacts/{contactId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*id | str | Required | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet*. |
| contact*id | str | Required | ID of the contact. String starting with the prefix cont*. |

**Return Type**

[DeleteEwalletContact200Response](/src/rapydsdk/models/README.md#deleteewalletcontact200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.delete_ewallet_contact(
	ewallet_id = 'ewalletId',
	contact_id = 'contactId'
)

pprint(vars(results))

```

### **get_ewallet_contact_compliance_levels**

Get the compliance status of a personal contact.

- HTTP Method: GET
- Endpoint: /v1/ewallets/{ewalletId}/contacts/{contactId}/compliance_levels

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*id | str | Required | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet*. |
| contact*id | str | Required | ID of the contact. String starting with cont*. |

**Return Type**

[GetEwalletContactComplianceLevels200Response](/src/rapydsdk/models/README.md#getewalletcontactcompliancelevels200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.get_ewallet_contact_compliance_levels(
	ewallet_id = 'ewalletId',
	contact_id = 'contactId'
)

pprint(vars(results))

```

### **create_user**

Create Wallet

- HTTP Method: POST
- Endpoint: /v1/ewallets

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateUserRequest](/src/rapydsdk/models/README.md#createuserrequest) | Required | Request body. |

**Return Type**

[CreateUser200Response](/src/rapydsdk/models/README.md#createuser200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'contact': {"data":[],"has_more":false,"total_count":18626743.140101492,"url":"url"},
	'ewallet_reference_id': 'ewallet_reference_id',
	'first_name': 'first_name',
	'last_name': 'last_name',
	'metadata': {},
	'type_': 'type'
}
results = sdk.e_wallets.create_user(request_input = request_body)

pprint(vars(results))

```

### **get_users**

List eWallets.

- HTTP Method: GET
- Endpoint: /v1/ewallets

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| phone*number | str | Optional | Phone number of the Rapyd Wallet in E.164 format. |
| email | str | Optional | Email address of the wallet owner. |
| ewallet_reference_id | str | Optional | Wallet ID defined by the customer or end user. |
| page_number | float | Optional | Page number to retrieve. If page_number is not specified, page 1 is retrieved. |
| page_size | float | Optional | Number of results per page. |
| type* | str | Optional | Type of wallet - company, person, client. |
| min_balance | float | Optional | |
| currency | str | Optional | |

**Return Type**

[GetUsers200Response](/src/rapydsdk/models/README.md#getusers200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.get_users(
	phone_number = 'phone_number',
	email = 'email',
	ewallet_reference_id = 'ewallet_reference_id',
	page_number = -57836464.352939345,
	page_size = -85469571.08767344,
	type_ = 'type',
	min_balance = 18623916.871657982,
	currency = 'currency'
)

pprint(vars(results))

```

### **updated_user**

Update Wallet

- HTTP Method: POST
- Endpoint: /v1/ewallets/{ewalletToken}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*token | str | Required | ID of the wallet. String starting with ewallet*. |
| request_input | [UpdatedUserRequest](/src/rapydsdk/models/README.md#updateduserrequest) | Required | Request body. |

**Return Type**

[UpdatedUser200Response](/src/rapydsdk/models/README.md#updateduser200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'ewallet_reference_id': 'ewallet_reference_id',
	'first_name': 'first_name',
	'last_name': 'last_name',
	'metadata': {}
}
results = sdk.e_wallets.updated_user(
	request_input = request_body,
	ewallet_token = 'ewalletToken'
)

pprint(vars(results))

```

### **get_user**

Retrieve Wallet

- HTTP Method: GET
- Endpoint: /v1/ewallets/{ewalletToken}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*token | str | Required | ID of the wallet. String starting with ewallet*. |

**Return Type**

[GetUser200Response](/src/rapydsdk/models/README.md#getuser200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.get_user(ewallet_token = 'ewalletToken')

pprint(vars(results))

```

### **delete_user**

Delete a Wallet.

- HTTP Method: DELETE
- Endpoint: /v1/ewallets/{ewalletToken}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*token | str | Required | ID of the wallet. String starting with ewallet*. |

**Return Type**

[DeleteUser200Response](/src/rapydsdk/models/README.md#deleteuser200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.delete_user(ewallet_token = 'ewalletToken')

pprint(vars(results))

```

### **update_ewallet_status**

Change Wallet status

- HTTP Method: POST
- Endpoint: /v1/ewallets/{ewalletToken}/statuses/{status}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ewallet*token | str | Required | ID of the Rapyd Wallet. String starting with ewallet*. Required when phone number is not used. |
| status | [EWalletsStatus](/src/rapydsdk/models/README.md#ewalletsstatus) | Required | Status of the wallet. One of the following: enable, disable, close. disable - Change to disabled status (DIS). close - Close the wallet. Changes the status to closed (CLO). enable - Change to active status (ACT).<br> |

**Return Type**

[UpdateEwalletStatus200Response](/src/rapydsdk/models/README.md#updateewalletstatus200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.update_ewallet_status(
	ewallet_token = 'ewalletToken',
	status = 'close'
)

pprint(vars(results))

```

### **set_account_limit**

Set Wallet Account Limit

- HTTP Method: POST
- Endpoint: /v1/ewallets/{walletId}/account/limits

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| wallet*id | str | Required | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet* |
| request_input | [SetAccountLimitRequest](/src/rapydsdk/models/README.md#setaccountlimitrequest) | Optional | Request body. |

**Return Type**

[SetAccountLimit200Response](/src/rapydsdk/models/README.md#setaccountlimit200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'account_id': 'account_id',
	'amount': 'amount',
	'currency': 'currency',
	'type_': 'type'
}
results = sdk.e_wallets.set_account_limit(
	request_input = request_body,
	wallet_id = 'walletId'
)

pprint(vars(results))

```

### **remove_account_limit**

Delete a coupon from the Rapyd platform

- HTTP Method: DELETE
- Endpoint: /v1/ewallets/{walletId}/account/limits

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| wallet*id | str | Required | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet* |
| request_input | [RemoveAccountLimitRequest](/src/rapydsdk/models/README.md#removeaccountlimitrequest) | Optional | Request body. |

**Return Type**

[RemoveAccountLimit200Response](/src/rapydsdk/models/README.md#removeaccountlimit200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'account_id': 'account_id',
	'currency': 'currency',
	'type_': 'type'
}
results = sdk.e_wallets.remove_account_limit(
	request_input = request_body,
	wallet_id = 'walletId'
)

pprint(vars(results))

```

### **get_user_accounts**

Retrieve Wallet Balances

- HTTP Method: GET
- Endpoint: /v1/ewallets/{walletId}/accounts

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| wallet*id | str | Required | ID of the Rapyd Wallet that this contact is associated with. String starting with ewallet* |

**Return Type**

[GetUserAccounts200Response](/src/rapydsdk/models/README.md#getuseraccounts200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.get_user_accounts(wallet_id = 'walletId')

pprint(vars(results))

```

### **get_user_transactions**

List Wallet Transactions

- HTTP Method: GET
- Endpoint: /v1/ewallets/{walletId}/transactions

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| wallet*id | str | Required | ID of the wallet. String starting with ewallet*. |
| balance | float | Optional | The updated wallet balance after successful completion of the transaction. |
| currency | str | Optional | Three-letter ISO 4217 code for the currency of the transactions. Uppercase. |
| end*date | str | Optional | Timestamp of the last transaction or later, in Unix time. |
| ending_before | str | Optional | The ID of the wallet transaction created after the last wallet transaction you want to retrieve. String starting with wt*. |
| page*number | str | Optional | Page number to retrieve. |
| page_size | str | Optional | Number of results per page. |
| start_date | str | Optional | Timestamp of the first transaction or earlier, in Unix time. |
| starting_after | str | Optional | The ID of the wallet transaction created before the first wallet transaction you want to retrieve. String starting with wt* |
| type\_ | str | Optional | Type of transaction. |

**Return Type**

[GetUserTransactions200Response](/src/rapydsdk/models/README.md#getusertransactions200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.get_user_transactions(
	wallet_id = 'walletId',
	balance = -30000321.71797833,
	currency = 'currency',
	end_date = 'end_date',
	ending_before = 'ending_before',
	page_number = 'page_number',
	page_size = 'page_size',
	start_date = 'start_date',
	starting_after = 'starting_after',
	type_ = 'type'
)

pprint(vars(results))

```

### **get_user_transaction_details**

Get Details of Wallet Transaction

- HTTP Method: GET
- Endpoint: /v1/ewallets/{walletId}/transactions/{transactionId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| wallet*id | str | Required | ID of the wallet. String starting with ewallet*. |
| transaction*id | str | Required | ID of the transaction, from the response to List Wallet Transactions. String starting with wt*. |

**Return Type**

[GetUserTransactionDetails200Response](/src/rapydsdk/models/README.md#getusertransactiondetails200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.e_wallets.get_user_transaction_details(
	wallet_id = 'walletId',
	transaction_id = 'transactionId'
)

pprint(vars(results))

```

### **create_address**

Create an address

- HTTP Method: POST
- Endpoint: /v1/addresses

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateAddressRequest](/src/rapydsdk/models/README.md#createaddressrequest) | Required | Request body. |

**Return Type**

[CreateAddress200Response](/src/rapydsdk/models/README.md#createaddress200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'canton': 'canton',
	'city': 'city',
	'country': 'AF',
	'district': 'district',
	'line_1': 'line_1',
	'line_2': 'line_2',
	'line_3': 'line_3',
	'metadata': {},
	'name': 'name',
	'phone_number': 'phone_number',
	'state': 'state',
	'zip': 'zip'
}
results = sdk.collect.create_address(request_input = request_body)

pprint(vars(results))

```

### **update_address**

Update an address

- HTTP Method: POST
- Endpoint: /v1/addresses/{addressesId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| addresses_id | str | Required | address Id |
| request_input | [AddressRequest](/src/rapydsdk/models/README.md#addressrequest) | Optional | Request body. |

**Return Type**

[UpdateAddress200Response](/src/rapydsdk/models/README.md#updateaddress200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'canton': 'canton',
	'city': 'city',
	'country': 'TH',
	'district': 'district',
	'line_1': 'line_1',
	'line_2': 'line_2',
	'line_3': 'line_3',
	'metadata': {},
	'name': 'name',
	'phone_number': 'phone_number',
	'state': 'state',
	'zip': 'zip'
}
results = sdk.collect.update_address(
	request_input = request_body,
	addresses_id = 'addressesId'
)

pprint(vars(results))

```

### **retrieve_address**

Retrieve an address

- HTTP Method: GET
- Endpoint: /v1/addresses/{addressesId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| addresses_id | str | Required | address Id |

**Return Type**

[RetrieveAddress200Response](/src/rapydsdk/models/README.md#retrieveaddress200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_address(addresses_id = 'addressesId')

pprint(vars(results))

```

### **create_coupon**

Create new coupon

- HTTP Method: POST
- Endpoint: /v1/coupons

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateCouponRequest](/src/rapydsdk/models/README.md#createcouponrequest) | Required | Request body. |

**Return Type**

[CreateCoupon200Response](/src/rapydsdk/models/README.md#createcoupon200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.create_coupon()

pprint(vars(results))

```

### **list_coupon**

Retrieve list of coupons

- HTTP Method: GET
- Endpoint: /v1/coupons

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| starting_after | str | Optional | The ID of the coupon created before the first coupon you want to retrieve |
| ending_before | str | Optional | The ID of the coupon created after the last coupon you want to retrieve |
| limit | str | Optional | The maximum number of coupons to return. Range is 1-100. Default is 10 |

**Return Type**

[ListCoupon200Response](/src/rapydsdk/models/README.md#listcoupon200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.list_coupon(
	starting_after = 'starting_after',
	ending_before = 'ending_before',
	limit = '100'
)

pprint(vars(results))

```

### **update_coupon**

Update a coupon

- HTTP Method: POST
- Endpoint: /v1/coupons/{couponId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| coupon*id | str | Required | coupon Id. String starting with coupon*. |
| request_input | [Coupon](/src/rapydsdk/models/README.md#coupon) | Required | Request body. |

**Return Type**

[UpdateCoupon200Response](/src/rapydsdk/models/README.md#updatecoupon200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'amount_off': 0,
	'created': 1671697165,
	'currency': 'TND',
	'description': 'Sample Coupon 1',
	'discount_duration_in_uses': 2,
	'discount_valid_until': 0,
	'discount_validity_in_months': 2,
	'duration': 'forever',
	'duration_in_months': 3,
	'id': 'coupon_c1194a18a9972ca7f9804826f00c9eb8',
	'max_redemptions': 2,
	'metadata': {},
	'percent_off': 10,
	'redeem_by': 0,
	'times_redeemed': 0,
	'valid': True
}
results = sdk.collect.update_coupon(
	request_input = request_body,
	coupon_id = 'couponId'
)

pprint(vars(results))

```

### **retrieve_coupon**

Retrieve an coupon

- HTTP Method: GET
- Endpoint: /v1/coupons/{couponId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| coupon*id | str | Required | coupon Id. String starting with coupon*. |

**Return Type**

[RetrieveCoupon200Response](/src/rapydsdk/models/README.md#retrievecoupon200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_coupon(coupon_id = 'couponId')

pprint(vars(results))

```

### **delete_coupon**

Delete a coupon from the Rapyd platform

- HTTP Method: DELETE
- Endpoint: /v1/coupons/{couponId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| coupon*id | str | Required | coupon Id. String starting with coupon*. |

**Return Type**

[DeleteCoupon200Response](/src/rapydsdk/models/README.md#deletecoupon200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_coupon(coupon_id = 'couponId')

pprint(vars(results))

```

### **get_hosted_page_payment**

Retrieve a checkout page.

- HTTP Method: GET
- Endpoint: /v1/checkout/{checkout_token}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| checkout*token | str | Required | ID of the checkout page. String starting with checkout*. |

**Return Type**

[GetHostedPagePayment200Response](/src/rapydsdk/models/README.md#gethostedpagepayment200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_hosted_page_payment(checkout_token = 'checkout_token')

pprint(vars(results))

```

### **generate_hosted_page_payment**

Create checkout page

- HTTP Method: POST
- Endpoint: /v1/checkout

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [GenerateHostedPagePaymentRequest](/src/rapydsdk/models/README.md#generatehostedpagepaymentrequest) | Optional | Request body. |

**Return Type**

[GenerateHostedPagePayment200Response](/src/rapydsdk/models/README.md#generatehostedpagepayment200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'account_funding_transaction': {},
	'amount': -28540627.918057874,
	'cart_items': {"amount":38184962.49735427,"image":"image","name":"name","quantity":-86033183.97418618},
	'country': 'MN',
	'currency': 'KWD',
	'custom_elements': {"billing_address_collect":true,"cardholder_name":"cardholder_name","cardholder_preferred_currency":"cardholder_preferred_currency","display_description":true,"dynamic_currency_conversion":true,"merchant_currency_only":true,"payment_fees_display":false,"save_card_default":true},
	'customer': 'customer',
	'escrow': True,
	'escrow_release_days': 6841037.886552796,
	'id': 'id',
	'merchant_main_button': 'merchant_main_button',
	'merchant_privacy_policy': 'merchant_privacy_policy',
	'merchant_terms': 'merchant_terms',
	'merchant_website': 'merchant_website',
	'page_expiration': -45373983.748719305,
	'payment': {},
	'payment_expiration': -87879323.35412206,
	'payment_method_type': 'payment_method_type',
	'payment_method_type_categories': ["aute","in in"],
	'payment_method_types_exclude': ["amet","nulla Excepteur"],
	'payment_method_types_include': ["amet tempor sint enim sit","officia eiusmod commodo"],
	'timestamp': -9148325.481704637
}
results = sdk.collect.generate_hosted_page_payment(request_input = request_body)

pprint(vars(results))

```

### **create_customer**

Create a customer

- HTTP Method: POST
- Endpoint: /v1/customers

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateCustomerRequest](/src/rapydsdk/models/README.md#createcustomerrequest) | Required | Request body. |

**Return Type**

[CreateCustomer200Response](/src/rapydsdk/models/README.md#createcustomer200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {}
results = sdk.collect.create_customer(request_input = request_body)

pprint(vars(results))

```

### **list_customer**

Retrieve list of customers

- HTTP Method: GET
- Endpoint: /v1/customers

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| starting_after | str | Optional | The ID of the customer created before the first customer you want to retrieve |
| ending_before | str | Optional | The ID of the customer created after the last customer you want to retrieve |
| limit | str | Optional | The maximum number of customers to return. Range is 1-100. Default is 10 |

**Return Type**

[ListCustomer200Response](/src/rapydsdk/models/README.md#listcustomer200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.list_customer(
	starting_after = 'starting_after',
	ending_before = 'ending_before',
	limit = '5'
)

pprint(vars(results))

```

### **update_customer**

Update customer

- HTTP Method: POST
- Endpoint: /v1/customers/{customerId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer_id | str | Required | customer Id |
| request_input | [CustomerRequest](/src/rapydsdk/models/README.md#customerrequest) | Optional | Request body. |

**Return Type**

[UpdateCustomer200Response](/src/rapydsdk/models/README.md#updatecustomer200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {}
results = sdk.collect.update_customer(
	request_input = request_body,
	customer_id = 'customerId'
)

pprint(vars(results))

```

### **retrieve_customer**

Retrieve a customer details

- HTTP Method: GET
- Endpoint: /v1/customers/{customerId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer_id | str | Required | customer Id |

**Return Type**

[RetrieveCustomer200Response](/src/rapydsdk/models/README.md#retrievecustomer200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_customer(customer_id = 'customerId')

pprint(vars(results))

```

### **delete_customer**

Delete a customer from the Rapyd platform

- HTTP Method: DELETE
- Endpoint: /v1/customers/{customerId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer_id | str | Required | customer Id |

**Return Type**

[DeleteCustomer200Response](/src/rapydsdk/models/README.md#deletecustomer200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_customer(customer_id = 'customerId')

pprint(vars(results))

```

### **delete_customer_discount**

Delete the discount that has been assigned to a customer

- HTTP Method: DELETE
- Endpoint: /v1/customers/{customerId}/discount

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer_id | str | Required | customer Id |

**Return Type**

[DeleteCustomerDiscount200Response](/src/rapydsdk/models/README.md#deletecustomerdiscount200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_customer_discount(customer_id = 'customerId')

pprint(vars(results))

```

### **create_customer_payment_method**

Add a payment method to a customer profile

- HTTP Method: POST
- Endpoint: /v1/customers/{customerId}/payment_methods

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer_id | str | Required | customer Id |
| request_input | [CreateCustomerPaymentMethodRequest](/src/rapydsdk/models/README.md#createcustomerpaymentmethodrequest) | Required | Request body. |

**Return Type**

[CreateCustomerPaymentMethod200Response](/src/rapydsdk/models/README.md#createcustomerpaymentmethod200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {'data': {}}
results = sdk.collect.create_customer_payment_method(
	request_input = request_body,
	customer_id = 'customerId'
)

pprint(vars(results))

```

### **get_customer_payment_methods**

Retrieve payment methods for a customer

- HTTP Method: GET
- Endpoint: /v1/customers/{customerId}/payment_methods

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer*id | str | Required | customer Id |
| category | [Category](/src/rapydsdk/models/README.md#category) | Optional | |
| starting_after | str | Optional | The ID of the coupon created before the first coupon you want to retrieve |
| ending_before | str | Optional | The ID of the coupon created after the last coupon you want to retrieve |
| limit | str | Optional | The maximum number of coupons to return. Range is 1-100. Default is 10 |
| type* | str | Optional | The type of payment method to find. |

**Return Type**

[GetCustomerPaymentMethods200Response](/src/rapydsdk/models/README.md#getcustomerpaymentmethods200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_customer_payment_methods(
	customer_id = 'customerId',
	category = 'bank',
	starting_after = 'starting_after',
	ending_before = 'ending_before',
	limit = 'limit',
	type_ = 'type'
)

pprint(vars(results))

```

### **update_customer_payment_method**

Update payment method for customer

- HTTP Method: POST
- Endpoint: /v1/customers/{customerId}/payment_methods/{pmtId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer_id | str | Required | customer Id |
| pmt_id | str | Required | Pmt Id |
| request_input | [CustomerPaymentMethod](/src/rapydsdk/models/README.md#customerpaymentmethod) | Required | Request body. |

**Return Type**

[UpdateCustomerPaymentMethod200Response](/src/rapydsdk/models/README.md#updatecustomerpaymentmethod200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.update_customer_payment_method(
	customer_id = 'customerId',
	pmt_id = 'pmtId'
)

pprint(vars(results))

```

### **get_customer_payment_method**

Retrieve a payment method for a specific customer

- HTTP Method: GET
- Endpoint: /v1/customers/{customerId}/payment_methods/{pmtId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer_id | str | Required | customer Id |
| pmt_id | str | Required | Pmt Id |

**Return Type**

[GetCustomerPaymentMethod200Response](/src/rapydsdk/models/README.md#getcustomerpaymentmethod200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_customer_payment_method(
	customer_id = 'customerId',
	pmt_id = 'pmtId'
)

pprint(vars(results))

```

### **delete_customer_payment_method**

Delete a payment method type from customer

- HTTP Method: DELETE
- Endpoint: /v1/customers/{customerId}/payment_methods/{pmtId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer_id | str | Required | customer Id |
| pmt_id | str | Required | Pmt Id |

**Return Type**

[DeleteCustomerPaymentMethod200Response](/src/rapydsdk/models/README.md#deletecustomerpaymentmethod200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_customer_payment_method(
	customer_id = 'customerId',
	pmt_id = 'pmtId'
)

pprint(vars(results))

```

### **get_disputes_list_by_org_id**

Retrieve list of disputes

- HTTP Method: GET
- Endpoint: /v1/disputes

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| starting*after | str | Optional | The ID of the dispute created before the first dispute you want to retrieve. String starting with dispute*. |
| ending*before | str | Optional | The ID of the dispute created after the last dispute you want to retrieve. String starting with dispute*. |
| limit | str | Optional | The maximum number of disputes to return. Range is 1-100. Default is 10. |
| status | [Status](/src/rapydsdk/models/README.md#status) | Optional | Filters the list for disputes with the specified dispute status. |
| payment | str | Optional | The ID of the payment that is linked to the dispute. String starting with payment\_. |

**Return Type**

[GetDisputesListByOrgId200Response](/src/rapydsdk/models/README.md#getdisputeslistbyorgid200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_disputes_list_by_org_id(
	starting_after = 'starting_after',
	ending_before = 'ending_before',
	limit = '2',
	status = Status(),
	payment = 'payment'
)

pprint(vars(results))

```

### **get_dispute**

Retrieve an dispute.

- HTTP Method: GET
- Endpoint: /v1/disputes/{disputeId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| dispute*id | str | Required | ID of the dispute you want to retrieve. String starting with dispute*. |

**Return Type**

[GetDispute200Response](/src/rapydsdk/models/README.md#getdispute200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_dispute(dispute_id = 'disputeId')

pprint(vars(results))

```

### **list_invoices**

List Invoices

- HTTP Method: GET
- Endpoint: /v1/invoices

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| customer | [Customer](/src/rapydsdk/models/README.md#customer) | Optional | ID of the customer. String starting with cus*. |
| date* | str | Optional | Date that the invoice was created. |
| due*date | str | Optional | The date payment is due on this invoice. This value is calculated from the date the invoice is created, plus the number of days specified in the days_until_due field. Format is in Unix time. |
| ending_before | str | Optional | The ID of the invoice created after the last invoice you want to retrieve. card. |
| limit | str | Optional | The maximum number of invoices to return. Range 1-100. Default is 10. |
| starting_after | str | Optional | The ID of the invoice created before the first invoice you want to retrieve. |
| subscription | bool | Optional | ID of the subscription. String starting with sub*. |

**Return Type**

[ListInvoices200Response](/src/rapydsdk/models/README.md#listinvoices200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.list_invoices(
	customer = 'foo',
	date_ = 'date',
	due_date = 'due_date',
	ending_before = 'ending_before',
	limit = 'limit',
	starting_after = 'starting_after',
	subscription = True
)

pprint(vars(results))

```

### **update_invoice**

Update Invoice

- HTTP Method: POST
- Endpoint: /v1/invoices/{invoiceId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| invoice_id | str | Required | The ID of the invoice that you want to updated. |
| request_input | [UpdateInvoiceRequest](/src/rapydsdk/models/README.md#updateinvoicerequest) | Optional | Request body. |

**Return Type**

[UpdateInvoice200Response](/src/rapydsdk/models/README.md#updateinvoice200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'days_until_due': -95282732.43276253,
	'description': 'description',
	'due_date': 'due_date',
	'metadata': {},
	'payment_fields': {},
	'statement_descriptor': 'statement_descriptor',
	'tax_percent': -43822908.510768555
}
results = sdk.collect.update_invoice(
	request_input = request_body,
	invoice_id = 'invoiceId'
)

pprint(vars(results))

```

### **retrieve_invoice**

Retrieve Invoice

- HTTP Method: GET
- Endpoint: /v1/invoices/{invoiceId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| invoice_id | str | Required | The ID of the invoice that you want to retrieve. |

**Return Type**

[RetrieveInvoice200Response](/src/rapydsdk/models/README.md#retrieveinvoice200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_invoice(invoice_id = 'invoiceId')

pprint(vars(results))

```

### **delete_invoice**

Delete Invoice

- HTTP Method: DELETE
- Endpoint: /v1/invoices/{invoiceId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| invoice_id | str | Required | The ID of the invoice that you want to delete. |

**Return Type**

[DeleteInvoice200Response](/src/rapydsdk/models/README.md#deleteinvoice200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_invoice(invoice_id = 'invoiceId')

pprint(vars(results))

```

### **finalize_invoice**

Finalize Invoice

- HTTP Method: POST
- Endpoint: /v1/invoices/{invoiceId}/finalize

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| invoice_id | str | Required | ID of the invoice you want to pay. |

**Return Type**

[FinalizeInvoice200Response](/src/rapydsdk/models/README.md#finalizeinvoice200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.finalize_invoice(invoice_id = 'invoiceId')

pprint(vars(results))

```

### **pay_invoice**

payInvoice

- HTTP Method: POST
- Endpoint: /v1/invoices/{invoiceId}/pay

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| invoice_id | str | Required | ID of the invoice you want to pay. |
| request_input | [PayInvoiceRequest](/src/rapydsdk/models/README.md#payinvoicerequest) | Optional | Request body. |

**Return Type**

[PayInvoice200Response](/src/rapydsdk/models/README.md#payinvoice200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {'payment_method': 'payment_method'}
results = sdk.collect.pay_invoice(
	request_input = request_body,
	invoice_id = 'invoiceId'
)

pprint(vars(results))

```

### **create_order**

Create an Order

- HTTP Method: POST
- Endpoint: /v1/orders

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateOrderRequest](/src/rapydsdk/models/README.md#createorderrequest) | Optional | Request body. |

**Return Type**

[CreateOrder200Response](/src/rapydsdk/models/README.md#createorder200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {}
results = sdk.collect.create_order(request_input = request_body)

pprint(vars(results))

```

### **list_order**

List Orders

- HTTP Method: GET
- Endpoint: /v1/orders

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| limit | str | Optional | The maximum number of orders to return. Range - 1-100. Default is 10. |
| ending_before | str | Optional | The ID of the order created after the last order you want to retrieve. |
| starting_after | str | Optional | The ID of the order created before the first order you want to retrieve. |

**Return Type**

[ListOrder200Response](/src/rapydsdk/models/README.md#listorder200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.list_order(
	limit = 'limit',
	ending_before = 'ending_before',
	starting_after = 'starting_after'
)

pprint(vars(results))

```

### **update_order**

Update an Order

- HTTP Method: POST
- Endpoint: /v1/orders/{orderId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| order*id | str | Required | ID of the order. String starting with order*. |
| request_input | [UpdateOrderRequest](/src/rapydsdk/models/README.md#updateorderrequest) | Required | Request body. |

**Return Type**

[UpdateOrder200Response](/src/rapydsdk/models/README.md#updateorder200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'coupon': 'coupon',
	'metadata': {},
	'status': 'returned',
	'tax_percent': -54093866.80965369
}
results = sdk.collect.update_order(
	request_input = request_body,
	order_id = 'orderId'
)

pprint(vars(results))

```

### **retrieve_order**

Retrieve an Order

- HTTP Method: GET
- Endpoint: /v1/orders/{orderId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| order*id | str | Required | ID of the order. String starting with order*. |

**Return Type**

[RetrieveOrder200Response](/src/rapydsdk/models/README.md#retrieveorder200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_order(order_id = 'orderId')

pprint(vars(results))

```

### **returns_order**

Create a Return Against an Order

- HTTP Method: POST
- Endpoint: /v1/orders/{orderId}/returns

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| order*id | str | Required | ID of the order. String starting with order*. |
| request_input | [ReturnsOrderRequest](/src/rapydsdk/models/README.md#returnsorderrequest) | Required | Request body. |

**Return Type**

[ReturnsOrder200Response](/src/rapydsdk/models/README.md#returnsorder200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'items': [{"amount":-71848570.66028032,"currency":"deserunt ipsum","description":"fugiat aliqua tempor","order_id":"veniam minim","parent":"veniam consectetur","quantity":75542449.2355735,"type_":"sku"},{"amount":45661400.49029851,"currency":"sint","description":"irure ullamco culpa","order_id":"do dolor","parent":"elit veniam nulla Lorem","quantity":66411871.83280963,"type_":"shipping"}],
	'order_id': 'order_id'
}
results = sdk.collect.returns_order(
	request_input = request_body,
	order_id = 'orderId'
)

pprint(vars(results))

```

### **pay_order**

Pay an order.

- HTTP Method: POST
- Endpoint: /v1/orders/{orderId}/pay

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| order*id | str | Required | ID of the order. String starting with order*. |
| request_input | [PayOrderRequest](/src/rapydsdk/models/README.md#payorderrequest) | Required | Request body. |

**Return Type**

[PayOrder200Response](/src/rapydsdk/models/README.md#payorder200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'customer': 'customer',
	'metadata': {},
	'payment_method': 'payment_method'
}
results = sdk.collect.pay_order(
	request_input = request_body,
	order_id = 'orderId'
)

pprint(vars(results))

```

### **list_order_return**

List Returns

- HTTP Method: GET
- Endpoint: /v1/order_returns

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| limit | str | Optional | The maximum number of returns to list. Range - 1-100. Default is 10. |
| ending_before | str | Optional | The ID of the order created after the last order you want to retrieve a return from. |
| starting_after | str | Optional | The ID of the order created before the first order you want to retrieve a return from. |
| tokens | List[str] | Optional | Filters the list for orders related to the specified order. |

**Return Type**

[ListOrderReturn200Response](/src/rapydsdk/models/README.md#listorderreturn200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.list_order_return(
	limit = 'limit',
	ending_before = 'ending_before',
	starting_after = 'starting_after',
	tokens = ['veniam dolore aute sint','nisi et anim aliqua']
)

pprint(vars(results))

```

### **retrieve_order_return**

Retrieve a Return

- HTTP Method: GET
- Endpoint: /v1/order_returns/{orderReturnsId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| order*returns_id | str | Required | ID of the return. String starting with orre*. |

**Return Type**

[RetrieveOrderReturn200Response](/src/rapydsdk/models/README.md#retrieveorderreturn200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_order_return(order_returns_id = 'orderReturnsId')

pprint(vars(results))

```

### **get_payment_methods_types_by_country**

Retrieve a list of all payment methods available for a country

- HTTP Method: GET
- Endpoint: /v1/payment_methods/countries/{countryId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| country_id | str | Required | Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. |
| currency | str | Optional | currency |

**Return Type**

[GetPaymentMethodsTypesByCountry200Response](/src/rapydsdk/models/README.md#getpaymentmethodstypesbycountry200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_payment_methods_types_by_country(
	country_id = 'BG',
	currency = 'CHF'
)

pprint(vars(results))

```

### **get_payment_method_type_required_fields**

Retrieve the required fields for a payment method

- HTTP Method: GET
- Endpoint: /v1/payment_methods/{pmtId}/required_fields

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| pmt_id | str | Required | The type of the payment method. |

**Return Type**

[GetPaymentMethodTypeRequiredFields200Response](/src/rapydsdk/models/README.md#getpaymentmethodtyperequiredfields200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_payment_method_type_required_fields(pmt_id = 'pmtId')

pprint(vars(results))

```

### **create_payment**

Create a payment

- HTTP Method: POST
- Endpoint: /v1/payments

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreatePaymentRequest](/src/rapydsdk/models/README.md#createpaymentrequest) | Required | Request body. |

**Return Type**

[CreatePayment200Response](/src/rapydsdk/models/README.md#createpayment200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.create_payment()

pprint(vars(results))

```

### **list_payments**

List Payments

- HTTP Method: GET
- Endpoint: /v1/payments

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| created*after | str | Optional | The ID of the payment created before the first payment you want to retrieve. String starting with payment*. |
| created*before | str | Optional | The ID of the payment created after the last payment you want to retrieve. String starting with payment*. |
| customer | [Customer](/src/rapydsdk/models/README.md#customer) | Optional | Filters the list for payments related to the specified customer. |
| destination*card | str | Optional | Filters the list for payments related to the specified destination card. |
| ending_before | str | Optional | The ID of the payment created after the last payment you want to retrieve. String starting with payment*. Deprecated. |
| ewallet | str | Optional | Filters the list for payments related to the specified wallet. |
| group | bool | Optional | When true, includes only group payments in the response. When false, excludes group payments from the response. Default is false. |
| invoice | str | Optional | Filters according to the invoice. String starting with invoice*. |
| limit | str | Optional | The maximum number of payments to return. Range, 1-100. Default is 10. |
| payment_method | str | Optional | Filters the list for payments related to the specified payment method. |
| order | str | Optional | Filters the list for payments related to the specified order. |
| starting_after | str | Optional | The ID of a payment in the list. The list begins with the payment that was created next after the payment with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used. String starting with payment*. |
| subscription | str | Optional | Filters the list for payments related to the specified subscription. |
| merchant_reference_id | str | Optional | Merchant-defined ID. |

**Return Type**

[ListPayments200Response](/src/rapydsdk/models/README.md#listpayments200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.list_payments(
	created_after = 'created_after',
	created_before = 'created_before',
	customer = 'foo',
	destination_card = 'destination_card',
	ending_before = 'ending_before',
	ewallet = 'ewallet',
	group = True,
	invoice = 'invoice',
	limit = 'limit',
	payment_method = 'payment_method',
	order = 'order',
	starting_after = 'starting_after',
	subscription = 'subscription',
	merchant_reference_id = 'merchant_reference_id'
)

pprint(vars(results))

```

### **update_payment**

Update Payment

- HTTP Method: POST
- Endpoint: /v1/payments/{paymentId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| payment*id | str | Required | ID of the payment. String starting with payment*. |
| request_input | [UpdatePaymentRequest](/src/rapydsdk/models/README.md#updatepaymentrequest) | Required | Request body. |

**Return Type**

[UpdatePayment200Response](/src/rapydsdk/models/README.md#updatepayment200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {}
results = sdk.collect.update_payment(
	request_input = request_body,
	payment_id = 'paymentId'
)

pprint(vars(results))

```

### **retrieve_payment**

Retrieve Payment

- HTTP Method: GET
- Endpoint: /v1/payments/{paymentId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| payment*id | str | Required | ID of the payment. String starting with 'payment*'. |

**Return Type**

[RetrievePayment200Response](/src/rapydsdk/models/README.md#retrievepayment200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_payment(payment_id = 'paymentId')

pprint(vars(results))

```

### **cancel_payment**

Cancel Payment

- HTTP Method: DELETE
- Endpoint: /v1/payments/{paymentId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| payment*id | str | Required | ID of the payment. String starting with payment*. |

**Return Type**

[CancelPayment200Response](/src/rapydsdk/models/README.md#cancelpayment200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.cancel_payment(payment_id = 'paymentId')

pprint(vars(results))

```

### **create_subscription**

Create Subscription

- HTTP Method: POST
- Endpoint: /v1/payments/subscriptions

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateSubscriptionRequest](/src/rapydsdk/models/README.md#createsubscriptionrequest) | Required | Request body. |

**Return Type**

[CreateSubscription200Response](/src/rapydsdk/models/README.md#createsubscription200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'billing': 'billing',
	'billing_cycle_anchor': 40294335.55177215,
	'cancel_at_period_end': False,
	'coupon': 'coupon',
	'customer': 'customer',
	'days_until_due': -35396580.37476601,
	'metadata': {},
	'payment_fields': {},
	'payment_method': {},
	'simultaneous_invoice': False,
	'subscription_items': [{"plan":"fugiat Duis deserunt in Lorem","quantity":66850531.28095752},{"plan":"aliquip adipisicing enim","quantity":-37476925.448285535}],
	'tax_percent': 64087970.779761106,
	'trial_end': 48875623.61546755,
	'trial_from_plan': False,
	'trial_period_days': 72544272.3973015
}
results = sdk.collect.create_subscription(request_input = request_body)

pprint(vars(results))

```

### **get_subscription_list**

List Subscriptions

- HTTP Method: GET
- Endpoint: /v1/payments/subscriptions

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| billing | str | Optional | Method of billing. One of the following, pay*automatically, send_invoice. |
| customer | str | Optional | ID of the customer. String starting with cus* |
| status | str | Optional | Status of the subscription. One of the following, active, canceled, trialing |
| product | str | Optional | ID of a 'product' object. The product must have type set to service. String starting with product\_. Filter for one product at a time. |
| starting_after | str | Required | The ID of a record in the list. The list begins with the record that was created next after the record with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used. |
| ending_before | str | Optional | The ID of a record in the list. The list ends with the last record that was created before the record with this ID. Use this filter to get the previous page of results. |
| limit | str | Optional | The maximum number of subscriptions to return. Range, 1-100. Default is 10. |

**Return Type**

[GetSubscriptionList200Response](/src/rapydsdk/models/README.md#getsubscriptionlist200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_subscription_list(
	starting_after = 'starting_after',
	billing = 'billing',
	customer = 'customer',
	status = 'status',
	product = 'product',
	ending_before = 'ending_before',
	limit = 'limit'
)

pprint(vars(results))

```

### **update_subscription**

Update Subscription

- HTTP Method: POST
- Endpoint: /v1/payments/subscriptions/{subscriptionId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| subscription*id | str | Required | ID of the subscription. String starting with sub*. |
| request_input | [UpdateSubscriptionRequest](/src/rapydsdk/models/README.md#updatesubscriptionrequest) | Required | Request body. |

**Return Type**

[UpdateSubscription200Response](/src/rapydsdk/models/README.md#updatesubscription200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'billing': 'billing',
	'billing_cycle_anchor': 'billing_cycle_anchor',
	'cancel_at_period_end': True,
	'coupon': 'coupon',
	'days_until_due': -2130265.6254733205,
	'metadata': {},
	'payment_fields': {},
	'payment_method': 'tempor ad ex velit',
	'simultaneous_invoice': True,
	'subscription_items': ["qui eu","in proident"],
	'tax_percent': -26580506.179450452,
	'trial_end': 8127127.273606226,
	'trial_from_plan': False,
	'trial_period_days': 4374936.058031723
}
results = sdk.collect.update_subscription(
	request_input = request_body,
	subscription_id = 'subscriptionId'
)

pprint(vars(results))

```

### **get_subscription**

Retrieve Subscription

- HTTP Method: GET
- Endpoint: /v1/payments/subscriptions/{subscriptionId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| subscription*id | str | Required | ID of the subscription. String starting with sub*. |

**Return Type**

[GetSubscription200Response](/src/rapydsdk/models/README.md#getsubscription200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_subscription(subscription_id = 'subscriptionId')

pprint(vars(results))

```

### **cancel_subscription**

Cancel Subscription

- HTTP Method: DELETE
- Endpoint: /v1/payments/subscriptions/{subscriptionId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| subscription*id | str | Required | ID of the subscription. String starting with sub*. |
| cancel_at_period_end | bool | Optional | < Determines when the subscription is canceled. true - Cancels the subscription at the end of the current period. false - Cancels the subscription immediately. |

**Return Type**

[CancelSubscription200Response](/src/rapydsdk/models/README.md#cancelsubscription200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.cancel_subscription(
	subscription_id = 'subscriptionId',
	cancel_at_period_end = True
)

pprint(vars(results))

```

### **delete_subscription_discount**

Delete Discount from Subscription

- HTTP Method: DELETE
- Endpoint: /v1/payments/subscriptions/{subscriptionId}/discount

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| subscription*id | str | Required | ID of the subscription. String starting with sub* |

**Return Type**

[DeleteSubscriptionDiscount200Response](/src/rapydsdk/models/README.md#deletesubscriptiondiscount200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_subscription_discount(subscription_id = 'subscriptionId')

pprint(vars(results))

```

### **create_plan**

Create Plan Item

- HTTP Method: POST
- Endpoint: /v1/plans

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreatePlanRequest](/src/rapydsdk/models/README.md#createplanrequest) | Required | Request body. |

**Return Type**

[CreatePlan200Response](/src/rapydsdk/models/README.md#createplan200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'aggregate_usage': 'aggregate_usage',
	'amount': 43154418.09567678,
	'billing_scheme': 'billing_scheme',
	'currency': 'currency',
	'id': 'id',
	'interval': 'interval',
	'interval_count': -72449528.09337226,
	'metadata': {},
	'nickname': 'nickname',
	'product': 'product',
	'tiers': 'tiers',
	'tiers_mode': 'tiers_mode',
	'transform_usage': {},
	'trial_period_days': 47967007.14868912,
	'usage_type': 'usage_type'
}
results = sdk.collect.create_plan(request_input = request_body)

pprint(vars(results))

```

### **list_plans**

List Plans

- HTTP Method: GET
- Endpoint: /v1/plans

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ending_before | float | Optional | The ID of the plan created after the last plan you want to retrieve. |
| limit | float | Optional | The maximum number of plans to return. Range 1-100. Default is 10. |
| starting_after | str | Optional | The ID of the plan created before the first plan you want to retrieve. |

**Return Type**

[ListPlans200Response](/src/rapydsdk/models/README.md#listplans200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.list_plans(
	ending_before = 54636865.813328624,
	limit = 9622275.593752146,
	starting_after = 'starting_after'
)

pprint(vars(results))

```

### **update_plan**

Update Plan

- HTTP Method: POST
- Endpoint: /v1/plans/{plan_id}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| plan_id | str | Required | ID of the plan. |
| request_input | [UpdatePlanRequest](/src/rapydsdk/models/README.md#updateplanrequest) | Required | Request body. |

**Return Type**

[UpdatePlan200Response](/src/rapydsdk/models/README.md#updateplan200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'metadata': {},
	'nickname': 'nickname'
}
results = sdk.collect.update_plan(
	request_input = request_body,
	plan_id = 'plan_id'
)

pprint(vars(results))

```

### **retrieve_plan**

Retrieve plan

- HTTP Method: GET
- Endpoint: /v1/plans/{plan_id}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| plan_id | str | Required | ID of the plan. |

**Return Type**

[RetrievePlan200Response](/src/rapydsdk/models/README.md#retrieveplan200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_plan(plan_id = 'plan_id')

pprint(vars(results))

```

### **delete_plan**

Delete Plan

- HTTP Method: DELETE
- Endpoint: /v1/plans/{plan_id}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| plan_id | str | Required | ID of the plan. |

**Return Type**

[DeletePlan200Response](/src/rapydsdk/models/README.md#deleteplan200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_plan(plan_id = 'plan_id')

pprint(vars(results))

```

### **create_product**

Create Product

- HTTP Method: POST
- Endpoint: /v1/products

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateProductRequest](/src/rapydsdk/models/README.md#createproductrequest) | Required | Request body. |

**Return Type**

[CreateProduct200Response](/src/rapydsdk/models/README.md#createproduct200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'active': False,
	'attributes': ["ex eu","dolor velit minim et"],
	'description': 'description',
	'id': 'id',
	'images': ["nulla","sit dolor"],
	'metadata': {},
	'name': 'name',
	'package_dimensions': {"height":-45808073.55021737,"length":78277231.16046831,"weight":-20932918.382235765,"width":55209428.78723577},
	'shippable': False,
	'statement_descriptor': 'statement_descriptor',
	'type_': 'goods',
	'unit_label': 'unit_label'
}
results = sdk.collect.create_product(request_input = request_body)

pprint(vars(results))

```

### **get_products_list**

List Products

- HTTP Method: GET
- Endpoint: /v1/products

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ending_before | float | Optional | The ID of the products created after the last product you want to retrieve. |
| limit | float | Optional | The maximum number of products to return. Range 1-100. Default is 10. |
| starting_after | str | Optional | The ID of the product created before the first products you want to retrieve. |

**Return Type**

[GetProductsList200Response](/src/rapydsdk/models/README.md#getproductslist200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_products_list(
	ending_before = -86174224.70049512,
	limit = 79061533.0142777,
	starting_after = 'starting_after'
)

pprint(vars(results))

```

### **update_product**

Update Product

- HTTP Method: POST
- Endpoint: /v1/products/{products_id}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| products_id | str | Required | ID of the product. |
| request_input | [UpdateProductRequest](/src/rapydsdk/models/README.md#updateproductrequest) | Optional | Request body. |

**Return Type**

[UpdateProduct200Response](/src/rapydsdk/models/README.md#updateproduct200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'active': True,
	'attributes': ["sit","elit adipisicing"],
	'metadata': {},
	'name': 'name',
	'package_dimensions': {"height":-29641724.731922597,"length":-77697787.19623214,"weight":17684979.750677913,"width":-55649931.45668104},
	'statement_descriptor': 'statement_descriptor',
	'type': undefined,
	'unit_label': 'unit_label'
}
results = sdk.collect.update_product(
	request_input = request_body,
	products_id = 'products_id'
)

pprint(vars(results))

```

### **get_product**

Retrieve Product

- HTTP Method: GET
- Endpoint: /v1/products/{products_id}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| products_id | str | Required | ID of the product. |

**Return Type**

[GetProduct200Response](/src/rapydsdk/models/README.md#getproduct200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_product(products_id = 'products_id')

pprint(vars(results))

```

### **delete_product**

Delete Product

- HTTP Method: DELETE
- Endpoint: /v1/products/{products_id}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| products_id | str | Required | ID of the product. |

**Return Type**

[DeleteProduct200Response](/src/rapydsdk/models/README.md#deleteproduct200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_product(products_id = 'products_id')

pprint(vars(results))

```

### **request_total_create_refund**

Create Refund

- HTTP Method: POST
- Endpoint: /v1/refunds

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [RequestTotalCreateRefundRequest](/src/rapydsdk/models/README.md#requesttotalcreaterefundrequest) | Required | Request body. |

**Return Type**

[RequestTotalCreateRefund200Response](/src/rapydsdk/models/README.md#requesttotalcreaterefund200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'amount': 40184018.32753748,
	'currency': 'currency',
	'ewallets': ["Lorem ad qui dolor","do dolore officia irure est"],
	'merchant_reference_id': 'merchant_reference_id',
	'metadata': {},
	'payment': 'payment',
	'reason': 'reason'
}
results = sdk.collect.request_total_create_refund(request_input = request_body)

pprint(vars(results))

```

### **all_refunds**

List Refunds

- HTTP Method: GET
- Endpoint: /v1/refunds

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ending*before | str | Optional | The ID of the refund created after the last refund you want to retrieve. String starting with refund*. |
| limit | str | Optional | The maximum number of refunds to return. Range, 1-100. Default is 10. |
| starting*after | str | Optional | The ID of the refund created before the first refund you want to retrieve. String starting with refund*. |

**Return Type**

[AllRefunds200Response](/src/rapydsdk/models/README.md#allrefunds200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.all_refunds(
	ending_before = 'ending_before',
	limit = 'limit',
	starting_after = 'starting_after'
)

pprint(vars(results))

```

### **simulate_complete_refund**

Complete Refund

- HTTP Method: POST
- Endpoint: /v1/refunds/complete

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [SimulateCompleteRefundRequest](/src/rapydsdk/models/README.md#simulatecompleterefundrequest) | Required | Request body. |

**Return Type**

[SimulateCompleteRefund200Response](/src/rapydsdk/models/README.md#simulatecompleterefund200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {'token': 'token'}
results = sdk.collect.simulate_complete_refund(request_input = request_body)

pprint(vars(results))

```

### **refund_group_payment**

Create Group Refund

- HTTP Method: POST
- Endpoint: /v1/refunds/group_payments

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [RefundGroupPaymentRequest](/src/rapydsdk/models/README.md#refundgrouppaymentrequest) | Required | Request body. |

**Return Type**

[RefundGroupPayment200Response](/src/rapydsdk/models/README.md#refundgrouppayment200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'amount': -94489002.54077359,
	'group_payment': 'group_payment'
}
results = sdk.collect.refund_group_payment(request_input = request_body)

pprint(vars(results))

```

### **update_refund**

Update Refund

- HTTP Method: POST
- Endpoint: /v1/refunds/{refundId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| refund*id | str | Required | ID of the 'refund' object you want to retrieve. String starting with refund*. |
| request_input | [UpdateRefundRequest](/src/rapydsdk/models/README.md#updaterefundrequest) | Required | Request body. |

**Return Type**

[UpdateRefund200Response](/src/rapydsdk/models/README.md#updaterefund200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {'metadata': {}}
results = sdk.collect.update_refund(
	request_input = request_body,
	refund_id = 'refundId'
)

pprint(vars(results))

```

### **refund_by_token**

Retrieve Refund

- HTTP Method: GET
- Endpoint: /v1/refunds/{refundId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| refund*id | str | Required | ID of the 'refund' object you want to retrieve. String starting with refund*. |

**Return Type**

[RefundByToken200Response](/src/rapydsdk/models/README.md#refundbytoken200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.refund_by_token(refund_id = 'refundId')

pprint(vars(results))

```

### **create_subscription_item**

Create Subscription Item

- HTTP Method: POST
- Endpoint: /v1/subscription_items

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateSubscriptionItemRequest](/src/rapydsdk/models/README.md#createsubscriptionitemrequest) | Required | Request body. |

**Return Type**

[CreateSubscriptionItem200Response](/src/rapydsdk/models/README.md#createsubscriptionitem200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'metadata': {},
	'plan': 'plan',
	'prorate': True,
	'proration_date': -89062018.18171677,
	'quantity': 39066464.09589359,
	'subscription': 'subscription'
}
results = sdk.collect.create_subscription_item(request_input = request_body)

pprint(vars(results))

```

### **list_subscription_item**

List Subscription Items

- HTTP Method: GET
- Endpoint: /v1/subscription_items

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| ending_before | float | Optional | The ID of the subscription item created after the last subscription item you want to retrieve. |
| limit | float | Optional | The maximum number of subscription items to return. Range 1-100. Default is 10. |
| starting_after | str | Optional | The ID of the subscription item created before the first subscription item you want to retrieve. |
| subscription | str | Optional | ID of the subscription. |

**Return Type**

[ListSubscriptionItem200Response](/src/rapydsdk/models/README.md#listsubscriptionitem200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.list_subscription_item(
	ending_before = 61760505.72470647,
	limit = -84460226.52114683,
	starting_after = 'starting_after',
	subscription = 'subscription'
)

pprint(vars(results))

```

### **update_subscription_item**

Update Subscription Item

- HTTP Method: POST
- Endpoint: /v1/subscription_items/{subscriptionItemId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| subscription*item_id | str | Required | ID of the subscription item. String starting with subi*. |
| request_input | [UpdateSubscriptionItemRequest](/src/rapydsdk/models/README.md#updatesubscriptionitemrequest) | Required | Request body. |

**Return Type**

[UpdateSubscriptionItem200Response](/src/rapydsdk/models/README.md#updatesubscriptionitem200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'metadata': {},
	'prorate': True,
	'proration_date': 50935574.892552435,
	'quantity': -48973335.96318654
}
results = sdk.collect.update_subscription_item(
	request_input = request_body,
	subscription_item_id = 'subscriptionItemId'
)

pprint(vars(results))

```

### **retrieve_subscription_item**

Retrieve Subscription Item

- HTTP Method: GET
- Endpoint: /v1/subscription_items/{subscriptionItemId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| subscription*item_id | str | Required | ID of the subscription item. String starting with subi*. |

**Return Type**

[RetrieveSubscriptionItem200Response](/src/rapydsdk/models/README.md#retrievesubscriptionitem200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_subscription_item(subscription_item_id = 'subscriptionItemId')

pprint(vars(results))

```

### **delete_subscription_item**

Delete Subscription Item

- HTTP Method: DELETE
- Endpoint: /v1/subscription_items/{subscriptionItemId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| subscription*item_id | str | Required | ID of the subscription item. String starting with subi*. |

**Return Type**

[DeleteSubscriptionItem200Response](/src/rapydsdk/models/README.md#deletesubscriptionitem200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_subscription_item(subscription_item_id = 'subscriptionItemId')

pprint(vars(results))

```

### **usage_record_summaries**

Create Usage Record

- HTTP Method: GET
- Endpoint: /v1/subscription_items/{subscriptionItemId}/usage_record_summaries

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| subscription*item_id | str | Required | ID of the subscription item. String starting with subi*. |
| limit | float | Optional | The maximum number of usage records that are returned. Range is 1-100. Default is 10. |
| ending_before | float | Optional | The latest date and time of the returned usage records. Format is in Unix time. |
| starting_after | float | Optional | The earliest date and time of the returned usage records. Format is in Unix time. |

**Return Type**

[UsageRecordSummaries200Response](/src/rapydsdk/models/README.md#usagerecordsummaries200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.usage_record_summaries(
	subscription_item_id = 'subscriptionItemId',
	limit = 31359294.825749457,
	ending_before = 80688930.88344571,
	starting_after = -29233095.98146501
)

pprint(vars(results))

```

### **create_subscription_item_usage_record**

Create Usage Record

- HTTP Method: POST
- Endpoint: /v1/subscription_items/{subscriptionItemId}/usage_records

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| subscription*item_id | str | Required | ID of the subscription item. String starting with subi*. |
| request_input | [CreateSubscriptionItemUsageRecordRequest](/src/rapydsdk/models/README.md#createsubscriptionitemusagerecordrequest) | Required | Request body. |

**Return Type**

[CreateSubscriptionItemUsageRecord200Response](/src/rapydsdk/models/README.md#createsubscriptionitemusagerecord200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'action': 'action',
	'metadata': {},
	'quantity': -24881109.04735805,
	'timestamp': 92993027.70825747
}
results = sdk.collect.create_subscription_item_usage_record(
	request_input = request_body,
	subscription_item_id = 'subscriptionItemId'
)

pprint(vars(results))

```

### **get_subscription_discount_by_id**

Retrieve an discount

- HTTP Method: GET
- Endpoint: /v1/subscriptions/discount/{discountId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| discount_id | str | Required | discount Id |

**Return Type**

[GetSubscriptionDiscountById200Response](/src/rapydsdk/models/README.md#getsubscriptiondiscountbyid200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.get_subscription_discount_by_id(discount_id = 'discountId')

pprint(vars(results))

```

### **update_sku**

Retrieve SKU.

- HTTP Method: POST
- Endpoint: /v1/skus/{skuId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| sku*id | str | Required | ID of the 'sku' object. String starting with sku*. |
| request_input | [UpdateSkuRequest](/src/rapydsdk/models/README.md#updateskurequest) | Optional | Request body. |

**Return Type**

[UpdateSku200Response](/src/rapydsdk/models/README.md#updatesku200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'active': True,
	'attributes': ["laboris esse","in reprehenderit adipisicing quis elit"],
	'currency': 'GGP',
	'image': 'image',
	'inventory': {"quantity":-98132397,"type_":"infinite","value":"limited"},
	'metadata': {},
	'package_dimensions': {"height":72228599.90616396,"length":-23060185.231993377,"weight":66327438.776373,"width":9098177.88947098},
	'price': 89096776.8880535,
	'product': 'product'
}
results = sdk.collect.update_sku(
	request_input = request_body,
	sku_id = 'skuId'
)

pprint(vars(results))

```

### **retrieve_sku**

Retrieve SKU.

- HTTP Method: GET
- Endpoint: /v1/skus/{skuId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| sku*id | str | Required | ID of the 'sku' object. String starting with sku*. |

**Return Type**

[RetrieveSku200Response](/src/rapydsdk/models/README.md#retrievesku200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.retrieve_sku(sku_id = 'skuId')

pprint(vars(results))

```

### **delete_sku**

Delete SKU.

- HTTP Method: DELETE
- Endpoint: /v1/skus/{skuId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| sku*id | str | Required | ID of the 'sku' object. String starting with sku*. |

**Return Type**

[DeleteSku200Response](/src/rapydsdk/models/README.md#deletesku200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.delete_sku(sku_id = 'skuId')

pprint(vars(results))

```

### **create_sku**

Create SKU

- HTTP Method: POST
- Endpoint: /v1/skus

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateSkuRequest](/src/rapydsdk/models/README.md#createskurequest) | Optional | Request body. |

**Return Type**

[CreateSku200Response](/src/rapydsdk/models/README.md#createsku200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'active': False,
	'attributes': ["enim","Excepteur exercitation occaecat anim labore"],
	'currency': 'MAD',
	'image': 'image',
	'inventory': {"quantity":-12104998,"type_":"infinite","value":"limited"},
	'metadata': {},
	'package_dimensions': {"height":-85967018.9454655,"length":72862763.25894755,"weight":76539329.93342546,"width":14309851.724398375},
	'price': -3853153.3703535497,
	'product': 'product'
}
results = sdk.collect.create_sku(request_input = request_body)

pprint(vars(results))

```

### **list_sku**

List SKUs.

- HTTP Method: GET
- Endpoint: /v1/skus

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| active | bool | Optional | Determines whether the query returns active SKUs or inactive SKUs. Default is true. |
| starting_after | float | Optional | The ID of the SKU created before the first SKU you want to retrieve. |
| ending_before | float | Optional | The ID of the SKU created after the last SKU you want to retrieve. |
| limit | float | Optional | The maximum number of SKUs to return. Range 1-100. Default is 10. |

**Return Type**

[ListSku200Response](/src/rapydsdk/models/README.md#listsku200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.collect.list_sku(
	active = True,
	starting_after = 38010773.440541744,
	ending_before = 72491555.39821747,
	limit = 55665380.42485756
)

pprint(vars(results))

```

### **get_countries**

List Countries

- HTTP Method: GET
- Endpoint: /v1/data/countries

**Parameters**

This method has no parameters.

**Return Type**

[GetCountries200Response](/src/rapydsdk/models/README.md#getcountries200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.general_resources.get_countries()

pprint(vars(results))

```

### **get_currencies**

List Currencies

- HTTP Method: GET
- Endpoint: /v1/data/currencies

**Parameters**

This method has no parameters.

**Return Type**

[GetCurrencies200Response](/src/rapydsdk/models/README.md#getcurrencies200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.general_resources.get_currencies()

pprint(vars(results))

```

### **get_daily_rate**

Resource Methods

- HTTP Method: GET
- Endpoint: /v1/rates/daily

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| action*type | str | Required | Determines the type of transaction that the currency exchange applies to. One of the following - payment, payout |
| amount | float | Optional | Amount of the currency exchange transaction, in units of the fixed-side currency in Decimal. |
| buy_currency | str | Required | Defines the currency purchased in the currency exchange transaction. Three-letter ISO 4217 code in Uppercase. |
| date* | str | Optional | The date when the rate is applicable. Today or earlier. Format YYYY-MM-DD |
| fixed_side | str | Optional | Indicates whether the rate is fixed for the currency defined by buy_currency or sell_currency. One of the following - buy, sell. |
| sell_currency | str | Required | Defines the currency sold in the currency exchange transaction. Three-letter ISO 4217 code in Uppercase. |

**Return Type**

[GetDailyRate200Response](/src/rapydsdk/models/README.md#getdailyrate200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.general_resources.get_daily_rate(
	action_type = 'action_type',
	buy_currency = 'buy_currency',
	sell_currency = 'sell_currency',
	amount = -60069570.179776475,
	date_ = '1917-04-22',
	fixed_side = 'fixed_side'
)

pprint(vars(results))

```

### **get_webhooks**

List Webhooks.

- HTTP Method: GET
- Endpoint: /v1/webhooks

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| from*created_at | float | Optional | The earliest date and time when the object was created, in Unix time (seconds). |
| limit | str | Optional | The maximum number of objects to return. Range: 1-1000. |
| page | float | Optional | Page number for pagination. |
| status | str | Optional | The status of the webhook. One of the following values: *NEW - The webhook was created and has not yet been sent successfully. *RET - The webhook was resent. *CLO - The webhook was sent successfully. *ERR - Attempts were made to send the webhook, but the maximum number of retries was reached. The automatic retry process failed. The webhook was not sent. |
| type* | str | Optional | The type of webhook. |
| to_created_at | float | Optional | The latest date and time when the object was created, in Unix time (seconds). |

**Return Type**

[GetWebhooks200Response](/src/rapydsdk/models/README.md#getwebhooks200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.general_resources.get_webhooks(
	from_created_at = 67755024.46657887,
	limit = 'limit',
	page = 28749150.11010444,
	status = 'status',
	type_ = 'type',
	to_created_at = -57254427.22775047
)

pprint(vars(results))

```

### **resend_webhook_by_token**

Use List Webhooks to find the IDs of webhooks. You can resend a webhook that is in status ERR.

- HTTP Method: POST
- Endpoint: /v1/webhooks/{webhookId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| webhook*id | str | Required | The webhook ID. String starting with wh*. |

**Return Type**

[ResendWebhookByToken200Response](/src/rapydsdk/models/README.md#resendwebhookbytoken200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.general_resources.resend_webhook_by_token(webhook_id = 'webhookId')

pprint(vars(results))

```

### **get_webhook_by_token**

Use List Webhooks to find the IDs of webhooks.

- HTTP Method: GET
- Endpoint: /v1/webhooks/{webhookId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| webhook*id | str | Required | ID of the webhook. String starting with wh*. |

**Return Type**

[GetWebhookByToken200Response](/src/rapydsdk/models/README.md#getwebhookbytoken200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.general_resources.get_webhook_by_token(webhook_id = 'webhookId')

pprint(vars(results))

```

### **generate_card_tokenization_page**

Create a hosted page for a customer to save card details and manage cards.

- HTTP Method: POST
- Endpoint: /v1/hosted/collect/card

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [GenerateCardTokenizationPageRequest](/src/rapydsdk/models/README.md#generatecardtokenizationpagerequest) | Required | Request body. |

**Return Type**

[GenerateCardTokenizationPage200Response](/src/rapydsdk/models/README.md#generatecardtokenizationpage200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'billing_address_collect': 'billing_address_collect',
	'cancel_url': 'cancel_url',
	'complete_payment_url': 'complete_payment_url',
	'complete_url': 'complete_url',
	'country': 'SK',
	'currency': 'BRL',
	'customer': 'customer',
	'error_payment_url': 'error_payment_url',
	'language': 'language',
	'page_expiration': 97593889.32785907,
	'payment_method_type': 'payment_method_type'
}
results = sdk.hosted.generate_card_tokenization_page(request_input = request_body)

pprint(vars(results))

```

### **generate_idv_page**

Create Identity Verification Page

- HTTP Method: POST
- Endpoint: /v1/hosted/idv

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [GenerateIdvPageRequest](/src/rapydsdk/models/README.md#generateidvpagerequest) | Required | Request body. |

**Return Type**

[GenerateIdvPage200Response](/src/rapydsdk/models/README.md#generateidvpage200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'cancel_url': 'cancel_url',
	'complete_url': 'complete_url',
	'contact': 'contact',
	'country': 'country',
	'document_type': 'document_type',
	'ewallet': 'ewallet',
	'force_camera': False,
	'language': 'language',
	'page_expiration': -27853761.238905102,
	'reference_id': 'reference_id',
	'request_type': 'verify'
}
results = sdk.hosted.generate_idv_page(request_input = request_body)

pprint(vars(results))

```

### **generate_card_issuing_page**

Generate a hosted page that displays details of a virtual issued card directly to the customer.

- HTTP Method: POST
- Endpoint: /v1/hosted/issuing/card_details/{cardToken}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| card_token | str | Required | ID of the Issued Card Details to Customer. |
| request_input | [GenerateCardIssuingPageRequest](/src/rapydsdk/models/README.md#generatecardissuingpagerequest) | Required | Request body. |

**Return Type**

[GenerateCardIssuingPage200Response](/src/rapydsdk/models/README.md#generatecardissuingpage200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'card_color': 'card_color',
	'language': 'language',
	'logo': 'logo',
	'logo_orientation': 'logo_orientation'
}
results = sdk.hosted.generate_card_issuing_page(
	request_input = request_body,
	card_token = 'cardToken'
)

pprint(vars(results))

```

### **perform_identity_verification**

Verify the identity of an individual or a personal contact for a 'person' wallet.

- HTTP Method: POST
- Endpoint: /v1/identities

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [PerformIdentityVerificationRequest](/src/rapydsdk/models/README.md#performidentityverificationrequest) | Required | Request body. |

**Return Type**

[PerformIdentityVerification200Response](/src/rapydsdk/models/README.md#performidentityverification200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'back_side_image': 'back_side_image',
	'back_side_image_mime_type': 'back_side_image_mime_type',
	'contact': 'contact',
	'country': 'JM',
	'document_type': 'document_type',
	'ewallet': 'ewallet',
	'face_image': 'face_image',
	'face_image_mime_type': 'face_image_mime_type',
	'front_side_image': 'front_side_image',
	'front_side_image_mime_type': 'front_side_image_mime_type',
	'reference_id': 'reference_id',
	'request_type': 'request_type',
	'send_callback': 'send_callback'
}
results = sdk.verify.perform_identity_verification(request_input = request_body)

pprint(vars(results))

```

### **get_kyc_id_verification_supported_doc_types**

Retrieve a list of the types of official identification documents for a country.

- HTTP Method: GET
- Endpoint: /v1/identities/types

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| country | str | Required | Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. |

**Return Type**

[GetKycIdVerificationSupportedDocTypes200Response](/src/rapydsdk/models/README.md#getkycidverificationsupporteddoctypes200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.verify.get_kyc_id_verification_supported_doc_types(country = 'MC')

pprint(vars(results))

```

### **get_application_types_by_country**

List Rapyd Verify Application Types.

- HTTP Method: GET
- Endpoint: /v1/verify/applications/types/country/{country}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| country | str | Required | Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. |

**Return Type**

[GetApplicationTypesByCountry200Response](/src/rapydsdk/models/README.md#getapplicationtypesbycountry200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.verify.get_application_types_by_country(country = 'RU')

pprint(vars(results))

```

### **get_application_status**

Retrieve Status of Rapyd Verify Application

- HTTP Method: GET
- Endpoint: /v1/verify/applications/status/{application}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| application | str | Required | ID of the application. String starting with app\_. |

**Return Type**

[GetApplicationStatus200Response](/src/rapydsdk/models/README.md#getapplicationstatus200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.verify.get_application_status(application = 'application')

pprint(vars(results))

```

### **create_hosted_application_token**

Create Rapyd Verify Application

- HTTP Method: POST
- Endpoint: /v1/verify/applications/hosted

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateHostedApplicationTokenRequest](/src/rapydsdk/models/README.md#createhostedapplicationtokenrequest) | Optional | Request body. |

**Return Type**

[CreateHostedApplicationToken200Response](/src/rapydsdk/models/README.md#createhostedapplicationtoken200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'application_type': 'application_type',
	'cancel_url': 'cancel_url',
	'client_reference_id': 'client_reference_id',
	'complete_url': 'complete_url',
	'country': 'country',
	'metadata': {},
	'phone_number': 'phone_number',
	'rapyd_entity_token': 'ewallet_ef84c580177dbfc4293b1cf73c73fc77'
}
results = sdk.verify.create_hosted_application_token(request_input = request_body)

pprint(vars(results))

```

### **get_hosted_application_by_token**

Create Rapyd Verify Application

- HTTP Method: GET
- Endpoint: /v1/verify/applications/hosted/{verifyAppId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| verify*app_id | str | Required | ID of the Rapyd Verify application. String starting with happ*. |

**Return Type**

[GetHostedApplicationByToken200Response](/src/rapydsdk/models/README.md#gethostedapplicationbytoken200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.verify.get_hosted_application_by_token(verify_app_id = 'verifyAppId')

pprint(vars(results))

```

### **create_issuing**

Issue Virtual Account Number to Wallet

- HTTP Method: POST
- Endpoint: /v1/virtual_accounts

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateIssuingRequest](/src/rapydsdk/models/README.md#createissuingrequest) | Required | Request body. |

**Return Type**

[CreateIssuing200Response](/src/rapydsdk/models/README.md#createissuing200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'country': 'country',
	'currency': 'currency',
	'description': 'description',
	'ewallet': 'ewallet',
	'merchant_reference_id': 'merchant_reference_id',
	'metadata': {},
	'requested_currency': 'requested_currency'
}
results = sdk.issuing.create_issuing(request_input = request_body)

pprint(vars(results))

```

### **simulate_complete_bank_account_issuing_transaction**

Simulate a Bank Transfer to a Wallet

- HTTP Method: POST
- Endpoint: /v1/virtual_accounts/transactions

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [SimulateCompleteBankAccountIssuingTransactionRequest](/src/rapydsdk/models/README.md#simulatecompletebankaccountissuingtransactionrequest) | Required | Request body. |

**Return Type**

[SimulateCompleteBankAccountIssuingTransaction200Response](/src/rapydsdk/models/README.md#simulatecompletebankaccountissuingtransaction200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'amount': 'amount',
	'currency': 'currency',
	'issued_bank_account': 'issued_bank_account'
}
results = sdk.issuing.simulate_complete_bank_account_issuing_transaction(request_input = request_body)

pprint(vars(results))

```

### **update_receiving_currency**

- HTTP Method: POST
- Endpoint: /v1/virtual_accounts/{virtualAccountId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| virtual*account_id | str | Required | ID of the Virtual Account Number object. String starting with issuing*. |
| request_input | [UpdateReceivingCurrencyRequest](/src/rapydsdk/models/README.md#updatereceivingcurrencyrequest) | Required | Request body. |

**Return Type**

[UpdateReceivingCurrency200Response](/src/rapydsdk/models/README.md#updatereceivingcurrency200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {'requesting_currency': 'SGD'}
results = sdk.issuing.update_receiving_currency(
	request_input = request_body,
	virtual_account_id = 'virtualAccountId'
)

pprint(vars(results))

```

### **retrieve_issuing_by_rapyd_token**

Retrieve Virtual Account History

- HTTP Method: GET
- Endpoint: /v1/virtual_accounts/{virtualAccountId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| virtual*account_id | str | Required | ID of the Virtual Account Number object. String starting with issuing*. |

**Return Type**

[RetrieveIssuingByRapydToken200Response](/src/rapydsdk/models/README.md#retrieveissuingbyrapydtoken200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.issuing.retrieve_issuing_by_rapyd_token(virtual_account_id = 'virtualAccountId')

pprint(vars(results))

```

### **close_issuing**

Close VA

- HTTP Method: DELETE
- Endpoint: /v1/virtual_accounts/{virtualAccountId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| virtual*account_id | str | Required | ID of the virtual account. String starting with issuing*. |

**Return Type**

[CloseIssuing200Response](/src/rapydsdk/models/README.md#closeissuing200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.issuing.close_issuing(virtual_account_id = 'virtualAccountId')

pprint(vars(results))

```

### **retrieve_issuing_transaction**

Retrieve Virtual Account Transaction

- HTTP Method: GET
- Endpoint: /v1/virtual_accounts/{virtualAccountId}/transactions/{transactionId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| virtual*account_id | str | Required | ID of the Virtual Account Number object. String starting with issuing*. |
| transaction_id | str | Required | ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'. |

**Return Type**

[RetrieveIssuingTransaction200Response](/src/rapydsdk/models/README.md#retrieveissuingtransaction200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.issuing.retrieve_issuing_transaction(
	virtual_account_id = 'virtualAccountId',
	transaction_id = 'transactionId'
)

pprint(vars(results))

```

### **issue_card**

Issue Card

- HTTP Method: POST
- Endpoint: /v1/issuing/cards

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [IssueCardRequest](/src/rapydsdk/models/README.md#issuecardrequest) | Required | Request body. |

**Return Type**

[IssueCard200Response](/src/rapydsdk/models/README.md#issuecard200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'card_program': 'card_program',
	'country': 'country',
	'ewallet_contact': 'ewallet_contact',
	'expiration_month': 'expiration_month',
	'expiration_year': 'expiration_year',
	'metadata': {}
}
results = sdk.issuing.issue_card(request_input = request_body)

pprint(vars(results))

```

### **get_card_issuing_list**

List issuing cards.

- HTTP Method: GET
- Endpoint: /v1/issuing/cards

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| contact | str | Optional | ID of a wallet contact. String starting with cont\_. |
| page_number | float | Optional | Page number to retrieve. |
| page_size | float | Optional | Number of results per page. |
| creation_start_date | float | Optional | Start date of card creation. |
| creation_end_date | float | Optional | End date of card creation. |
| activation_start_date | float | Optional | Start date of card activation. |
| activation_end_date | float | Optional | End date of card activation. |
| card_program | str | Optional | Card program token. |
| status | str | Optional | Card status. |
| allow_deleted | bool | Optional | Is card allow delete. |

**Return Type**

[GetCardIssuingList200Response](/src/rapydsdk/models/README.md#getcardissuinglist200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.issuing.get_card_issuing_list(
	contact = 'contact',
	page_number = -88440900.79881126,
	page_size = -54577447.3109081,
	creation_start_date = 13722196.733498484,
	creation_end_date = -49701811.76119795,
	activation_start_date = 86741238.73606452,
	activation_end_date = -44828941.48939076,
	card_program = 'card_program',
	status = 'status',
	allow_deleted = True
)

pprint(vars(results))

```

### **get_card_issuing_details**

Card details.

- HTTP Method: GET
- Endpoint: /v1/issuing/cards/{cardId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| card*id | str | Required | ID of a cardId. String starting with ci*. |

**Return Type**

[GetCardIssuingDetails200Response](/src/rapydsdk/models/README.md#getcardissuingdetails200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.issuing.get_card_issuing_details(card_id = 'cardId')

pprint(vars(results))

```

### **activate_card**

Activate Issued Card Using API

- HTTP Method: POST
- Endpoint: /v1/issuing/cards/activate

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [ActivateCardRequest](/src/rapydsdk/models/README.md#activatecardrequest) | Required | Request body. |

**Return Type**

[ActivateCard200Response](/src/rapydsdk/models/README.md#activatecard200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {'card': 'card'}
results = sdk.issuing.activate_card(request_input = request_body)

pprint(vars(results))

```

### **modify_card**

Personalize Bulk-Issued Card

- HTTP Method: POST
- Endpoint: /v1/issuing/cards/personalize

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [ModifyCardRequest](/src/rapydsdk/models/README.md#modifycardrequest) | Required | Request body. |

**Return Type**

[ModifyCard200Response](/src/rapydsdk/models/README.md#modifycard200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'card': 'card',
	'ewallet_contact': 'ewallet_contact'
}
results = sdk.issuing.modify_card(request_input = request_body)

pprint(vars(results))

```

### **update_card_status**

Update Card Status

- HTTP Method: POST
- Endpoint: /v1/issuing/cards/status

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [UpdateCardStatusRequest](/src/rapydsdk/models/README.md#updatecardstatusrequest) | Required | Request body. |

**Return Type**

[UpdateCardStatus200Response](/src/rapydsdk/models/README.md#updatecardstatus200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'blocked_reason': 'blocked_reason',
	'card': 'card',
	'status': 'status'
}
results = sdk.issuing.update_card_status(request_input = request_body)

pprint(vars(results))

```

### **get_card_issuing_transactions**

List Issued Card Transactions

- HTTP Method: GET
- Endpoint: /v1/issuing/cards/{cardId}/transactions

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| card*id | str | Required | ID of the issued card. String starting with card*. |
| end_date | str | Optional | Timestamp of the last transaction or later, in Unix time. |
| min_amount | str | Optional | Transactions greater than a specific amount. |
| max_amount | str | Optional | Transactions smaller than a specific amount. |
| merchant_name_search | str | Optional | Filters the results to return only transactions that have this string as part of the name or location. |
| page_size | str | Required | ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'. |
| page_number | str | Required | Page number to retrieve. |
| start_date | str | Optional | ID of the transaction, as appears in the array of transactions in the response to 'Retrieve Virtual Account History'. |

**Return Type**

[GetCardIssuingTransactions200Response](/src/rapydsdk/models/README.md#getcardissuingtransactions200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.issuing.get_card_issuing_transactions(
	card_id = 'cardId',
	page_size = 'page_size',
	page_number = 'page_number',
	end_date = 'end_date',
	min_amount = 'min_amount',
	max_amount = 'max_amount',
	merchant_name_search = 'merchant_name_search',
	start_date = 'start_date'
)

pprint(vars(results))

```

### **get_card_issuing_transaction**

Retrieve Issued Card Transaction Details

- HTTP Method: GET
- Endpoint: /v1/issuing/cards/{cardId}/transactions/{transactionId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| card_id | str | Required | Card id |
| transaction_id | str | Required | Card transaction id |

**Return Type**

[GetCardIssuingTransaction200Response](/src/rapydsdk/models/README.md#getcardissuingtransaction200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.issuing.get_card_issuing_transaction(
	card_id = 'cardId',
	transaction_id = 'transactionId'
)

pprint(vars(results))

```

### **get_payout_method_types_details**

Get Payout Required Fields

- HTTP Method: GET
- Endpoint: /v1/payout_methods/{pomt}/required_fields

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| pomt | str | Required | The type of the payout method. Set to the name of a payout method listed in the response to List Payout Method Types. The two-letter prefix must match the beneficiary country code. |
| beneficiary_country | str | Required | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase. |
| beneficiary_entity_type | str | Required | Type of entity for the beneficiary. One of the following, individual, company |
| payout_amount | float | Required | Amount of the payout, in units of the currency that the beneficiary is receiving. Decimal. |
| payout_currency | str | Required | Currency received by the beneficiary. Three-letter ISO 4217 code. Uppercase. |
| sender_country | str | Required | Country of the sender. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase. |
| sender_currency | str | Required | Currency that the sender is paying with. Three-letter ISO 4217 code. Uppercase. |
| sender_entity_type | str | Required | Type of entity for the sender. One of the following: individual, company |

**Return Type**

[GetPayoutMethodTypesDetails200Response](/src/rapydsdk/models/README.md#getpayoutmethodtypesdetails200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.get_payout_method_types_details(
	pomt = 'pomt',
	beneficiary_country = 'beneficiary_country',
	beneficiary_entity_type = 'beneficiary_entity_type',
	payout_amount = -70950757.61231545,
	payout_currency = 'payout_currency',
	sender_country = 'sender_country',
	sender_currency = 'sender_currency',
	sender_entity_type = 'sender_entity_type'
)

pprint(vars(results))

```

### **create_payout**

Create Payout

- HTTP Method: POST
- Endpoint: /v1/payouts

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreatePayoutRequest](/src/rapydsdk/models/README.md#createpayoutrequest) | Required | Request body. |

**Return Type**

[CreatePayout200Response](/src/rapydsdk/models/README.md#createpayout200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.create_payout()

pprint(vars(results))

```

### **list_payouts**

List Payouts

- HTTP Method: GET
- Endpoint: /v1/payouts

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| beneficiary | str | Optional | Filters according to the beneficiary ID. String starting with beneficiary*. |
| created_after | str | Optional | The ID of the payout created before the first payout you want to retrieve. String starting with payout*. |
| created*before | str | Optional | The ID of the payout created after the last payout you want to retrieve. String starting with payout*. |
| ending*before | str | Optional | The ID of a payout in the list. The list ends with the payout that was created before the payout with this ID. Use this filter to get the previous page of results. String starting with payout*. Deprecated. |
| ewallet | str | Optional | Filters according to the wallet ID. String starting with ewallet*. |
| limit | str | Optional | The maximum number of payouts to return. Range: 1-100. Default is 10. |
| merchant_reference_id | str | Optional | Filters according to the merchant reference ID. |
| payout_method_type | str | Optional | Filters according to the type of payout method. The two-letter prefix must match the beneficiary country code. |
| sender | str | Optional | Filters according to the sender ID. String starting with sender*. |
| sender*country | str | Optional | Filters according to the country of the sender. Two-letter ISO 3166-1 ALPHA-2 code. |
| sender_currency | str | Optional | Filters according to the currency that the sender is paying with. Three-letter ISO 4217 code. |
| starting_after | str | Optional | The ID of a payout in the list. The list begins with the payout that was created next after the payout with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used. String starting with payout*. Deprecated |

**Return Type**

[ListPayouts200Response](/src/rapydsdk/models/README.md#listpayouts200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.list_payouts(
	beneficiary = 'beneficiary',
	created_after = 'created_after',
	created_before = 'created_before',
	ending_before = 'ending_before',
	ewallet = 'ewallet',
	limit = 'limit',
	merchant_reference_id = 'merchant_reference_id',
	payout_method_type = 'payout_method_type',
	sender = 'sender',
	sender_country = 'YE',
	sender_currency = 'SCR',
	starting_after = 'starting_after'
)

pprint(vars(results))

```

### **create_beneficiary**

Create Beneficiary

- HTTP Method: POST
- Endpoint: /v1/payouts/beneficiary

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateBeneficiaryRequest](/src/rapydsdk/models/README.md#createbeneficiaryrequest) | Required | Request body. |

**Return Type**

[CreateBeneficiary200Response](/src/rapydsdk/models/README.md#createbeneficiary200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'category': 'category',
	'company_name': 'ABC',
	'country': 'ER',
	'currency': 'KGS',
	'default_payout_method_type': 'us_general_bank',
	'entity_type': 'entity_type',
	'first_name': 'John',
	'identification_type': 'drivers_license',
	'identification_value': 'ABNHDLK354665',
	'last_name': 'John',
	'merchant_reference_id': 'GHY-0YU-HUJ-POI'
}
results = sdk.disburse.create_beneficiary(request_input = request_body)

pprint(vars(results))

```

### **validate_beneficiary**

Validate Beneficiary

- HTTP Method: POST
- Endpoint: /v1/payouts/beneficiary/validate

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [ValidateBeneficiaryRequest](/src/rapydsdk/models/README.md#validatebeneficiaryrequest) | Required | Request body. |

**Return Type**

[ValidateBeneficiary200Response](/src/rapydsdk/models/README.md#validatebeneficiary200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'amount': -68900823.43974182,
	'beneficiary': 'beneficiary_d895d90d276869efe1e359386a1fb3e3',
	'identifier_type': 'identifier_type',
	'identifier_value': 'identifier_value',
	'payout_method_type': 'us_general_bank',
	'sender_country': 'IL',
	'sender_currency': 'WST',
	'sender_entity_type': 'sender_entity_type'
}
results = sdk.disburse.validate_beneficiary(request_input = request_body)

pprint(vars(results))

```

### **get_beneficiary**

Retrieve Beneficiary

- HTTP Method: GET
- Endpoint: /v1/payouts/beneficiary/{beneficiaryId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| beneficiary*id | str | Required | ID of the 'beneficiary' object. String starting with beneficiary*. |

**Return Type**

[GetBeneficiary200Response](/src/rapydsdk/models/README.md#getbeneficiary200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.get_beneficiary(beneficiary_id = 'beneficiaryId')

pprint(vars(results))

```

### **delete_beneficiary**

Delete Beneficiary

- HTTP Method: DELETE
- Endpoint: /v1/payouts/beneficiary/{beneficiaryId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| beneficiary*id | str | Required | ID of the 'beneficiary' object. String starting with beneficiary*. |

**Return Type**

[DeleteBeneficiary200Response](/src/rapydsdk/models/README.md#deletebeneficiary200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.delete_beneficiary(beneficiary_id = 'beneficiaryId')

pprint(vars(results))

```

### **simulate_complete_payout**

Complete the Payout

- HTTP Method: POST
- Endpoint: /v1/payouts/complete/{payoutToken}/{amount}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| payout*token | str | Required | ID of the payout. String starting with 'payout*'. |
| amount | str | Required | The payout amount. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. |

**Return Type**

[SimulateCompletePayout200Response](/src/rapydsdk/models/README.md#simulatecompletepayout200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.simulate_complete_payout(
	payout_token = 'payoutToken',
	amount = 'amount'
)

pprint(vars(results))

```

### **confirm_payout**

Confirm Payout that involves foreign exchange

- HTTP Method: POST
- Endpoint: /v1/payouts/confirm/{payoutToken}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| payout*token | str | Required | ID of the payout. String starting with 'payout*'. |

**Return Type**

[ConfirmPayout200Response](/src/rapydsdk/models/README.md#confirmpayout200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.confirm_payout(payout_token = 'payoutToken')

pprint(vars(results))

```

### **create_sender**

Create Sender

- HTTP Method: POST
- Endpoint: /v1/payouts/sender

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [CreateSenderRequest](/src/rapydsdk/models/README.md#createsenderrequest) | Required | Request body. |

**Return Type**

[CreateSender200Response](/src/rapydsdk/models/README.md#createsender200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'company_name': 'ABC',
	'country': 'AM',
	'currency': 'VUV',
	'entity_type': 'entity_type',
	'first_name': 'Scott',
	'identification_type': 'drivers_license',
	'identification_value': 'ANDSFS8974562',
	'last_name': 'Williams'
}
results = sdk.disburse.create_sender(request_input = request_body)

pprint(vars(results))

```

### **get_payer**

Retrieve details of a payout sender.

- HTTP Method: GET
- Endpoint: /v1/payouts/sender/{senderId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| sender*id | str | Required | ID of the Sender object. String starting with 'sender*'. |

**Return Type**

[GetPayer200Response](/src/rapydsdk/models/README.md#getpayer200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.get_payer(sender_id = 'senderId')

pprint(vars(results))

```

### **delete_payer**

Delete Sender

- HTTP Method: DELETE
- Endpoint: /v1/payouts/sender/{senderId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| sender*id | str | Required | ID of the 'sender' object. String starting with sender*. |

**Return Type**

[DeletePayer200Response](/src/rapydsdk/models/README.md#deletepayer200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.delete_payer(sender_id = 'senderId')

pprint(vars(results))

```

### **get_payout_method_types**

List Payout Method Types

- HTTP Method: GET
- Endpoint: /v1/payout_methods

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| sender_entity_type | str | Optional | Filters the type of entity for the payer. One of the following: individual, company |
| beneficiary_country | str | Optional | Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. |
| payout_currency | str | Optional | Currency received by the beneficiary. Three-letter ISO 4217 code. |
| sender_currency | str | Optional | Currency that the sender is paying with. Three-letter ISO 4217 code. |
| sender_country | str | Optional | Country of the sender. Two-letter ISO 3166-1 ALPHA-2 code. Note: This field does not appear in the response. |
| beneficiary_entity_type | str | Optional | Filters the type of entity for the beneficiary. One of the following: individual, company |
| category | str | Optional | The category of payout method. One of the following: bank, card, cash, rapyd_ewallet, ewallet |
| is_cancelable | bool | Optional | Indicates whether the payout can be canceled. Relevant when category is cash. |
| is_location_specific | bool | Optional | Indicates whether the payout must be made at a specific physical location. Relevant when category is cash. |
| is_expirable | bool | Optional | Indicates whether the payout expires if not completed. Relevant when category is cash. |
| starting_after | str | Optional | The name of a payout method in the list. The list begins with the record that was created next after the record with this payout method. Use this filter to get the next page of results. Relevant when ending_before is not used. |
| ending_before | str | Optional | The name of a payout method in the list. The list ends with the last record that was created before the record with this payout method. Use this filter to get the previous page of results. |
| limit | str | Optional | The maximum number of payout methods to return. Range: 1-100. Default is 10. |

**Return Type**

[GetPayoutMethodTypes200Response](/src/rapydsdk/models/README.md#getpayoutmethodtypes200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.get_payout_method_types(
	sender_entity_type = 'sender_entity_type',
	beneficiary_country = 'beneficiary_country',
	payout_currency = 'payout_currency',
	sender_currency = 'sender_currency',
	sender_country = 'sender_country',
	beneficiary_entity_type = 'beneficiary_entity_type',
	category = 'category',
	is_cancelable = True,
	is_location_specific = True,
	is_expirable = True,
	starting_after = 'starting_after',
	ending_before = 'ending_before',
	limit = 'limit'
)

pprint(vars(results))

```

### **update_payout**

Update Payout

- HTTP Method: POST
- Endpoint: /v1/payouts/{payoutId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| payout*id | str | Required | ID of the payout. String starting with payout*. |
| request_input | [UpdatePayoutRequest](/src/rapydsdk/models/README.md#updatepayoutrequest) | Required | Request body. |

**Return Type**

[UpdatePayout200Response](/src/rapydsdk/models/README.md#updatepayout200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

request_body = {
	'description': 'description',
	'metadata': {}
}
results = sdk.disburse.update_payout(
	request_input = request_body,
	payout_id = 'payoutId'
)

pprint(vars(results))

```

### **get_payout**

Retrieve Payout

- HTTP Method: GET
- Endpoint: /v1/payouts/{payoutId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| payout*id | str | Required | ID of the payout. String starting with 'payout*'. |

**Return Type**

[GetPayout200Response](/src/rapydsdk/models/README.md#getpayout200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.get_payout(payout_id = 'payoutId')

pprint(vars(results))

```

### **cancel_payout**

Cancel Payout

- HTTP Method: DELETE
- Endpoint: /v1/payouts/{payoutId}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| payout*id | str | Required | ID of the payout. String starting with payout*. |

**Return Type**

[CancelPayout200Response](/src/rapydsdk/models/README.md#cancelpayout200response)

**Example Usage Code Snippet**

```Python
from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk
sdk = Rapydsdk()

results = sdk.disburse.cancel_payout(payout_id = 'payoutId')

pprint(vars(results))

```

## License

License: MIT. See license in LICENSE.
