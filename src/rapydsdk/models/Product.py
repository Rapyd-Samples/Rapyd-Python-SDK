from __future__ import annotations
from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Sku import Sku


@JsonMap({})
class PackageDimensions(BaseModel):
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


class Type(Enum):
    GOODS = "goods"
    SERVICES = "services"
    SERVICE = "service"

    def list():
        return list(map(lambda x: x.value, Type._member_map_.values()))


@JsonMap({"type_": "type"})
class Product(BaseModel):
    def __init__(
        self,
        active: bool = None,
        attributes: List[str] = None,
        created_at: float = None,
        description: str = None,
        id: str = None,
        images: List[str] = None,
        metadata: dict = None,
        name: str = None,
        package_dimensions: PackageDimensions = None,
        shippable: bool = None,
        skus: List[Sku] = None,
        statement_descriptor: str = None,
        type_: Type = None,
        unit_label: str = None,
        updated_at: float = None,
    ):
        self.active = active
        self.attributes = attributes
        self.created_at = created_at
        self.description = description
        self.id = id
        self.images = images
        self.metadata = metadata
        self.name = name
        self.package_dimensions = self._define_object(
            package_dimensions, PackageDimensions
        )
        self.shippable = shippable
        self.skus = self._define_list(skus, Sku)
        self.statement_descriptor = statement_descriptor
        self.type_ = self._enum_matching(type_, Type.list(), "type_") if type_ else None
        self.unit_label = unit_label
        self.updated_at = updated_at
