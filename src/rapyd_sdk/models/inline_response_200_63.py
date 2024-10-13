from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .payment import Payment


@JsonMap({})
class InlineResponse200_63(BaseModel):
    """InlineResponse200_63

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
    :type data: Payment, optional
    """

    def __init__(self, status: Status1 = None, data: Payment = None):
        """InlineResponse200_63

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
        :type data: Payment, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, Payment)
