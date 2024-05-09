from __future__ import annotations
from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .PaymentFields import PaymentFields


class NetworkStatus(Enum):
    APPROVED_BY_NETWORK = "approved_by_network"
    DECLINED_BY_NETWORK = "declined_by_network"
    NOT_SENT_TO_NETWORK = "not_sent_to_network"
    REVERSED_AFTER_APPROVAL = "reversed_after_approval"

    def list():
        return list(map(lambda x: x.value, NetworkStatus._member_map_.values()))


class PaymentFlowType(Enum):
    DIRECT = "direct"
    E_WALLET = "eWallet"
    EWALLET_PAYOUT = "ewallet_payout"
    CARD = "card"
    REDIRECT_URL = "redirect_url"

    def list():
        return list(map(lambda x: x.value, PaymentFlowType._member_map_.values()))


class RiskLevel(Enum):
    NORMAL = "normal"
    ELEVATED = "elevated"
    HIGHEST = "highest"
    NOT_ASSESSED = "not_assessed"

    def list():
        return list(map(lambda x: x.value, RiskLevel._member_map_.values()))


@JsonMap({})
class Outcome(BaseModel):
    def __init__(
        self,
        network_status: NetworkStatus = None,
        payment_flow_type: PaymentFlowType = None,
        payment_options: PaymentFields = None,
        status: str = None,
        risk_level: RiskLevel = None,
        seller_message: str = None,
    ):
        self.network_status = (
            self._enum_matching(network_status, NetworkStatus.list(), "network_status")
            if network_status
            else None
        )
        self.payment_flow_type = (
            self._enum_matching(
                payment_flow_type, PaymentFlowType.list(), "payment_flow_type"
            )
            if payment_flow_type
            else None
        )
        self.payment_options = self._define_object(payment_options, PaymentFields)
        self.status = status
        self.risk_level = (
            self._enum_matching(risk_level, RiskLevel.list(), "risk_level")
            if risk_level
            else None
        )
        self.seller_message = seller_message
