# OrderResponseStatusTransitions

Indicates the last time in Unix time that the order transitioned to one of the following statuses. A zero value for a status indicates that the order has never transitioned to it.

**Properties**

| Name      | Type  | Required | Description |
| :-------- | :---- | :------- | :---------- |
| canceled  | float | ❌       |             |
| fulfilled | float | ❌       |             |
| paid      | float | ❌       |             |
| returned  | float | ❌       |             |
| pending   | float | ❌       |             |
| partial   | float | ❌       |             |
