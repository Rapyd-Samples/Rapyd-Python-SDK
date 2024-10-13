from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class InlineResponse200_88DataStatus(Enum):
    """An enumeration representing different categories.

    :cvar NEW: "NEW"
    :vartype NEW: str
    :cvar DON: "DON"
    :vartype DON: str
    :cvar EXP: "EXP"
    :vartype EXP: str
    """

    NEW = "NEW"
    DON = "DON"
    EXP = "EXP"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, InlineResponse200_88DataStatus._member_map_.values())
        )


@JsonMap({})
class InlineResponse200_88Data(BaseModel):
    """InlineResponse200_88Data

    :param status: status, defaults to None
    :type status: InlineResponse200_88DataStatus, optional
    """

    def __init__(self, status: InlineResponse200_88DataStatus = None):
        """InlineResponse200_88Data

        :param status: status, defaults to None
        :type status: InlineResponse200_88DataStatus, optional
        """
        self.status = (
            self._enum_matching(status, InlineResponse200_88DataStatus.list(), "status")
            if status
            else None
        )
