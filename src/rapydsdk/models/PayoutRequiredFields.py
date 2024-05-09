from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class Type6(Enum):
    BOOLEAN = "boolean"
    NUMBER = "number"
    STRING = "string"

    def list():
        return list(map(lambda x: x.value, Type6._member_map_.values()))


@JsonMap({"type_": "type"})
class PayoutRequiredFields(BaseModel):
    def __init__(
        self,
        allowed_values: str = None,
        description: str = None,
        is_required: bool = None,
        name: str = None,
        regex: str = None,
        transfer_type: str = None,
        type_: Type6 = None,
    ):
        self.allowed_values = allowed_values
        self.description = description
        self.is_required = is_required
        self.name = name
        self.regex = regex
        self.transfer_type = transfer_type
        self.type_ = (
            self._enum_matching(type_, Type6.list(), "type_") if type_ else None
        )
