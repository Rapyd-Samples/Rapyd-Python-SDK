from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class Duration(Enum):
    """An enumeration representing different categories.

    :cvar FOREVER: "forever"
    :vartype FOREVER: str
    :cvar REPEATING: "repeating"
    :vartype REPEATING: str
    """

    FOREVER = "forever"
    REPEATING = "repeating"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Duration._member_map_.values()))


@JsonMap({"id_": "id"})
class Coupon(BaseModel):
    """The coupon can be applied to the following objects - * Subscription - All charges in the subscription are subject to the discount described in the coupon. To add a coupon to a subscription, first use Create Coupon. Then add the coupon ID to the coupon field of the subscription with Create Subscription or Update Subscription. * Customer - The discount applies to all charges to the customer. To add a coupon to a customer, first use Create Coupon. Then add the coupon ID to the coupon field of the customer with Create Customer or Update Customer. * Order - The discount applies to a single order. To add a coupon to an order, first use Create Coupon. The duration field of the coupon must be set to repeating, and the duration_in_months and discount_duration_in_uses fields must be set to 1. Then add the coupon ID to the coupon field of the order with Create an Order or Update Order. A coupon can be applied to one or more customers or subscriptions. However, a subscription can have only one coupon, and the only way to assign two or more coupons to a customer is to assign them to separate subscriptions. If there is a coupon for the customer and another coupon for the customer's subscription, the subscription coupon takes precedence.

    :param amount_off: The amount of money to subtract from the payment. Decimal. Range: Positive decimal number, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015., defaults to None
    :type amount_off: float, optional
    :param created: When the coupon was created, in Unix time. Response only., defaults to None
    :type created: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param description: Description of the coupon., defaults to None
    :type description: str, optional
    :param discount_duration_in_uses: The number of times that the coupon can be redeemed by a specific customer or subscription. Relevant when duration is repeating and redeem_by is not set., defaults to None
    :type discount_duration_in_uses: float, optional
    :param discount_valid_until: The final date that a discount can be used, in Unix time. Relevant when discount_validity_in_months is not set., defaults to None
    :type discount_valid_until: float, optional
    :param discount_validity_in_months: The number of months after the discount is created that it can be used. Relevant when discount_valid_until is not set., defaults to None
    :type discount_validity_in_months: float, optional
    :param duration: Determines how long the discount remains in effect. One of the following:  * forever  * repeating , defaults to None
    :type duration: Duration, optional
    :param duration_in_months: Determines the number of months that the coupon remains in effect after its creation. Integer. Required when duration is repeating., defaults to None
    :type duration_in_months: float, optional
    :param id_: Unique ID for this coupon. English alphanumeric characters with no special characters except underscore. If the merchant does not define an ID, Rapyd generates a string starting with coupon_., defaults to None
    :type id_: str, optional
    :param max_redemptions: Determines the number of times the coupon can be redeemed. The number of customers, subscriptions or orders that the coupon is applied to cannot exceed this number. Integer., defaults to None
    :type max_redemptions: float, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param percent_off: Determines the size of the discount, measured in percent. Integer. Range: 1-100., defaults to None
    :type percent_off: float, optional
    :param redeem_by: The last time at which the coupon can be redeemed, in Unix time. After the redeem_by date, the coupon can no longer be applied to new customers. 'redeem_by' takes precedence over the setting of discount_duration_in_uses and duration_in_months., defaults to None
    :type redeem_by: float, optional
    :param times_redeemed: Indicates the number of times the coupon has been applied to a customer, subscription or invoice. If the discount has been used more than one time by a customer, subscription or invoice, the number of redemptions after the first is also added to this value. Integer. When this value equals max_redemptions, the coupon becomes no longer valid. Response only., defaults to None
    :type times_redeemed: float, optional
    :param valid: Indicates whether the coupon can be redeemed., defaults to None
    :type valid: bool, optional
    """

    def __init__(
        self,
        amount_off: float = None,
        created: float = None,
        currency: str = None,
        description: str = None,
        discount_duration_in_uses: float = None,
        discount_valid_until: float = None,
        discount_validity_in_months: float = None,
        duration: Duration = None,
        duration_in_months: float = None,
        id_: str = None,
        max_redemptions: float = None,
        metadata: dict = None,
        percent_off: float = None,
        redeem_by: float = None,
        times_redeemed: float = None,
        valid: bool = None,
    ):
        """The coupon can be applied to the following objects - * Subscription - All charges in the subscription are subject to the discount described in the coupon. To add a coupon to a subscription, first use Create Coupon. Then add the coupon ID to the coupon field of the subscription with Create Subscription or Update Subscription. * Customer - The discount applies to all charges to the customer. To add a coupon to a customer, first use Create Coupon. Then add the coupon ID to the coupon field of the customer with Create Customer or Update Customer. * Order - The discount applies to a single order. To add a coupon to an order, first use Create Coupon. The duration field of the coupon must be set to repeating, and the duration_in_months and discount_duration_in_uses fields must be set to 1. Then add the coupon ID to the coupon field of the order with Create an Order or Update Order. A coupon can be applied to one or more customers or subscriptions. However, a subscription can have only one coupon, and the only way to assign two or more coupons to a customer is to assign them to separate subscriptions. If there is a coupon for the customer and another coupon for the customer's subscription, the subscription coupon takes precedence.

        :param amount_off: The amount of money to subtract from the payment. Decimal. Range: Positive decimal number, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015., defaults to None
        :type amount_off: float, optional
        :param created: When the coupon was created, in Unix time. Response only., defaults to None
        :type created: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param description: Description of the coupon., defaults to None
        :type description: str, optional
        :param discount_duration_in_uses: The number of times that the coupon can be redeemed by a specific customer or subscription. Relevant when duration is repeating and redeem_by is not set., defaults to None
        :type discount_duration_in_uses: float, optional
        :param discount_valid_until: The final date that a discount can be used, in Unix time. Relevant when discount_validity_in_months is not set., defaults to None
        :type discount_valid_until: float, optional
        :param discount_validity_in_months: The number of months after the discount is created that it can be used. Relevant when discount_valid_until is not set., defaults to None
        :type discount_validity_in_months: float, optional
        :param duration: Determines how long the discount remains in effect. One of the following:  * forever  * repeating , defaults to None
        :type duration: Duration, optional
        :param duration_in_months: Determines the number of months that the coupon remains in effect after its creation. Integer. Required when duration is repeating., defaults to None
        :type duration_in_months: float, optional
        :param id_: Unique ID for this coupon. English alphanumeric characters with no special characters except underscore. If the merchant does not define an ID, Rapyd generates a string starting with coupon_., defaults to None
        :type id_: str, optional
        :param max_redemptions: Determines the number of times the coupon can be redeemed. The number of customers, subscriptions or orders that the coupon is applied to cannot exceed this number. Integer., defaults to None
        :type max_redemptions: float, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param percent_off: Determines the size of the discount, measured in percent. Integer. Range: 1-100., defaults to None
        :type percent_off: float, optional
        :param redeem_by: The last time at which the coupon can be redeemed, in Unix time. After the redeem_by date, the coupon can no longer be applied to new customers. 'redeem_by' takes precedence over the setting of discount_duration_in_uses and duration_in_months., defaults to None
        :type redeem_by: float, optional
        :param times_redeemed: Indicates the number of times the coupon has been applied to a customer, subscription or invoice. If the discount has been used more than one time by a customer, subscription or invoice, the number of redemptions after the first is also added to this value. Integer. When this value equals max_redemptions, the coupon becomes no longer valid. Response only., defaults to None
        :type times_redeemed: float, optional
        :param valid: Indicates whether the coupon can be redeemed., defaults to None
        :type valid: bool, optional
        """
        self.amount_off = self._define_number("amount_off", amount_off, nullable=True)
        self.created = self._define_number("created", created, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.description = self._define_str("description", description, nullable=True)
        self.discount_duration_in_uses = self._define_number(
            "discount_duration_in_uses", discount_duration_in_uses, nullable=True
        )
        self.discount_valid_until = self._define_number(
            "discount_valid_until", discount_valid_until, nullable=True
        )
        self.discount_validity_in_months = self._define_number(
            "discount_validity_in_months", discount_validity_in_months, nullable=True
        )
        self.duration = (
            self._enum_matching(duration, Duration.list(), "duration")
            if duration
            else None
        )
        self.duration_in_months = self._define_number(
            "duration_in_months", duration_in_months, nullable=True
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.max_redemptions = self._define_number(
            "max_redemptions", max_redemptions, nullable=True
        )
        self.metadata = metadata
        self.percent_off = self._define_number(
            "percent_off", percent_off, nullable=True
        )
        self.redeem_by = self._define_number("redeem_by", redeem_by, nullable=True)
        self.times_redeemed = self._define_number(
            "times_redeemed", times_redeemed, nullable=True
        )
        self.valid = valid
