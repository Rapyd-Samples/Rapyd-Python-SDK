from enum import Enum


class PaymentStatus(Enum):
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
        return list(map(lambda x: x.value, PaymentStatus._member_map_.values()))
