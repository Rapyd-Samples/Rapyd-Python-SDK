from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PayoutsPayoutIdBody(BaseModel):
    """PayoutsPayoutIdBody

    :param description: Description of the payout., defaults to None
    :type description: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    """

    def __init__(self, description: str = None, metadata: dict = None):
        """PayoutsPayoutIdBody

        :param description: Description of the payout., defaults to None
        :type description: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        """
        self.description = self._define_str("description", description, nullable=True)
        self.metadata = metadata
