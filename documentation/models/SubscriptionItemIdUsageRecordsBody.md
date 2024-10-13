# SubscriptionItemIdUsageRecordsBody

**Properties**

| Name      | Type  | Required | Description                                                     |
| :-------- | :---- | :------- | :-------------------------------------------------------------- |
| quantity  | float | ✅       | The usage quantity for the specified date and time (timestamp). |
| timestamp | float | ✅       | Timestamp for the usage record in Unix time.                    |
| action    | str   | ❌       | Determines how the quantity is defined in the usage record.     |
| metadata  | dict  | ❌       | A JSON object defined by the client.                            |
