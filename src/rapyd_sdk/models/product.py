from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .product_package_dimensions import ProductPackageDimensions
from .sku import Sku


class ProductType(Enum):
    """An enumeration representing different categories.

    :cvar GOODS: "goods"
    :vartype GOODS: str
    :cvar SERVICES: "services"
    :vartype SERVICES: str
    """

    GOODS = "goods"
    SERVICES = "services"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ProductType._member_map_.values()))


@JsonMap({"id_": "id", "type_": "type"})
class Product(BaseModel):
    """Product

    :param active: Indicates whether the product is currently available for purchase., defaults to None
    :type active: bool, optional
    :param attributes: Up to 5 unique alphanumeric strings defined by the merchant. Cannot contain spaces. For example: [ > "size", > "color"] Each string defines the key in a key-value pair in the 'attributes' object in the corresponding 'sku' objects., defaults to None
    :type attributes: List[str], optional
    :param created_at: Time of creation of this product, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param description: Full text description of the product., defaults to None
    :type description: str, optional
    :param id_: Unique string for identification of the product. Legal input includes alphanumeric characters and the underscore () character. If the merchant does not define an ID, Rapyd generates it with a string that starts with **product**., defaults to None
    :type id_: str, optional
    :param images: Images associated with the product., defaults to None
    :type images: List[str], optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param name: The name of the product or service that appears in the line items in invoices., defaults to None
    :type name: str, optional
    :param package_dimensions: Describes the physical size and weight of the product. Contains the following fields:  * height  * length  * weight  * width  These fields are represented as numbers, but it is the responsibility of the merchant to define and interpret the relevant units of length and weight. , defaults to None
    :type package_dimensions: ProductPackageDimensions, optional
    :param shippable: Indicates whether the product can be shipped., defaults to None
    :type shippable: bool, optional
    :param skus: skus, defaults to None
    :type skus: List[Sku], optional
    :param statement_descriptor: Description that is suitable for a customer's statement. Limited to 22 characters. Relevant when type is service. Must be null when type is goods., defaults to None
    :type statement_descriptor: str, optional
    :param type_: One of the following:  * services - Relevant to subscriptions and plans.  * goods - Relevant to orders and SKUs. , defaults to None
    :type type_: ProductType, optional
    :param unit_label: Determines what one unit of this product is called on customersâ€™ receipts and invoices, such as minutes, viewings, kilometers or packages. Relevant when type is service. Must be null when type is goods., defaults to None
    :type unit_label: str, optional
    :param updated_at: Time that this product was last updated, in Unix time. Response only., defaults to None
    :type updated_at: float, optional
    """

    def __init__(
        self,
        active: bool = None,
        attributes: List[str] = None,
        created_at: float = None,
        description: str = None,
        id_: str = None,
        images: List[str] = None,
        metadata: dict = None,
        name: str = None,
        package_dimensions: ProductPackageDimensions = None,
        shippable: bool = None,
        skus: List[Sku] = None,
        statement_descriptor: str = None,
        type_: ProductType = None,
        unit_label: str = None,
        updated_at: float = None,
    ):
        """Product

        :param active: Indicates whether the product is currently available for purchase., defaults to None
        :type active: bool, optional
        :param attributes: Up to 5 unique alphanumeric strings defined by the merchant. Cannot contain spaces. For example: [ > "size", > "color"] Each string defines the key in a key-value pair in the 'attributes' object in the corresponding 'sku' objects., defaults to None
        :type attributes: List[str], optional
        :param created_at: Time of creation of this product, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param description: Full text description of the product., defaults to None
        :type description: str, optional
        :param id_: Unique string for identification of the product. Legal input includes alphanumeric characters and the underscore () character. If the merchant does not define an ID, Rapyd generates it with a string that starts with **product**., defaults to None
        :type id_: str, optional
        :param images: Images associated with the product., defaults to None
        :type images: List[str], optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param name: The name of the product or service that appears in the line items in invoices., defaults to None
        :type name: str, optional
        :param package_dimensions: Describes the physical size and weight of the product. Contains the following fields:  * height  * length  * weight  * width  These fields are represented as numbers, but it is the responsibility of the merchant to define and interpret the relevant units of length and weight. , defaults to None
        :type package_dimensions: ProductPackageDimensions, optional
        :param shippable: Indicates whether the product can be shipped., defaults to None
        :type shippable: bool, optional
        :param skus: skus, defaults to None
        :type skus: List[Sku], optional
        :param statement_descriptor: Description that is suitable for a customer's statement. Limited to 22 characters. Relevant when type is service. Must be null when type is goods., defaults to None
        :type statement_descriptor: str, optional
        :param type_: One of the following:  * services - Relevant to subscriptions and plans.  * goods - Relevant to orders and SKUs. , defaults to None
        :type type_: ProductType, optional
        :param unit_label: Determines what one unit of this product is called on customersâ€™ receipts and invoices, such as minutes, viewings, kilometers or packages. Relevant when type is service. Must be null when type is goods., defaults to None
        :type unit_label: str, optional
        :param updated_at: Time that this product was last updated, in Unix time. Response only., defaults to None
        :type updated_at: float, optional
        """
        self.active = active
        self.attributes = attributes
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.description = self._define_str("description", description, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.images = images
        self.metadata = metadata
        self.name = self._define_str("name", name, nullable=True)
        self.package_dimensions = self._define_object(
            package_dimensions, ProductPackageDimensions
        )
        self.shippable = shippable
        self.skus = self._define_list(skus, Sku)
        self.statement_descriptor = self._define_str(
            "statement_descriptor", statement_descriptor, nullable=True
        )
        self.type_ = (
            self._enum_matching(type_, ProductType.list(), "type_") if type_ else None
        )
        self.unit_label = self._define_str("unit_label", unit_label, nullable=True)
        self.updated_at = self._define_number("updated_at", updated_at, nullable=True)
