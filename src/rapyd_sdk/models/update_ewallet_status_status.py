from enum import Enum


class UpdateEwalletStatusStatus(Enum):
    """An enumeration representing different categories.

    :cvar ENABLE: "enable"
    :vartype ENABLE: str
    :cvar DISABLE: "disable"
    :vartype DISABLE: str
    :cvar CLOSE: "close"
    :vartype CLOSE: str
    """

    ENABLE = "enable"
    DISABLE = "disable"
    CLOSE = "close"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, UpdateEwalletStatusStatus._member_map_.values())
        )
