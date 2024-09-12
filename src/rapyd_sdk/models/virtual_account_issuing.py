from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .virtual_account_transaction_response import VirtualAccountTransactionResponse


class VirtualAccountIssuingStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACT: "ACT"
    :vartype ACT: str
    :cvar CLO: "CLO"
    :vartype CLO: str
    :cvar ERR: "ERR"
    :vartype ERR: str
    :cvar PEN: "PEN"
    :vartype PEN: str
    :cvar REJ: "REJ"
    :vartype REJ: str
    :cvar DIS: "DIS"
    :vartype DIS: str
    :cvar ENA: "ENA"
    :vartype ENA: str
    """

    ACT = "ACT"
    CLO = "CLO"
    ERR = "ERR"
    PEN = "PEN"
    REJ = "REJ"
    DIS = "DIS"
    ENA = "ENA"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, VirtualAccountIssuingStatus._member_map_.values())
        )


@JsonMap({"id_": "id"})
class VirtualAccountIssuing(BaseModel):
    """VirtualAccountIssuing

    :param id_: ID of the virtual account number object. String starting with issuing_., defaults to None
    :type id_: str, optional
    :param merchant_reference_id: Identifier defined by the client for reference purposes. Limit - 45 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param ewallet: ID of the Rapyd Wallet that the virtual account is attached to. String starting with ewallet_., defaults to None
    :type ewallet: str, optional
    :param bank_account: Details about the virtual account., defaults to None
    :type bank_account: dict, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param status: Indicates the status of the virtual account. * ACT (Active) * CLO (Closed)  * ERR (Error)  * PEN (Pending)  * REJ (REjected)  * DIS  * ENA , defaults to None
    :type status: VirtualAccountIssuingStatus, optional
    :param description: Description of the transaction, as defined by the client., defaults to None
    :type description: str, optional
    :param funding_instructions: Issuied virtual account funding instructions., defaults to None
    :type funding_instructions: dict, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param requested_currency: Currency received by the virtual account after conversion. One of the following: AUD - Australian Dollar EUR - Euro GBP - Pound Sterling HKD - Hong Kong Dollar SGD - Singapore Dollar USD - US Dollar , defaults to None
    :type requested_currency: str, optional
    :param transactions: Issuied virtual account transactions., defaults to None
    :type transactions: List[VirtualAccountTransactionResponse], optional
    """

    def __init__(
        self,
        id_: str = None,
        merchant_reference_id: str = None,
        ewallet: str = None,
        bank_account: dict = None,
        metadata: dict = None,
        status: VirtualAccountIssuingStatus = None,
        description: str = None,
        funding_instructions: dict = None,
        currency: str = None,
        requested_currency: str = None,
        transactions: List[VirtualAccountTransactionResponse] = None,
    ):
        """VirtualAccountIssuing

        :param id_: ID of the virtual account number object. String starting with issuing_., defaults to None
        :type id_: str, optional
        :param merchant_reference_id: Identifier defined by the client for reference purposes. Limit - 45 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param ewallet: ID of the Rapyd Wallet that the virtual account is attached to. String starting with ewallet_., defaults to None
        :type ewallet: str, optional
        :param bank_account: Details about the virtual account., defaults to None
        :type bank_account: dict, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param status: Indicates the status of the virtual account. * ACT (Active) * CLO (Closed)  * ERR (Error)  * PEN (Pending)  * REJ (REjected)  * DIS  * ENA , defaults to None
        :type status: VirtualAccountIssuingStatus, optional
        :param description: Description of the transaction, as defined by the client., defaults to None
        :type description: str, optional
        :param funding_instructions: Issuied virtual account funding instructions., defaults to None
        :type funding_instructions: dict, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param requested_currency: Currency received by the virtual account after conversion. One of the following: AUD - Australian Dollar EUR - Euro GBP - Pound Sterling HKD - Hong Kong Dollar SGD - Singapore Dollar USD - US Dollar , defaults to None
        :type requested_currency: str, optional
        :param transactions: Issuied virtual account transactions., defaults to None
        :type transactions: List[VirtualAccountTransactionResponse], optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.bank_account = bank_account
        self.metadata = metadata
        self.status = (
            self._enum_matching(status, VirtualAccountIssuingStatus.list(), "status")
            if status
            else None
        )
        self.description = self._define_str("description", description, nullable=True)
        self.funding_instructions = funding_instructions
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.requested_currency = self._define_str(
            "requested_currency", requested_currency, nullable=True
        )
        self.transactions = self._define_list(
            transactions, VirtualAccountTransactionResponse
        )
