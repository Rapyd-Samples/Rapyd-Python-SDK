# Outcome

The outcome object describes the outcome of the Rapyd Protect risk assessment

**Properties**

| Name              | Type                   | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :---------------- | :--------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| network_status    | NetworkStatus          | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| payment_flow_type | OutcomePaymentFlowType | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| payment_options   | PaymentOptions         | ❌       | A payment method type is a type of payment method that any customer can use, for example, ee*mastercard_card, Mastercard for Estonia. When it is added to a customer profile, it becomes a payment method that is specific to that one customer. The name of the payment method type starts with a prefix for the country, the 2-letter ISO 3166-1 alpha-2 code. If the payment method is valid in multiple countries, the prefix is xx*. The payment method type has a suffix with one of the following values - \_bank - Bank transfer or bank redirect \_card - Credit card, debit card or other card \_cash - Cash \_ewallet - Local eWallet |
| status            | str                    | ❌       | Indicates the status of the payment method. One of the following value is 1 means the payment_method_type is Valid                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| risk_level        | RiskLevel              | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| seller_message    | str                    | ❌       | Message to the merchant                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

# NetworkStatus

**Properties**

| Name                  | Type | Required | Description               |
| :-------------------- | :--- | :------- | :------------------------ |
| APPROVEDBYNETWORK     | str  | ✅       | "approved_by_network"     |
| DECLINEDBYNETWORK     | str  | ✅       | "declined_by_network"     |
| NOTSENTTONETWORK      | str  | ✅       | "not_sent_to_network"     |
| REVERSEDAFTERAPPROVAL | str  | ✅       | "reversed_after_approval" |

# OutcomePaymentFlowType

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| DIRECT        | str  | ✅       | "direct"         |
| EWALLET       | str  | ✅       | "eWallet"        |
| EWALLETPAYOUT | str  | ✅       | "ewallet_payout" |
| CARD          | str  | ✅       | "card"           |
| REDIRECTURL   | str  | ✅       | "redirect_url"   |

# RiskLevel

**Properties**

| Name        | Type | Required | Description    |
| :---------- | :--- | :------- | :------------- |
| NORMAL      | str  | ✅       | "normal"       |
| ELEVATED    | str  | ✅       | "elevated"     |
| HIGHEST     | str  | ✅       | "highest"      |
| NOTASSESSED | str  | ✅       | "not_assessed" |
