from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inline_response_200_40_data import InlineResponse200_40Data
from .status_1 import Status1


@JsonMap({})
class InlineResponse200_42(BaseModel):
    """InlineResponse200_42

    :param data: data, defaults to None
    :type data: InlineResponse200_40Data, optional
    :param status: status, defaults to None
    :type status: Status1, optional
    """

    def __init__(self, data: InlineResponse200_40Data = None, status: Status1 = None):
        """InlineResponse200_42

        :param data: data, defaults to None
        :type data: InlineResponse200_40Data, optional
        :param status: status, defaults to None
        :type status: Status1, optional
        """
        self.data = self._define_object(data, InlineResponse200_40Data)
        self.status = self._define_object(status, Status1)
