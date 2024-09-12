from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .checkout_page_response import CheckoutPageResponse
from .status import Status


@JsonMap({})
class InlineResponse200_28(BaseModel):
    """InlineResponse200_28

    :param data: data, defaults to None
    :type data: CheckoutPageResponse, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: CheckoutPageResponse = None, status: Status = None):
        """InlineResponse200_28

        :param data: data, defaults to None
        :type data: CheckoutPageResponse, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, CheckoutPageResponse)
        self.status = self._define_object(status, Status)
