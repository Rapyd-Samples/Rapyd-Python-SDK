from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .entity_type import EntityType
from .payout_required_fields import PayoutRequiredFields


@JsonMap({})
class PayoutMethodTypeDetails(BaseModel):
    """PayoutMethodTypeDetails

    :param batch_file_header: concatenation of all fields., defaults to None
    :type batch_file_header: str, optional
    :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
    :type beneficiary_country: str, optional
    :param beneficiary_entity_type: beneficiary_entity_type, defaults to None
    :type beneficiary_entity_type: EntityType, optional
    :param beneficiary_required_fields: Lists all the beneficiary required fields for payout method, defaults to None
    :type beneficiary_required_fields: List[PayoutRequiredFields], optional
    :param image: URL of an image that the merchant can use to represent the payout method., defaults to None
    :type image: str, optional
    :param is_cancelable: Indicates whether the payout can be canceled. Relevant when category is cash. One of the following values 0 - Not cancelable. 1 - cancelable.', defaults to None
    :type is_cancelable: int, optional
    :param is_expirable: Indicates whether the payout expires if not completed. Relevant when category is cash. One of the following values 0 - Not expirable. 1 - expirable.', defaults to None
    :type is_expirable: int, optional
    :param is_location_specific: Indicates whether the payout must be made at a specific physical location. Relevant when category is cash. One of the following values 0 - Not location specific. 1 - location specific.', defaults to None
    :type is_location_specific: int, optional
    :param is_online: Indicates whether the payout is made automatically, without any action by the beneficiary., defaults to None
    :type is_online: bool, optional
    :param maximum_amount: Maximum amount supported by this payout method for the indicated currency. Decimal number., defaults to None
    :type maximum_amount: float, optional
    :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payout. Relevant when is_expirable is true., defaults to None
    :type maximum_expiration_seconds: float, optional
    :param minimum_amount: Minimum amount supported by this payout method for the indicated currency. Decimal number., defaults to None
    :type minimum_amount: float, optional
    :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payout. Relevant when is_expirable is true., defaults to None
    :type minimum_expiration_seconds: float, optional
    :param payout_currency: payout_currency, defaults to None
    :type payout_currency: str, optional
    :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country code. Required when default_payout_method_type is not used., defaults to None
    :type payout_method_type: str, optional
    :param payout_options: Lists all the payout options for payout method., defaults to None
    :type payout_options: List[PayoutRequiredFields], optional
    :param sender_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
    :type sender_country: str, optional
    :param sender_currency: sender_currency, defaults to None
    :type sender_currency: str, optional
    :param sender_entity_type: sender_entity_type, defaults to None
    :type sender_entity_type: EntityType, optional
    :param sender_required_fields: Lists all the sender required fields for payout method, defaults to None
    :type sender_required_fields: List[PayoutRequiredFields], optional
    :param status: Indicates whether the payout method is currently available. One of the following values: 0 - Not available. 1 - Available., defaults to None
    :type status: int, optional
    """

    def __init__(
        self,
        batch_file_header: str = None,
        beneficiary_country: str = None,
        beneficiary_entity_type: EntityType = None,
        beneficiary_required_fields: List[PayoutRequiredFields] = None,
        image: str = None,
        is_cancelable: int = None,
        is_expirable: int = None,
        is_location_specific: int = None,
        is_online: bool = None,
        maximum_amount: float = None,
        maximum_expiration_seconds: float = None,
        minimum_amount: float = None,
        minimum_expiration_seconds: float = None,
        payout_currency: str = None,
        payout_method_type: str = None,
        payout_options: List[PayoutRequiredFields] = None,
        sender_country: str = None,
        sender_currency: str = None,
        sender_entity_type: EntityType = None,
        sender_required_fields: List[PayoutRequiredFields] = None,
        status: int = None,
    ):
        """PayoutMethodTypeDetails

        :param batch_file_header: concatenation of all fields., defaults to None
        :type batch_file_header: str, optional
        :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
        :type beneficiary_country: str, optional
        :param beneficiary_entity_type: beneficiary_entity_type, defaults to None
        :type beneficiary_entity_type: EntityType, optional
        :param beneficiary_required_fields: Lists all the beneficiary required fields for payout method, defaults to None
        :type beneficiary_required_fields: List[PayoutRequiredFields], optional
        :param image: URL of an image that the merchant can use to represent the payout method., defaults to None
        :type image: str, optional
        :param is_cancelable: Indicates whether the payout can be canceled. Relevant when category is cash. One of the following values 0 - Not cancelable. 1 - cancelable.', defaults to None
        :type is_cancelable: int, optional
        :param is_expirable: Indicates whether the payout expires if not completed. Relevant when category is cash. One of the following values 0 - Not expirable. 1 - expirable.', defaults to None
        :type is_expirable: int, optional
        :param is_location_specific: Indicates whether the payout must be made at a specific physical location. Relevant when category is cash. One of the following values 0 - Not location specific. 1 - location specific.', defaults to None
        :type is_location_specific: int, optional
        :param is_online: Indicates whether the payout is made automatically, without any action by the beneficiary., defaults to None
        :type is_online: bool, optional
        :param maximum_amount: Maximum amount supported by this payout method for the indicated currency. Decimal number., defaults to None
        :type maximum_amount: float, optional
        :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payout. Relevant when is_expirable is true., defaults to None
        :type maximum_expiration_seconds: float, optional
        :param minimum_amount: Minimum amount supported by this payout method for the indicated currency. Decimal number., defaults to None
        :type minimum_amount: float, optional
        :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payout. Relevant when is_expirable is true., defaults to None
        :type minimum_expiration_seconds: float, optional
        :param payout_currency: payout_currency, defaults to None
        :type payout_currency: str, optional
        :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country code. Required when default_payout_method_type is not used., defaults to None
        :type payout_method_type: str, optional
        :param payout_options: Lists all the payout options for payout method., defaults to None
        :type payout_options: List[PayoutRequiredFields], optional
        :param sender_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
        :type sender_country: str, optional
        :param sender_currency: sender_currency, defaults to None
        :type sender_currency: str, optional
        :param sender_entity_type: sender_entity_type, defaults to None
        :type sender_entity_type: EntityType, optional
        :param sender_required_fields: Lists all the sender required fields for payout method, defaults to None
        :type sender_required_fields: List[PayoutRequiredFields], optional
        :param status: Indicates whether the payout method is currently available. One of the following values: 0 - Not available. 1 - Available., defaults to None
        :type status: int, optional
        """
        self.batch_file_header = self._define_str(
            "batch_file_header", batch_file_header, nullable=True
        )
        self.beneficiary_country = self._define_str(
            "beneficiary_country", beneficiary_country, nullable=True
        )
        self.beneficiary_entity_type = (
            self._enum_matching(
                beneficiary_entity_type, EntityType.list(), "beneficiary_entity_type"
            )
            if beneficiary_entity_type
            else None
        )
        self.beneficiary_required_fields = self._define_list(
            beneficiary_required_fields, PayoutRequiredFields
        )
        self.image = self._define_str("image", image, nullable=True)
        self.is_cancelable = self._define_number(
            "is_cancelable", is_cancelable, nullable=True
        )
        self.is_expirable = self._define_number(
            "is_expirable", is_expirable, nullable=True
        )
        self.is_location_specific = self._define_number(
            "is_location_specific", is_location_specific, nullable=True
        )
        self.is_online = is_online
        self.maximum_amount = self._define_number(
            "maximum_amount", maximum_amount, nullable=True
        )
        self.maximum_expiration_seconds = self._define_number(
            "maximum_expiration_seconds", maximum_expiration_seconds, nullable=True
        )
        self.minimum_amount = self._define_number(
            "minimum_amount", minimum_amount, nullable=True
        )
        self.minimum_expiration_seconds = self._define_number(
            "minimum_expiration_seconds", minimum_expiration_seconds, nullable=True
        )
        self.payout_currency = self._define_str(
            "payout_currency",
            payout_currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.payout_method_type = self._define_str(
            "payout_method_type", payout_method_type, nullable=True
        )
        self.payout_options = self._define_list(payout_options, PayoutRequiredFields)
        self.sender_country = self._define_str(
            "sender_country", sender_country, nullable=True
        )
        self.sender_currency = self._define_str(
            "sender_currency",
            sender_currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.sender_entity_type = (
            self._enum_matching(
                sender_entity_type, EntityType.list(), "sender_entity_type"
            )
            if sender_entity_type
            else None
        )
        self.sender_required_fields = self._define_list(
            sender_required_fields, PayoutRequiredFields
        )
        self.status = self._define_number("status", status, nullable=True)
