from enum import Enum


class PayoutStatus(Enum):
    CREATED = "Created"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    REJECTED = "Rejected"
    ERROR = "Error"
    CONFIRMATION = "Confirmation"
    EXPIRED = "Expired"
    RETURNED = "Returned"

    def list():
        return list(map(lambda x: x.value, PayoutStatus._member_map_.values()))
