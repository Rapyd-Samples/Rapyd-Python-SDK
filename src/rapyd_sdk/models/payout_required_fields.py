from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class PayoutRequiredFieldsType(Enum):
    """An enumeration representing different categories.

    :cvar BOOLEAN: "boolean"
    :vartype BOOLEAN: str
    :cvar NUMBER: "number"
    :vartype NUMBER: str
    :cvar STRING: "string"
    :vartype STRING: str
    """

    BOOLEAN = "boolean"
    NUMBER = "number"
    STRING = "string"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, PayoutRequiredFieldsType._member_map_.values())
        )


@JsonMap({"type_": "type"})
class PayoutRequiredFields(BaseModel):
    """PayoutRequiredFields

    :param allowed_values: List out the allowed values, defaults to None
    :type allowed_values: str, optional
    :param description: Description of the field, defaults to None
    :type description: str, optional
    :param is_required: Indicates whether the field is always required for using the payout method, defaults to None
    :type is_required: bool, optional
    :param name: Name of the field, defaults to None
    :type name: str, optional
    :param regex: A regular expression that defines the format when type is string. Note: Rapyd uses a unique variant of the regex standard. See note in           "https://docs.rapyd.net/en/get-payment-method-required-fields.html" , defaults to None
    :type regex: str, optional
    :param transfer_type: Indicates transfer type of the payout, defaults to None
    :type transfer_type: str, optional
    :param type_: Indicates datatype of the field, defaults to None
    :type type_: PayoutRequiredFieldsType, optional
    """

    def __init__(
        self,
        allowed_values: str = None,
        description: str = None,
        is_required: bool = None,
        name: str = None,
        regex: str = None,
        transfer_type: str = None,
        type_: PayoutRequiredFieldsType = None,
    ):
        """PayoutRequiredFields

        :param allowed_values: List out the allowed values, defaults to None
        :type allowed_values: str, optional
        :param description: Description of the field, defaults to None
        :type description: str, optional
        :param is_required: Indicates whether the field is always required for using the payout method, defaults to None
        :type is_required: bool, optional
        :param name: Name of the field, defaults to None
        :type name: str, optional
        :param regex: A regular expression that defines the format when type is string. Note: Rapyd uses a unique variant of the regex standard. See note in           "https://docs.rapyd.net/en/get-payment-method-required-fields.html" , defaults to None
        :type regex: str, optional
        :param transfer_type: Indicates transfer type of the payout, defaults to None
        :type transfer_type: str, optional
        :param type_: Indicates datatype of the field, defaults to None
        :type type_: PayoutRequiredFieldsType, optional
        """
        self.allowed_values = self._define_str(
            "allowed_values", allowed_values, nullable=True
        )
        self.description = self._define_str("description", description, nullable=True)
        self.is_required = is_required
        self.name = self._define_str("name", name, nullable=True)
        self.regex = self._define_str("regex", regex, nullable=True)
        self.transfer_type = self._define_str(
            "transfer_type", transfer_type, nullable=True
        )
        self.type_ = (
            self._enum_matching(type_, PayoutRequiredFieldsType.list(), "type_")
            if type_
            else None
        )
