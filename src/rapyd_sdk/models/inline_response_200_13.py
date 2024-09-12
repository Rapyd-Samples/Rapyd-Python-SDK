from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .beneficiary import Beneficiary
from .status import Status


@JsonMap({})
class InlineResponse200_13(BaseModel):
    """InlineResponse200_13

    :param data: data, defaults to None
    :type data: Beneficiary, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Beneficiary = None, status: Status = None):
        """InlineResponse200_13

        :param data: data, defaults to None
        :type data: Beneficiary, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Beneficiary)
        self.status = self._define_object(status, Status)
