from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .field import Field


@JsonMap({"type_": "type"})
class PaymentMethodTypeRequiredFields(BaseModel):
    """Payment Method Type required fields

    :param fields: Payment Method Type required field, defaults to None
    :type fields: List[Field], optional
    :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
    :type maximum_expiration_seconds: float, optional
    :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
    :type minimum_expiration_seconds: float, optional
    :param payment_method_options: payment method option, defaults to None
    :type payment_method_options: List[Field], optional
    :param payment_options: payment_options, defaults to None
    :type payment_options: List[Field], optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        fields: List[Field] = None,
        maximum_expiration_seconds: float = None,
        minimum_expiration_seconds: float = None,
        payment_method_options: List[Field] = None,
        payment_options: List[Field] = None,
        type_: str = None,
    ):
        """Payment Method Type required fields

        :param fields: Payment Method Type required field, defaults to None
        :type fields: List[Field], optional
        :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
        :type maximum_expiration_seconds: float, optional
        :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
        :type minimum_expiration_seconds: float, optional
        :param payment_method_options: payment method option, defaults to None
        :type payment_method_options: List[Field], optional
        :param payment_options: payment_options, defaults to None
        :type payment_options: List[Field], optional
        :param type_: type_, defaults to None
        :type type_: str, optional
        """
        self.fields = self._define_list(fields, Field)
        self.maximum_expiration_seconds = self._define_number(
            "maximum_expiration_seconds", maximum_expiration_seconds, nullable=True
        )
        self.minimum_expiration_seconds = self._define_number(
            "minimum_expiration_seconds", minimum_expiration_seconds, nullable=True
        )
        self.payment_method_options = self._define_list(payment_method_options, Field)
        self.payment_options = self._define_list(payment_options, Field)
        self.type_ = self._define_str("type_", type_, nullable=True)
