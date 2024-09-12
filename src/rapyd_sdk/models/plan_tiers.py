from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel


class UpToGuard(OneOfBaseModel):
    class_list = {"str": str, "float": float}


UpTo = Union[str, float]


@JsonMap({})
class PlanTiers(BaseModel):
    """PlanTiers

    :param amount: The price for each item in this tier. Decimal number., defaults to None
    :type amount: float, optional
    :param flat_amount: Additional price for the entire tier. Default is 0., defaults to None
    :type flat_amount: float, optional
    :param up_to: The upper volume limit for this tier. Valid values: inf (infinite) or an integer., defaults to None
    :type up_to: UpTo, optional
    """

    def __init__(
        self, amount: float = None, flat_amount: float = None, up_to: UpTo = None
    ):
        """PlanTiers

        :param amount: The price for each item in this tier. Decimal number., defaults to None
        :type amount: float, optional
        :param flat_amount: Additional price for the entire tier. Default is 0., defaults to None
        :type flat_amount: float, optional
        :param up_to: The upper volume limit for this tier. Valid values: inf (infinite) or an integer., defaults to None
        :type up_to: UpTo, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.flat_amount = self._define_number(
            "flat_amount", flat_amount, nullable=True
        )
        self.up_to = UpToGuard.return_one_of(up_to)
