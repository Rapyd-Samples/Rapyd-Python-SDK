from enum import Enum


class NextAction(Enum):
    V3_D_VERIFICATION = "3d_verification"
    PENDING_CAPTURE = "pending_capture"
    PENDING_CONFIRMATION = "pending_confirmation"
    NOT_APPLICABLE = "not_applicable"

    def list():
        return list(map(lambda x: x.value, NextAction._member_map_.values()))
