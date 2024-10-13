from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .daily_rate import DailyRate
from .status_1 import Status1


@JsonMap({})
class InlineResponse200_20(BaseModel):
    """InlineResponse200_20

    :param data: Describes currency conversion for payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees., defaults to None
    :type data: DailyRate, optional
    :param status: status, defaults to None
    :type status: Status1, optional
    """

    def __init__(self, data: DailyRate = None, status: Status1 = None):
        """InlineResponse200_20

        :param data: Describes currency conversion for payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees., defaults to None
        :type data: DailyRate, optional
        :param status: status, defaults to None
        :type status: Status1, optional
        """
        self.data = self._define_object(data, DailyRate)
        self.status = self._define_object(status, Status1)
