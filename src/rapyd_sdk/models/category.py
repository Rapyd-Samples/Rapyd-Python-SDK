from enum import Enum


class Category(Enum):
    """An enumeration representing different categories.

    :cvar BANK: "bank"
    :vartype BANK: str
    :cvar CARD: "card"
    :vartype CARD: str
    :cvar CASH: "cash"
    :vartype CASH: str
    :cvar EWALLET: "ewallet"
    :vartype EWALLET: str
    :cvar RAPYDEWALLET: "rapyd_ewallet"
    :vartype RAPYDEWALLET: str
    :cvar BANKREDIRECT: "bank_redirect"
    :vartype BANKREDIRECT: str
    :cvar BANKTRANSFER: "bank_transfer"
    :vartype BANKTRANSFER: str
    """

    BANK = "bank"
    CARD = "card"
    CASH = "cash"
    EWALLET = "ewallet"
    RAPYDEWALLET = "rapyd_ewallet"
    BANKREDIRECT = "bank_redirect"
    BANKTRANSFER = "bank_transfer"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Category._member_map_.values()))
