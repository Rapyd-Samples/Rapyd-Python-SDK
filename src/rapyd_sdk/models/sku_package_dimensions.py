from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class SkuPackageDimensions(BaseModel):
    """Physical attributes of the SKU item. Contains the following fields, height length weight width These fields are represented as numbers, but it is the responsibility of the merchant to define and interpret the relevant units of length and weight.

    :param height: NA, defaults to None
    :type height: float, optional
    :param length: NA, defaults to None
    :type length: float, optional
    :param weight: NA, defaults to None
    :type weight: float, optional
    :param width: NA, defaults to None
    :type width: float, optional
    """

    def __init__(
        self,
        height: float = None,
        length: float = None,
        weight: float = None,
        width: float = None,
    ):
        """Physical attributes of the SKU item. Contains the following fields, height length weight width These fields are represented as numbers, but it is the responsibility of the merchant to define and interpret the relevant units of length and weight.

        :param height: NA, defaults to None
        :type height: float, optional
        :param length: NA, defaults to None
        :type length: float, optional
        :param weight: NA, defaults to None
        :type weight: float, optional
        :param width: NA, defaults to None
        :type width: float, optional
        """
        self.height = self._define_number("height", height, nullable=True)
        self.length = self._define_number("length", length, nullable=True)
        self.weight = self._define_number("weight", weight, nullable=True)
        self.width = self._define_number("width", width, nullable=True)
