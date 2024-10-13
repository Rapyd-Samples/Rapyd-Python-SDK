from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .inline_response_200_88_data import InlineResponse200_88Data


@JsonMap({})
class InlineResponse200_88(BaseModel):
    """InlineResponse200_88

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: InlineResponse200_88Data, optional
    """

    def __init__(self, status: Status1 = None, data: InlineResponse200_88Data = None):
        """InlineResponse200_88

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: InlineResponse200_88Data, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, InlineResponse200_88Data)
