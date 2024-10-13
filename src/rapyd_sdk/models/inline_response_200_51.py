from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .group_payment import GroupPayment


@JsonMap({})
class InlineResponse200_51(BaseModel):
    """InlineResponse200_51

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: Group Payment, defaults to None
    :type data: GroupPayment, optional
    """

    def __init__(self, status: Status1 = None, data: GroupPayment = None):
        """InlineResponse200_51

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: Group Payment, defaults to None
        :type data: GroupPayment, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, GroupPayment)
