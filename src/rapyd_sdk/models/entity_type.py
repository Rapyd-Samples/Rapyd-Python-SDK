from enum import Enum


class EntityType(Enum):
    """An enumeration representing different categories.

    :cvar COMPANY: "company"
    :vartype COMPANY: str
    :cvar INDIVIDUAL: "individual"
    :vartype INDIVIDUAL: str
    """

    COMPANY = "company"
    INDIVIDUAL = "individual"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EntityType._member_map_.values()))
