# SubscriptionItem

**Properties**

| Name            | Type  | Required | Description                                                                                                                                                                 |
| :-------------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| created         | float | ❌       | The time the subscription item was created, in Unix time. Response only.                                                                                                    |
| id\_            | str   | ❌       | ID of the Subscription Item object. String starting with subi\_.                                                                                                            |
| metadata        | dict  | ❌       | A JSON object defined by the client.                                                                                                                                        |
| plan            | Plan  | ❌       |                                                                                                                                                                             |
| quantity        | float | ❌       | The number of units of the service defined in the plan. Integer. This number can be updated during the billing cycle using Update Subscription or Update Subscription Item. |
| subscription_id | str   | ❌       | ID of the subscription that this item belongs to. String starting with sub\_.                                                                                               |
