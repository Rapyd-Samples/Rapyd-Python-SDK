# PlanTiers

**Properties**

| Name        | Type  | Required | Description                                                                       |
| :---------- | :---- | :------- | :-------------------------------------------------------------------------------- |
| amount      | float | ❌       | The price for each item in this tier. Decimal number.                             |
| flat_amount | float | ❌       | Additional price for the entire tier. Default is 0.                               |
| up_to       | UpTo  | ❌       | The upper volume limit for this tier. Valid values: inf (infinite) or an integer. |

# UpTo

The upper volume limit for this tier. Valid values: inf (infinite) or an integer.
