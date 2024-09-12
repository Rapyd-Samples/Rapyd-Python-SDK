from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .dispute import Dispute
from .status import Status


@JsonMap({})
class InlineResponse200_42(BaseModel):
    """InlineResponse200_42

    :param data: Describes the fields contained in REST messages and webhooks for disputes of payments., defaults to None
    :type data: Dispute, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Dispute = None, status: Status = None):
        """InlineResponse200_42

        :param data: Describes the fields contained in REST messages and webhooks for disputes of payments., defaults to None
        :type data: Dispute, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Dispute)
        self.status = self._define_object(status, Status)
