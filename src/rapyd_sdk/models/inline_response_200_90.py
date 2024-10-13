from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inline_response_200_90_data import InlineResponse200_90Data
from .status_1 import Status1


@JsonMap({})
class InlineResponse200_90(BaseModel):
    """InlineResponse200_90

    :param data: data, defaults to None
    :type data: InlineResponse200_90Data, optional
    :param status: status, defaults to None
    :type status: Status1, optional
    """

    def __init__(self, data: InlineResponse200_90Data = None, status: Status1 = None):
        """InlineResponse200_90

        :param data: data, defaults to None
        :type data: InlineResponse200_90Data, optional
        :param status: status, defaults to None
        :type status: Status1, optional
        """
        self.data = self._define_object(data, InlineResponse200_90Data)
        self.status = self._define_object(status, Status1)
