from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .field_conditions import FieldConditions


class FieldType(Enum):
    """An enumeration representing different categories.

    :cvar BOOLEAN: "boolean"
    :vartype BOOLEAN: str
    :cvar NUMBER: "number"
    :vartype NUMBER: str
    :cvar STRING: "string"
    :vartype STRING: str
    :cvar OBJECT: "object"
    :vartype OBJECT: str
    """

    BOOLEAN = "boolean"
    NUMBER = "number"
    STRING = "string"
    OBJECT = "object"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, FieldType._member_map_.values()))


@JsonMap({"type_": "type"})
class Field(BaseModel):
    """Field Object

    :param code: Three-letter alphabetic ISO 4217 code for the official currency used in the country., defaults to None
    :type code: str, optional
    :param is_required: Whether the field is always required for using the payment method, defaults to None
    :type is_required: bool, optional
    :param is_updatable: Indicates whether the field can be updated with Update Payment Method, defaults to None
    :type is_updatable: bool, optional
    :param instructions: instructions, defaults to None
    :type instructions: str, optional
    :param name: Name of the currency in English., defaults to None
    :type name: str, optional
    :param numeric_code: Three-letter ISO numeric 4217 code for the currency., defaults to None
    :type numeric_code: str, optional
    :param required_fields: required_fields, defaults to None
    :type required_fields: List[Field], optional
    :param type_: type_, defaults to None
    :type type_: FieldType, optional
    :param regex: A regular expression that defines the format when type is string., defaults to None
    :type regex: str, optional
    :param conditions: Defines specific conditions when a field is required for a payment method. When the conditions defined by conditions are met, the field is required even though the value of is_required is false., defaults to None
    :type conditions: List[FieldConditions], optional
    :param description: Description of the field., defaults to None
    :type description: str, optional
    """

    def __init__(
        self,
        code: str = None,
        is_required: bool = None,
        is_updatable: bool = None,
        instructions: str = None,
        name: str = None,
        numeric_code: str = None,
        required_fields: List[Field] = None,
        type_: FieldType = None,
        regex: str = None,
        conditions: List[FieldConditions] = None,
        description: str = None,
    ):
        """Field Object

        :param code: Three-letter alphabetic ISO 4217 code for the official currency used in the country., defaults to None
        :type code: str, optional
        :param is_required: Whether the field is always required for using the payment method, defaults to None
        :type is_required: bool, optional
        :param is_updatable: Indicates whether the field can be updated with Update Payment Method, defaults to None
        :type is_updatable: bool, optional
        :param instructions: instructions, defaults to None
        :type instructions: str, optional
        :param name: Name of the currency in English., defaults to None
        :type name: str, optional
        :param numeric_code: Three-letter ISO numeric 4217 code for the currency., defaults to None
        :type numeric_code: str, optional
        :param required_fields: required_fields, defaults to None
        :type required_fields: List[Field], optional
        :param type_: type_, defaults to None
        :type type_: FieldType, optional
        :param regex: A regular expression that defines the format when type is string., defaults to None
        :type regex: str, optional
        :param conditions: Defines specific conditions when a field is required for a payment method. When the conditions defined by conditions are met, the field is required even though the value of is_required is false., defaults to None
        :type conditions: List[FieldConditions], optional
        :param description: Description of the field., defaults to None
        :type description: str, optional
        """
        self.code = self._define_str("code", code, nullable=True)
        self.is_required = is_required
        self.is_updatable = is_updatable
        self.instructions = self._define_str(
            "instructions", instructions, nullable=True
        )
        self.name = self._define_str("name", name, nullable=True)
        self.numeric_code = self._define_str(
            "numeric_code", numeric_code, nullable=True
        )
        self.required_fields = self._define_list(required_fields, Field)
        self.type_ = (
            self._enum_matching(type_, FieldType.list(), "type_") if type_ else None
        )
        self.regex = self._define_str("regex", regex, nullable=True)
        self.conditions = self._define_list(conditions, FieldConditions)
        self.description = self._define_str("description", description, nullable=True)
