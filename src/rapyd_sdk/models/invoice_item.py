from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .invoice_item_period import InvoiceItemPeriod
from .plan import Plan


@JsonMap({"id_": "id", "type_": "type"})
class InvoiceItem(BaseModel):
    """Invoice item

    :param id_: line item id, defaults to None
    :type id_: str, optional
    :param amount: amount, defaults to None
    :type amount: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param description: item description, defaults to None
    :type description: str, optional
    :param discountable: discountable, defaults to None
    :type discountable: bool, optional
    :param invoice_item: invoice item id, defaults to None
    :type invoice_item: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param period: period, defaults to None
    :type period: InvoiceItemPeriod, optional
    :param proration: proration, defaults to None
    :type proration: bool, optional
    :param quantity: quantity, defaults to None
    :type quantity: float, optional
    :param plan: plan, defaults to None
    :type plan: Plan, optional
    :param subscription: ID of the subscription that generates charges to this customer. String starting with sub_., defaults to None
    :type subscription: str, optional
    :param subscription_item: ID of the subscription item that generates charges to this customer., defaults to None
    :type subscription_item: str, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        amount: float = None,
        currency: str = None,
        description: str = None,
        discountable: bool = None,
        invoice_item: str = None,
        metadata: dict = None,
        period: InvoiceItemPeriod = None,
        proration: bool = None,
        quantity: float = None,
        plan: Plan = None,
        subscription: str = None,
        subscription_item: str = None,
        type_: str = None,
    ):
        """Invoice item

        :param id_: line item id, defaults to None
        :type id_: str, optional
        :param amount: amount, defaults to None
        :type amount: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param description: item description, defaults to None
        :type description: str, optional
        :param discountable: discountable, defaults to None
        :type discountable: bool, optional
        :param invoice_item: invoice item id, defaults to None
        :type invoice_item: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param period: period, defaults to None
        :type period: InvoiceItemPeriod, optional
        :param proration: proration, defaults to None
        :type proration: bool, optional
        :param quantity: quantity, defaults to None
        :type quantity: float, optional
        :param plan: plan, defaults to None
        :type plan: Plan, optional
        :param subscription: ID of the subscription that generates charges to this customer. String starting with sub_., defaults to None
        :type subscription: str, optional
        :param subscription_item: ID of the subscription item that generates charges to this customer., defaults to None
        :type subscription_item: str, optional
        :param type_: type_, defaults to None
        :type type_: str, optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.amount = self._define_number("amount", amount, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.description = self._define_str("description", description, nullable=True)
        self.discountable = discountable
        self.invoice_item = self._define_str(
            "invoice_item", invoice_item, nullable=True
        )
        self.metadata = metadata
        self.period = self._define_object(period, InvoiceItemPeriod)
        self.proration = proration
        self.quantity = self._define_number("quantity", quantity, nullable=True)
        self.plan = self._define_object(plan, Plan)
        self.subscription = self._define_str(
            "subscription", subscription, nullable=True
        )
        self.subscription_item = self._define_str(
            "subscription_item", subscription_item, nullable=True
        )
        self.type_ = self._define_str("type_", type_, nullable=True)
