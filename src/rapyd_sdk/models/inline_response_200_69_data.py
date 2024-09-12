from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_69Data(BaseModel):
    """InlineResponse200_69Data

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param quantity: The usage quantity for the specified date and time (timestamp)., defaults to None
    :type quantity: float, optional
    :param subscription_item: ID of the subscription item., defaults to None
    :type subscription_item: str, optional
    :param timestamp: Timestamp for the usage record in Unix time., defaults to None
    :type timestamp: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        quantity: float = None,
        subscription_item: str = None,
        timestamp: str = None,
    ):
        """InlineResponse200_69Data

        :param id_: id_, defaults to None
        :type id_: str, optional
        :param quantity: The usage quantity for the specified date and time (timestamp)., defaults to None
        :type quantity: float, optional
        :param subscription_item: ID of the subscription item., defaults to None
        :type subscription_item: str, optional
        :param timestamp: Timestamp for the usage record in Unix time., defaults to None
        :type timestamp: str, optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.quantity = self._define_number("quantity", quantity, nullable=True)
        self.subscription_item = self._define_str(
            "subscription_item", subscription_item, nullable=True
        )
        self.timestamp = self._define_str("timestamp", timestamp, nullable=True)
