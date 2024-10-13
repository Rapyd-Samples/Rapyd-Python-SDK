from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_79Data(BaseModel):
    """InlineResponse200_79Data

    :param deleted: true if the item deleted successfully, else false., defaults to None
    :type deleted: bool, optional
    :param id_: ID of the subscription item., defaults to None
    :type id_: str, optional
    """

    def __init__(self, deleted: bool = None, id_: str = None):
        """InlineResponse200_79Data

        :param deleted: true if the item deleted successfully, else false., defaults to None
        :type deleted: bool, optional
        :param id_: ID of the subscription item., defaults to None
        :type id_: str, optional
        """
        self.deleted = deleted
        self.id_ = self._define_str("id_", id_, nullable=True)
