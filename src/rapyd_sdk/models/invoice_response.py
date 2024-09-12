from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .discount import Discount
from .payment import Payment
from .invoice_item import InvoiceItem


class InvoiceResponseType(Enum):
    """An enumeration representing different categories.

    :cvar PAYMENT: "payment"
    :vartype PAYMENT: str
    :cvar PAYOUT: "payout"
    :vartype PAYOUT: str
    """

    PAYMENT = "payment"
    PAYOUT = "payout"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, InvoiceResponseType._member_map_.values()))


@JsonMap({"id_": "id", "type_": "type"})
class InvoiceResponse(BaseModel):
    """Invoice

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param attempt_count: attempt_count, defaults to None
    :type attempt_count: float, optional
    :param billing: Determines the method of collection, pay_automatically or send_invoice. Default is pay_automatically, defaults to None
    :type billing: str, optional
    :param billing_reason: The reason for billing, defaults to None
    :type billing_reason: str, optional
    :param created_at: The time the invoice was created, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param discount: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process - 1. Create Coupon, which returns a coupon ID. 2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
    :type discount: Discount, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param customer: ID of the customer. String starting with cus_., defaults to None
    :type customer: str, optional
    :param days_until_due: The number of days until the due date., defaults to None
    :type days_until_due: float, optional
    :param description: Description of the invoice., defaults to None
    :type description: str, optional
    :param due_date: The date payment is due on this invoice. This value is calculated from the date the invoice is created, plus the number of days specified in the days_until_due field. Format is in Unix time., defaults to None
    :type due_date: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payment_fields: Object containing additional payment_options fields., defaults to None
    :type payment_fields: dict, optional
    :param payment_method: Payment method for the invoice., defaults to None
    :type payment_method: str, optional
    :param statement_descriptor: Description of the invoice for the customer's credit card statement. Limited to 22 characters., defaults to None
    :type statement_descriptor: str, optional
    :param subscription: ID of the subscription that is the basis for this invoice., defaults to None
    :type subscription: str, optional
    :param tax_percent: The tax rate, defined as a percentage., defaults to None
    :type tax_percent: float, optional
    :param payment: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
    :type payment: Payment, optional
    :param payout: payout, defaults to None
    :type payout: str, optional
    :param period_end: Last date in the period covered by the invoice, in Unix time. Response only., defaults to None
    :type period_end: float, optional
    :param period_start: First date in the period covered by the invoice, in Unix time. Response only., defaults to None
    :type period_start: float, optional
    :param lines: lines, defaults to None
    :type lines: List[InvoiceItem], optional
    :param subtotal: Total of all line items before discount and before tax. Decimal. Response only., defaults to None
    :type subtotal: float, optional
    :param tax: The amount of tax charged. Decimal, defaults to None
    :type tax: float, optional
    :param number: number, defaults to None
    :type number: str, optional
    :param total: Total after discount and tax. Decimal., defaults to None
    :type total: float, optional
    :param status: An invoice moves through a series of statuses. See status table below., defaults to None
    :type status: str, optional
    :param payout_fields: Reserved, defaults to None
    :type payout_fields: dict, optional
    :param type_: type_, defaults to None
    :type type_: InvoiceResponseType, optional
    """

    def __init__(
        self,
        id_: str = None,
        attempt_count: float = None,
        billing: str = None,
        billing_reason: str = None,
        created_at: float = None,
        discount: Discount = None,
        currency: str = None,
        customer: str = None,
        days_until_due: float = None,
        description: str = None,
        due_date: str = None,
        metadata: dict = None,
        payment_fields: dict = None,
        payment_method: str = None,
        statement_descriptor: str = None,
        subscription: str = None,
        tax_percent: float = None,
        payment: Payment = None,
        payout: str = None,
        period_end: float = None,
        period_start: float = None,
        lines: List[InvoiceItem] = None,
        subtotal: float = None,
        tax: float = None,
        number: str = None,
        total: float = None,
        status: str = None,
        payout_fields: dict = None,
        type_: InvoiceResponseType = None,
    ):
        """Invoice

        :param id_: id_, defaults to None
        :type id_: str, optional
        :param attempt_count: attempt_count, defaults to None
        :type attempt_count: float, optional
        :param billing: Determines the method of collection, pay_automatically or send_invoice. Default is pay_automatically, defaults to None
        :type billing: str, optional
        :param billing_reason: The reason for billing, defaults to None
        :type billing_reason: str, optional
        :param created_at: The time the invoice was created, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param discount: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process - 1. Create Coupon, which returns a coupon ID. 2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
        :type discount: Discount, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param customer: ID of the customer. String starting with cus_., defaults to None
        :type customer: str, optional
        :param days_until_due: The number of days until the due date., defaults to None
        :type days_until_due: float, optional
        :param description: Description of the invoice., defaults to None
        :type description: str, optional
        :param due_date: The date payment is due on this invoice. This value is calculated from the date the invoice is created, plus the number of days specified in the days_until_due field. Format is in Unix time., defaults to None
        :type due_date: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payment_fields: Object containing additional payment_options fields., defaults to None
        :type payment_fields: dict, optional
        :param payment_method: Payment method for the invoice., defaults to None
        :type payment_method: str, optional
        :param statement_descriptor: Description of the invoice for the customer's credit card statement. Limited to 22 characters., defaults to None
        :type statement_descriptor: str, optional
        :param subscription: ID of the subscription that is the basis for this invoice., defaults to None
        :type subscription: str, optional
        :param tax_percent: The tax rate, defined as a percentage., defaults to None
        :type tax_percent: float, optional
        :param payment: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
        :type payment: Payment, optional
        :param payout: payout, defaults to None
        :type payout: str, optional
        :param period_end: Last date in the period covered by the invoice, in Unix time. Response only., defaults to None
        :type period_end: float, optional
        :param period_start: First date in the period covered by the invoice, in Unix time. Response only., defaults to None
        :type period_start: float, optional
        :param lines: lines, defaults to None
        :type lines: List[InvoiceItem], optional
        :param subtotal: Total of all line items before discount and before tax. Decimal. Response only., defaults to None
        :type subtotal: float, optional
        :param tax: The amount of tax charged. Decimal, defaults to None
        :type tax: float, optional
        :param number: number, defaults to None
        :type number: str, optional
        :param total: Total after discount and tax. Decimal., defaults to None
        :type total: float, optional
        :param status: An invoice moves through a series of statuses. See status table below., defaults to None
        :type status: str, optional
        :param payout_fields: Reserved, defaults to None
        :type payout_fields: dict, optional
        :param type_: type_, defaults to None
        :type type_: InvoiceResponseType, optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.attempt_count = self._define_number(
            "attempt_count", attempt_count, nullable=True
        )
        self.billing = self._define_str("billing", billing, nullable=True)
        self.billing_reason = self._define_str(
            "billing_reason", billing_reason, nullable=True
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.discount = self._define_object(discount, Discount)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.customer = self._define_str("customer", customer, nullable=True)
        self.days_until_due = self._define_number(
            "days_until_due", days_until_due, nullable=True
        )
        self.description = self._define_str("description", description, nullable=True)
        self.due_date = self._define_str("due_date", due_date, nullable=True)
        self.metadata = metadata
        self.payment_fields = payment_fields
        self.payment_method = self._define_str(
            "payment_method", payment_method, nullable=True
        )
        self.statement_descriptor = self._define_str(
            "statement_descriptor", statement_descriptor, nullable=True
        )
        self.subscription = self._define_str(
            "subscription", subscription, nullable=True
        )
        self.tax_percent = self._define_number(
            "tax_percent", tax_percent, nullable=True
        )
        self.payment = self._define_object(payment, Payment)
        self.payout = self._define_str("payout", payout, nullable=True)
        self.period_end = self._define_number("period_end", period_end, nullable=True)
        self.period_start = self._define_number(
            "period_start", period_start, nullable=True
        )
        self.lines = self._define_list(lines, InvoiceItem)
        self.subtotal = self._define_number("subtotal", subtotal, nullable=True)
        self.tax = self._define_number("tax", tax, nullable=True)
        self.number = self._define_str("number", number, nullable=True)
        self.total = self._define_number("total", total, nullable=True)
        self.status = self._define_str("status", status, nullable=True)
        self.payout_fields = payout_fields
        self.type_ = (
            self._enum_matching(type_, InvoiceResponseType.list(), "type_")
            if type_
            else None
        )
