from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .limit import Limit


@JsonMap({"id_": "id"})
class Account(BaseModel):
    """Account

    :param alias: Three-letter ISO 4217 code for the currency of the account., defaults to None
    :type alias: str, optional
    :param balance: Available funds in the account., defaults to None
    :type balance: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param id_: ID of the account. UUID, defaults to None
    :type id_: str, optional
    :param limit: limit, defaults to None
    :type limit: str, optional
    :param limits: limits, defaults to None
    :type limits: List[Limit], optional
    :param on_hold_balance: Amount in the on-hold balance of the account., defaults to None
    :type on_hold_balance: float, optional
    :param received_balance: Amount of escrow funds in the account., defaults to None
    :type received_balance: float, optional
    :param reserve_balance: Amount in the reserve balance of the account., defaults to None
    :type reserve_balance: float, optional
    """

    def __init__(
        self,
        alias: str = None,
        balance: float = None,
        currency: str = None,
        id_: str = None,
        limit: str = None,
        limits: List[Limit] = None,
        on_hold_balance: float = None,
        received_balance: float = None,
        reserve_balance: float = None,
    ):
        """Account

        :param alias: Three-letter ISO 4217 code for the currency of the account., defaults to None
        :type alias: str, optional
        :param balance: Available funds in the account., defaults to None
        :type balance: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param id_: ID of the account. UUID, defaults to None
        :type id_: str, optional
        :param limit: limit, defaults to None
        :type limit: str, optional
        :param limits: limits, defaults to None
        :type limits: List[Limit], optional
        :param on_hold_balance: Amount in the on-hold balance of the account., defaults to None
        :type on_hold_balance: float, optional
        :param received_balance: Amount of escrow funds in the account., defaults to None
        :type received_balance: float, optional
        :param reserve_balance: Amount in the reserve balance of the account., defaults to None
        :type reserve_balance: float, optional
        """
        self.alias = self._define_str("alias", alias, nullable=True)
        self.balance = self._define_number("balance", balance, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.limit = self._define_str("limit", limit, nullable=True)
        self.limits = self._define_list(limits, Limit)
        self.on_hold_balance = self._define_number(
            "on_hold_balance", on_hold_balance, nullable=True
        )
        self.received_balance = self._define_number(
            "received_balance", received_balance, nullable=True
        )
        self.reserve_balance = self._define_number(
            "reserve_balance", reserve_balance, nullable=True
        )
