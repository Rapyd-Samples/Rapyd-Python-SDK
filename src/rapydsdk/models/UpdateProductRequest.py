from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class PackageDimensions3(BaseModel):
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


@JsonMap({})
class UpdateProductRequest(BaseModel):
    def __init__(
        self,
        name: str,
        active: bool = None,
        attributes: List[str] = None,
        metadata: dict = None,
        package_dimensions: PackageDimensions3 = None,
        statement_descriptor: str = None,
        unit_label: str = None,
    ):
        self.active = active
        self.attributes = attributes
        self.metadata = metadata
        self.name = name
        self.package_dimensions = self._define_object(
            package_dimensions, PackageDimensions3
        )
        self.statement_descriptor = statement_descriptor
        self.unit_label = unit_label
