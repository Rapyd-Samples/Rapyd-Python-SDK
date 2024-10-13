from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .dispute import Dispute


@JsonMap({})
class InlineResponse200_48(BaseModel):
    """InlineResponse200_48

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: Describes the fields contained in REST messages and webhooks for disputes of payments., defaults to None
    :type data: Dispute, optional
    """

    def __init__(self, status: Status1 = None, data: Dispute = None):
        """InlineResponse200_48

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: Describes the fields contained in REST messages and webhooks for disputes of payments., defaults to None
        :type data: Dispute, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, Dispute)
