from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .v1products_package_dimensions import V1productsPackageDimensions


class V1ProductsBodyType(Enum):
    """An enumeration representing different categories.

    :cvar SERVICES: "services"
    :vartype SERVICES: str
    :cvar GOODS: "goods"
    :vartype GOODS: str
    """

    SERVICES = "services"
    GOODS = "goods"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, V1ProductsBodyType._member_map_.values()))


@JsonMap({"id_": "id", "type_": "type"})
class V1ProductsBody(BaseModel):
    """V1ProductsBody

    :param active: Indicates whether the product is currently available for purchase. Default is true., defaults to None
    :type active: bool, optional
    :param attributes: Array of up to 5 alphanumeric strings defined by the merchant. Each string defines the key in a key-value pair in the 'attributes' object in the corresponding 'sku' objects., defaults to None
    :type attributes: List[str], optional
    :param description: Full text description of the product., defaults to None
    :type description: str, optional
    :param id_: Unique string for identification of the product. Legal input includes all the English alphanumeric characters and the underscore (_) character. If the merchant does not define an ID, Rapyd generates it with a string that starts with product_, defaults to None
    :type id_: str, optional
    :param images: An array of images. Each image is a string in Base64 encoding., defaults to None
    :type images: List[str], optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param name: The name of the product or service that is displayed to the customer.
    :type name: str
    :param package_dimensions: Describes the physical size and weight of the product. Relevant when type is goods., defaults to None
    :type package_dimensions: V1productsPackageDimensions, optional
    :param shippable: Indicates whether the product is physically shipped to the customer. Relevant when type is goods. Default is false., defaults to None
    :type shippable: bool, optional
    :param statement_descriptor: A text description that appears in the customer's invoice. Limited to 22 characters. Relevant when type is service., defaults to None
    :type statement_descriptor: str, optional
    :param type_: One of the following - services, goods
    :type type_: V1ProductsBodyType
    :param unit_label: A label that represents units of this product, such as seats, on customers’ invoices. Relevant when type is service., defaults to None
    :type unit_label: str, optional
    """

    def __init__(
        self,
        name: str,
        type_: V1ProductsBodyType,
        active: bool = None,
        attributes: List[str] = None,
        description: str = None,
        id_: str = None,
        images: List[str] = None,
        metadata: dict = None,
        package_dimensions: V1productsPackageDimensions = None,
        shippable: bool = None,
        statement_descriptor: str = None,
        unit_label: str = None,
    ):
        """V1ProductsBody

        :param active: Indicates whether the product is currently available for purchase. Default is true., defaults to None
        :type active: bool, optional
        :param attributes: Array of up to 5 alphanumeric strings defined by the merchant. Each string defines the key in a key-value pair in the 'attributes' object in the corresponding 'sku' objects., defaults to None
        :type attributes: List[str], optional
        :param description: Full text description of the product., defaults to None
        :type description: str, optional
        :param id_: Unique string for identification of the product. Legal input includes all the English alphanumeric characters and the underscore (_) character. If the merchant does not define an ID, Rapyd generates it with a string that starts with product_, defaults to None
        :type id_: str, optional
        :param images: An array of images. Each image is a string in Base64 encoding., defaults to None
        :type images: List[str], optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param name: The name of the product or service that is displayed to the customer.
        :type name: str
        :param package_dimensions: Describes the physical size and weight of the product. Relevant when type is goods., defaults to None
        :type package_dimensions: V1productsPackageDimensions, optional
        :param shippable: Indicates whether the product is physically shipped to the customer. Relevant when type is goods. Default is false., defaults to None
        :type shippable: bool, optional
        :param statement_descriptor: A text description that appears in the customer's invoice. Limited to 22 characters. Relevant when type is service., defaults to None
        :type statement_descriptor: str, optional
        :param type_: One of the following - services, goods
        :type type_: V1ProductsBodyType
        :param unit_label: A label that represents units of this product, such as seats, on customers’ invoices. Relevant when type is service., defaults to None
        :type unit_label: str, optional
        """
        self.active = active
        self.attributes = attributes
        self.description = self._define_str("description", description, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.images = images
        self.metadata = metadata
        self.name = name
        self.package_dimensions = self._define_object(
            package_dimensions, V1productsPackageDimensions
        )
        self.shippable = shippable
        self.statement_descriptor = self._define_str(
            "statement_descriptor", statement_descriptor, nullable=True
        )
        self.type_ = self._enum_matching(type_, V1ProductsBodyType.list(), "type_")
        self.unit_label = self._define_str("unit_label", unit_label, nullable=True)
