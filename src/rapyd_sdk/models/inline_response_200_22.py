from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status


@JsonMap({})
class InlineResponse200_22(BaseModel):
    """InlineResponse200_22

    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, status: Status = None):
        """InlineResponse200_22

        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.status = self._define_object(status, Status)
