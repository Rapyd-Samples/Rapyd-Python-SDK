from enum import Enum


class Gender(Enum):
    """An enumeration representing different categories.

    :cvar MALE: "male"
    :vartype MALE: str
    :cvar FEMALE: "female"
    :vartype FEMALE: str
    :cvar OTHER: "other"
    :vartype OTHER: str
    :cvar NOTAPPLICABLE: "not_applicable"
    :vartype NOTAPPLICABLE: str
    """

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    NOTAPPLICABLE = "not_applicable"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Gender._member_map_.values()))
