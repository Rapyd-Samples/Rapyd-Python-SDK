from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class V1productsPackageDimensions(BaseModel):
    """Describes the physical size and weight of the product. Relevant when type is goods.

    :param height: height, defaults to None
    :type height: float, optional
    :param length: length, defaults to None
    :type length: float, optional
    :param weight: weight, defaults to None
    :type weight: float, optional
    :param width: width, defaults to None
    :type width: float, optional
    """

    def __init__(
        self,
        height: float = None,
        length: float = None,
        weight: float = None,
        width: float = None,
    ):
        """Describes the physical size and weight of the product. Relevant when type is goods.

        :param height: height, defaults to None
        :type height: float, optional
        :param length: length, defaults to None
        :type length: float, optional
        :param weight: weight, defaults to None
        :type weight: float, optional
        :param width: width, defaults to None
        :type width: float, optional
        """
        self.height = self._define_number("height", height, nullable=True)
        self.length = self._define_number("length", length, nullable=True)
        self.weight = self._define_number("weight", weight, nullable=True)
        self.width = self._define_number("width", width, nullable=True)
