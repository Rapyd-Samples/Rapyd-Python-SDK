# V1SubscriptionItemsBody

**Properties**

| Name           | Type  | Required | Description                                                                                                                         |
| :------------- | :---- | :------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| plan           | str   | ✅       | ID of the plan assigned to this subscription item. Cannot be a plan that is already part of the subscription.                       |
| subscription   | str   | ✅       | ID of the subscription that this item belongs to. String starting with **sub\_**.                                                   |
| metadata       | dict  | ❌       | A JSON object defined by the client.                                                                                                |
| prorate        | bool  | ❌       | Determines whether the charge is prorated when a subscription item is switched from one subscription to another in a billing cycle. |
| proration_date | float | ❌       | Indicates the date in the middle of the billing period that is the start of the prorated charges.                                   |
| quantity       | float | ❌       | The number of units of the service defined in the plan.                                                                             |
