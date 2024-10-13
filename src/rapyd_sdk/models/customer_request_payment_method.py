from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .field_1 import Field1


@JsonMap({"type_": "type"})
class CustomerRequestPaymentMethod(BaseModel):
    """The payment method that is used when the transaction does not specify a payment method. String starting with **card_** or other_.

    :param fields: Payment Method Type required field, defaults to None
    :type fields: List[Field1], optional
    :param type_: Type of the payment method. For example, it_visa_card, defaults to None
    :type type_: str, optional
    """

    def __init__(self, fields: List[Field1] = None, type_: str = None):
        """The payment method that is used when the transaction does not specify a payment method. String starting with **card_** or other_.

        :param fields: Payment Method Type required field, defaults to None
        :type fields: List[Field1], optional
        :param type_: Type of the payment method. For example, it_visa_card, defaults to None
        :type type_: str, optional
        """
        self.fields = self._define_list(fields, Field1)
        self.type_ = self._define_str("type_", type_, nullable=True)
