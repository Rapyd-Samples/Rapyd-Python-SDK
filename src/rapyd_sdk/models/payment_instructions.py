from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payment_steps import PaymentSteps


@JsonMap({})
class PaymentInstructions(BaseModel):
    """PaymentInstructions

    :param name: name, defaults to None
    :type name: str, optional
    :param steps: steps, defaults to None
    :type steps: List[PaymentSteps], optional
    """

    def __init__(self, name: str = None, steps: List[PaymentSteps] = None):
        """PaymentInstructions

        :param name: name, defaults to None
        :type name: str, optional
        :param steps: steps, defaults to None
        :type steps: List[PaymentSteps], optional
        """
        self.name = self._define_str("name", name, nullable=True)
        self.steps = self._define_list(steps, PaymentSteps)
