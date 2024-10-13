from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_71Data(BaseModel):
    """InlineResponse200_71Data

    :param deleted: deleted, defaults to None
    :type deleted: bool, optional
    :param id_: ID of the plan, defaults to None
    :type id_: str, optional
    """

    def __init__(self, deleted: bool = None, id_: str = None):
        """InlineResponse200_71Data

        :param deleted: deleted, defaults to None
        :type deleted: bool, optional
        :param id_: ID of the plan, defaults to None
        :type id_: str, optional
        """
        self.deleted = deleted
        self.id_ = self._define_str("id_", id_, nullable=True)
