from enum import Enum


class UpdateEwalletStatusStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACT: "ACT"
    :vartype ACT: str
    :cvar DIS: "DIS"
    :vartype DIS: str
    :cvar CLO: "CLO"
    :vartype CLO: str
    """

    ACT = "ACT"
    DIS = "DIS"
    CLO = "CLO"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, UpdateEwalletStatusStatus._member_map_.values())
        )
