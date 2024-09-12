from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .checkout_page_response import CheckoutPageResponse


@JsonMap({})
class InlineResponse200_27(BaseModel):
    """InlineResponse200_27

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: data, defaults to None
    :type data: CheckoutPageResponse, optional
    """

    def __init__(self, status: Status = None, data: CheckoutPageResponse = None):
        """InlineResponse200_27

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: data, defaults to None
        :type data: CheckoutPageResponse, optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, CheckoutPageResponse)
