from enum import Enum


class EWalletsStatus(Enum):
    ENABLE = "enable"
    DISABLE = "disable"
    CLOSE = "close"

    def list():
        return list(map(lambda x: x.value, EWalletsStatus._member_map_.values()))
