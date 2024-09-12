from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PayoutInstructions(BaseModel):
    """PayoutInstructions

    :param name: name, defaults to None
    :type name: str, optional
    :param steps: steps, defaults to None
    :type steps: List[dict], optional
    """

    def __init__(self, name: str = None, steps: List[dict] = None):
        """PayoutInstructions

        :param name: name, defaults to None
        :type name: str, optional
        :param steps: steps, defaults to None
        :type steps: List[dict], optional
        """
        self.name = self._define_str("name", name, nullable=True)
        self.steps = steps
