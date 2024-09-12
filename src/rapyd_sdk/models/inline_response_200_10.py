from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payout_method_type_details import PayoutMethodTypeDetails
from .status import Status


@JsonMap({})
class InlineResponse200_10(BaseModel):
    """InlineResponse200_10

    :param data: data, defaults to None
    :type data: PayoutMethodTypeDetails, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: PayoutMethodTypeDetails = None, status: Status = None):
        """InlineResponse200_10

        :param data: data, defaults to None
        :type data: PayoutMethodTypeDetails, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, PayoutMethodTypeDetails)
        self.status = self._define_object(status, Status)
