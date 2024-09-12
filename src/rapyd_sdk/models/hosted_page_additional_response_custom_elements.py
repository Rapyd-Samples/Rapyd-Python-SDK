from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class HostedPageAdditionalResponseCustomElements(BaseModel):
    """Description of the payment transaction.

    :param save_card_default: save_card_default
    :type save_card_default: bool
    :param payment_fees_display: payment_fees_display
    :type payment_fees_display: bool
    :param billing_address_collect: billing_address_collect
    :type billing_address_collect: bool
    :param display_description: display_description
    :type display_description: bool
    :param merchant_currency_only: merchant_currency_only
    :type merchant_currency_only: bool
    :param cardholder_name: cardholder_name
    :type cardholder_name: str
    :param cardholder_preferred_currency: cardholder_preferred_currency, defaults to None
    :type cardholder_preferred_currency: str, optional
    :param dynamic_currency_conversion: dynamic_currency_conversion, defaults to None
    :type dynamic_currency_conversion: bool, optional
    """

    def __init__(
        self,
        save_card_default: bool,
        payment_fees_display: bool,
        billing_address_collect: bool,
        display_description: bool,
        merchant_currency_only: bool,
        cardholder_name: str,
        cardholder_preferred_currency: str = None,
        dynamic_currency_conversion: bool = None,
    ):
        """Description of the payment transaction.

        :param save_card_default: save_card_default
        :type save_card_default: bool
        :param payment_fees_display: payment_fees_display
        :type payment_fees_display: bool
        :param billing_address_collect: billing_address_collect
        :type billing_address_collect: bool
        :param display_description: display_description
        :type display_description: bool
        :param merchant_currency_only: merchant_currency_only
        :type merchant_currency_only: bool
        :param cardholder_name: cardholder_name
        :type cardholder_name: str
        :param cardholder_preferred_currency: cardholder_preferred_currency, defaults to None
        :type cardholder_preferred_currency: str, optional
        :param dynamic_currency_conversion: dynamic_currency_conversion, defaults to None
        :type dynamic_currency_conversion: bool, optional
        """
        self.save_card_default = save_card_default
        self.payment_fees_display = payment_fees_display
        self.billing_address_collect = billing_address_collect
        self.display_description = display_description
        self.merchant_currency_only = merchant_currency_only
        self.cardholder_name = cardholder_name
        self.cardholder_preferred_currency = self._define_str(
            "cardholder_preferred_currency",
            cardholder_preferred_currency,
            nullable=True,
        )
        self.dynamic_currency_conversion = dynamic_currency_conversion
