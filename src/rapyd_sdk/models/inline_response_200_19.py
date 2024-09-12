from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .daily_rate import DailyRate
from .status import Status


@JsonMap({})
class InlineResponse200_19(BaseModel):
    """InlineResponse200_19

    :param data: Describes currency conversion for payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees., defaults to None
    :type data: DailyRate, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: DailyRate = None, status: Status = None):
        """InlineResponse200_19

        :param data: Describes currency conversion for payments and payouts. Rapyd uses a snapshot of daily foreign exchange rates fetched at 9 PM UTC. The rate returned includes the FX markup fees., defaults to None
        :type data: DailyRate, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, DailyRate)
        self.status = self._define_object(status, Status)
