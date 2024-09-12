from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class V1skusskuIdPackageDimensions(BaseModel):
    """Physical attributes of the SKU item. Object containing the following fields - height, length, weight, width

    :param length: length, defaults to None
    :type length: float, optional
    :param height: height, defaults to None
    :type height: float, optional
    :param weight: weight, defaults to None
    :type weight: float, optional
    :param width: width, defaults to None
    :type width: float, optional
    """

    def __init__(
        self,
        length: float = None,
        height: float = None,
        weight: float = None,
        width: float = None,
    ):
        """Physical attributes of the SKU item. Object containing the following fields - height, length, weight, width

        :param length: length, defaults to None
        :type length: float, optional
        :param height: height, defaults to None
        :type height: float, optional
        :param weight: weight, defaults to None
        :type weight: float, optional
        :param width: width, defaults to None
        :type width: float, optional
        """
        self.length = self._define_number("length", length, nullable=True)
        self.height = self._define_number("height", height, nullable=True)
        self.weight = self._define_number("weight", weight, nullable=True)
        self.width = self._define_number("width", width, nullable=True)
