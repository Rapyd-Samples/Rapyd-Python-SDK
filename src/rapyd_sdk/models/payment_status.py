from enum import Enum


class PaymentStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACT: "ACT"
    :vartype ACT: str
    :cvar CLO: "CLO"
    :vartype CLO: str
    :cvar ERR: "ERR"
    :vartype ERR: str
    :cvar CAN: "CAN"
    :vartype CAN: str
    :cvar EXP: "EXP"
    :vartype EXP: str
    :cvar DLD: "DLD"
    :vartype DLD: str
    :cvar REV: "REV"
    :vartype REV: str
    :cvar UND: "UND"
    :vartype UND: str
    :cvar CRE: "CRE"
    :vartype CRE: str
    """

    ACT = "ACT"
    CLO = "CLO"
    ERR = "ERR"
    CAN = "CAN"
    EXP = "EXP"
    DLD = "DLD"
    REV = "REV"
    UND = "UND"
    CRE = "CRE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PaymentStatus._member_map_.values()))
