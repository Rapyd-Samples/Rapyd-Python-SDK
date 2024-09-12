from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .customer_payment_method import CustomerPaymentMethod
from .status import Status


@JsonMap({})
class InlineResponse200_39(BaseModel):
    """InlineResponse200_39

    :param data: Describes the fields contained in REST messages and webhooks for payment methods saved to a customer profile, defaults to None
    :type data: CustomerPaymentMethod, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: CustomerPaymentMethod = None, status: Status = None):
        """InlineResponse200_39

        :param data: Describes the fields contained in REST messages and webhooks for payment methods saved to a customer profile, defaults to None
        :type data: CustomerPaymentMethod, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, CustomerPaymentMethod)
        self.status = self._define_object(status, Status)
