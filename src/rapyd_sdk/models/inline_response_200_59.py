from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .payment_method_type_required_fields import PaymentMethodTypeRequiredFields


@JsonMap({})
class InlineResponse200_59(BaseModel):
    """InlineResponse200_59

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: Payment Method Type required fields - this is the response of GET required fields for Payment_Method_Type, defaults to None
    :type data: PaymentMethodTypeRequiredFields, optional
    """

    def __init__(
        self, status: Status1 = None, data: PaymentMethodTypeRequiredFields = None
    ):
        """InlineResponse200_59

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: Payment Method Type required fields - this is the response of GET required fields for Payment_Method_Type, defaults to None
        :type data: PaymentMethodTypeRequiredFields, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, PaymentMethodTypeRequiredFields)
