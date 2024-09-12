from enum import Enum


class NextAction(Enum):
    """An enumeration representing different categories.

    :cvar _3DVERIFICATION: "3d_verification"
    :vartype _3DVERIFICATION: str
    :cvar PENDINGCAPTURE: "pending_capture"
    :vartype PENDINGCAPTURE: str
    :cvar PENDINGCONFIRMATION: "pending_confirmation"
    :vartype PENDINGCONFIRMATION: str
    :cvar NOTAPPLICABLE: "not_applicable"
    :vartype NOTAPPLICABLE: str
    """

    _3DVERIFICATION = "3d_verification"
    PENDINGCAPTURE = "pending_capture"
    PENDINGCONFIRMATION = "pending_confirmation"
    NOTAPPLICABLE = "not_applicable"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, NextAction._member_map_.values()))
