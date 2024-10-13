from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InlineResponse200_85Data(BaseModel):
    """InlineResponse200_85Data

    :param id_: ID Verification., defaults to None
    :type id_: str, optional
    :param reference_id: Organization Reference Token., defaults to None
    :type reference_id: str, optional
    """

    def __init__(self, id_: str = None, reference_id: str = None):
        """InlineResponse200_85Data

        :param id_: ID Verification., defaults to None
        :type id_: str, optional
        :param reference_id: Organization Reference Token., defaults to None
        :type reference_id: str, optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.reference_id = self._define_str(
            "reference_id", reference_id, nullable=True
        )
