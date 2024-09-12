from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payment_method_type import PaymentMethodType


@JsonMap({})
class CustomerIdPaymentMethodsBody(BaseModel):
    """CustomerIdPaymentMethodsBody

    :param data: A type of payment method that a customer can use for making payments., defaults to None
    :type data: PaymentMethodType, optional
    """

    def __init__(self, data: PaymentMethodType = None):
        """CustomerIdPaymentMethodsBody

        :param data: A type of payment method that a customer can use for making payments., defaults to None
        :type data: PaymentMethodType, optional
        """
        self.data = self._define_object(data, PaymentMethodType)
