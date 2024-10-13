from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .escrow_response import EscrowResponse


@JsonMap({})
class InlineResponse200_50(BaseModel):
    """InlineResponse200_50

    :param data: data, defaults to None
    :type data: EscrowResponse, optional
    """

    def __init__(self, data: EscrowResponse = None):
        """InlineResponse200_50

        :param data: data, defaults to None
        :type data: EscrowResponse, optional
        """
        self.data = self._define_object(data, EscrowResponse)
