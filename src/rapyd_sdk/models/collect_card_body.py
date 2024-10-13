from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .v1hostedcollectcard_card_fields import V1hostedcollectcardCardFields


@JsonMap({})
class CollectCardBody(BaseModel):
    """CollectCardBody

    :param billing_address_collect: Indicates whether the hosted page displays address fields to fill in.<BR> * **true** - The address fields are displayed. <BR> * **false** - The address fields are displayed only for country codes **US**, **GB** and **CA**., defaults to None
    :type billing_address_collect: bool, optional
    :param cancel_url: URL where the customer is redirected after pressing **Back to Website** to exit the hosted page. This URL overrides the `merchant_website` URL. Does not support localhost URLs., defaults to None
    :type cancel_url: str, optional
    :param card_fields: Contains details about the card., defaults to None
    :type card_fields: V1hostedcollectcardCardFields, optional
    :param complete_url: URL where the customer is redirected after pressing **Close** to exit the hosted page. This URL overrides the `merchant_website` URL. Does not support localhost URLs.The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
    :type complete_url: str, optional
    :param complete_payment_url: URL where the customer is redirected when payment is successful, after returning from an external page such as a 3DS page. Does not support localhost URLs., defaults to None
    :type complete_payment_url: str, optional
    :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country.
    :type country: str
    :param currency: In transactions without FX, defines the currency of the transaction. Three-letter ISO 4217 code. <BR> In FX transactions: <BR> * When `fixed_side` is **buy**, it is the currency received in the Rapyd wallet. <BR> * When `fixed_side` is **sell**, it is the currency charged to the buyer. <BR> See also `fixed_side` and `requested_currency` fields., defaults to None
    :type currency: str, optional
    :param customer: ID of a specific customer. String starting with **cus_**. Restricts the payment link to the customer.
    :type customer: str
    :param error_payment_url: URL where the customer is redirected when payment is not successful, after returning from an external page, such as a 3DS page. Does not support localhost URLs., defaults to None
    :type error_payment_url: str, optional
    :param language: Determines the default language of the hosted page. For a list of values, see [List Supported Languages](https://docs.rapyd.net/en/list-supported-languages.html). <BR> * When this parameter is null, the language of the user's browser is used. <BR> * If the language of the user's browser cannot be determined, the default language is English., defaults to None
    :type language: str, optional
    :param page_expiration: End of the time when the customer can use the hosted page, in Unix time. If `page_expiration` is not set, the hosted page expires 14 days after creation. Range: 1 minute to 30 days., defaults to None
    :type page_expiration: str, optional
    :param payment_method_type: Limits the page to a specific type of payment method. For example, **dk_visa_card**. For a list of payment methods, use [List Payment Methods by Country](https://docs.rapyd.net/en/list-payment-methods-by-country.html)., defaults to None
    :type payment_method_type: str, optional
    """

    def __init__(
        self,
        country: str,
        customer: str,
        billing_address_collect: bool = None,
        cancel_url: str = None,
        card_fields: V1hostedcollectcardCardFields = None,
        complete_url: str = None,
        complete_payment_url: str = None,
        currency: str = None,
        error_payment_url: str = None,
        language: str = None,
        page_expiration: str = None,
        payment_method_type: str = None,
    ):
        """CollectCardBody

        :param billing_address_collect: Indicates whether the hosted page displays address fields to fill in.<BR> * **true** - The address fields are displayed. <BR> * **false** - The address fields are displayed only for country codes **US**, **GB** and **CA**., defaults to None
        :type billing_address_collect: bool, optional
        :param cancel_url: URL where the customer is redirected after pressing **Back to Website** to exit the hosted page. This URL overrides the `merchant_website` URL. Does not support localhost URLs., defaults to None
        :type cancel_url: str, optional
        :param card_fields: Contains details about the card., defaults to None
        :type card_fields: V1hostedcollectcardCardFields, optional
        :param complete_url: URL where the customer is redirected after pressing **Close** to exit the hosted page. This URL overrides the `merchant_website` URL. Does not support localhost URLs.The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
        :type complete_url: str, optional
        :param complete_payment_url: URL where the customer is redirected when payment is successful, after returning from an external page such as a 3DS page. Does not support localhost URLs., defaults to None
        :type complete_payment_url: str, optional
        :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country.
        :type country: str
        :param currency: In transactions without FX, defines the currency of the transaction. Three-letter ISO 4217 code. <BR> In FX transactions: <BR> * When `fixed_side` is **buy**, it is the currency received in the Rapyd wallet. <BR> * When `fixed_side` is **sell**, it is the currency charged to the buyer. <BR> See also `fixed_side` and `requested_currency` fields., defaults to None
        :type currency: str, optional
        :param customer: ID of a specific customer. String starting with **cus_**. Restricts the payment link to the customer.
        :type customer: str
        :param error_payment_url: URL where the customer is redirected when payment is not successful, after returning from an external page, such as a 3DS page. Does not support localhost URLs., defaults to None
        :type error_payment_url: str, optional
        :param language: Determines the default language of the hosted page. For a list of values, see [List Supported Languages](https://docs.rapyd.net/en/list-supported-languages.html). <BR> * When this parameter is null, the language of the user's browser is used. <BR> * If the language of the user's browser cannot be determined, the default language is English., defaults to None
        :type language: str, optional
        :param page_expiration: End of the time when the customer can use the hosted page, in Unix time. If `page_expiration` is not set, the hosted page expires 14 days after creation. Range: 1 minute to 30 days., defaults to None
        :type page_expiration: str, optional
        :param payment_method_type: Limits the page to a specific type of payment method. For example, **dk_visa_card**. For a list of payment methods, use [List Payment Methods by Country](https://docs.rapyd.net/en/list-payment-methods-by-country.html)., defaults to None
        :type payment_method_type: str, optional
        """
        self.billing_address_collect = billing_address_collect
        self.cancel_url = self._define_str("cancel_url", cancel_url, nullable=True)
        self.card_fields = self._define_object(
            card_fields, V1hostedcollectcardCardFields
        )
        self.complete_url = self._define_str(
            "complete_url", complete_url, nullable=True
        )
        self.complete_payment_url = self._define_str(
            "complete_payment_url", complete_payment_url, nullable=True
        )
        self.country = country
        self.currency = self._define_str("currency", currency, nullable=True)
        self.customer = customer
        self.error_payment_url = self._define_str(
            "error_payment_url", error_payment_url, nullable=True
        )
        self.language = self._define_str("language", language, nullable=True)
        self.page_expiration = self._define_str(
            "page_expiration", page_expiration, nullable=True
        )
        self.payment_method_type = self._define_str(
            "payment_method_type", payment_method_type, nullable=True
        )
