from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .ewallet import Ewallet
from .status import Status


@JsonMap({})
class InlineResponse200_22(BaseModel):
    """InlineResponse200_22

    :param data: data, defaults to None
    :type data: Ewallet, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Ewallet = None, status: Status = None):
        """InlineResponse200_22

        :param data: data, defaults to None
        :type data: Ewallet, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Ewallet)
        self.status = self._define_object(status, Status)
