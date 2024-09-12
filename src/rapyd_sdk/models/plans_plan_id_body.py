from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PlansPlanIdBody(BaseModel):
    """PlansPlanIdBody

    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param nickname: Brief description of the pricing plan., defaults to None
    :type nickname: str, optional
    """

    def __init__(self, metadata: dict = None, nickname: str = None):
        """PlansPlanIdBody

        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param nickname: Brief description of the pricing plan., defaults to None
        :type nickname: str, optional
        """
        self.metadata = metadata
        self.nickname = self._define_str("nickname", nickname, nullable=True)
