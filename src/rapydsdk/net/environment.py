"""
An enum class containing all the possible environments that 
a user can switch between in this SDK.
"""

from enum import Enum


class Environment(Enum):
    """The environments available for this SDK"""

    DEFAULT = "https://api.rapyd.net"
    SANDBOX = "https://sandboxapi.rapyd.net"
    PRODUCTION = "https://api.rapyd.net"
