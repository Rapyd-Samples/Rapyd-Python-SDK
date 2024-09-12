from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inline_response_200_65_data import InlineResponse200_65Data
from .status import Status


@JsonMap({})
class InlineResponse200_65(BaseModel):
    """InlineResponse200_65

    :param data: data, defaults to None
    :type data: InlineResponse200_65Data, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: InlineResponse200_65Data = None, status: Status = None):
        """InlineResponse200_65

        :param data: data, defaults to None
        :type data: InlineResponse200_65Data, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, InlineResponse200_65Data)
        self.status = self._define_object(status, Status)
