from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .card_token_response_card_fields import CardTokenResponseCardFields
from .merchant_customer_support import MerchantCustomerSupport
from .card_token_response_payment_params import CardTokenResponsePaymentParams


@JsonMap({"id_": "id"})
class CardTokenResponse(BaseModel):
    """CardTokenResponse

    :param billing_address_collect: Indicates whether the hosted page displays address fields to fill in.<BR> * **true** - The address fields are displayed. <BR> * **false** - The address fields are displayed only for country codes **US**, **GB** and **CA**., defaults to None
    :type billing_address_collect: bool, optional
    :param cancel_url: URL where the customer is redirected after pressing **Back to Website** to exit the hosted page. This URL overrides the `merchant_website` URL. Does not support localhost URLs., defaults to None
    :type cancel_url: str, optional
    :param card_fields: Contains details about the card., defaults to None
    :type card_fields: CardTokenResponseCardFields, optional
    :param category: Category of payment method: **card**., defaults to None
    :type category: str, optional
    :param complete_url: URL where the customer is redirected after pressing **Close** to exit the hosted page. This URL overrides the `merchant_website` URL. Does not support localhost URLs.The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
    :type complete_url: str, optional
    :param complete_payment_url: URL where the customer is redirected when payment is successful, after returning from an external page such as a 3DS page. Does not support localhost URLs., defaults to None
    :type complete_payment_url: str, optional
    :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
    :type country: str, optional
    :param currency: In transactions without FX, defines the currency of the transaction. Three-letter ISO 4217 code. <BR> In FX transactions: <BR> * When `fixed_side` is **buy**, it is the currency received in the Rapyd wallet. <BR> * When `fixed_side` is **sell**, it is the currency charged to the buyer. <BR> See also `fixed_side` and `requested_currency` fields., defaults to None
    :type currency: str, optional
    :param customer: ID of a specific customer. String starting with **cus_**., defaults to None
    :type customer: str, optional
    :param error_code: Relevant error message and ID number of the error., defaults to None
    :type error_code: str, optional
    :param error_payment_url: URL where the customer is redirected when payment is not successful, after returning from an external page, such as a 3DS page. Does not support localhost URLs., defaults to None
    :type error_payment_url: str, optional
    :param id_: ID of the card token hosted page, a string starting with **hp_card_**., defaults to None
    :type id_: str, optional
    :param language: Determines the default language of the hosted page. For a list of values, see [List Supported Languages](https://docs.rapyd.net/en/list-supported-languages.html). <BR> * When this parameter is null, the language of the user's browser is used. <BR> If the language of the user's browser cannot be determined, the default language is English., defaults to None
    :type language: str, optional
    :param merchant_alias: Reserved., defaults to None
    :type merchant_alias: str, optional
    :param merchant_color: Color of the call-to-action (CTA) button on the hosted page. To configure this field, use the Client Portal. See [Customizing Your Hosted Page](https://docs.rapyd.net/en/customizing-your-hosted-page.html)., defaults to None
    :type merchant_color: str, optional
    :param merchant_customer_support: Contains details of the client’s customer support. To configure these fields, use the Client Portal., defaults to None
    :type merchant_customer_support: MerchantCustomerSupport, optional
    :param merchant_website: The URL where the customer is redirected after exiting the hosted page. Relevant when one or both of the following fields is unset: <BR>* `cancel_url` <BR>* `complete_url`.<BR> To configure this field, use the **Fallback URL** field in the Client Portal. See [Customizing Your Hosted Page](https://docs.rapyd.net/en/customizing-your-hosted-page.html)., defaults to None
    :type merchant_website: str, optional
    :param page_expiration: End of the time when the customer can use the hosted page, in Unix time. If `page_expiration` is not set, the hosted page expires 14 days after creation. Range: 1 minute to 30 days., defaults to None
    :type page_expiration: str, optional
    :param payment_method_type: Limits the page to a specific type of payment method. For example, **dk_visa_card**. For a list of payment methods, use []List Payment Methods by Country](https://docs.rapyd.net/en/list-payment-methods-by-country.html)., defaults to None
    :type payment_method_type: str, optional
    :param payment_params: Contains the following fields. When these fields do not include values, the user is redirected to the hosted page, and a related status message appears at the top of the page., defaults to None
    :type payment_params: CardTokenResponsePaymentParams, optional
    :param redirect_url: URL of the hosted page that is shown to the customer.Contains the following fields. When these fields do not include values, the user is redirected to the hosted page, and a related status message appears at the top of the page., defaults to None
    :type redirect_url: str, optional
    :param status: Status of the hosted page. One of the following: <BR> * **NEW** - The hosted page was created. <BR> * **DON** - Done. The card was added to the customer profile. <BR> * **EXP** - The hosted page expired.URL of the hosted page that is shown to the customer., defaults to None
    :type status: str, optional
    """

    def __init__(
        self,
        billing_address_collect: bool = None,
        cancel_url: str = None,
        card_fields: CardTokenResponseCardFields = None,
        category: str = None,
        complete_url: str = None,
        complete_payment_url: str = None,
        country: str = None,
        currency: str = None,
        customer: str = None,
        error_code: str = None,
        error_payment_url: str = None,
        id_: str = None,
        language: str = None,
        merchant_alias: str = None,
        merchant_color: str = None,
        merchant_customer_support: MerchantCustomerSupport = None,
        merchant_website: str = None,
        page_expiration: str = None,
        payment_method_type: str = None,
        payment_params: CardTokenResponsePaymentParams = None,
        redirect_url: str = None,
        status: str = None,
    ):
        """CardTokenResponse

        :param billing_address_collect: Indicates whether the hosted page displays address fields to fill in.<BR> * **true** - The address fields are displayed. <BR> * **false** - The address fields are displayed only for country codes **US**, **GB** and **CA**., defaults to None
        :type billing_address_collect: bool, optional
        :param cancel_url: URL where the customer is redirected after pressing **Back to Website** to exit the hosted page. This URL overrides the `merchant_website` URL. Does not support localhost URLs., defaults to None
        :type cancel_url: str, optional
        :param card_fields: Contains details about the card., defaults to None
        :type card_fields: CardTokenResponseCardFields, optional
        :param category: Category of payment method: **card**., defaults to None
        :type category: str, optional
        :param complete_url: URL where the customer is redirected after pressing **Close** to exit the hosted page. This URL overrides the `merchant_website` URL. Does not support localhost URLs.The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
        :type complete_url: str, optional
        :param complete_payment_url: URL where the customer is redirected when payment is successful, after returning from an external page such as a 3DS page. Does not support localhost URLs., defaults to None
        :type complete_payment_url: str, optional
        :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
        :type country: str, optional
        :param currency: In transactions without FX, defines the currency of the transaction. Three-letter ISO 4217 code. <BR> In FX transactions: <BR> * When `fixed_side` is **buy**, it is the currency received in the Rapyd wallet. <BR> * When `fixed_side` is **sell**, it is the currency charged to the buyer. <BR> See also `fixed_side` and `requested_currency` fields., defaults to None
        :type currency: str, optional
        :param customer: ID of a specific customer. String starting with **cus_**., defaults to None
        :type customer: str, optional
        :param error_code: Relevant error message and ID number of the error., defaults to None
        :type error_code: str, optional
        :param error_payment_url: URL where the customer is redirected when payment is not successful, after returning from an external page, such as a 3DS page. Does not support localhost URLs., defaults to None
        :type error_payment_url: str, optional
        :param id_: ID of the card token hosted page, a string starting with **hp_card_**., defaults to None
        :type id_: str, optional
        :param language: Determines the default language of the hosted page. For a list of values, see [List Supported Languages](https://docs.rapyd.net/en/list-supported-languages.html). <BR> * When this parameter is null, the language of the user's browser is used. <BR> If the language of the user's browser cannot be determined, the default language is English., defaults to None
        :type language: str, optional
        :param merchant_alias: Reserved., defaults to None
        :type merchant_alias: str, optional
        :param merchant_color: Color of the call-to-action (CTA) button on the hosted page. To configure this field, use the Client Portal. See [Customizing Your Hosted Page](https://docs.rapyd.net/en/customizing-your-hosted-page.html)., defaults to None
        :type merchant_color: str, optional
        :param merchant_customer_support: Contains details of the client’s customer support. To configure these fields, use the Client Portal., defaults to None
        :type merchant_customer_support: MerchantCustomerSupport, optional
        :param merchant_website: The URL where the customer is redirected after exiting the hosted page. Relevant when one or both of the following fields is unset: <BR>* `cancel_url` <BR>* `complete_url`.<BR> To configure this field, use the **Fallback URL** field in the Client Portal. See [Customizing Your Hosted Page](https://docs.rapyd.net/en/customizing-your-hosted-page.html)., defaults to None
        :type merchant_website: str, optional
        :param page_expiration: End of the time when the customer can use the hosted page, in Unix time. If `page_expiration` is not set, the hosted page expires 14 days after creation. Range: 1 minute to 30 days., defaults to None
        :type page_expiration: str, optional
        :param payment_method_type: Limits the page to a specific type of payment method. For example, **dk_visa_card**. For a list of payment methods, use []List Payment Methods by Country](https://docs.rapyd.net/en/list-payment-methods-by-country.html)., defaults to None
        :type payment_method_type: str, optional
        :param payment_params: Contains the following fields. When these fields do not include values, the user is redirected to the hosted page, and a related status message appears at the top of the page., defaults to None
        :type payment_params: CardTokenResponsePaymentParams, optional
        :param redirect_url: URL of the hosted page that is shown to the customer.Contains the following fields. When these fields do not include values, the user is redirected to the hosted page, and a related status message appears at the top of the page., defaults to None
        :type redirect_url: str, optional
        :param status: Status of the hosted page. One of the following: <BR> * **NEW** - The hosted page was created. <BR> * **DON** - Done. The card was added to the customer profile. <BR> * **EXP** - The hosted page expired.URL of the hosted page that is shown to the customer., defaults to None
        :type status: str, optional
        """
        self.billing_address_collect = billing_address_collect
        self.cancel_url = self._define_str("cancel_url", cancel_url, nullable=True)
        self.card_fields = self._define_object(card_fields, CardTokenResponseCardFields)
        self.category = self._define_str("category", category, nullable=True)
        self.complete_url = self._define_str(
            "complete_url", complete_url, nullable=True
        )
        self.complete_payment_url = self._define_str(
            "complete_payment_url", complete_payment_url, nullable=True
        )
        self.country = self._define_str("country", country, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.customer = self._define_str("customer", customer, nullable=True)
        self.error_code = self._define_str("error_code", error_code, nullable=True)
        self.error_payment_url = self._define_str(
            "error_payment_url", error_payment_url, nullable=True
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
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
        self.merchant_website = self._define_str(
            "merchant_website", merchant_website, nullable=True
        )
        self.page_expiration = self._define_str(
            "page_expiration", page_expiration, nullable=True
        )
        self.payment_method_type = self._define_str(
            "payment_method_type", payment_method_type, nullable=True
        )
        self.payment_params = self._define_object(
            payment_params, CardTokenResponsePaymentParams
        )
        self.redirect_url = self._define_str(
            "redirect_url", redirect_url, nullable=True
        )
        self.status = self._define_str("status", status, nullable=True)
