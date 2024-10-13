from enum import Enum


class EntityTypeVerify(Enum):
    """An enumeration representing different categories.

    :cvar PARTNERSHIP: "Partnership"
    :vartype PARTNERSHIP: str
    :cvar SOLEPROPRIETOR: "Sole Proprietor"
    :vartype SOLEPROPRIETOR: str
    :cvar PRIVATELIMITEDCOMPANY: "Private Limited Company"
    :vartype PRIVATELIMITEDCOMPANY: str
    :cvar CHARITYORNPO: "Charity or NPO"
    :vartype CHARITYORNPO: str
    :cvar INDIVIDUAL: "Individual"
    :vartype INDIVIDUAL: str
    """

    PARTNERSHIP = "Partnership"
    SOLEPROPRIETOR = "Sole Proprietor"
    PRIVATELIMITEDCOMPANY = "Private Limited Company"
    CHARITYORNPO = "Charity or NPO"
    INDIVIDUAL = "Individual"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EntityTypeVerify._member_map_.values()))
