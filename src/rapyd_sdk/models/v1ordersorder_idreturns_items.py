from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class V1ordersorderIdreturnsItemsType(Enum):
    """An enumeration representing different categories.

    :cvar SKU: "sku"
    :vartype SKU: str
    :cvar SHIPPING: "shipping"
    :vartype SHIPPING: str
    :cvar TAX: "tax"
    :vartype TAX: str
    """

    SKU = "sku"
    SHIPPING = "shipping"
    TAX = "tax"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, V1ordersorderIdreturnsItemsType._member_map_.values()
            )
        )


@JsonMap({"type_": "type"})
class V1ordersorderIdreturnsItems(BaseModel):
    """V1ordersorderIdreturnsItems

    :param description: description, defaults to None
    :type description: str, optional
    :param parent: parent, defaults to None
    :type parent: str, optional
    :param type_: type_, defaults to None
    :type type_: V1ordersorderIdreturnsItemsType, optional
    :param quantity: quantity, defaults to None
    :type quantity: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param amount: amount, defaults to None
    :type amount: float, optional
    :param order_id: order_id, defaults to None
    :type order_id: str, optional
    """

    def __init__(
        self,
        description: str = None,
        parent: str = None,
        type_: V1ordersorderIdreturnsItemsType = None,
        quantity: float = None,
        currency: str = None,
        amount: float = None,
        order_id: str = None,
    ):
        """V1ordersorderIdreturnsItems

        :param description: description, defaults to None
        :type description: str, optional
        :param parent: parent, defaults to None
        :type parent: str, optional
        :param type_: type_, defaults to None
        :type type_: V1ordersorderIdreturnsItemsType, optional
        :param quantity: quantity, defaults to None
        :type quantity: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param amount: amount, defaults to None
        :type amount: float, optional
        :param order_id: order_id, defaults to None
        :type order_id: str, optional
        """
        self.description = self._define_str("description", description, nullable=True)
        self.parent = self._define_str("parent", parent, nullable=True)
        self.type_ = (
            self._enum_matching(type_, V1ordersorderIdreturnsItemsType.list(), "type_")
            if type_
            else None
        )
        self.quantity = self._define_number("quantity", quantity, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.amount = self._define_number("amount", amount, nullable=True)
        self.order_id = self._define_str("order_id", order_id, nullable=True)
