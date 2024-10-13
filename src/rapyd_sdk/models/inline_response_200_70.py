from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .plan import Plan


@JsonMap({})
class InlineResponse200_70(BaseModel):
    """InlineResponse200_70

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: Plan, optional
    """

    def __init__(self, status: Status1 = None, data: Plan = None):
        """InlineResponse200_70

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: Plan, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, Plan)
