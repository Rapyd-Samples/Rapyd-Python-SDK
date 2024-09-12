from __future__ import annotations
from enum import Enum
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel
from .address import Address
from .client_details_object import ClientDetailsObject
from .fee import Fee
from .payment_method_type import PaymentMethodType


class InitiationType(Enum):
    """An enumeration representing different categories.

    :cvar CUSTOMERPRESENT: "customer_present"
    :vartype CUSTOMERPRESENT: str
    :cvar INSTALLMENT: "installment"
    :vartype INSTALLMENT: str
    :cvar MOTO: "moto"
    :vartype MOTO: str
    :cvar RECURRING: "recurring"
    :vartype RECURRING: str
    :cvar UNSCHEDULED: "unscheduled"
    :vartype UNSCHEDULED: str
    """

    CUSTOMERPRESENT = "customer_present"
    INSTALLMENT = "installment"
    MOTO = "moto"
    RECURRING = "recurring"
    UNSCHEDULED = "unscheduled"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, InitiationType._member_map_.values()))


class V1PaymentsBodyPaymentMethodGuard(OneOfBaseModel):
    class_list = {"str": str, "PaymentMethodType": PaymentMethodType}


V1PaymentsBodyPaymentMethod = Union[str, PaymentMethodType]


@JsonMap({})
class V1PaymentsBody(BaseModel):
    """V1PaymentsBody

    :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
    :type address: Address, optional
    :param amount: The amount received by the recipient, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. To verify a card, set to 0.
    :type amount: float
    :param capture: Determines when the payment is processed for capture. When true, the payment is captured immediately. When false, the payment is captured at a later time. Relevant to cards. Default is true., defaults to None
    :type capture: bool, optional
    :param client_details: Describes the fields in the client_details object in REST messages for payments. The client_details object describes the browser that the customer is using. The client collects this information and sends it as part of the Create Payment request. This information is used for processing the 3DS version 2 authentication of the customer. Note that Client Details information is not returned in the API response and it does not appear in any webhooks., defaults to None
    :type client_details: ClientDetailsObject, optional
    :param complete_payment_url: URL where the customer is redirected after successfully completing an operation on an external page., defaults to None
    :type complete_payment_url: str, optional
    :param currency: currency
    :type currency: str
    :param customer: string - ID of the customer who is making the payment. String starting with cus_. Required if payment_method is blank. object - Contains all required fields, defaults to None
    :type customer: str, optional
    :param description: Description of the payment, defaults to None
    :type description: str, optional
    :param error_payment_url: URL where the customer is redirected in case of an error in the operation. Provided by the client.Relevant to bank redirect payment methods, defaults to None
    :type error_payment_url: str, optional
    :param escrow: Determines whether the payment is held in escrow for later release., defaults to None
    :type escrow: bool, optional
    :param escrow_release_days: Determines the number of days after creation of the payment that funds are released from escrow. Funds are released at 5:00 pm GMT on the day indicated. Integer, range between 1-90. Default is 90., defaults to None
    :type escrow_release_days: int, optional
    :param ewallet: ID of the wallet that the money is paid into. String starting with ewallet_. Relevant when the request includes a single wallet., defaults to None
    :type ewallet: str, optional
    :param ewallets: Represents the wallets that the money is paid into. Array of objects., defaults to None
    :type ewallets: any, optional
    :param expiration: End of the time allowed for customer to make this payment, in Unix time. Must be after the current time, defaults to None
    :type expiration: float, optional
    :param fixed_side: Indicates whether the FX rate is fixed for the buy side (seller's Rapyd Wallet) or for the sell side (buyer)., defaults to None
    :type fixed_side: str, optional
    :param group_payment: ID of the group payment, a string starting with 'gp_'. Relevant to replacing a payment that failed., defaults to None
    :type group_payment: str, optional
    :param initiation_type: Describes how the transaction was initiated., defaults to None
    :type initiation_type: InitiationType, optional
    :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payment_fees: payment_fees, defaults to None
    :type payment_fees: Fee, optional
    :param payment_method: Payment Method object or ID., defaults to None
    :type payment_method: V1PaymentsBodyPaymentMethod, optional
    :param payment_method_options: Object describing additional information required for the payment. The object is returned by Get Payment Method Required Fields. Note that Transactions with 3DS authentication must be authenticated within 15 minutes, after which the possibility to authenticate expires., defaults to None
    :type payment_method_options: dict, optional
    :param receipt_email: Email address that the receipt for this transaction is sent to., defaults to None
    :type receipt_email: str, optional
    :param requested_currency: When fixed_side is sell, it is the currency received in the Rapyd Wallet. . When fixed_side is buy, it is the currency charged to the buyer (customer). Three-letter ISO 4217 code., defaults to None
    :type requested_currency: str, optional
    :param statement_descriptor: A text description that appears in the customer's bank statement., defaults to None
    :type statement_descriptor: str, optional
    """

    def __init__(
        self,
        amount: float,
        currency: str,
        address: Address = None,
        capture: bool = None,
        client_details: ClientDetailsObject = None,
        complete_payment_url: str = None,
        customer: str = None,
        description: str = None,
        error_payment_url: str = None,
        escrow: bool = None,
        escrow_release_days: int = None,
        ewallet: str = None,
        ewallets: any = None,
        expiration: float = None,
        fixed_side: str = None,
        group_payment: str = None,
        initiation_type: InitiationType = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payment_fees: Fee = None,
        payment_method: V1PaymentsBodyPaymentMethod = None,
        payment_method_options: dict = None,
        receipt_email: str = None,
        requested_currency: str = None,
        statement_descriptor: str = None,
    ):
        """V1PaymentsBody

        :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
        :type address: Address, optional
        :param amount: The amount received by the recipient, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. To verify a card, set to 0.
        :type amount: float
        :param capture: Determines when the payment is processed for capture. When true, the payment is captured immediately. When false, the payment is captured at a later time. Relevant to cards. Default is true., defaults to None
        :type capture: bool, optional
        :param client_details: Describes the fields in the client_details object in REST messages for payments. The client_details object describes the browser that the customer is using. The client collects this information and sends it as part of the Create Payment request. This information is used for processing the 3DS version 2 authentication of the customer. Note that Client Details information is not returned in the API response and it does not appear in any webhooks., defaults to None
        :type client_details: ClientDetailsObject, optional
        :param complete_payment_url: URL where the customer is redirected after successfully completing an operation on an external page., defaults to None
        :type complete_payment_url: str, optional
        :param currency: currency
        :type currency: str
        :param customer: string - ID of the customer who is making the payment. String starting with cus_. Required if payment_method is blank. object - Contains all required fields, defaults to None
        :type customer: str, optional
        :param description: Description of the payment, defaults to None
        :type description: str, optional
        :param error_payment_url: URL where the customer is redirected in case of an error in the operation. Provided by the client.Relevant to bank redirect payment methods, defaults to None
        :type error_payment_url: str, optional
        :param escrow: Determines whether the payment is held in escrow for later release., defaults to None
        :type escrow: bool, optional
        :param escrow_release_days: Determines the number of days after creation of the payment that funds are released from escrow. Funds are released at 5:00 pm GMT on the day indicated. Integer, range between 1-90. Default is 90., defaults to None
        :type escrow_release_days: int, optional
        :param ewallet: ID of the wallet that the money is paid into. String starting with ewallet_. Relevant when the request includes a single wallet., defaults to None
        :type ewallet: str, optional
        :param ewallets: Represents the wallets that the money is paid into. Array of objects., defaults to None
        :type ewallets: any, optional
        :param expiration: End of the time allowed for customer to make this payment, in Unix time. Must be after the current time, defaults to None
        :type expiration: float, optional
        :param fixed_side: Indicates whether the FX rate is fixed for the buy side (seller's Rapyd Wallet) or for the sell side (buyer)., defaults to None
        :type fixed_side: str, optional
        :param group_payment: ID of the group payment, a string starting with 'gp_'. Relevant to replacing a payment that failed., defaults to None
        :type group_payment: str, optional
        :param initiation_type: Describes how the transaction was initiated., defaults to None
        :type initiation_type: InitiationType, optional
        :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payment_fees: payment_fees, defaults to None
        :type payment_fees: Fee, optional
        :param payment_method: Payment Method object or ID., defaults to None
        :type payment_method: V1PaymentsBodyPaymentMethod, optional
        :param payment_method_options: Object describing additional information required for the payment. The object is returned by Get Payment Method Required Fields. Note that Transactions with 3DS authentication must be authenticated within 15 minutes, after which the possibility to authenticate expires., defaults to None
        :type payment_method_options: dict, optional
        :param receipt_email: Email address that the receipt for this transaction is sent to., defaults to None
        :type receipt_email: str, optional
        :param requested_currency: When fixed_side is sell, it is the currency received in the Rapyd Wallet. . When fixed_side is buy, it is the currency charged to the buyer (customer). Three-letter ISO 4217 code., defaults to None
        :type requested_currency: str, optional
        :param statement_descriptor: A text description that appears in the customer's bank statement., defaults to None
        :type statement_descriptor: str, optional
        """
        self.address = self._define_object(address, Address)
        self.amount = amount
        self.capture = capture
        self.client_details = self._define_object(client_details, ClientDetailsObject)
        self.complete_payment_url = self._define_str(
            "complete_payment_url", complete_payment_url, nullable=True
        )
        self.currency = self._define_str(
            "currency",
            currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.customer = self._define_str("customer", customer, nullable=True)
        self.description = self._define_str("description", description, nullable=True)
        self.error_payment_url = self._define_str(
            "error_payment_url", error_payment_url, nullable=True
        )
        self.escrow = escrow
        self.escrow_release_days = self._define_number(
            "escrow_release_days", escrow_release_days, nullable=True
        )
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.ewallets = ewallets
        self.expiration = self._define_number("expiration", expiration, nullable=True)
        self.fixed_side = self._define_str("fixed_side", fixed_side, nullable=True)
        self.group_payment = self._define_str(
            "group_payment", group_payment, nullable=True
        )
        self.initiation_type = (
            self._enum_matching(
                initiation_type, InitiationType.list(), "initiation_type"
            )
            if initiation_type
            else None
        )
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.payment_fees = self._define_object(payment_fees, Fee)
        self.payment_method = V1PaymentsBodyPaymentMethodGuard.return_one_of(
            payment_method
        )
        self.payment_method_options = payment_method_options
        self.receipt_email = self._define_str(
            "receipt_email", receipt_email, nullable=True
        )
        self.requested_currency = self._define_str(
            "requested_currency", requested_currency, nullable=True
        )
        self.statement_descriptor = self._define_str(
            "statement_descriptor", statement_descriptor, nullable=True
        )
