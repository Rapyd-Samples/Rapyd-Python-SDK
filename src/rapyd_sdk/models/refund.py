from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .refund_ewallets import RefundEwallets


@JsonMap({"id_": "id"})
class Refund(BaseModel):
    """Refund

    :param amount: Amount of the refund, in units defined by currency in the original payment. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015., defaults to None
    :type amount: float, optional
    :param created_at: Time of creation of this refund, in Unix time. Response only., defaults to None
    :type created_at: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param ewallets: An array of one object, which contains the following fields: * ewallet_id - The ID of the wallet that the money is transferred from, a string starting with ewallet_. * amount - Amount of the transaction in currency units defined in currency. * percent - A decimal number representing a percentage of the total payout. Response only., defaults to None
    :type ewallets: List[RefundEwallets], optional
    :param failure_reason: Indicates the reason that the refund failed., defaults to None
    :type failure_reason: str, optional
    :param fixed_side: Indicates whether the FX rate is fixed for the buy side or for the sell side. Relevant for refunds with foreign exchange. Response only., defaults to None
    :type fixed_side: str, optional
    :param fx_rate: Exchange rate for the transaction. When fixed_side is buy, fx_rate is the buy rate. When fixed_side is sell, fx_rate is the sell rate. Decimal number as string. Relevant to refunds with foreign exchange. Response only., defaults to None
    :type fx_rate: str, optional
    :param id_: ID of the Refund object. String starting with refund_., defaults to None
    :type id_: str, optional
    :param merchant_debited_amount: Amount debited from the merchant. Relevant to refunds with foreign exchange. Response only., defaults to None
    :type merchant_debited_amount: str, optional
    :param merchant_debited_currency: Indicates the currency that is debited from the merchant. Three-letter ISO 4217 code. Relevant to refunds with foreign exchange. Response only., defaults to None
    :type merchant_debited_currency: str, optional
    :param merchant_reference_id: Merchant-defined ID. Limited to 255 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payment: D of the Payment object that the refund is credited against. String starting with payment_., defaults to None
    :type payment: str, optional
    :param payment_created_at: Time that the original payment was created, in Unix time. Response only., defaults to None
    :type payment_created_at: float, optional
    :param payment_method_type: The original payment payment method type. Use List Payment Methods by Country for a list of supported types for a country, defaults to None
    :type payment_method_type: str, optional
    :param proportional_refund: Indicates whether the refund was returned in proportion to the amounts received by the wallets in the payment. Relevant to a refund for a payment split among multiple wallets., defaults to None
    :type proportional_refund: bool, optional
    :param reason: Description of the reason for the refund, provided by the merchant., defaults to None
    :type reason: str, optional
    :param receipt_number: Number of the receipt for the refund, provided by the merchant. Response only., defaults to None
    :type receipt_number: float, optional
    :param status: Indicates the status of the refund operation, defaults to None
    :type status: str, optional
    :param updated_at: Time that this refund was last updated, in Unix time. Response only., defaults to None
    :type updated_at: float, optional
    """

    def __init__(
        self,
        amount: float = None,
        created_at: float = None,
        currency: str = None,
        ewallets: List[RefundEwallets] = None,
        failure_reason: str = None,
        fixed_side: str = None,
        fx_rate: str = None,
        id_: str = None,
        merchant_debited_amount: str = None,
        merchant_debited_currency: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payment: str = None,
        payment_created_at: float = None,
        payment_method_type: str = None,
        proportional_refund: bool = None,
        reason: str = None,
        receipt_number: float = None,
        status: str = None,
        updated_at: float = None,
    ):
        """Refund

        :param amount: Amount of the refund, in units defined by currency in the original payment. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015., defaults to None
        :type amount: float, optional
        :param created_at: Time of creation of this refund, in Unix time. Response only., defaults to None
        :type created_at: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param ewallets: An array of one object, which contains the following fields: * ewallet_id - The ID of the wallet that the money is transferred from, a string starting with ewallet_. * amount - Amount of the transaction in currency units defined in currency. * percent - A decimal number representing a percentage of the total payout. Response only., defaults to None
        :type ewallets: List[RefundEwallets], optional
        :param failure_reason: Indicates the reason that the refund failed., defaults to None
        :type failure_reason: str, optional
        :param fixed_side: Indicates whether the FX rate is fixed for the buy side or for the sell side. Relevant for refunds with foreign exchange. Response only., defaults to None
        :type fixed_side: str, optional
        :param fx_rate: Exchange rate for the transaction. When fixed_side is buy, fx_rate is the buy rate. When fixed_side is sell, fx_rate is the sell rate. Decimal number as string. Relevant to refunds with foreign exchange. Response only., defaults to None
        :type fx_rate: str, optional
        :param id_: ID of the Refund object. String starting with refund_., defaults to None
        :type id_: str, optional
        :param merchant_debited_amount: Amount debited from the merchant. Relevant to refunds with foreign exchange. Response only., defaults to None
        :type merchant_debited_amount: str, optional
        :param merchant_debited_currency: Indicates the currency that is debited from the merchant. Three-letter ISO 4217 code. Relevant to refunds with foreign exchange. Response only., defaults to None
        :type merchant_debited_currency: str, optional
        :param merchant_reference_id: Merchant-defined ID. Limited to 255 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payment: D of the Payment object that the refund is credited against. String starting with payment_., defaults to None
        :type payment: str, optional
        :param payment_created_at: Time that the original payment was created, in Unix time. Response only., defaults to None
        :type payment_created_at: float, optional
        :param payment_method_type: The original payment payment method type. Use List Payment Methods by Country for a list of supported types for a country, defaults to None
        :type payment_method_type: str, optional
        :param proportional_refund: Indicates whether the refund was returned in proportion to the amounts received by the wallets in the payment. Relevant to a refund for a payment split among multiple wallets., defaults to None
        :type proportional_refund: bool, optional
        :param reason: Description of the reason for the refund, provided by the merchant., defaults to None
        :type reason: str, optional
        :param receipt_number: Number of the receipt for the refund, provided by the merchant. Response only., defaults to None
        :type receipt_number: float, optional
        :param status: Indicates the status of the refund operation, defaults to None
        :type status: str, optional
        :param updated_at: Time that this refund was last updated, in Unix time. Response only., defaults to None
        :type updated_at: float, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.ewallets = self._define_list(ewallets, RefundEwallets)
        self.failure_reason = self._define_str(
            "failure_reason", failure_reason, nullable=True
        )
        self.fixed_side = self._define_str("fixed_side", fixed_side, nullable=True)
        self.fx_rate = self._define_str("fx_rate", fx_rate, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.merchant_debited_amount = self._define_str(
            "merchant_debited_amount", merchant_debited_amount, nullable=True
        )
        self.merchant_debited_currency = self._define_str(
            "merchant_debited_currency", merchant_debited_currency, nullable=True
        )
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.payment = self._define_str("payment", payment, nullable=True)
        self.payment_created_at = self._define_number(
            "payment_created_at", payment_created_at, nullable=True
        )
        self.payment_method_type = self._define_str(
            "payment_method_type", payment_method_type, nullable=True
        )
        self.proportional_refund = proportional_refund
        self.reason = self._define_str("reason", reason, nullable=True)
        self.receipt_number = self._define_number(
            "receipt_number", receipt_number, nullable=True
        )
        self.status = self._define_str("status", status, nullable=True)
        self.updated_at = self._define_number("updated_at", updated_at, nullable=True)
