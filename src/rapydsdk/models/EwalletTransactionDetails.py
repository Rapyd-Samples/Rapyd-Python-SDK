from __future__ import annotations
from enum import Enum
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .EwalletTransaction import EwalletTransaction


class BalanceType(Enum):
    AVAILABLE_BALANCE = "available_balance"
    ON_HOLD_BALANCE = "on_hold_balance"
    RECEIVED_BALANCE = "received_balance"
    RESERVE_BALANCE = "reserve_balance"

    def list():
        return list(map(lambda x: x.value, BalanceType._member_map_.values()))


class DestinationBalanceType(Enum):
    AVAILABLE_BALANCE = "available_balance"
    ON_HOLD_BALANCE = "on_hold_balance"
    RECEIVED_BALANCE = "received_balance"
    RESERVE_BALANCE = "reserve_balance"

    def list():
        return list(
            map(lambda x: x.value, DestinationBalanceType._member_map_.values())
        )


class SourceBalanceType(Enum):
    AVAILABLE_BALANCE = "available_balance"
    ON_HOLD_BALANCE = "on_hold_balance"
    RECEIVED_BALANCE = "received_balance"
    RESERVE_BALANCE = "reserve_balance"

    def list():
        return list(map(lambda x: x.value, SourceBalanceType._member_map_.values()))


@JsonMap({"type_": "type"})
class EwalletTransactionDetails1(BaseModel):
    def __init__(
        self,
        metadata: dict = None,
        amount: float = None,
        balance: float = None,
        balance_type: BalanceType = None,
        created_at: float = None,
        currency: str = None,
        destination_balance_type: DestinationBalanceType = None,
        ewallet_id: str = None,
        id: str = None,
        reason: str = None,
        source_balance_type: SourceBalanceType = None,
        status: str = None,
        type_: str = None,
        subtype: float = None,
        action_data: dict = None,
        source_ewallet_id: str = None,
        destination_ewallet_id: str = None,
    ):
        self.metadata = metadata
        self.amount = amount
        self.balance = balance
        self.balance_type = (
            self._enum_matching(balance_type, BalanceType.list(), "balance_type")
            if balance_type
            else None
        )
        self.created_at = created_at
        self.currency = currency
        self.destination_balance_type = (
            self._enum_matching(
                destination_balance_type,
                DestinationBalanceType.list(),
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
                source_balance_type, SourceBalanceType.list(), "source_balance_type"
            )
            if source_balance_type
            else None
        )
        self.status = status
        self.type_ = type_
        self.subtype = subtype
        self.action_data = action_data
        self.source_ewallet_id = source_ewallet_id
        self.destination_ewallet_id = destination_ewallet_id


class EwalletTransactionDetailsGuard(OneOfBaseModel):
    class_list = {
        "EwalletTransactionDetails1": EwalletTransactionDetails1,
        "EwalletTransaction": EwalletTransaction,
    }


EwalletTransactionDetails = Union[EwalletTransactionDetails1, EwalletTransaction]
