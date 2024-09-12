from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .sku import Sku


@JsonMap({})
class InlineResponse200_72(BaseModel):
    """InlineResponse200_72

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: data, defaults to None
    :type data: Sku, optional
    """

    def __init__(self, status: Status = None, data: Sku = None):
        """InlineResponse200_72

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: data, defaults to None
        :type data: Sku, optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, Sku)
