# V1PlansBody

**Properties**

| Name              | Type  | Required | Description                                                                                                                                                                                         |
| :---------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| currency          | str   | ✅       | Three-letter ISO 4217 code for the currency used in fields that represent monetary amounts. Uppercase.                                                                                              |
| interval          | str   | ✅       | Specifies the units used in defining the billing cycle.                                                                                                                                             |
| product           | str   | ✅       | ID of the 'product' object that this plan is for. The product must have type set to service.                                                                                                        |
| aggregate_usage   | str   | ❌       | Determines which quantity is used to calculate the pricing. Relevant when usage_type is metered. Default is sum.                                                                                    |
| amount            | float | ❌       | The amount to charge in the billing cycle. For a free service, use 0. Relevant when billing_scheme is set to per_unit. When the billing_scheme is set to tiered, set the amount in the tiers array. |
| billing_scheme    | str   | ❌       | Describes how to compute the price per billing period. One of the following values - per_unit, tiered                                                                                               |
| id\_              | str   | ❌       | Unique ID for this payment plan. English alphanumeric characters and underscore. Limited to 44 characters. If the merchant does not define an ID, Rapyd generates a string starting with plan\_.    |
| interval_count    | float | ❌       | Number of intervals in the billing cycle. Default is 1.                                                                                                                                             |
| metadata          | dict  | ❌       | A JSON object defined by the client.                                                                                                                                                                |
| nickname          | str   | ❌       | Brief description of the pricing plan.                                                                                                                                                              |
| tiers             | str   | ❌       | Defines a tiered pricing structure. Array of objects. Must be null when billing_scheme is set to per_unit.                                                                                          |
| tiers_mode        | str   | ❌       | Determines the mode for calculating the total tiered charge.                                                                                                                                        |
| transform_usage   | dict  | ❌       | Defines the transformation that is applied to the reported usage before the billed price is computed.                                                                                               |
| trial_period_days | float | ❌       | Specifies the number of days before charges begin to accrue. Use this parameter to define a free trial period for a service.                                                                        |
| usage_type        | str   | ❌       | Determines whether the customer is billed when the service is not actually used. One of the following values - metered, licensed                                                                    |
