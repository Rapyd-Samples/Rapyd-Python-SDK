from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PlanTransformUsage(BaseModel):
    """Defines the transformation that is applied to the reported usage before the billed price is computed. The transformation divides the quantity by the divisor specified in divide_by, then rounds up or down according to the setting in round. Relevant when billing_scheme is set to per_unit.

    :param divide_by: Indicates the divisor in the transformation calculation. Integer. Default is 1., defaults to None
    :type divide_by: float, optional
    :param round: Indicates whether the reported number of units should be rounded up or down to the next whole quantity specified in divide_by. String. Default is up., defaults to None
    :type round: str, optional
    """

    def __init__(self, divide_by: float = None, round: str = None):
        """Defines the transformation that is applied to the reported usage before the billed price is computed. The transformation divides the quantity by the divisor specified in divide_by, then rounds up or down according to the setting in round. Relevant when billing_scheme is set to per_unit.

        :param divide_by: Indicates the divisor in the transformation calculation. Integer. Default is 1., defaults to None
        :type divide_by: float, optional
        :param round: Indicates whether the reported number of units should be rounded up or down to the next whole quantity specified in divide_by. String. Default is up., defaults to None
        :type round: str, optional
        """
        self.divide_by = self._define_number("divide_by", divide_by, nullable=True)
        self.round = self._define_str("round", round, nullable=True)
