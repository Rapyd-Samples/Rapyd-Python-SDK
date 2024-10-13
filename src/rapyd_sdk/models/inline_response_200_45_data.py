from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_45Data(BaseModel):
    """InlineResponse200_45Data

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param deleted: deleted, defaults to None
    :type deleted: bool, optional
    """

    def __init__(self, id_: str = None, deleted: bool = None):
        """InlineResponse200_45Data

        :param id_: id_, defaults to None
        :type id_: str, optional
        :param deleted: deleted, defaults to None
        :type deleted: bool, optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.deleted = deleted
