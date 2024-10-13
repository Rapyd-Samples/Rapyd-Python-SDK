from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .customer_payment_method import CustomerPaymentMethod


@JsonMap({})
class InlineResponse200_44(BaseModel):
    """InlineResponse200_44

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: Describes the fields contained in REST messages and webhooks for payment methods saved to a customer profile, defaults to None
    :type data: CustomerPaymentMethod, optional
    """

    def __init__(self, status: Status1 = None, data: CustomerPaymentMethod = None):
        """InlineResponse200_44

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: Describes the fields contained in REST messages and webhooks for payment methods saved to a customer profile, defaults to None
        :type data: CustomerPaymentMethod, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, CustomerPaymentMethod)
