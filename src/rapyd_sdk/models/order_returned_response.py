from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .order_returned_item_response import OrderReturnedItemResponse


@JsonMap({"id_": "id"})
class OrderReturnedResponse(BaseModel):
    """OrderReturnedResponse

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param amount: amount, defaults to None
    :type amount: float, optional
    :param created: created, defaults to None
    :type created: int, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param items: items, defaults to None
    :type items: List[OrderReturnedItemResponse], optional
    :param order: order, defaults to None
    :type order: str, optional
    :param refund: refund, defaults to None
    :type refund: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        amount: float = None,
        created: int = None,
        currency: str = None,
        items: List[OrderReturnedItemResponse] = None,
        order: str = None,
        refund: str = None,
    ):
        """OrderReturnedResponse

        :param id_: id_, defaults to None
        :type id_: str, optional
        :param amount: amount, defaults to None
        :type amount: float, optional
        :param created: created, defaults to None
        :type created: int, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param items: items, defaults to None
        :type items: List[OrderReturnedItemResponse], optional
        :param order: order, defaults to None
        :type order: str, optional
        :param refund: refund, defaults to None
        :type refund: str, optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.amount = self._define_number("amount", amount, nullable=True)
        self.created = self._define_number("created", created, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.items = self._define_list(items, OrderReturnedItemResponse)
        self.order = self._define_str("order", order, nullable=True)
        self.refund = self._define_str("refund", refund, nullable=True)
