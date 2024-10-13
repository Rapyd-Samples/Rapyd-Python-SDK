from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .field_1 import Field1


@JsonMap({"type_": "type"})
class PaymentMethodTypeRequiredFields(BaseModel):
    """Payment Method Type required fields - this is the response of GET required fields for Payment_Method_Type

    :param fields: Payment Method Type required field, defaults to None
    :type fields: List[Field1], optional
    :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
    :type maximum_expiration_seconds: float, optional
    :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
    :type minimum_expiration_seconds: float, optional
    :param payment_method_options: payment method option, defaults to None
    :type payment_method_options: List[Field1], optional
    :param payment_options: payment_options, defaults to None
    :type payment_options: List[Field1], optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        fields: List[Field1] = None,
        maximum_expiration_seconds: float = None,
        minimum_expiration_seconds: float = None,
        payment_method_options: List[Field1] = None,
        payment_options: List[Field1] = None,
        type_: str = None,
    ):
        """Payment Method Type required fields - this is the response of GET required fields for Payment_Method_Type

        :param fields: Payment Method Type required field, defaults to None
        :type fields: List[Field1], optional
        :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
        :type maximum_expiration_seconds: float, optional
        :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
        :type minimum_expiration_seconds: float, optional
        :param payment_method_options: payment method option, defaults to None
        :type payment_method_options: List[Field1], optional
        :param payment_options: payment_options, defaults to None
        :type payment_options: List[Field1], optional
        :param type_: type_, defaults to None
        :type type_: str, optional
        """
        self.fields = self._define_list(fields, Field1)
        self.maximum_expiration_seconds = self._define_number(
            "maximum_expiration_seconds", maximum_expiration_seconds, nullable=True
        )
        self.minimum_expiration_seconds = self._define_number(
            "minimum_expiration_seconds", minimum_expiration_seconds, nullable=True
        )
        self.payment_method_options = self._define_list(payment_method_options, Field1)
        self.payment_options = self._define_list(payment_options, Field1)
        self.type_ = self._define_str("type_", type_, nullable=True)
