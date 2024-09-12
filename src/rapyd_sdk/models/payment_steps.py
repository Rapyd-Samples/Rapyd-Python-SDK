from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PaymentSteps(BaseModel):
    """PaymentSteps

    :param step: step, defaults to None
    :type step: str, optional
    """

    def __init__(self, step: str = None):
        """PaymentSteps

        :param step: step, defaults to None
        :type step: str, optional
        """
        self.step = self._define_str("step", step, nullable=True)
