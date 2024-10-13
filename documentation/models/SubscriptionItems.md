# SubscriptionItems

**Properties**

| Name        | Type                   | Required | Description                                                             |
| :---------- | :--------------------- | :------- | :---------------------------------------------------------------------- |
| data        | List[SubscriptionItem] | ❌       | A list of up to three subscription items.                               |
| has_more    | bool                   | ❌       | Indicates whether there are more than three items in this subscription. |
| total_count | float                  | ❌       | Total number of items in this subscription.                             |
| url         | str                    | ❌       | URL for requesting all of the items in this subscription.               |
