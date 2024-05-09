from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class PackageDimensions2(BaseModel):
    def __init__(
        self,
        height: float = None,
        length: float = None,
        weight: float = None,
        width: float = None,
    ):
        self.height = height
        self.length = length
        self.weight = weight
        self.width = width


class Type7(Enum):
    SERVICES = "services"
    GOODS = "goods"

    def list():
        return list(map(lambda x: x.value, Type7._member_map_.values()))


@JsonMap({"type_": "type"})
class CreateProductRequest(BaseModel):
    def __init__(
        self,
        name: str,
        type_: Type7,
        active: bool = None,
        attributes: List[str] = None,
        description: str = None,
        id: str = None,
        images: List[str] = None,
        metadata: dict = None,
        package_dimensions: PackageDimensions2 = None,
        shippable: bool = None,
        statement_descriptor: str = None,
        unit_label: str = None,
    ):
        self.active = active
        self.attributes = attributes
        self.description = description
        self.id = id
        self.images = images
        self.metadata = metadata
        self.name = name
        self.package_dimensions = self._define_object(
            package_dimensions, PackageDimensions2
        )
        self.shippable = shippable
        self.statement_descriptor = statement_descriptor
        self.type_ = self._enum_matching(type_, Type7.list(), "type_")
        self.unit_label = unit_label
