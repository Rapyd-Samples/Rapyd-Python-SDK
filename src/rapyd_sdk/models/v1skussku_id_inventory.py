from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class V1skusskuIdInventoryType(Enum):
    """An enumeration representing different categories.

    :cvar FINITE: "finite"
    :vartype FINITE: str
    :cvar INFINITE: "infinite"
    :vartype INFINITE: str
    :cvar BUCKET: "bucket"
    :vartype BUCKET: str
    """

    FINITE = "finite"
    INFINITE = "infinite"
    BUCKET = "bucket"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, V1skusskuIdInventoryType._member_map_.values())
        )


class Value(Enum):
    """An enumeration representing different categories.

    :cvar INSTOCK: "in_stock"
    :vartype INSTOCK: str
    :cvar LIMITED: "limited"
    :vartype LIMITED: str
    :cvar OUTOFSTOCK: "out_of_stock"
    :vartype OUTOFSTOCK: str
    """

    INSTOCK = "in_stock"
    LIMITED = "limited"
    OUTOFSTOCK = "out_of_stock"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Value._member_map_.values()))


@JsonMap({"type_": "type"})
class V1skusskuIdInventory(BaseModel):
    """inventory object {quantity, type, value}

    :param type_: type_, defaults to None
    :type type_: V1skusskuIdInventoryType, optional
    :param quantity: quantity, defaults to None
    :type quantity: int, optional
    :param value: value, defaults to None
    :type value: Value, optional
    """

    def __init__(
        self,
        type_: V1skusskuIdInventoryType = None,
        quantity: int = None,
        value: Value = None,
    ):
        """inventory object {quantity, type, value}

        :param type_: type_, defaults to None
        :type type_: V1skusskuIdInventoryType, optional
        :param quantity: quantity, defaults to None
        :type quantity: int, optional
        :param value: value, defaults to None
        :type value: Value, optional
        """
        self.type_ = (
            self._enum_matching(type_, V1skusskuIdInventoryType.list(), "type_")
            if type_
            else None
        )
        self.quantity = self._define_number("quantity", quantity, nullable=True)
        self.value = (
            self._enum_matching(value, Value.list(), "value") if value else None
        )
