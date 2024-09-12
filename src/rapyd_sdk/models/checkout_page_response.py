from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .merchant_customer_support import MerchantCustomerSupport
from .hosted_page_status import HostedPageStatus
from .hosted_page_additional_response_cart_items import (
    HostedPageAdditionalResponseCartItems,
)
from .hosted_page_additional_response_custom_elements import (
    HostedPageAdditionalResponseCustomElements,
)


@JsonMap({"id_": "id"})
class CheckoutPageResponse(BaseModel):
    """CheckoutPageResponse

    :param language: Determines the default language of the hosted page. When this parameter is null, the language of the user's browser is used. If the language of the user's browser cannot be determined, the default language is English, defaults to None
    :type language: str, optional
    :param merchant_alias: Reserved, the default language is Rapyd, defaults to None
    :type merchant_alias: str, optional
    :param merchant_color: Color of the call-to-action (CTA) button on the hosted page. To configure this field, use the Client Portal, defaults to None
    :type merchant_color: str, optional
    :param merchant_customer_support: merchant_customer_support, defaults to None
    :type merchant_customer_support: MerchantCustomerSupport, optional
    :param merchant_logo: URL for the image of the client's logo. To configure this field, use the Client Portal, defaults to None
    :type merchant_logo: str, optional
    :param merchant_website: The URL where the customer is redirected after exiting the hosted page. Relevant when one or both of the following fields is unset: * cancel_url* complete_url. To configure this field, use the Client Portal, defaults to None
    :type merchant_website: str, optional
    :param redirect_url: URL of the hosted page that is shown to the customer., defaults to None
    :type redirect_url: str, optional
    :param merchant_terms: URL for the client's terms and conditions. To configure this field, use the Client Porta, defaults to None
    :type merchant_terms: str, optional
    :param merchant_privacy_policy: URL for the terms and conditions of the agreement between the client and the client’s customers. To configure this field, use the Client Portal., defaults to None
    :type merchant_privacy_policy: str, optional
    :param page_expiration: Length of time for the payment to be completed after it is created, measured in seconds. When both expiration and payment_expiration are set, the payment expires at the earlier time., defaults to None
    :type page_expiration: float, optional
    :param status: Status of the hosted page. One of the following: NEW - The hosted page was created. DON - Done. The card was added to the customer profile. EXP - The hosted page expired. , defaults to None
    :type status: HostedPageStatus, optional
    :param account_funding_transaction: Details of an account funding transaction (AFT), which transfers funds from a card to a cardholder's wallet., defaults to None
    :type account_funding_transaction: dict, optional
    :param amount: The amount of the payment, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal., defaults to None
    :type amount: float, optional
    :param cart_items: Describes the cart items that the customer is purchasing. These items are displayed at the checkout page., defaults to None
    :type cart_items: HostedPageAdditionalResponseCartItems, optional
    :param country: country, defaults to None
    :type country: str, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param customer: Description of the payment transaction. To display the description, set display_description to true in custom_elements., defaults to None
    :type customer: str, optional
    :param escrow: Determines whether the payment is held in escrow for later release., defaults to None
    :type escrow: bool, optional
    :param escrow_release_days: Determines the number of days after creation of the payment that funds are released from escrow. Funds are released at 5:00 pm GMT on the day indicated. Integer, range: 1-90., defaults to None
    :type escrow_release_days: float, optional
    :param id_: ID of the Rapyd checkout page. String starting with checkout_., defaults to None
    :type id_: str, optional
    :param merchant_main_button: A string that represents the text on the main Call to Action (CTA) button. One of the following:* place_your_order - Place Your Order.* pay - Pay.* pay_now - Pay Now.* make_payment - Make Payment.* purchase - Purchase.* buy - Buy.* donate - Donate.* place_your_order To configure this button, use the Client Portal., defaults to None
    :type merchant_main_button: str, optional
    :param custom_elements: Description of the payment transaction., defaults to None
    :type custom_elements: HostedPageAdditionalResponseCustomElements, optional
    :param complete_checkout_url: URL where the customer is redirected after pressing Finish to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
    :type complete_checkout_url: str, optional
    :param cancel_checkout_url: URL where the customer is redirected after pressing Back to Website to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
    :type cancel_checkout_url: str, optional
    """

    def __init__(
        self,
        language: str = None,
        merchant_alias: str = None,
        merchant_color: str = None,
        merchant_customer_support: MerchantCustomerSupport = None,
        merchant_logo: str = None,
        merchant_website: str = None,
        redirect_url: str = None,
        merchant_terms: str = None,
        merchant_privacy_policy: str = None,
        page_expiration: float = None,
        status: HostedPageStatus = None,
        account_funding_transaction: dict = None,
        amount: float = None,
        cart_items: HostedPageAdditionalResponseCartItems = None,
        country: str = None,
        currency: str = None,
        customer: str = None,
        escrow: bool = None,
        escrow_release_days: float = None,
        id_: str = None,
        merchant_main_button: str = None,
        custom_elements: HostedPageAdditionalResponseCustomElements = None,
        complete_checkout_url: str = None,
        cancel_checkout_url: str = None,
    ):
        """CheckoutPageResponse

        :param language: Determines the default language of the hosted page. When this parameter is null, the language of the user's browser is used. If the language of the user's browser cannot be determined, the default language is English, defaults to None
        :type language: str, optional
        :param merchant_alias: Reserved, the default language is Rapyd, defaults to None
        :type merchant_alias: str, optional
        :param merchant_color: Color of the call-to-action (CTA) button on the hosted page. To configure this field, use the Client Portal, defaults to None
        :type merchant_color: str, optional
        :param merchant_customer_support: merchant_customer_support, defaults to None
        :type merchant_customer_support: MerchantCustomerSupport, optional
        :param merchant_logo: URL for the image of the client's logo. To configure this field, use the Client Portal, defaults to None
        :type merchant_logo: str, optional
        :param merchant_website: The URL where the customer is redirected after exiting the hosted page. Relevant when one or both of the following fields is unset: * cancel_url* complete_url. To configure this field, use the Client Portal, defaults to None
        :type merchant_website: str, optional
        :param redirect_url: URL of the hosted page that is shown to the customer., defaults to None
        :type redirect_url: str, optional
        :param merchant_terms: URL for the client's terms and conditions. To configure this field, use the Client Porta, defaults to None
        :type merchant_terms: str, optional
        :param merchant_privacy_policy: URL for the terms and conditions of the agreement between the client and the client’s customers. To configure this field, use the Client Portal., defaults to None
        :type merchant_privacy_policy: str, optional
        :param page_expiration: Length of time for the payment to be completed after it is created, measured in seconds. When both expiration and payment_expiration are set, the payment expires at the earlier time., defaults to None
        :type page_expiration: float, optional
        :param status: Status of the hosted page. One of the following: NEW - The hosted page was created. DON - Done. The card was added to the customer profile. EXP - The hosted page expired. , defaults to None
        :type status: HostedPageStatus, optional
        :param account_funding_transaction: Details of an account funding transaction (AFT), which transfers funds from a card to a cardholder's wallet., defaults to None
        :type account_funding_transaction: dict, optional
        :param amount: The amount of the payment, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal., defaults to None
        :type amount: float, optional
        :param cart_items: Describes the cart items that the customer is purchasing. These items are displayed at the checkout page., defaults to None
        :type cart_items: HostedPageAdditionalResponseCartItems, optional
        :param country: country, defaults to None
        :type country: str, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param customer: Description of the payment transaction. To display the description, set display_description to true in custom_elements., defaults to None
        :type customer: str, optional
        :param escrow: Determines whether the payment is held in escrow for later release., defaults to None
        :type escrow: bool, optional
        :param escrow_release_days: Determines the number of days after creation of the payment that funds are released from escrow. Funds are released at 5:00 pm GMT on the day indicated. Integer, range: 1-90., defaults to None
        :type escrow_release_days: float, optional
        :param id_: ID of the Rapyd checkout page. String starting with checkout_., defaults to None
        :type id_: str, optional
        :param merchant_main_button: A string that represents the text on the main Call to Action (CTA) button. One of the following:* place_your_order - Place Your Order.* pay - Pay.* pay_now - Pay Now.* make_payment - Make Payment.* purchase - Purchase.* buy - Buy.* donate - Donate.* place_your_order To configure this button, use the Client Portal., defaults to None
        :type merchant_main_button: str, optional
        :param custom_elements: Description of the payment transaction., defaults to None
        :type custom_elements: HostedPageAdditionalResponseCustomElements, optional
        :param complete_checkout_url: URL where the customer is redirected after pressing Finish to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
        :type complete_checkout_url: str, optional
        :param cancel_checkout_url: URL where the customer is redirected after pressing Back to Website to exit the hosted page. This URL overrides the merchant_website URL. Does not support localhost URLs., defaults to None
        :type cancel_checkout_url: str, optional
        """
        self.language = self._define_str("language", language, nullable=True)
        self.merchant_alias = self._define_str(
            "merchant_alias", merchant_alias, nullable=True
        )
        self.merchant_color = self._define_str(
            "merchant_color", merchant_color, nullable=True
        )
        self.merchant_customer_support = self._define_object(
            merchant_customer_support, MerchantCustomerSupport
        )
        self.merchant_logo = self._define_str(
            "merchant_logo", merchant_logo, nullable=True
        )
        self.merchant_website = self._define_str(
            "merchant_website", merchant_website, nullable=True
        )
        self.redirect_url = self._define_str(
            "redirect_url", redirect_url, nullable=True
        )
        self.merchant_terms = self._define_str(
            "merchant_terms", merchant_terms, nullable=True
        )
        self.merchant_privacy_policy = self._define_str(
            "merchant_privacy_policy", merchant_privacy_policy, nullable=True
        )
        self.page_expiration = self._define_number(
            "page_expiration", page_expiration, nullable=True
        )
        self.status = (
            self._enum_matching(status, HostedPageStatus.list(), "status")
            if status
            else None
        )
        self.account_funding_transaction = account_funding_transaction
        self.amount = self._define_number("amount", amount, nullable=True)
        self.cart_items = self._define_object(
            cart_items, HostedPageAdditionalResponseCartItems
        )
        self.country = self._define_str(
            "country",
            country,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.customer = self._define_str("customer", customer, nullable=True)
        self.escrow = escrow
        self.escrow_release_days = self._define_number(
            "escrow_release_days", escrow_release_days, nullable=True
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.merchant_main_button = self._define_str(
            "merchant_main_button", merchant_main_button, nullable=True
        )
        self.custom_elements = self._define_object(
            custom_elements, HostedPageAdditionalResponseCustomElements
        )
        self.complete_checkout_url = self._define_str(
            "complete_checkout_url", complete_checkout_url, nullable=True
        )
        self.cancel_checkout_url = self._define_str(
            "cancel_checkout_url", cancel_checkout_url, nullable=True
        )
