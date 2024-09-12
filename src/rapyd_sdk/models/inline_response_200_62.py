from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .product import Product
from .status import Status


@JsonMap({})
class InlineResponse200_62(BaseModel):
    """InlineResponse200_62

    :param data: data, defaults to None
    :type data: Product, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Product = None, status: Status = None):
        """InlineResponse200_62

        :param data: data, defaults to None
        :type data: Product, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Product)
        self.status = self._define_object(status, Status)
