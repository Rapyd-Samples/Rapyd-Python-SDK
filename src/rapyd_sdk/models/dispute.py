from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class DisputeStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACT: "ACT"
    :vartype ACT: str
    :cvar RVW: "RVW"
    :vartype RVW: str
    :cvar PRA: "PRA"
    :vartype PRA: str
    :cvar ARB: "ARB"
    :vartype ARB: str
    :cvar LOS: "LOS"
    :vartype LOS: str
    :cvar WIN: "WIN"
    :vartype WIN: str
    :cvar REV: "REV"
    :vartype REV: str
    """

    ACT = "ACT"
    RVW = "RVW"
    PRA = "PRA"
    ARB = "ARB"
    LOS = "LOS"
    WIN = "WIN"
    REV = "REV"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DisputeStatus._member_map_.values()))


@JsonMap({"id_": "id"})
class Dispute(BaseModel):
    """Describes the fields contained in REST messages and webhooks for disputes of payments.

    :param id_: Reserved., defaults to None
    :type id_: str, optional
    :param token: ID of the dispute. String starting with dispute_., defaults to None
    :type token: str, optional
    :param status: Indicates the status of the dispute operation. One of the following values: * ACT (Active) - The dispute was initiated and is awaiting action by the merchant. * RVW (Review) - Rapyd is reviewing the merchant's evidence contesting the dispute. * PRA (Pre-Arbitration) - Rapyd is reviewing the merchant's evidence contesting a previously contested dispute. * ARB (Arbitration) - The merchant rejected a pre-arbitration outcome. Rapyd is awaiting a ruling by an arbitration committee from the card schemes. * LOS (Lose) - The merchant lost the dispute. Funds were deducted from the merchant wallet. Final status. * WIN (Win) - The merchant won the dispute. Funds were credited to the merchant wallet. Final status. * REV (Reverse) - The card issuer reversed the dispute. Funds were credited to the merchant wallet. Final status. , defaults to None
    :type status: DisputeStatus, optional
    :param amount: Amount that Rapyd deducted from the merchant due to the dispute., defaults to None
    :type amount: float, optional
    :param currency: Three-letter ISO 4217 code for the currency used in the amount field., defaults to None
    :type currency: str, optional
    :param dispute_category: The category of dispute that was provided by the card network., defaults to None
    :type dispute_category: str, optional
    :param dispute_reason_description: A short description of the reason for the dispute., defaults to None
    :type dispute_reason_description: str, optional
    :param original_transaction_currency: original_transaction_currency, defaults to None
    :type original_transaction_currency: str, optional
    :param original_transaction_amount: Amount of the original payment., defaults to None
    :type original_transaction_amount: float, optional
    :param original_dispute_amount: Amount of the dispute, as reported to Rapyd., defaults to None
    :type original_dispute_amount: float, optional
    :param original_dispute_currency: original_dispute_currency, defaults to None
    :type original_dispute_currency: str, optional
    :param original_transaction_id: ID of the payment that the dispute is charged against. String starting with payment_., defaults to None
    :type original_transaction_id: str, optional
    :param ewallet_id: ID of the wallet that the money is paid into. String starting with ewallet_. Relevant when the request includes a single wallet. Response only., defaults to None
    :type ewallet_id: str, optional
    :param central_processing_date: The date the transaction was processed by the card network., defaults to None
    :type central_processing_date: float, optional
    :param created_at: Time of creation of the dispute, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param updated_at: Time that the dispute was last updated, in Unix time. Response only., defaults to None
    :type updated_at: float, optional
    :param due_date: The latest date for the dispute to be contested in Unix time. Response only., defaults to None
    :type due_date: float, optional
    :param payment_method: ID of the payment method. String starting with card_., defaults to None
    :type payment_method: str, optional
    :param payment_method_data: Details of the payment method that was used for the payment. See Payment Method Data Object. Response only., defaults to None
    :type payment_method_data: dict, optional
    :param rate: FX rate. Relevant to FX payments., defaults to None
    :type rate: float, optional
    :param evidence: Reserved., defaults to None
    :type evidence: str, optional
    :param evidence_reason_code: Reserved., defaults to None
    :type evidence_reason_code: str, optional
    :param pre_dispute: When true, indicates that the disputed payment was automatically refunded based on pre-determined criteria. Response only., defaults to None
    :type pre_dispute: bool, optional
    :param arn: An Acquirer Reference Number (ARN) is a unique number assigned to a credit card transaction as it moves through the payment flow. Banks can use it to help trace the payment/ refund if it appears to be missing. An ARN will be available for Visa and Mastercard charges. , defaults to None
    :type arn: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        token: str = None,
        status: DisputeStatus = None,
        amount: float = None,
        currency: str = None,
        dispute_category: str = None,
        dispute_reason_description: str = None,
        original_transaction_currency: str = None,
        original_transaction_amount: float = None,
        original_dispute_amount: float = None,
        original_dispute_currency: str = None,
        original_transaction_id: str = None,
        ewallet_id: str = None,
        central_processing_date: float = None,
        created_at: float = None,
        updated_at: float = None,
        due_date: float = None,
        payment_method: str = None,
        payment_method_data: dict = None,
        rate: float = None,
        evidence: str = None,
        evidence_reason_code: str = None,
        pre_dispute: bool = None,
        arn: str = None,
    ):
        """Describes the fields contained in REST messages and webhooks for disputes of payments.

        :param id_: Reserved., defaults to None
        :type id_: str, optional
        :param token: ID of the dispute. String starting with dispute_., defaults to None
        :type token: str, optional
        :param status: Indicates the status of the dispute operation. One of the following values: * ACT (Active) - The dispute was initiated and is awaiting action by the merchant. * RVW (Review) - Rapyd is reviewing the merchant's evidence contesting the dispute. * PRA (Pre-Arbitration) - Rapyd is reviewing the merchant's evidence contesting a previously contested dispute. * ARB (Arbitration) - The merchant rejected a pre-arbitration outcome. Rapyd is awaiting a ruling by an arbitration committee from the card schemes. * LOS (Lose) - The merchant lost the dispute. Funds were deducted from the merchant wallet. Final status. * WIN (Win) - The merchant won the dispute. Funds were credited to the merchant wallet. Final status. * REV (Reverse) - The card issuer reversed the dispute. Funds were credited to the merchant wallet. Final status. , defaults to None
        :type status: DisputeStatus, optional
        :param amount: Amount that Rapyd deducted from the merchant due to the dispute., defaults to None
        :type amount: float, optional
        :param currency: Three-letter ISO 4217 code for the currency used in the amount field., defaults to None
        :type currency: str, optional
        :param dispute_category: The category of dispute that was provided by the card network., defaults to None
        :type dispute_category: str, optional
        :param dispute_reason_description: A short description of the reason for the dispute., defaults to None
        :type dispute_reason_description: str, optional
        :param original_transaction_currency: original_transaction_currency, defaults to None
        :type original_transaction_currency: str, optional
        :param original_transaction_amount: Amount of the original payment., defaults to None
        :type original_transaction_amount: float, optional
        :param original_dispute_amount: Amount of the dispute, as reported to Rapyd., defaults to None
        :type original_dispute_amount: float, optional
        :param original_dispute_currency: original_dispute_currency, defaults to None
        :type original_dispute_currency: str, optional
        :param original_transaction_id: ID of the payment that the dispute is charged against. String starting with payment_., defaults to None
        :type original_transaction_id: str, optional
        :param ewallet_id: ID of the wallet that the money is paid into. String starting with ewallet_. Relevant when the request includes a single wallet. Response only., defaults to None
        :type ewallet_id: str, optional
        :param central_processing_date: The date the transaction was processed by the card network., defaults to None
        :type central_processing_date: float, optional
        :param created_at: Time of creation of the dispute, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param updated_at: Time that the dispute was last updated, in Unix time. Response only., defaults to None
        :type updated_at: float, optional
        :param due_date: The latest date for the dispute to be contested in Unix time. Response only., defaults to None
        :type due_date: float, optional
        :param payment_method: ID of the payment method. String starting with card_., defaults to None
        :type payment_method: str, optional
        :param payment_method_data: Details of the payment method that was used for the payment. See Payment Method Data Object. Response only., defaults to None
        :type payment_method_data: dict, optional
        :param rate: FX rate. Relevant to FX payments., defaults to None
        :type rate: float, optional
        :param evidence: Reserved., defaults to None
        :type evidence: str, optional
        :param evidence_reason_code: Reserved., defaults to None
        :type evidence_reason_code: str, optional
        :param pre_dispute: When true, indicates that the disputed payment was automatically refunded based on pre-determined criteria. Response only., defaults to None
        :type pre_dispute: bool, optional
        :param arn: An Acquirer Reference Number (ARN) is a unique number assigned to a credit card transaction as it moves through the payment flow. Banks can use it to help trace the payment/ refund if it appears to be missing. An ARN will be available for Visa and Mastercard charges. , defaults to None
        :type arn: str, optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.token = self._define_str("token", token, nullable=True)
        self.status = (
            self._enum_matching(status, DisputeStatus.list(), "status")
            if status
            else None
        )
        self.amount = self._define_number("amount", amount, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.dispute_category = self._define_str(
            "dispute_category", dispute_category, nullable=True
        )
        self.dispute_reason_description = self._define_str(
            "dispute_reason_description", dispute_reason_description, nullable=True
        )
        self.original_transaction_currency = self._define_str(
            "original_transaction_currency",
            original_transaction_currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.original_transaction_amount = self._define_number(
            "original_transaction_amount", original_transaction_amount, nullable=True
        )
        self.original_dispute_amount = self._define_number(
            "original_dispute_amount", original_dispute_amount, nullable=True
        )
        self.original_dispute_currency = self._define_str(
            "original_dispute_currency",
            original_dispute_currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.original_transaction_id = self._define_str(
            "original_transaction_id", original_transaction_id, nullable=True
        )
        self.ewallet_id = self._define_str("ewallet_id", ewallet_id, nullable=True)
        self.central_processing_date = self._define_number(
            "central_processing_date", central_processing_date, nullable=True
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.updated_at = self._define_number("updated_at", updated_at, nullable=True)
        self.due_date = self._define_number("due_date", due_date, nullable=True)
        self.payment_method = self._define_str(
            "payment_method", payment_method, nullable=True
        )
        self.payment_method_data = payment_method_data
        self.rate = self._define_number("rate", rate, nullable=True)
        self.evidence = self._define_str("evidence", evidence, nullable=True)
        self.evidence_reason_code = self._define_str(
            "evidence_reason_code", evidence_reason_code, nullable=True
        )
        self.pre_dispute = pre_dispute
        self.arn = self._define_str("arn", arn, nullable=True)
