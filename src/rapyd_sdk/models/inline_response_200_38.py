from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .customer_payment_method import CustomerPaymentMethod


@JsonMap({})
class InlineResponse200_38(BaseModel):
    """InlineResponse200_38

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: Describes the fields contained in REST messages and webhooks for payment methods saved to a customer profile, defaults to None
    :type data: CustomerPaymentMethod, optional
    """

    def __init__(self, status: Status = None, data: CustomerPaymentMethod = None):
        """InlineResponse200_38

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: Describes the fields contained in REST messages and webhooks for payment methods saved to a customer profile, defaults to None
        :type data: CustomerPaymentMethod, optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, CustomerPaymentMethod)
