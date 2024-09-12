from enum import Enum


class PayoutStatus(Enum):
    """An enumeration representing different categories.

    :cvar CREATED: "Created"
    :vartype CREATED: str
    :cvar COMPLETED: "Completed"
    :vartype COMPLETED: str
    :cvar CANCELED: "Canceled"
    :vartype CANCELED: str
    :cvar REJECTED: "Rejected"
    :vartype REJECTED: str
    :cvar ERROR: "Error"
    :vartype ERROR: str
    :cvar CONFIRMATION: "Confirmation"
    :vartype CONFIRMATION: str
    :cvar EXPIRED: "Expired"
    :vartype EXPIRED: str
    :cvar RETURNED: "Returned"
    :vartype RETURNED: str
    """

    CREATED = "Created"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    REJECTED = "Rejected"
    ERROR = "Error"
    CONFIRMATION = "Confirmation"
    EXPIRED = "Expired"
    RETURNED = "Returned"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PayoutStatus._member_map_.values()))
