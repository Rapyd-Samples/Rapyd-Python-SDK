from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payment import Payment
from .status import Status


@JsonMap({})
class InlineResponse200_54(BaseModel):
    """InlineResponse200_54

    :param data: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
    :type data: Payment, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Payment = None, status: Status = None):
        """InlineResponse200_54

        :param data: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
        :type data: Payment, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Payment)
        self.status = self._define_object(status, Status)
