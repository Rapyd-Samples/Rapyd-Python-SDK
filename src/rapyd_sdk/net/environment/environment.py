"""
An enum class containing all the possible environments for the SDK
"""

from enum import Enum


class Environment(Enum):
    """The environments available for the SDK"""

    DEFAULT = "https://sandboxapi.rapyd.net"
    SANDBOX = "https://sandboxapi.rapyd.net"
    PRODUCTION = "https://api.rapyd.net"
