from enum import Enum


class HostedPageStatus(Enum):
    NEW = "NEW"
    DON = "DON"
    EXP = "EXP"

    def list():
        return list(map(lambda x: x.value, HostedPageStatus._member_map_.values()))
