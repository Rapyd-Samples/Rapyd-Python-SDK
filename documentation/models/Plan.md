# Plan

**Properties**

| Name              | Type               | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :---------------- | :----------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| active            | bool               | ❌       | Indicates whether the plan is available to be added to a subscription.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| aggregate_usage   | AggregateUsage     | ❌       | Determines which quantity is used to calculate the pricing. One of the following: _ max - The maximum reported usage within the billing cycle. _ sum - The sum of all usage during a billing cycle. This is the default. _ last_during_period - The last usage reported within the billing cycle. _ last_ever - The last usage ever reported, if the latest billing cycles contain no usage at all. Required when usage_type is metered. Relevant when billing_scheme is set to per_unit. |
| amount            | float              | ❌       | The amount to charge, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal. For a free service, use 0. Must be null when tiers is set. Relevant when billing_scheme is set to per_unit.                                                                                                                        |
| billing_scheme    | BillingScheme      | ❌       | Describes how to compute the price. One of the following: _ per_unit - The amount specified in amount is charged for each unit. Also set these related fields: amount, transform_usage, usage_type, aggregate_usage. This is the default. _ tiered - The unit pricing is computed using a tiering strategy as defined with the tiers and tiers_mode fields.                                                                                                                               |
| created_at        | float              | ❌       | Time the 'plan' object was created, in Unix time. Response only.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| currency          | str                | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| id\_              | str                | ❌       | Unique ID for this plan. English alphanumeric characters with no special characters except underscore. If the client does not define an ID, Rapyd generates a string starting with **plan\_**.                                                                                                                                                                                                                                                                                            |
| interval          | Interval           | ❌       | Specifies the units used in defining the billing cycle. One of the following: _ day _ week _ month _ year Maximum interval is 1 year.                                                                                                                                                                                                                                                                                                                                                     |
| interval_count    | float              | ❌       | Number of time intervals in the billing cycle. Integer                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| metadata          | dict               | ❌       | A JSON object defined by the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| nickname          | str                | ❌       | Brief description of the plan.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| product           | PlanProduct        | ❌       | The ID of the product that this plan is for, and fields describing this product in the plan.                                                                                                                                                                                                                                                                                                                                                                                              |
| tiers             | List[PlanTiers]    | ❌       | Defines a tiered pricing structure. Each tier object represents a pricing tier.                                                                                                                                                                                                                                                                                                                                                                                                           |
| tiers_mode        | TiersMode          | ❌       | Determines the mode for calculating the total tiered charge. One of the following values: _ graduated - The total cost at each price tier is calculated separately, then all tier charges are added together. _ volume - The total cost is calculated as the number of items times the applicable tier price. Relevant when billing_scheme is set to tiered                                                                                                                               |
| transform_usage   | PlanTransformUsage | ❌       | Defines the transformation that is applied to the reported usage before the billed price is computed. The transformation divides the quantity by the divisor specified in divide_by, then rounds up or down according to the setting in round. Relevant when billing_scheme is set to per_unit.                                                                                                                                                                                           |
| trial_period_days | float              | ❌       | Specifies the number of days before charges begin to accrue. Use this parameter to define a free trial period for a service.                                                                                                                                                                                                                                                                                                                                                              |
| usage_type        | UsageType          | ❌       | Determines whether the customer is billed when the service is not actually used. Relevant when billing_scheme is set to per_unit. One of the following: _ metered - The customer is billed only for actual usage. You must also set aggregate_usage. _ licensed - The customer is billed even if the service is not used. This is the default.                                                                                                                                            |

# AggregateUsage

Determines which quantity is used to calculate the pricing. One of the following: _ max - The maximum reported usage within the billing cycle. _ sum - The sum of all usage during a billing cycle. This is the default. _ last_during_period - The last usage reported within the billing cycle. _ last_ever - The last usage ever reported, if the latest billing cycles contain no usage at all. Required when usage_type is metered. Relevant when billing_scheme is set to per_unit.

**Properties**

| Name             | Type | Required | Description          |
| :--------------- | :--- | :------- | :------------------- |
| MAX              | str  | ✅       | "max"                |
| SUM              | str  | ✅       | "sum"                |
| LASTDURINGPERIOD | str  | ✅       | "last_during_period" |
| LASTEVER         | str  | ✅       | "last_ever"          |

# BillingScheme

Describes how to compute the price. One of the following: _ per_unit - The amount specified in amount is charged for each unit. Also set these related fields: amount, transform_usage, usage_type, aggregate_usage. This is the default. _ tiered - The unit pricing is computed using a tiering strategy as defined with the tiers and tiers_mode fields.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| PERUNIT | str  | ✅       | "per_unit"  |
| TIERED  | str  | ✅       | "tiered"    |

# Interval

Specifies the units used in defining the billing cycle. One of the following: _ day _ week _ month _ year Maximum interval is 1 year.

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| MONTH | str  | ✅       | "month"     |
| DAY   | str  | ✅       | "day"       |
| WEEK  | str  | ✅       | "week"      |
| YEAR  | str  | ✅       | "year"      |

# PlanProduct

The ID of the product that this plan is for, and fields describing this product in the plan.

# TiersMode

Determines the mode for calculating the total tiered charge. One of the following values: _ graduated - The total cost at each price tier is calculated separately, then all tier charges are added together. _ volume - The total cost is calculated as the number of items times the applicable tier price. Relevant when billing_scheme is set to tiered

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| GRADUATED | str  | ✅       | "graduated" |
| VOLUME    | str  | ✅       | "volume"    |

# UsageType

Determines whether the customer is billed when the service is not actually used. Relevant when billing_scheme is set to per_unit. One of the following: _ metered - The customer is billed only for actual usage. You must also set aggregate_usage. _ licensed - The customer is billed even if the service is not used. This is the default.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| METERED  | str  | ✅       | "metered"   |
| LICENSED | str  | ✅       | "licensed"  |
