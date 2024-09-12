from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class SubscriptionItemIdUsageRecordsBody(BaseModel):
    """SubscriptionItemIdUsageRecordsBody

    :param action: Determines how the quantity is defined in the usage record., defaults to None
    :type action: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param quantity: The usage quantity for the specified date and time (timestamp).
    :type quantity: float
    :param timestamp: Timestamp for the usage record in Unix time.
    :type timestamp: float
    """

    def __init__(
        self,
        quantity: float,
        timestamp: float,
        action: str = None,
        metadata: dict = None,
    ):
        """SubscriptionItemIdUsageRecordsBody

        :param action: Determines how the quantity is defined in the usage record., defaults to None
        :type action: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param quantity: The usage quantity for the specified date and time (timestamp).
        :type quantity: float
        :param timestamp: Timestamp for the usage record in Unix time.
        :type timestamp: float
        """
        self.action = self._define_str("action", action, nullable=True)
        self.metadata = metadata
        self.quantity = quantity
        self.timestamp = timestamp
