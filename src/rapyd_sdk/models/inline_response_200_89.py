from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .verify_hosted_app_response import VerifyHostedAppResponse
from .status_1 import Status1


@JsonMap({})
class InlineResponse200_89(BaseModel):
    """InlineResponse200_89

    :param data: data, defaults to None
    :type data: VerifyHostedAppResponse, optional
    :param status: status, defaults to None
    :type status: Status1, optional
    """

    def __init__(self, data: VerifyHostedAppResponse = None, status: Status1 = None):
        """InlineResponse200_89

        :param data: data, defaults to None
        :type data: VerifyHostedAppResponse, optional
        :param status: status, defaults to None
        :type status: Status1, optional
        """
        self.data = self._define_object(data, VerifyHostedAppResponse)
        self.status = self._define_object(status, Status1)
