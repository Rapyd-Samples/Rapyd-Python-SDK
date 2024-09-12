# SubscriptionItemsSubscriptionItemIdBody

**Properties**

| Name           | Type    | Required | Description                                                                                                                         |
| :------------- | :------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| metadata       | `dict`  | ❌       | A JSON object defined by the client.                                                                                                |
| prorate        | `bool`  | ❌       | Determines whether the charge is prorated when a subscription item is switched from one subscription to another in a billing cycle. |
| proration_date | `float` | ❌       | Indicates the date in the middle of the billing period that is the start of the prorated charges.                                   |
| quantity       | `float` | ❌       | The number of units of the service defined in the plan.                                                                             |
