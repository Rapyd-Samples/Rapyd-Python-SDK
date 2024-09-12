from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payment_options import PaymentOptions


class NetworkStatus(Enum):
    """An enumeration representing different categories.

    :cvar APPROVEDBYNETWORK: "approved_by_network"
    :vartype APPROVEDBYNETWORK: str
    :cvar DECLINEDBYNETWORK: "declined_by_network"
    :vartype DECLINEDBYNETWORK: str
    :cvar NOTSENTTONETWORK: "not_sent_to_network"
    :vartype NOTSENTTONETWORK: str
    :cvar REVERSEDAFTERAPPROVAL: "reversed_after_approval"
    :vartype REVERSEDAFTERAPPROVAL: str
    """

    APPROVEDBYNETWORK = "approved_by_network"
    DECLINEDBYNETWORK = "declined_by_network"
    NOTSENTTONETWORK = "not_sent_to_network"
    REVERSEDAFTERAPPROVAL = "reversed_after_approval"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, NetworkStatus._member_map_.values()))


class OutcomePaymentFlowType(Enum):
    """An enumeration representing different categories.

    :cvar DIRECT: "direct"
    :vartype DIRECT: str
    :cvar EWALLET: "eWallet"
    :vartype EWALLET: str
    :cvar EWALLETPAYOUT: "ewallet_payout"
    :vartype EWALLETPAYOUT: str
    :cvar CARD: "card"
    :vartype CARD: str
    :cvar REDIRECTURL: "redirect_url"
    :vartype REDIRECTURL: str
    """

    DIRECT = "direct"
    EWALLET = "eWallet"
    EWALLETPAYOUT = "ewallet_payout"
    CARD = "card"
    REDIRECTURL = "redirect_url"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, OutcomePaymentFlowType._member_map_.values())
        )


class RiskLevel(Enum):
    """An enumeration representing different categories.

    :cvar NORMAL: "normal"
    :vartype NORMAL: str
    :cvar ELEVATED: "elevated"
    :vartype ELEVATED: str
    :cvar HIGHEST: "highest"
    :vartype HIGHEST: str
    :cvar NOTASSESSED: "not_assessed"
    :vartype NOTASSESSED: str
    """

    NORMAL = "normal"
    ELEVATED = "elevated"
    HIGHEST = "highest"
    NOTASSESSED = "not_assessed"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, RiskLevel._member_map_.values()))


@JsonMap({})
class Outcome(BaseModel):
    """The outcome object describes the outcome of the Rapyd Protect risk assessment

    :param network_status: network_status, defaults to None
    :type network_status: NetworkStatus, optional
    :param payment_flow_type: payment_flow_type, defaults to None
    :type payment_flow_type: OutcomePaymentFlowType, optional
    :param payment_options: A payment method type is a type of payment method that any customer can use, for example, ee_mastercard_card, Mastercard for Estonia. When it is added to a customer profile, it becomes a payment method that is specific to that one customer. The name of the payment method type starts with a prefix for the country, the 2-letter ISO 3166-1 alpha-2 code. If the payment method is valid in multiple countries, the prefix is xx_. The payment method type has a suffix with one of the following values - _bank - Bank transfer or bank redirect _card - Credit card, debit card or other card _cash - Cash _ewallet - Local eWallet, defaults to None
    :type payment_options: PaymentOptions, optional
    :param status: Indicates the status of the payment method. One of the following value is 1 means the payment_method_type is Valid, defaults to None
    :type status: str, optional
    :param risk_level: risk_level, defaults to None
    :type risk_level: RiskLevel, optional
    :param seller_message: Message to the merchant, defaults to None
    :type seller_message: str, optional
    """

    def __init__(
        self,
        network_status: NetworkStatus = None,
        payment_flow_type: OutcomePaymentFlowType = None,
        payment_options: PaymentOptions = None,
        status: str = None,
        risk_level: RiskLevel = None,
        seller_message: str = None,
    ):
        """The outcome object describes the outcome of the Rapyd Protect risk assessment

        :param network_status: network_status, defaults to None
        :type network_status: NetworkStatus, optional
        :param payment_flow_type: payment_flow_type, defaults to None
        :type payment_flow_type: OutcomePaymentFlowType, optional
        :param payment_options: A payment method type is a type of payment method that any customer can use, for example, ee_mastercard_card, Mastercard for Estonia. When it is added to a customer profile, it becomes a payment method that is specific to that one customer. The name of the payment method type starts with a prefix for the country, the 2-letter ISO 3166-1 alpha-2 code. If the payment method is valid in multiple countries, the prefix is xx_. The payment method type has a suffix with one of the following values - _bank - Bank transfer or bank redirect _card - Credit card, debit card or other card _cash - Cash _ewallet - Local eWallet, defaults to None
        :type payment_options: PaymentOptions, optional
        :param status: Indicates the status of the payment method. One of the following value is 1 means the payment_method_type is Valid, defaults to None
        :type status: str, optional
        :param risk_level: risk_level, defaults to None
        :type risk_level: RiskLevel, optional
        :param seller_message: Message to the merchant, defaults to None
        :type seller_message: str, optional
        """
        self.network_status = (
            self._enum_matching(network_status, NetworkStatus.list(), "network_status")
            if network_status
            else None
        )
        self.payment_flow_type = (
            self._enum_matching(
                payment_flow_type, OutcomePaymentFlowType.list(), "payment_flow_type"
            )
            if payment_flow_type
            else None
        )
        self.payment_options = self._define_object(payment_options, PaymentOptions)
        self.status = self._define_str("status", status, nullable=True)
        self.risk_level = (
            self._enum_matching(risk_level, RiskLevel.list(), "risk_level")
            if risk_level
            else None
        )
        self.seller_message = self._define_str(
            "seller_message", seller_message, nullable=True
        )
