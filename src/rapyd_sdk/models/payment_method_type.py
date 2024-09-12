from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payment_amount_range_per_currency_inner import PaymentAmountRangePerCurrencyInner
from .category import Category
from .field import Field


class PaymentMethodTypePaymentFlowType(Enum):
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
            map(
                lambda x: x.value,
                PaymentMethodTypePaymentFlowType._member_map_.values(),
            )
        )


@JsonMap({"type_": "type"})
class PaymentMethodType(BaseModel):
    """A type of payment method that a customer can use for making payments.

    :param amount_range_per_currency: Indicates the amount range for the payment method's currencies. Each object contains the following fields:* currency - Three-letter ISO 4217 format of currency* maximum_amount - The maximum payment amount* minimum_amount - The minimum payment amount, defaults to None
    :type amount_range_per_currency: List[PaymentAmountRangePerCurrencyInner], optional
    :param category: category, defaults to None
    :type category: Category, optional
    :param country: country, defaults to None
    :type country: str, optional
    :param currencies: currencies, defaults to None
    :type currencies: List[str], optional
    :param image: A URL to the image of the icon for the type of payment method. Response only, defaults to None
    :type image: str, optional
    :param is_cancelable: Indicates whether a payment made with this payment method can be canceled. Response only, defaults to None
    :type is_cancelable: bool, optional
    :param is_expirable: Indicates whether the merchant can set an expiration time for the customer to complete the payment. Response only, defaults to None
    :type is_expirable: bool, optional
    :param is_online: Indicates whether the payment is completed immediately online. Response only, defaults to None
    :type is_online: bool, optional
    :param is_refundable: Indicates whether the payment method type supports refunds, defaults to None
    :type is_refundable: bool, optional
    :param is_tokenizable: Indicates whether the token of the payment method can be used in a collect operation, defaults to None
    :type is_tokenizable: bool, optional
    :param is_virtual: Indicates whether a Web-based version of the payment method type exists, defaults to None
    :type is_virtual: bool, optional
    :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
    :type maximum_expiration_seconds: float, optional
    :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
    :type minimum_expiration_seconds: float, optional
    :param multiple_overage_allowed: Indicates whether multiple overage charges are allowed for this payment method type, defaults to None
    :type multiple_overage_allowed: bool, optional
    :param name: The name of the payment method, in user-friendly terms. For example, Ireland Visa card. Response only, defaults to None
    :type name: str, optional
    :param payment_flow_type: payment_flow_type, defaults to None
    :type payment_flow_type: PaymentMethodTypePaymentFlowType, optional
    :param payment_options: payment_options, defaults to None
    :type payment_options: List[Field], optional
    :param status: Indicates the status of the payment method. One of the following value is 1 means the payment_method_type is Valid, defaults to None
    :type status: str, optional
    :param supported_digital_wallet_providers: Describes the digital wallet providers that support the payment method. These providers may include apple_pay and google_pay, defaults to None
    :type supported_digital_wallet_providers: List[str], optional
    :param type_: Type of the payment method. For example, it_visa_card, defaults to None
    :type type_: str, optional
    :param virtual_payment_method_type: Indicates the name of the Web-based version of this payment method type, defaults to None
    :type virtual_payment_method_type: str, optional
    :param is_restricted: Indicates if the payment method type restricted or not., defaults to None
    :type is_restricted: bool, optional
    :param supports_subscription: Indicates if the payment method type supports subscription., defaults to None
    :type supports_subscription: bool, optional
    """

    def __init__(
        self,
        amount_range_per_currency: List[PaymentAmountRangePerCurrencyInner] = None,
        category: Category = None,
        country: str = None,
        currencies: List[str] = None,
        image: str = None,
        is_cancelable: bool = None,
        is_expirable: bool = None,
        is_online: bool = None,
        is_refundable: bool = None,
        is_tokenizable: bool = None,
        is_virtual: bool = None,
        maximum_expiration_seconds: float = None,
        minimum_expiration_seconds: float = None,
        multiple_overage_allowed: bool = None,
        name: str = None,
        payment_flow_type: PaymentMethodTypePaymentFlowType = None,
        payment_options: List[Field] = None,
        status: str = None,
        supported_digital_wallet_providers: List[str] = None,
        type_: str = None,
        virtual_payment_method_type: str = None,
        is_restricted: bool = None,
        supports_subscription: bool = None,
    ):
        """A type of payment method that a customer can use for making payments.

        :param amount_range_per_currency: Indicates the amount range for the payment method's currencies. Each object contains the following fields:* currency - Three-letter ISO 4217 format of currency* maximum_amount - The maximum payment amount* minimum_amount - The minimum payment amount, defaults to None
        :type amount_range_per_currency: List[PaymentAmountRangePerCurrencyInner], optional
        :param category: category, defaults to None
        :type category: Category, optional
        :param country: country, defaults to None
        :type country: str, optional
        :param currencies: currencies, defaults to None
        :type currencies: List[str], optional
        :param image: A URL to the image of the icon for the type of payment method. Response only, defaults to None
        :type image: str, optional
        :param is_cancelable: Indicates whether a payment made with this payment method can be canceled. Response only, defaults to None
        :type is_cancelable: bool, optional
        :param is_expirable: Indicates whether the merchant can set an expiration time for the customer to complete the payment. Response only, defaults to None
        :type is_expirable: bool, optional
        :param is_online: Indicates whether the payment is completed immediately online. Response only, defaults to None
        :type is_online: bool, optional
        :param is_refundable: Indicates whether the payment method type supports refunds, defaults to None
        :type is_refundable: bool, optional
        :param is_tokenizable: Indicates whether the token of the payment method can be used in a collect operation, defaults to None
        :type is_tokenizable: bool, optional
        :param is_virtual: Indicates whether a Web-based version of the payment method type exists, defaults to None
        :type is_virtual: bool, optional
        :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
        :type maximum_expiration_seconds: float, optional
        :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payment. Relevant when is_expirable is true, defaults to None
        :type minimum_expiration_seconds: float, optional
        :param multiple_overage_allowed: Indicates whether multiple overage charges are allowed for this payment method type, defaults to None
        :type multiple_overage_allowed: bool, optional
        :param name: The name of the payment method, in user-friendly terms. For example, Ireland Visa card. Response only, defaults to None
        :type name: str, optional
        :param payment_flow_type: payment_flow_type, defaults to None
        :type payment_flow_type: PaymentMethodTypePaymentFlowType, optional
        :param payment_options: payment_options, defaults to None
        :type payment_options: List[Field], optional
        :param status: Indicates the status of the payment method. One of the following value is 1 means the payment_method_type is Valid, defaults to None
        :type status: str, optional
        :param supported_digital_wallet_providers: Describes the digital wallet providers that support the payment method. These providers may include apple_pay and google_pay, defaults to None
        :type supported_digital_wallet_providers: List[str], optional
        :param type_: Type of the payment method. For example, it_visa_card, defaults to None
        :type type_: str, optional
        :param virtual_payment_method_type: Indicates the name of the Web-based version of this payment method type, defaults to None
        :type virtual_payment_method_type: str, optional
        :param is_restricted: Indicates if the payment method type restricted or not., defaults to None
        :type is_restricted: bool, optional
        :param supports_subscription: Indicates if the payment method type supports subscription., defaults to None
        :type supports_subscription: bool, optional
        """
        self.amount_range_per_currency = self._define_list(
            amount_range_per_currency, PaymentAmountRangePerCurrencyInner
        )
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.country = self._define_str(
            "country",
            country,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.currencies = currencies
        self.image = self._define_str("image", image, nullable=True)
        self.is_cancelable = is_cancelable
        self.is_expirable = is_expirable
        self.is_online = is_online
        self.is_refundable = is_refundable
        self.is_tokenizable = is_tokenizable
        self.is_virtual = is_virtual
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
                PaymentMethodTypePaymentFlowType.list(),
                "payment_flow_type",
            )
            if payment_flow_type
            else None
        )
        self.payment_options = self._define_list(payment_options, Field)
        self.status = self._define_str("status", status, nullable=True)
        self.supported_digital_wallet_providers = supported_digital_wallet_providers
        self.type_ = self._define_str("type_", type_, nullable=True)
        self.virtual_payment_method_type = self._define_str(
            "virtual_payment_method_type", virtual_payment_method_type, nullable=True
        )
        self.is_restricted = is_restricted
        self.supports_subscription = supports_subscription
