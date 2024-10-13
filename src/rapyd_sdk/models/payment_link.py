from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .merchant_customer_support import MerchantCustomerSupport


@JsonMap({"id_": "id"})
class PaymentLink(BaseModel):
    """Retrieves details of a payment link.

    :param amount: The amount of the payment, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. On the hosted payment page, the customer: <BR><BR> Cannot modify the amount when amount_is_editable is false or not used. <BR><BR> Can modify the amount when amount_is_editable is true and amount has a positive value. <BR><BR> Must enter an amount when amount_is_editable is true and amount is 0, null, or not used., defaults to None
    :type amount: float, optional
    :param amount_is_editable: Determines whether the customer can edit the amount.<br><br> **true** - The customer can edit the amount. <br><br> **false** - The customer cannot edit the amount., defaults to None
    :type amount_is_editable: bool, optional
    :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
    :type country: str, optional
    :param currency: The two-letter ISO 3166-1 ALPHA-2 code for the country. <BR><BR> **Transactions without FX** - Indicates the currency of the amount received by the recipient. BR><BR> **FX transactions** - Indicates the currency of the amount paid by the buyer., defaults to None
    :type currency: str, optional
    :param customer: ID of a specific customer. String starting with **cus_**. Restricts the payment link to the customer., defaults to None
    :type customer: str, optional
    :param fixed_side: Indicates whether the FX rate is fixed for the buy side (seller) or for the sell side (buyer). <BR><BR> * buy - The currency that the Rapyd Wallet receives for goods or services. Fixed side buy relates to the seller (merchant) funds. For example, a US-based merchant wants to charge 100 USD. The buyer (customer) pays the amount in MXN that converts to 100 USD. This is the default. <BR><BR> * sell - The currency that the buyer is charged for purchasing goods or services. Fixed side sell relates to the buyer (customer) funds. For example, a US-based merchant wants to charge a buyer 2,000 MXN and will accept whatever amount in USD that is converted from 2,000 MXN., defaults to None
    :type fixed_side: str, optional
    :param id_: ID of the payment link. String starting with **hp_reuse_**., defaults to None
    :type id_: str, optional
    :param language: Determines the default language of the hosted page. For a list of values, see https://docs.rapyd.net/en/list-supported-languages.html. <BR><BR> When this parameter is null, the language of the user's browser is used. BR><BR> If the language of the user's browser cannot be determined, the default language is English., defaults to None
    :type language: str, optional
    :param max_payments: Indicates the maximum number of times that the payment link can be used for payments. When not defined, there is no limit., defaults to None
    :type max_payments: float, optional
    :param merchant_alias: Client's name., defaults to None
    :type merchant_alias: str, optional
    :param merchant_color: Color of the call-to-action (CTA) button on the hosted page. To configure this field, use the Client Portal. See https://docs.rapyd.net/en/customizing-your-hosted-page.html., defaults to None
    :type merchant_color: str, optional
    :param merchant_customer_support: Contains details of the client’s customer support. To configure these fields, use the Client Portal., defaults to None
    :type merchant_customer_support: MerchantCustomerSupport, optional
    :param merchant_logo: URL for the image of the client's logo. To configure this field, use the Client Portal., defaults to None
    :type merchant_logo: str, optional
    :param merchant_privacy_policy: URL for the terms and conditions of the agreement between the client and the client’s customers. To configure this field, use the Client Portal., defaults to None
    :type merchant_privacy_policy: str, optional
    :param merchant_reference_id: Identifier defined by the client for reference purposes. Limit: 45 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param merchant_website: The URL where the customer is redirected after exiting the hosted page. Relevant when one or both of the following fields is unset: <BR><BR> * `cancel_url` <BR><BR> * `complete_url`<BR><BR> To configure this field, use the Client Portal, defaults to None
    :type merchant_website: str, optional
    :param page_expiration: End of the time when the customer can use the payment link, in Unix time. One year after creation. <BR> <BR> **Note:** Each hosted page that the payment link generates expires 14 days after creation., defaults to None
    :type page_expiration: float, optional
    :param requested_currency: Currency for one side of an FX transaction. Three-letter ISO 4217 code. <BR><BR>* When `fixed_side` is **sell**, it is the currency received in the Rapyd Wallet. <BR><BR>* When `fixed_side` is **buy**, it is the currency charged to the buyer (customer)., defaults to None
    :type requested_currency: str, optional
    :param redirect_url: The payment link URL., defaults to None
    :type redirect_url: str, optional
    :param status: Status of the hosted payment page. One of the following: <BR><BR>* **NEW** - The hosted page was created. <BR><BR>* **EXP** - The hosted page expired., defaults to None
    :type status: str, optional
    :param template: Optional parameters for the checkout page., defaults to None
    :type template: dict, optional
    """

    def __init__(
        self,
        amount: float = None,
        amount_is_editable: bool = None,
        country: str = None,
        currency: str = None,
        customer: str = None,
        fixed_side: str = None,
        id_: str = None,
        language: str = None,
        max_payments: float = None,
        merchant_alias: str = None,
        merchant_color: str = None,
        merchant_customer_support: MerchantCustomerSupport = None,
        merchant_logo: str = None,
        merchant_privacy_policy: str = None,
        merchant_reference_id: str = None,
        merchant_website: str = None,
        page_expiration: float = None,
        requested_currency: str = None,
        redirect_url: str = None,
        status: str = None,
        template: dict = None,
    ):
        """Retrieves details of a payment link.

        :param amount: The amount of the payment, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. On the hosted payment page, the customer: <BR><BR> Cannot modify the amount when amount_is_editable is false or not used. <BR><BR> Can modify the amount when amount_is_editable is true and amount has a positive value. <BR><BR> Must enter an amount when amount_is_editable is true and amount is 0, null, or not used., defaults to None
        :type amount: float, optional
        :param amount_is_editable: Determines whether the customer can edit the amount.<br><br> **true** - The customer can edit the amount. <br><br> **false** - The customer cannot edit the amount., defaults to None
        :type amount_is_editable: bool, optional
        :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
        :type country: str, optional
        :param currency: The two-letter ISO 3166-1 ALPHA-2 code for the country. <BR><BR> **Transactions without FX** - Indicates the currency of the amount received by the recipient. BR><BR> **FX transactions** - Indicates the currency of the amount paid by the buyer., defaults to None
        :type currency: str, optional
        :param customer: ID of a specific customer. String starting with **cus_**. Restricts the payment link to the customer., defaults to None
        :type customer: str, optional
        :param fixed_side: Indicates whether the FX rate is fixed for the buy side (seller) or for the sell side (buyer). <BR><BR> * buy - The currency that the Rapyd Wallet receives for goods or services. Fixed side buy relates to the seller (merchant) funds. For example, a US-based merchant wants to charge 100 USD. The buyer (customer) pays the amount in MXN that converts to 100 USD. This is the default. <BR><BR> * sell - The currency that the buyer is charged for purchasing goods or services. Fixed side sell relates to the buyer (customer) funds. For example, a US-based merchant wants to charge a buyer 2,000 MXN and will accept whatever amount in USD that is converted from 2,000 MXN., defaults to None
        :type fixed_side: str, optional
        :param id_: ID of the payment link. String starting with **hp_reuse_**., defaults to None
        :type id_: str, optional
        :param language: Determines the default language of the hosted page. For a list of values, see https://docs.rapyd.net/en/list-supported-languages.html. <BR><BR> When this parameter is null, the language of the user's browser is used. BR><BR> If the language of the user's browser cannot be determined, the default language is English., defaults to None
        :type language: str, optional
        :param max_payments: Indicates the maximum number of times that the payment link can be used for payments. When not defined, there is no limit., defaults to None
        :type max_payments: float, optional
        :param merchant_alias: Client's name., defaults to None
        :type merchant_alias: str, optional
        :param merchant_color: Color of the call-to-action (CTA) button on the hosted page. To configure this field, use the Client Portal. See https://docs.rapyd.net/en/customizing-your-hosted-page.html., defaults to None
        :type merchant_color: str, optional
        :param merchant_customer_support: Contains details of the client’s customer support. To configure these fields, use the Client Portal., defaults to None
        :type merchant_customer_support: MerchantCustomerSupport, optional
        :param merchant_logo: URL for the image of the client's logo. To configure this field, use the Client Portal., defaults to None
        :type merchant_logo: str, optional
        :param merchant_privacy_policy: URL for the terms and conditions of the agreement between the client and the client’s customers. To configure this field, use the Client Portal., defaults to None
        :type merchant_privacy_policy: str, optional
        :param merchant_reference_id: Identifier defined by the client for reference purposes. Limit: 45 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param merchant_website: The URL where the customer is redirected after exiting the hosted page. Relevant when one or both of the following fields is unset: <BR><BR> * `cancel_url` <BR><BR> * `complete_url`<BR><BR> To configure this field, use the Client Portal, defaults to None
        :type merchant_website: str, optional
        :param page_expiration: End of the time when the customer can use the payment link, in Unix time. One year after creation. <BR> <BR> **Note:** Each hosted page that the payment link generates expires 14 days after creation., defaults to None
        :type page_expiration: float, optional
        :param requested_currency: Currency for one side of an FX transaction. Three-letter ISO 4217 code. <BR><BR>* When `fixed_side` is **sell**, it is the currency received in the Rapyd Wallet. <BR><BR>* When `fixed_side` is **buy**, it is the currency charged to the buyer (customer)., defaults to None
        :type requested_currency: str, optional
        :param redirect_url: The payment link URL., defaults to None
        :type redirect_url: str, optional
        :param status: Status of the hosted payment page. One of the following: <BR><BR>* **NEW** - The hosted page was created. <BR><BR>* **EXP** - The hosted page expired., defaults to None
        :type status: str, optional
        :param template: Optional parameters for the checkout page., defaults to None
        :type template: dict, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.amount_is_editable = amount_is_editable
        self.country = self._define_str("country", country, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.customer = self._define_str("customer", customer, nullable=True)
        self.fixed_side = self._define_str("fixed_side", fixed_side, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.language = self._define_str("language", language, nullable=True)
        self.max_payments = self._define_number(
            "max_payments", max_payments, nullable=True
        )
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
        self.merchant_privacy_policy = self._define_str(
            "merchant_privacy_policy", merchant_privacy_policy, nullable=True
        )
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.merchant_website = self._define_str(
            "merchant_website", merchant_website, nullable=True
        )
        self.page_expiration = self._define_number(
            "page_expiration", page_expiration, nullable=True
        )
        self.requested_currency = self._define_str(
            "requested_currency", requested_currency, nullable=True
        )
        self.redirect_url = self._define_str(
            "redirect_url", redirect_url, nullable=True
        )
        self.status = self._define_str("status", status, nullable=True)
        self.template = template
