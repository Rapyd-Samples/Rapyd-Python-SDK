from enum import Enum


class GetDisputesListByOrgIdStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACT: "ACT"
    :vartype ACT: str
    :cvar RVW: "RVW"
    :vartype RVW: str
    :cvar PRA: "PRA"
    :vartype PRA: str
    :cvar ARB: "ARB"
    :vartype ARB: str
    :cvar LOS: "LOS"
    :vartype LOS: str
    :cvar WIN: "WIN"
    :vartype WIN: str
    :cvar REV: "REV"
    :vartype REV: str
    """

    ACT = "ACT"
    RVW = "RVW"
    PRA = "PRA"
    ARB = "ARB"
    LOS = "LOS"
    WIN = "WIN"
    REV = "REV"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, GetDisputesListByOrgIdStatus._member_map_.values())
        )
