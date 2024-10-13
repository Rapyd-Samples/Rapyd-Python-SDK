from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel


class ConditionThresholdValueGuard(OneOfBaseModel):
    class_list = {"str": str, "int": int}


ConditionThresholdValue = Union[str, int]


@JsonMap({})
class Condition(BaseModel):
    """Condition

    :param description: Description of the condition, defaults to None
    :type description: str, optional
    :param element_name: The name of a field, including the path. The field is the first operand of the condition. The path starts with one of the following - * payment - The field is a Create Payment body parameter. Not relevant to the payment_method and payment_method_options objects. * payment.payment_method_type - The field appears in the current Get Payment Method Required Fields response under fields or payment_method_options. * organization - The field relates to your organization, such as your merchant type category. Your organization specifies the field when activating your account. See Activating Your Account (KYB), defaults to None
    :type element_name: str, optional
    :param operator: A symbol representing the operator of the condition. String starting with $. The operator determines the relationship between the operands See documentation - "https://docs.rapyd.net/en/payment-method-type.html", defaults to None
    :type operator: str, optional
    :param threshold_value: One or more possible values of the element_name field. The second operand of the condition "https://docs.rapyd.net/en/payment-method-type.html", defaults to None
    :type threshold_value: ConditionThresholdValue, optional
    """

    def __init__(
        self,
        description: str = None,
        element_name: str = None,
        operator: str = None,
        threshold_value: ConditionThresholdValue = None,
    ):
        """Condition

        :param description: Description of the condition, defaults to None
        :type description: str, optional
        :param element_name: The name of a field, including the path. The field is the first operand of the condition. The path starts with one of the following - * payment - The field is a Create Payment body parameter. Not relevant to the payment_method and payment_method_options objects. * payment.payment_method_type - The field appears in the current Get Payment Method Required Fields response under fields or payment_method_options. * organization - The field relates to your organization, such as your merchant type category. Your organization specifies the field when activating your account. See Activating Your Account (KYB), defaults to None
        :type element_name: str, optional
        :param operator: A symbol representing the operator of the condition. String starting with $. The operator determines the relationship between the operands See documentation - "https://docs.rapyd.net/en/payment-method-type.html", defaults to None
        :type operator: str, optional
        :param threshold_value: One or more possible values of the element_name field. The second operand of the condition "https://docs.rapyd.net/en/payment-method-type.html", defaults to None
        :type threshold_value: ConditionThresholdValue, optional
        """
        self.description = self._define_str("description", description, nullable=True)
        self.element_name = self._define_str(
            "element_name", element_name, nullable=True
        )
        self.operator = self._define_str("operator", operator, nullable=True)
        self.threshold_value = ConditionThresholdValueGuard.return_one_of(
            threshold_value
        )
