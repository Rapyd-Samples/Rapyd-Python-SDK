from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .v1products_package_dimensions import V1productsPackageDimensions


@JsonMap({})
class ProductsProductsIdBody(BaseModel):
    """ProductsProductsIdBody

    :param active: Indicates whether the product is currently available for purchase. Default is true., defaults to None
    :type active: bool, optional
    :param attributes: Array of up to 5 alphanumeric strings defined by the merchant. Each string defines the key in a key-value pair in the 'attributes' object in the corresponding 'sku' objects., defaults to None
    :type attributes: List[str], optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param name: The name of the product or service that is displayed to the customer.
    :type name: str
    :param package_dimensions: Describes the physical size and weight of the product. Relevant when type is goods., defaults to None
    :type package_dimensions: V1productsPackageDimensions, optional
    :param statement_descriptor: A text description that appears in the customer's invoice. Limited to 22 characters. Relevant when type is service., defaults to None
    :type statement_descriptor: str, optional
    :param unit_label: A label that represents units of this product, such as seats, on customersâ€™, defaults to None
    :type unit_label: str, optional
    """

    def __init__(
        self,
        name: str,
        active: bool = None,
        attributes: List[str] = None,
        metadata: dict = None,
        package_dimensions: V1productsPackageDimensions = None,
        statement_descriptor: str = None,
        unit_label: str = None,
    ):
        """ProductsProductsIdBody

        :param active: Indicates whether the product is currently available for purchase. Default is true., defaults to None
        :type active: bool, optional
        :param attributes: Array of up to 5 alphanumeric strings defined by the merchant. Each string defines the key in a key-value pair in the 'attributes' object in the corresponding 'sku' objects., defaults to None
        :type attributes: List[str], optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param name: The name of the product or service that is displayed to the customer.
        :type name: str
        :param package_dimensions: Describes the physical size and weight of the product. Relevant when type is goods., defaults to None
        :type package_dimensions: V1productsPackageDimensions, optional
        :param statement_descriptor: A text description that appears in the customer's invoice. Limited to 22 characters. Relevant when type is service., defaults to None
        :type statement_descriptor: str, optional
        :param unit_label: A label that represents units of this product, such as seats, on customersâ€™, defaults to None
        :type unit_label: str, optional
        """
        self.active = active
        self.attributes = attributes
        self.metadata = metadata
        self.name = name
        self.package_dimensions = self._define_object(
            package_dimensions, V1productsPackageDimensions
        )
        self.statement_descriptor = self._define_str(
            "statement_descriptor", statement_descriptor, nullable=True
        )
        self.unit_label = self._define_str("unit_label", unit_label, nullable=True)
