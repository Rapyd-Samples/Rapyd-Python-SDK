from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel


class FieldConditionsThresholdValueGuard(OneOfBaseModel):
    class_list = {"str": str, "List[str]": List[str]}


FieldConditionsThresholdValue = Union[str, List[str]]


@JsonMap({})
class FieldConditions(BaseModel):
    """FieldConditions

    :param description: Description of the condition., defaults to None
    :type description: str, optional
    :param element_name: The name of a field, including the path. The field is the first operand of the condition., defaults to None
    :type element_name: str, optional
    :param operator: A symbol representing the operator of the condition. String starting with $. The operator determines the relationship between the operands., defaults to None
    :type operator: str, optional
    :param threshold_value: des One or more possible values of the element_name field. The second operand of the condition., defaults to None
    :type threshold_value: FieldConditionsThresholdValue, optional
    """

    def __init__(
        self,
        description: str = None,
        element_name: str = None,
        operator: str = None,
        threshold_value: FieldConditionsThresholdValue = None,
    ):
        """FieldConditions

        :param description: Description of the condition., defaults to None
        :type description: str, optional
        :param element_name: The name of a field, including the path. The field is the first operand of the condition., defaults to None
        :type element_name: str, optional
        :param operator: A symbol representing the operator of the condition. String starting with $. The operator determines the relationship between the operands., defaults to None
        :type operator: str, optional
        :param threshold_value: des One or more possible values of the element_name field. The second operand of the condition., defaults to None
        :type threshold_value: FieldConditionsThresholdValue, optional
        """
        self.description = self._define_str("description", description, nullable=True)
        self.element_name = self._define_str(
            "element_name", element_name, nullable=True
        )
        self.operator = self._define_str("operator", operator, nullable=True)
        self.threshold_value = FieldConditionsThresholdValueGuard.return_one_of(
            threshold_value
        )
