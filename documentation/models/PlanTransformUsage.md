# PlanTransformUsage

Defines the transformation that is applied to the reported usage before the billed price is computed. The transformation divides the quantity by the divisor specified in divide_by, then rounds up or down according to the setting in round. Relevant when billing_scheme is set to per_unit.

**Properties**

| Name      | Type    | Required | Description                                                                                                                                           |
| :-------- | :------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| divide_by | `float` | ❌       | Indicates the divisor in the transformation calculation. Integer. Default is 1.                                                                       |
| round     | `str`   | ❌       | Indicates whether the reported number of units should be rounded up or down to the next whole quantity specified in divide_by. String. Default is up. |
