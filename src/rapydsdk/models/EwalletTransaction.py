from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class BalanceType1(Enum):
    AVAILABLE_BALANCE = "available_balance"
    ON_HOLD_BALANCE = "on_hold_balance"
    RECEIVED_BALANCE = "received_balance"
    RESERVE_BALANCE = "reserve_balance"

    def list():
        return list(map(lambda x: x.value, BalanceType1._member_map_.values()))


class DestinationBalanceType1(Enum):
    AVAILABLE_BALANCE = "available_balance"
    ON_HOLD_BALANCE = "on_hold_balance"
    RECEIVED_BALANCE = "received_balance"
    RESERVE_BALANCE = "reserve_balance"

    def list():
        return list(
            map(lambda x: x.value, DestinationBalanceType1._member_map_.values())
        )


class SourceBalanceType1(Enum):
    AVAILABLE_BALANCE = "available_balance"
    ON_HOLD_BALANCE = "on_hold_balance"
    RECEIVED_BALANCE = "received_balance"
    RESERVE_BALANCE = "reserve_balance"

    def list():
        return list(map(lambda x: x.value, SourceBalanceType1._member_map_.values()))


@JsonMap({"type_": "type"})
class EwalletTransaction(BaseModel):
    def __init__(
        self,
        metadata: dict = None,
        amount: float = None,
        balance: float = None,
        balance_type: BalanceType1 = None,
        created_at: float = None,
        currency: str = None,
        destination_balance_type: DestinationBalanceType1 = None,
        ewallet_id: str = None,
        id: str = None,
        reason: str = None,
        source_balance_type: SourceBalanceType1 = None,
        status: str = None,
        type_: str = None,
        subtype: float = None,
        action_data: dict = None,
    ):
        self.metadata = metadata
        self.amount = amount
        self.balance = balance
        self.balance_type = (
            self._enum_matching(balance_type, BalanceType1.list(), "balance_type")
            if balance_type
            else None
        )
        self.created_at = created_at
        self.currency = currency
        self.destination_balance_type = (
            self._enum_matching(
                destination_balance_type,
                DestinationBalanceType1.list(),
                "destination_balance_type",
            )
            if destination_balance_type
            else None
        )
        self.ewallet_id = ewallet_id
        self.id = id
        self.reason = reason
        self.source_balance_type = (
            self._enum_matching(
                source_balance_type, SourceBalanceType1.list(), "source_balance_type"
            )
            if source_balance_type
            else None
        )
        self.status = status
        self.type_ = type_
        self.subtype = subtype
        self.action_data = action_data
