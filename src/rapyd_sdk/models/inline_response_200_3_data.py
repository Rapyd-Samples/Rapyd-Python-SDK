from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_3Data(BaseModel):
    """InlineResponse200_3Data

    :param delete: Flag to indicate whether contact deleted or not, defaults to None
    :type delete: bool, optional
    :param id_: Contact id, defaults to None
    :type id_: str, optional
    """

    def __init__(self, delete: bool = None, id_: str = None):
        """InlineResponse200_3Data

        :param delete: Flag to indicate whether contact deleted or not, defaults to None
        :type delete: bool, optional
        :param id_: Contact id, defaults to None
        :type id_: str, optional
        """
        self.delete = delete
        self.id_ = self._define_str("id_", id_, nullable=True)
