from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CollectPaymentsBody(BaseModel):
    """CollectPaymentsBody

    :param amount: The amount of the payment, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015.<BR> On the hosted payment page, the customer: <BR> * Cannot modify the amount when amount_is_editable is false or not used. <BR> * Can modify the amount when amount_is_editable is true and amount has a positive value. <BR> * Must enter an amount when amount_is_editable is true and amount is 0, null, or not used.
    :type amount: str
    :param amount_is_editable: Determines whether the customer can edit the amount. <BR> * **true** - The customer can edit the amount. <BR> * **false** - The customer cannot edit the amount., defaults to None
    :type amount_is_editable: bool, optional
    :param checkout: Optional parameters for the checkout page., defaults to None
    :type checkout: dict, optional
    :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country.
    :type country: str
    :param currency: In transactions without FX, defines the currency of the transaction. Three-letter ISO 4217 code. <BR> In FX transactions: <BR> * When `fixed_side` is **buy**, it is the currency received in the Rapyd wallet. <BR> * When `fixed_side` is **sell**, it is the currency charged to the buyer. <BR> See also `fixed_side` and `requested_currency` fields.
    :type currency: str
    :param customer: ID of a specific customer. String starting with **cus_**. Restricts the payment link to the customer., defaults to None
    :type customer: str, optional
    :param fixed_side: Indicates whether the FX rate is fixed for the buy side (seller) or for the sell side (buyer).<BR>* **buy** - The currency that the Rapyd Wallet receives for goods or services. Fixed side buy relates to the seller (merchant) funds. For example, a US-based merchant wants to charge 100 USD. The buyer (customer) pays the amount in MXN that converts to 100 USD.<BR>* **sell** - The currency that the buyer is charged for purchasing goods or services. Fixed side sell relates to the buyer (customer) funds. For example, a US-based merchant wants to charge a buyer 2,000 MXN and will accept whatever amount in USD that is converted from 2,000 MXN., defaults to None
    :type fixed_side: str, optional
    :param language: Determines the default language of the hosted page. For a list of values, see 'List Supported Languages'. <BR> * When this parameter is null, the language of the user's browser is used. <BR> If the language of the user's browser cannot be determined, the default language is English., defaults to None
    :type language: str, optional
    :param max_payments: Indicates the maximum number of times that the payment link can be used for payments. When not indicated, there is no limit., defaults to None
    :type max_payments: float, optional
    :param merchant_reference_id: Identifier defined by the client for reference purposes. Limit: 45 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param requested_currency: Currency for one side of an FX transaction. Three-letter ISO 4217 code. <BR><BR>* When `fixed_side` is **sell**, it is the currency received in the Rapyd Wallet. <BR><BR>* When `fixed_side` is **buy**, it is the currency charged to the buyer (customer)., defaults to None
    :type requested_currency: str, optional
    """

    def __init__(
        self,
        amount: str,
        country: str,
        currency: str,
        amount_is_editable: bool = None,
        checkout: dict = None,
        customer: str = None,
        fixed_side: str = None,
        language: str = None,
        max_payments: float = None,
        merchant_reference_id: str = None,
        requested_currency: str = None,
    ):
        """CollectPaymentsBody

        :param amount: The amount of the payment, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015.<BR> On the hosted payment page, the customer: <BR> * Cannot modify the amount when amount_is_editable is false or not used. <BR> * Can modify the amount when amount_is_editable is true and amount has a positive value. <BR> * Must enter an amount when amount_is_editable is true and amount is 0, null, or not used.
        :type amount: str
        :param amount_is_editable: Determines whether the customer can edit the amount. <BR> * **true** - The customer can edit the amount. <BR> * **false** - The customer cannot edit the amount., defaults to None
        :type amount_is_editable: bool, optional
        :param checkout: Optional parameters for the checkout page., defaults to None
        :type checkout: dict, optional
        :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country.
        :type country: str
        :param currency: In transactions without FX, defines the currency of the transaction. Three-letter ISO 4217 code. <BR> In FX transactions: <BR> * When `fixed_side` is **buy**, it is the currency received in the Rapyd wallet. <BR> * When `fixed_side` is **sell**, it is the currency charged to the buyer. <BR> See also `fixed_side` and `requested_currency` fields.
        :type currency: str
        :param customer: ID of a specific customer. String starting with **cus_**. Restricts the payment link to the customer., defaults to None
        :type customer: str, optional
        :param fixed_side: Indicates whether the FX rate is fixed for the buy side (seller) or for the sell side (buyer).<BR>* **buy** - The currency that the Rapyd Wallet receives for goods or services. Fixed side buy relates to the seller (merchant) funds. For example, a US-based merchant wants to charge 100 USD. The buyer (customer) pays the amount in MXN that converts to 100 USD.<BR>* **sell** - The currency that the buyer is charged for purchasing goods or services. Fixed side sell relates to the buyer (customer) funds. For example, a US-based merchant wants to charge a buyer 2,000 MXN and will accept whatever amount in USD that is converted from 2,000 MXN., defaults to None
        :type fixed_side: str, optional
        :param language: Determines the default language of the hosted page. For a list of values, see 'List Supported Languages'. <BR> * When this parameter is null, the language of the user's browser is used. <BR> If the language of the user's browser cannot be determined, the default language is English., defaults to None
        :type language: str, optional
        :param max_payments: Indicates the maximum number of times that the payment link can be used for payments. When not indicated, there is no limit., defaults to None
        :type max_payments: float, optional
        :param merchant_reference_id: Identifier defined by the client for reference purposes. Limit: 45 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param requested_currency: Currency for one side of an FX transaction. Three-letter ISO 4217 code. <BR><BR>* When `fixed_side` is **sell**, it is the currency received in the Rapyd Wallet. <BR><BR>* When `fixed_side` is **buy**, it is the currency charged to the buyer (customer)., defaults to None
        :type requested_currency: str, optional
        """
        self.amount = amount
        self.amount_is_editable = amount_is_editable
        self.checkout = checkout
        self.country = country
        self.currency = currency
        self.customer = self._define_str("customer", customer, nullable=True)
        self.fixed_side = self._define_str("fixed_side", fixed_side, nullable=True)
        self.language = self._define_str("language", language, nullable=True)
        self.max_payments = self._define_number(
            "max_payments", max_payments, nullable=True
        )
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.requested_currency = self._define_str(
            "requested_currency", requested_currency, nullable=True
        )
