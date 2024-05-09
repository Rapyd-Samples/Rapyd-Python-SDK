from enum import Enum


class Category(Enum):
    BANK = "bank"
    CARD = "card"
    CASH = "cash"
    EWALLET = "ewallet"
    RAPYD_EWALLET = "rapyd_ewallet"
    BANK_REDIRECT = "bank_redirect"
    BANK_TRANSFER = "bank_transfer"

    def list():
        return list(map(lambda x: x.value, Category._member_map_.values()))
