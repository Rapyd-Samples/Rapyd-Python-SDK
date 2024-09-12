from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address import Address
from .dispute import Dispute
from .payment_ewallets import PaymentEwallets
from .payment_instructions import PaymentInstructions
from .next_action import NextAction
from .outcome import Outcome
from .fee import Fee
from .payment_refunds import PaymentRefunds
from .payment_status import PaymentStatus


class PaymentMethodTypeCategory(Enum):
    """An enumeration representing different categories.

    :cvar BANKTRANSFER: "bank_transfer"
    :vartype BANKTRANSFER: str
    :cvar BANKREDIRECT: "bank_redirect"
    :vartype BANKREDIRECT: str
    :cvar CARD: "card"
    :vartype CARD: str
    :cvar CASH: "cash"
    :vartype CASH: str
    :cvar EWALLET: "ewallet"
    :vartype EWALLET: str
    """

    BANKTRANSFER = "bank_transfer"
    BANKREDIRECT = "bank_redirect"
    CARD = "card"
    CASH = "cash"
    EWALLET = "ewallet"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, PaymentMethodTypeCategory._member_map_.values())
        )


@JsonMap({"id_": "id"})
class Payment(BaseModel):
    """Collects money from a payment method and deposits it into one or more Rapyd Wallets

    :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
    :type address: Address, optional
    :param amount: The amount received by the recipient, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. To verify a card, set to 0., defaults to None
    :type amount: float, optional
    :param auth_code: Indicates that the card payment was authorized by the card network., defaults to None
    :type auth_code: str, optional
    :param cancel_reason: Reason for cancellation or reversal of a payment. Response only., defaults to None
    :type cancel_reason: str, optional
    :param captured: Indicates whether the payment has been successfully captured. Response only., defaults to None
    :type captured: bool, optional
    :param complete_payment_url: URL where the customer is redirected for final steps in completing the operation. Provided by the clientRelevant to bank redirect payment methods, defaults to None
    :type complete_payment_url: str, optional
    :param country_code: country_code, defaults to None
    :type country_code: str, optional
    :param created_at: Time of creation of the payment, in Unix time. Response only., defaults to None
    :type created_at: int, optional
    :param currency_code: currency_code, defaults to None
    :type currency_code: str, optional
    :param customer_token: ID of the customer who is making the payment. String starting with cus_. When a payment is created without an existing customer, the platform creates an anonymous customer with no payment methods. Response only., defaults to None
    :type customer_token: str, optional
    :param description: Description of the payment, defaults to None
    :type description: str, optional
    :param dispute: Describes the fields contained in REST messages and webhooks for disputes of payments., defaults to None
    :type dispute: Dispute, optional
    :param error_code: Relevant error message (with an underscore between words) and ID number of the error. Response only., defaults to None
    :type error_code: str, optional
    :param error_payment_url: URL where the customer is redirected in case of an error in the operation. Provided by the client.Relevant to bank redirect payment methods, defaults to None
    :type error_payment_url: str, optional
    :param escrow: Describes the escrow. Relevant when the payment is created with escrow set to true. Response only., defaults to None
    :type escrow: dict, optional
    :param ewallet_id: ID of the wallet that the money is paid into. String starting with ewallet_. Relevant when the request includes a single wallet. Response only., defaults to None
    :type ewallet_id: str, optional
    :param ewallets: Specifies the wallets that the money is collected into. If this is left blank, the money goes into the oldest 'collection'-type client wallet. If there is no 'collection' client wallet, the money goes into the oldest 'general'-type client wallet., defaults to None
    :type ewallets: List[PaymentEwallets], optional
    :param expiration: End of the time allowed for customer to make this payment, in Unix time. Must be after the current time, defaults to None
    :type expiration: float, optional
    :param failure_code: Error code explaining the reason for failure of the payment. Response only., defaults to None
    :type failure_code: str, optional
    :param failure_message: Message to the merchant, explaining the reason for failure of the payment. Response only., defaults to None
    :type failure_message: str, optional
    :param fixed_side: Indicates whether the FX rate is fixed for the buy side (seller) or for the sell side (buyer). * buy - The currency that the Rapyd Wallet receives for goods or services. Fixed side buy relates to the seller (merchant) funds. For example, a US-based merchant wants to charge 100 USD. The buyer (customer) pays the amount in MXN that converts to 100 USD. This is the default. * sell - The currency that the buyer is charged for purchasing goods or services. Fixed side sell relates to the buyer (customer) funds. For example, a US-based merchant wants to charge a buyer 2,000 MXN and will accept whatever amount in USD that is converted from 2,000 MXN., defaults to None
    :type fixed_side: str, optional
    :param flow_type: Reserved., defaults to None
    :type flow_type: str, optional
    :param fx_rate: Exchange rate for the transaction. When fixed_side is buy, fx_rate is the buy rate. When fixed_side is sell, fx_rate is the sell rate. Decimal number as string. Response only., defaults to None
    :type fx_rate: float, optional
    :param group_payment: ID of the group payment. String starting with gp_. Relevant when the payment is part of a group payment., defaults to None
    :type group_payment: str, optional
    :param id_: ID of the payment. String starting with payment_. Response only, defaults to None
    :type id_: str, optional
    :param initiation_type: Reason for cancellation or reversal of a payment. Response only., defaults to None
    :type initiation_type: str, optional
    :param instructions: Describes how the customer makes the payment. Read-only. Contains the following fields - * name - Description of the payment method. * steps - A steps object containing a list of steps for the customer to take. Each step is named stepN, where N is an integer., defaults to None
    :type instructions: List[PaymentInstructions], optional
    :param invoice: ID of the invoice that this payment is for. String starting with inv_. Response only., defaults to None
    :type invoice: str, optional
    :param is_partial: Indicates whether the payment has been partially paid. When false, indicates that the payment is unpaid or fully paid. Response only., defaults to None
    :type is_partial: bool, optional
    :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param merchant_requested_amount: Indicates the amount paid by the payer, in units of the currency defined in merchant_requested_currency. Relevant to payments with FX. Read only., defaults to None
    :type merchant_requested_amount: str, optional
    :param merchant_requested_currency: Indicates the currency that merchant receives. Three-letter ISO 4217 code. Uppercase. Relevant to payments with FX. Response only., defaults to None
    :type merchant_requested_currency: str, optional
    :param metadata: A JSON object defined by the client in the Customer Payment Method object. Response only., defaults to None
    :type metadata: dict, optional
    :param mid: Reserved, defaults to None
    :type mid: str, optional
    :param next_action: Indicates the next action for completing the payment. Response only. One of the following values are - * 3d_verification - The next action is 3DS authentication. To simulate 3DS authentication in the sandbox, see Simulating 3DS Authentication. Relevant only to card payments. * pending_capture - The next action is pending the capture of the amount. Relevant only to card payments when the amount is not zero. * pending_confirmation - The next action is pending the confirmation for the payment. Relevant to all payment methods excluding card payment. * not_applicable - The payment has completed or the next action is not relevant., defaults to None
    :type next_action: NextAction, optional
    :param order: ID of the order that this payment is for. Read-only. Relevant when the payment is for an order., defaults to None
    :type order: str, optional
    :param original_amount: * Foreign exchange payments - The amount paid by the sender, in units of the currency defined in requested_currency, including gross transaction fees and gross FX fees. * Payments not involving foreign exchange - The amount of the payment, in units of the currency defined in currency, including gross transaction fees. Response only., defaults to None
    :type original_amount: float, optional
    :param outcome: The outcome object describes the outcome of the Rapyd Protect risk assessment, defaults to None
    :type outcome: Outcome, optional
    :param paid: Indicates whether the payment has been fully captured. Response only., defaults to None
    :type paid: bool, optional
    :param paid_at: Time of the last capture, in Unix time. Response only., defaults to None
    :type paid_at: float, optional
    :param payment_fees: payment_fees, defaults to None
    :type payment_fees: Fee, optional
    :param payment_method: payment_method ID or object. If not specified in this field, the payment method is the default payment method specified for the customer. Mandatory when there is no default payment method. For a description of the fields in the payment_method object, see Customer Payment Method Object., defaults to None
    :type payment_method: str, optional
    :param payment_method_data: Details of the payment_method_data object. See Payment Method Data Object. Response only., defaults to None
    :type payment_method_data: dict, optional
    :param payment_method_options: Object describing additional payment method fields required for the payment. These values are not saved as part of the payment method object. To determine the fields required, run Get Payment Method Required Fields., defaults to None
    :type payment_method_options: dict, optional
    :param payment_method_type: A type of payment method that a customer can use for making payments.  The payment method type has a suffix with one of the following values [_bank, _card, _cash, _ewallet], defaults to None
    :type payment_method_type: str, optional
    :param payment_method_type_category: Category of payment method type. Read-only., defaults to None
    :type payment_method_type_category: PaymentMethodTypeCategory, optional
    :param receipt_email: Email address that the receipt for this transaction is sent to, defaults to None
    :type receipt_email: str, optional
    :param receipt_number: Reserved. Response only, defaults to None
    :type receipt_number: str, optional
    :param redirect_url: URL where the customer is redirected for additional steps required for the payment. Response only. To simulate 3DS authentication in the sandbox, see Simulating 3DS Authentication, defaults to None
    :type redirect_url: str, optional
    :param refunded: Indicates whether there was a refund against this payment. Response only., defaults to None
    :type refunded: bool, optional
    :param refunded_amount: The total amount refunded against this payment, in units of the currency defined in currency. Response only., defaults to None
    :type refunded_amount: float, optional
    :param refunds: Refunds object, defaults to None
    :type refunds: PaymentRefunds, optional
    :param remitter_information: Contains the customer name and the associated bank account. This includes - * name - Name of the customer. * account_id - ID of the customer's bank account. * bank_code - SWIFT code for the customer's bank. Response only., defaults to None
    :type remitter_information: dict, optional
    :param save_payment_method: * true - Saves the card for future use. This is the default. * false - Does not save the card. Relevant when payment_method_type_category is card and the "Create Payment" request includes full card details., defaults to None
    :type save_payment_method: bool, optional
    :param statement_descriptor: A text description suitable for a customer's payment statement. Limited to 22 characters. If this field is not specified, Rapyd populates it with the name of the merchant, defaults to None
    :type statement_descriptor: str, optional
    :param status: status, defaults to None
    :type status: PaymentStatus, optional
    :param textual_codes: A set of text codes for the customer to use to complete the steps described in the instructions field. Response only.   The name of the field is the local name of the code, or some other label. For example   * code * paycode * pay_code * payid * pairing_code * payment_code * response_code, defaults to None
    :type textual_codes: dict, optional
    :param transaction_id: ID of the associated transaction. Response only, defaults to None
    :type transaction_id: str, optional
    :param visual_codes: A set of images for the customer to use to complete the steps described in the instructions field. For example, a QR code or barcode. Response only., defaults to None
    :type visual_codes: dict, optional
    """

    def __init__(
        self,
        address: Address = None,
        amount: float = None,
        auth_code: str = None,
        cancel_reason: str = None,
        captured: bool = None,
        complete_payment_url: str = None,
        country_code: str = None,
        created_at: int = None,
        currency_code: str = None,
        customer_token: str = None,
        description: str = None,
        dispute: Dispute = None,
        error_code: str = None,
        error_payment_url: str = None,
        escrow: dict = None,
        ewallet_id: str = None,
        ewallets: List[PaymentEwallets] = None,
        expiration: float = None,
        failure_code: str = None,
        failure_message: str = None,
        fixed_side: str = None,
        flow_type: str = None,
        fx_rate: float = None,
        group_payment: str = None,
        id_: str = None,
        initiation_type: str = None,
        instructions: List[PaymentInstructions] = None,
        invoice: str = None,
        is_partial: bool = None,
        merchant_reference_id: str = None,
        merchant_requested_amount: str = None,
        merchant_requested_currency: str = None,
        metadata: dict = None,
        mid: str = None,
        next_action: NextAction = None,
        order: str = None,
        original_amount: float = None,
        outcome: Outcome = None,
        paid: bool = None,
        paid_at: float = None,
        payment_fees: Fee = None,
        payment_method: str = None,
        payment_method_data: dict = None,
        payment_method_options: dict = None,
        payment_method_type: str = None,
        payment_method_type_category: PaymentMethodTypeCategory = None,
        receipt_email: str = None,
        receipt_number: str = None,
        redirect_url: str = None,
        refunded: bool = None,
        refunded_amount: float = None,
        refunds: PaymentRefunds = None,
        remitter_information: dict = None,
        save_payment_method: bool = None,
        statement_descriptor: str = None,
        status: PaymentStatus = None,
        textual_codes: dict = None,
        transaction_id: str = None,
        visual_codes: dict = None,
    ):
        """Collects money from a payment method and deposits it into one or more Rapyd Wallets

        :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
        :type address: Address, optional
        :param amount: The amount received by the recipient, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. To verify a card, set to 0., defaults to None
        :type amount: float, optional
        :param auth_code: Indicates that the card payment was authorized by the card network., defaults to None
        :type auth_code: str, optional
        :param cancel_reason: Reason for cancellation or reversal of a payment. Response only., defaults to None
        :type cancel_reason: str, optional
        :param captured: Indicates whether the payment has been successfully captured. Response only., defaults to None
        :type captured: bool, optional
        :param complete_payment_url: URL where the customer is redirected for final steps in completing the operation. Provided by the clientRelevant to bank redirect payment methods, defaults to None
        :type complete_payment_url: str, optional
        :param country_code: country_code, defaults to None
        :type country_code: str, optional
        :param created_at: Time of creation of the payment, in Unix time. Response only., defaults to None
        :type created_at: int, optional
        :param currency_code: currency_code, defaults to None
        :type currency_code: str, optional
        :param customer_token: ID of the customer who is making the payment. String starting with cus_. When a payment is created without an existing customer, the platform creates an anonymous customer with no payment methods. Response only., defaults to None
        :type customer_token: str, optional
        :param description: Description of the payment, defaults to None
        :type description: str, optional
        :param dispute: Describes the fields contained in REST messages and webhooks for disputes of payments., defaults to None
        :type dispute: Dispute, optional
        :param error_code: Relevant error message (with an underscore between words) and ID number of the error. Response only., defaults to None
        :type error_code: str, optional
        :param error_payment_url: URL where the customer is redirected in case of an error in the operation. Provided by the client.Relevant to bank redirect payment methods, defaults to None
        :type error_payment_url: str, optional
        :param escrow: Describes the escrow. Relevant when the payment is created with escrow set to true. Response only., defaults to None
        :type escrow: dict, optional
        :param ewallet_id: ID of the wallet that the money is paid into. String starting with ewallet_. Relevant when the request includes a single wallet. Response only., defaults to None
        :type ewallet_id: str, optional
        :param ewallets: Specifies the wallets that the money is collected into. If this is left blank, the money goes into the oldest 'collection'-type client wallet. If there is no 'collection' client wallet, the money goes into the oldest 'general'-type client wallet., defaults to None
        :type ewallets: List[PaymentEwallets], optional
        :param expiration: End of the time allowed for customer to make this payment, in Unix time. Must be after the current time, defaults to None
        :type expiration: float, optional
        :param failure_code: Error code explaining the reason for failure of the payment. Response only., defaults to None
        :type failure_code: str, optional
        :param failure_message: Message to the merchant, explaining the reason for failure of the payment. Response only., defaults to None
        :type failure_message: str, optional
        :param fixed_side: Indicates whether the FX rate is fixed for the buy side (seller) or for the sell side (buyer). * buy - The currency that the Rapyd Wallet receives for goods or services. Fixed side buy relates to the seller (merchant) funds. For example, a US-based merchant wants to charge 100 USD. The buyer (customer) pays the amount in MXN that converts to 100 USD. This is the default. * sell - The currency that the buyer is charged for purchasing goods or services. Fixed side sell relates to the buyer (customer) funds. For example, a US-based merchant wants to charge a buyer 2,000 MXN and will accept whatever amount in USD that is converted from 2,000 MXN., defaults to None
        :type fixed_side: str, optional
        :param flow_type: Reserved., defaults to None
        :type flow_type: str, optional
        :param fx_rate: Exchange rate for the transaction. When fixed_side is buy, fx_rate is the buy rate. When fixed_side is sell, fx_rate is the sell rate. Decimal number as string. Response only., defaults to None
        :type fx_rate: float, optional
        :param group_payment: ID of the group payment. String starting with gp_. Relevant when the payment is part of a group payment., defaults to None
        :type group_payment: str, optional
        :param id_: ID of the payment. String starting with payment_. Response only, defaults to None
        :type id_: str, optional
        :param initiation_type: Reason for cancellation or reversal of a payment. Response only., defaults to None
        :type initiation_type: str, optional
        :param instructions: Describes how the customer makes the payment. Read-only. Contains the following fields - * name - Description of the payment method. * steps - A steps object containing a list of steps for the customer to take. Each step is named stepN, where N is an integer., defaults to None
        :type instructions: List[PaymentInstructions], optional
        :param invoice: ID of the invoice that this payment is for. String starting with inv_. Response only., defaults to None
        :type invoice: str, optional
        :param is_partial: Indicates whether the payment has been partially paid. When false, indicates that the payment is unpaid or fully paid. Response only., defaults to None
        :type is_partial: bool, optional
        :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param merchant_requested_amount: Indicates the amount paid by the payer, in units of the currency defined in merchant_requested_currency. Relevant to payments with FX. Read only., defaults to None
        :type merchant_requested_amount: str, optional
        :param merchant_requested_currency: Indicates the currency that merchant receives. Three-letter ISO 4217 code. Uppercase. Relevant to payments with FX. Response only., defaults to None
        :type merchant_requested_currency: str, optional
        :param metadata: A JSON object defined by the client in the Customer Payment Method object. Response only., defaults to None
        :type metadata: dict, optional
        :param mid: Reserved, defaults to None
        :type mid: str, optional
        :param next_action: Indicates the next action for completing the payment. Response only. One of the following values are - * 3d_verification - The next action is 3DS authentication. To simulate 3DS authentication in the sandbox, see Simulating 3DS Authentication. Relevant only to card payments. * pending_capture - The next action is pending the capture of the amount. Relevant only to card payments when the amount is not zero. * pending_confirmation - The next action is pending the confirmation for the payment. Relevant to all payment methods excluding card payment. * not_applicable - The payment has completed or the next action is not relevant., defaults to None
        :type next_action: NextAction, optional
        :param order: ID of the order that this payment is for. Read-only. Relevant when the payment is for an order., defaults to None
        :type order: str, optional
        :param original_amount: * Foreign exchange payments - The amount paid by the sender, in units of the currency defined in requested_currency, including gross transaction fees and gross FX fees. * Payments not involving foreign exchange - The amount of the payment, in units of the currency defined in currency, including gross transaction fees. Response only., defaults to None
        :type original_amount: float, optional
        :param outcome: The outcome object describes the outcome of the Rapyd Protect risk assessment, defaults to None
        :type outcome: Outcome, optional
        :param paid: Indicates whether the payment has been fully captured. Response only., defaults to None
        :type paid: bool, optional
        :param paid_at: Time of the last capture, in Unix time. Response only., defaults to None
        :type paid_at: float, optional
        :param payment_fees: payment_fees, defaults to None
        :type payment_fees: Fee, optional
        :param payment_method: payment_method ID or object. If not specified in this field, the payment method is the default payment method specified for the customer. Mandatory when there is no default payment method. For a description of the fields in the payment_method object, see Customer Payment Method Object., defaults to None
        :type payment_method: str, optional
        :param payment_method_data: Details of the payment_method_data object. See Payment Method Data Object. Response only., defaults to None
        :type payment_method_data: dict, optional
        :param payment_method_options: Object describing additional payment method fields required for the payment. These values are not saved as part of the payment method object. To determine the fields required, run Get Payment Method Required Fields., defaults to None
        :type payment_method_options: dict, optional
        :param payment_method_type: A type of payment method that a customer can use for making payments.  The payment method type has a suffix with one of the following values [_bank, _card, _cash, _ewallet], defaults to None
        :type payment_method_type: str, optional
        :param payment_method_type_category: Category of payment method type. Read-only., defaults to None
        :type payment_method_type_category: PaymentMethodTypeCategory, optional
        :param receipt_email: Email address that the receipt for this transaction is sent to, defaults to None
        :type receipt_email: str, optional
        :param receipt_number: Reserved. Response only, defaults to None
        :type receipt_number: str, optional
        :param redirect_url: URL where the customer is redirected for additional steps required for the payment. Response only. To simulate 3DS authentication in the sandbox, see Simulating 3DS Authentication, defaults to None
        :type redirect_url: str, optional
        :param refunded: Indicates whether there was a refund against this payment. Response only., defaults to None
        :type refunded: bool, optional
        :param refunded_amount: The total amount refunded against this payment, in units of the currency defined in currency. Response only., defaults to None
        :type refunded_amount: float, optional
        :param refunds: Refunds object, defaults to None
        :type refunds: PaymentRefunds, optional
        :param remitter_information: Contains the customer name and the associated bank account. This includes - * name - Name of the customer. * account_id - ID of the customer's bank account. * bank_code - SWIFT code for the customer's bank. Response only., defaults to None
        :type remitter_information: dict, optional
        :param save_payment_method: * true - Saves the card for future use. This is the default. * false - Does not save the card. Relevant when payment_method_type_category is card and the "Create Payment" request includes full card details., defaults to None
        :type save_payment_method: bool, optional
        :param statement_descriptor: A text description suitable for a customer's payment statement. Limited to 22 characters. If this field is not specified, Rapyd populates it with the name of the merchant, defaults to None
        :type statement_descriptor: str, optional
        :param status: status, defaults to None
        :type status: PaymentStatus, optional
        :param textual_codes: A set of text codes for the customer to use to complete the steps described in the instructions field. Response only.   The name of the field is the local name of the code, or some other label. For example   * code * paycode * pay_code * payid * pairing_code * payment_code * response_code, defaults to None
        :type textual_codes: dict, optional
        :param transaction_id: ID of the associated transaction. Response only, defaults to None
        :type transaction_id: str, optional
        :param visual_codes: A set of images for the customer to use to complete the steps described in the instructions field. For example, a QR code or barcode. Response only., defaults to None
        :type visual_codes: dict, optional
        """
        self.address = self._define_object(address, Address)
        self.amount = self._define_number("amount", amount, nullable=True)
        self.auth_code = self._define_str("auth_code", auth_code, nullable=True)
        self.cancel_reason = self._define_str(
            "cancel_reason", cancel_reason, nullable=True
        )
        self.captured = captured
        self.complete_payment_url = self._define_str(
            "complete_payment_url", complete_payment_url, nullable=True
        )
        self.country_code = self._define_str(
            "country_code",
            country_code,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency_code = self._define_str(
            "currency_code",
            currency_code,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.customer_token = self._define_str(
            "customer_token", customer_token, nullable=True
        )
        self.description = self._define_str("description", description, nullable=True)
        self.dispute = self._define_object(dispute, Dispute)
        self.error_code = self._define_str("error_code", error_code, nullable=True)
        self.error_payment_url = self._define_str(
            "error_payment_url", error_payment_url, nullable=True
        )
        self.escrow = escrow
        self.ewallet_id = self._define_str("ewallet_id", ewallet_id, nullable=True)
        self.ewallets = self._define_list(ewallets, PaymentEwallets)
        self.expiration = self._define_number("expiration", expiration, nullable=True)
        self.failure_code = self._define_str(
            "failure_code", failure_code, nullable=True
        )
        self.failure_message = self._define_str(
            "failure_message", failure_message, nullable=True
        )
        self.fixed_side = self._define_str("fixed_side", fixed_side, nullable=True)
        self.flow_type = self._define_str("flow_type", flow_type, nullable=True)
        self.fx_rate = self._define_number("fx_rate", fx_rate, nullable=True)
        self.group_payment = self._define_str(
            "group_payment", group_payment, nullable=True
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.initiation_type = self._define_str(
            "initiation_type", initiation_type, nullable=True
        )
        self.instructions = self._define_list(instructions, PaymentInstructions)
        self.invoice = self._define_str("invoice", invoice, nullable=True)
        self.is_partial = is_partial
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.merchant_requested_amount = self._define_str(
            "merchant_requested_amount", merchant_requested_amount, nullable=True
        )
        self.merchant_requested_currency = self._define_str(
            "merchant_requested_currency", merchant_requested_currency, nullable=True
        )
        self.metadata = metadata
        self.mid = self._define_str("mid", mid, nullable=True)
        self.next_action = (
            self._enum_matching(next_action, NextAction.list(), "next_action")
            if next_action
            else None
        )
        self.order = self._define_str("order", order, nullable=True)
        self.original_amount = self._define_number(
            "original_amount", original_amount, nullable=True
        )
        self.outcome = self._define_object(outcome, Outcome)
        self.paid = paid
        self.paid_at = self._define_number("paid_at", paid_at, nullable=True)
        self.payment_fees = self._define_object(payment_fees, Fee)
        self.payment_method = self._define_str(
            "payment_method", payment_method, nullable=True
        )
        self.payment_method_data = payment_method_data
        self.payment_method_options = payment_method_options
        self.payment_method_type = self._define_str(
            "payment_method_type", payment_method_type, nullable=True
        )
        self.payment_method_type_category = (
            self._enum_matching(
                payment_method_type_category,
                PaymentMethodTypeCategory.list(),
                "payment_method_type_category",
            )
            if payment_method_type_category
            else None
        )
        self.receipt_email = self._define_str(
            "receipt_email", receipt_email, nullable=True
        )
        self.receipt_number = self._define_str(
            "receipt_number", receipt_number, nullable=True
        )
        self.redirect_url = self._define_str(
            "redirect_url", redirect_url, nullable=True
        )
        self.refunded = refunded
        self.refunded_amount = self._define_number(
            "refunded_amount", refunded_amount, nullable=True
        )
        self.refunds = self._define_object(refunds, PaymentRefunds)
        self.remitter_information = remitter_information
        self.save_payment_method = save_payment_method
        self.statement_descriptor = self._define_str(
            "statement_descriptor", statement_descriptor, nullable=True
        )
        self.status = (
            self._enum_matching(status, PaymentStatus.list(), "status")
            if status
            else None
        )
        self.textual_codes = textual_codes
        self.transaction_id = self._define_str(
            "transaction_id", transaction_id, nullable=True
        )
        self.visual_codes = visual_codes
