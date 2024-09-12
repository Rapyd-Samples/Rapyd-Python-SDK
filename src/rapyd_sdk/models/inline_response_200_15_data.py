from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_15Data(BaseModel):
    """InlineResponse200_15Data

    :param deleted: Flag to indicate whether beneficiary deleted or not, defaults to None
    :type deleted: bool, optional
    :param id_: Beneficiary token, defaults to None
    :type id_: str, optional
    """

    def __init__(self, deleted: bool = None, id_: str = None):
        """InlineResponse200_15Data

        :param deleted: Flag to indicate whether beneficiary deleted or not, defaults to None
        :type deleted: bool, optional
        :param id_: Beneficiary token, defaults to None
        :type id_: str, optional
        """
        self.deleted = deleted
        self.id_ = self._define_str("id_", id_, nullable=True)
