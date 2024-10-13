# FieldConditions

**Properties**

| Name            | Type                          | Required | Description                                                                                                                                 |
| :-------------- | :---------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| description     | str                           | ❌       | Description of the condition.                                                                                                               |
| element_name    | str                           | ❌       | The name of a field, including the path. The field is the first operand of the condition.                                                   |
| operator        | str                           | ❌       | A symbol representing the operator of the condition. String starting with $. The operator determines the relationship between the operands. |
| threshold_value | FieldConditionsThresholdValue | ❌       | des One or more possible values of the element_name field. The second operand of the condition.                                             |

# FieldConditionsThresholdValue

des One or more possible values of the element_name field. The second operand of the condition.
