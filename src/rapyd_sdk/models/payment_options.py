from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address import Address
from .payment_amount_range_per_currency_inner import PaymentAmountRangePerCurrencyInner
from .bin_details import BinDetails
from .category import Category
from .condition import Condition
from .customer import Customer


class PaymentOptionsPaymentFlowType(Enum):
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
            map(lambda x: x.value, PaymentOptionsPaymentFlowType._member_map_.values())
        )


@JsonMap({})
class PaymentOptions(BaseModel):
    """A payment method type is a type of payment method that any customer can use, for example, ee_mastercard_card, Mastercard for Estonia. When it is added to a customer profile, it becomes a payment method that is specific to that one customer. The name of the payment method type starts with a prefix for the country, the 2-letter ISO 3166-1 alpha-2 code. If the payment method is valid in multiple countries, the prefix is xx_. The payment method type has a suffix with one of the following values - _bank - Bank transfer or bank redirect _card - Credit card, debit card or other card _cash - Cash _ewallet - Local eWallet

    :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
    :type address: Address, optional
    :param amount_range_per_currency: Indicates the amount range for the payment method's currencies. Each object contains the following fields:* currency - Three-letter ISO 4217 format of currency* maximum_amount - The maximum payment amount* minimum_amount - The minimum payment amount, defaults to None
    :type amount_range_per_currency: List[PaymentAmountRangePerCurrencyInner], optional
    :param bin_details: Bank Identification Number (BIN) details. Read-only. Object containing the following fields - * bin_number - BIN number * country - The two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. * funding - Type of card funding. One of the following [credit, debit, prepaid, unknown] * bank - Name of the issuing bank. Relevant to cards, defaults to None
    :type bin_details: BinDetails, optional
    :param category: category, defaults to None
    :type category: Category, optional
    :param conditions: conditions, defaults to None
    :type conditions: List[Condition], optional
    :param country: country, defaults to None
    :type country: str, optional
    :param currencies: currencies, defaults to None
    :type currencies: List[str], optional
    :param customer: customer, defaults to None
    :type customer: Customer, optional
    :param fingerprint: Hash of the card number, expiration date and CVV. Read-only. Relevant to cards, defaults to None
    :type fingerprint: str, optional
    :param image: A URL to the image of the icon for the type of payment method. Response only, defaults to None
    :type image: str, optional
    :param instructions: Instructions for the field. Response only, defaults to None
    :type instructions: str, optional
    :param is_cancelable: Indicates whether a payment made with this payment method can be canceled. Response only, defaults to None
    :type is_cancelable: bool, optional
    :param is_expirable: Indicates whether the merchant can set an expiration time for the customer to complete the payment. Response only, defaults to None
    :type is_expirable: bool, optional
    :param is_online: Indicates whether the payment is completed immediately online. Response only, defaults to None
    :type is_online: bool, optional
    :param is_refundable: Indicates whether the payment method type supports refunds, defaults to None
    :type is_refundable: bool, optional
    :param is_required: Whether the field is required for using the payment method. When the conditions defined by conditions are met, the field is required even though the value of is_required is false. Response only, defaults to None
    :type is_required: bool, optional
    :param is_tokenizable: Indicates whether the token of the payment method can be used in a collect operation, defaults to None
    :type is_tokenizable: bool, optional
    :param is_virtual: Indicates whether a Web-based version of the payment method type exists, defaults to None
    :type is_virtual: bool, optional
    :param last4: last4 - Last four digits of the card number. Read-only. Relevant to cards, defaults to None
    :type last4: str, optional
    :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true. Response only, defaults to None
    :type maximum_expiration_seconds: int, optional
    :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true. Response only, defaults to None
    :type minimum_expiration_seconds: int, optional
    :param multiple_overage_allowed: Indicates whether multiple overage charges are allowed for this payment method type, defaults to None
    :type multiple_overage_allowed: bool, optional
    :param name: The name of the payment method, in user-friendly terms. For example, 'Ireland Visa card'. Response only, defaults to None
    :type name: str, optional
    :param payment_flow_type: payment_flow_type, defaults to None
    :type payment_flow_type: PaymentOptionsPaymentFlowType, optional
    """

    def __init__(
        self,
        address: Address = None,
        amount_range_per_currency: List[PaymentAmountRangePerCurrencyInner] = None,
        bin_details: BinDetails = None,
        category: Category = None,
        conditions: List[Condition] = None,
        country: str = None,
        currencies: List[str] = None,
        customer: Customer = None,
        fingerprint: str = None,
        image: str = None,
        instructions: str = None,
        is_cancelable: bool = None,
        is_expirable: bool = None,
        is_online: bool = None,
        is_refundable: bool = None,
        is_required: bool = None,
        is_tokenizable: bool = None,
        is_virtual: bool = None,
        last4: str = None,
        maximum_expiration_seconds: int = None,
        minimum_expiration_seconds: int = None,
        multiple_overage_allowed: bool = None,
        name: str = None,
        payment_flow_type: PaymentOptionsPaymentFlowType = None,
    ):
        """A payment method type is a type of payment method that any customer can use, for example, ee_mastercard_card, Mastercard for Estonia. When it is added to a customer profile, it becomes a payment method that is specific to that one customer. The name of the payment method type starts with a prefix for the country, the 2-letter ISO 3166-1 alpha-2 code. If the payment method is valid in multiple countries, the prefix is xx_. The payment method type has a suffix with one of the following values - _bank - Bank transfer or bank redirect _card - Credit card, debit card or other card _cash - Cash _ewallet - Local eWallet

        :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
        :type address: Address, optional
        :param amount_range_per_currency: Indicates the amount range for the payment method's currencies. Each object contains the following fields:* currency - Three-letter ISO 4217 format of currency* maximum_amount - The maximum payment amount* minimum_amount - The minimum payment amount, defaults to None
        :type amount_range_per_currency: List[PaymentAmountRangePerCurrencyInner], optional
        :param bin_details: Bank Identification Number (BIN) details. Read-only. Object containing the following fields - * bin_number - BIN number * country - The two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. * funding - Type of card funding. One of the following [credit, debit, prepaid, unknown] * bank - Name of the issuing bank. Relevant to cards, defaults to None
        :type bin_details: BinDetails, optional
        :param category: category, defaults to None
        :type category: Category, optional
        :param conditions: conditions, defaults to None
        :type conditions: List[Condition], optional
        :param country: country, defaults to None
        :type country: str, optional
        :param currencies: currencies, defaults to None
        :type currencies: List[str], optional
        :param customer: customer, defaults to None
        :type customer: Customer, optional
        :param fingerprint: Hash of the card number, expiration date and CVV. Read-only. Relevant to cards, defaults to None
        :type fingerprint: str, optional
        :param image: A URL to the image of the icon for the type of payment method. Response only, defaults to None
        :type image: str, optional
        :param instructions: Instructions for the field. Response only, defaults to None
        :type instructions: str, optional
        :param is_cancelable: Indicates whether a payment made with this payment method can be canceled. Response only, defaults to None
        :type is_cancelable: bool, optional
        :param is_expirable: Indicates whether the merchant can set an expiration time for the customer to complete the payment. Response only, defaults to None
        :type is_expirable: bool, optional
        :param is_online: Indicates whether the payment is completed immediately online. Response only, defaults to None
        :type is_online: bool, optional
        :param is_refundable: Indicates whether the payment method type supports refunds, defaults to None
        :type is_refundable: bool, optional
        :param is_required: Whether the field is required for using the payment method. When the conditions defined by conditions are met, the field is required even though the value of is_required is false. Response only, defaults to None
        :type is_required: bool, optional
        :param is_tokenizable: Indicates whether the token of the payment method can be used in a collect operation, defaults to None
        :type is_tokenizable: bool, optional
        :param is_virtual: Indicates whether a Web-based version of the payment method type exists, defaults to None
        :type is_virtual: bool, optional
        :param last4: last4 - Last four digits of the card number. Read-only. Relevant to cards, defaults to None
        :type last4: str, optional
        :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true. Response only, defaults to None
        :type maximum_expiration_seconds: int, optional
        :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true. Response only, defaults to None
        :type minimum_expiration_seconds: int, optional
        :param multiple_overage_allowed: Indicates whether multiple overage charges are allowed for this payment method type, defaults to None
        :type multiple_overage_allowed: bool, optional
        :param name: The name of the payment method, in user-friendly terms. For example, 'Ireland Visa card'. Response only, defaults to None
        :type name: str, optional
        :param payment_flow_type: payment_flow_type, defaults to None
        :type payment_flow_type: PaymentOptionsPaymentFlowType, optional
        """
        self.address = self._define_object(address, Address)
        self.amount_range_per_currency = self._define_list(
            amount_range_per_currency, PaymentAmountRangePerCurrencyInner
        )
        self.bin_details = self._define_object(bin_details, BinDetails)
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.conditions = self._define_list(conditions, Condition)
        self.country = self._define_str(
            "country",
            country,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.currencies = currencies
        self.customer = self._define_object(customer, Customer)
        self.fingerprint = self._define_str("fingerprint", fingerprint, nullable=True)
        self.image = self._define_str("image", image, nullable=True)
        self.instructions = self._define_str(
            "instructions", instructions, nullable=True
        )
        self.is_cancelable = is_cancelable
        self.is_expirable = is_expirable
        self.is_online = is_online
        self.is_refundable = is_refundable
        self.is_required = is_required
        self.is_tokenizable = is_tokenizable
        self.is_virtual = is_virtual
        self.last4 = self._define_str("last4", last4, nullable=True, pattern="^\d{4}$")
        self.maximum_expiration_seconds = self._define_number(
            "maximum_expiration_seconds", maximum_expiration_seconds, nullable=True
        )
        self.minimum_expiration_seconds = self._define_number(
            "minimum_expiration_seconds", minimum_expiration_seconds, nullable=True
        )
        self.multiple_overage_allowed = multiple_overage_allowed
        self.name = self._define_str("name", name, nullable=True)
        self.payment_flow_type = (
            self._enum_matching(
                payment_flow_type,
                PaymentOptionsPaymentFlowType.list(),
                "payment_flow_type",
            )
            if payment_flow_type
            else None
        )
