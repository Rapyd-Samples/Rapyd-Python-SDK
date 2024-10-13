from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .category import Category
from .entity_type import EntityType


@JsonMap({})
class PayoutsBeneficiaryBody(BaseModel):
    """PayoutsBeneficiaryBody

    :param category: category
    :type category: Category
    :param company_name: Name of the beneficiary company. Relevant when `entity_type` is company., defaults to None
    :type company_name: str, optional
    :param country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code.
    :type country: str
    :param currency: currency
    :type currency: str
    :param default_payout_method_type: The type of payout method for the beneficiary. The two-letter prefix must match the beneficiary country code., defaults to None
    :type default_payout_method_type: str, optional
    :param entity_type: entity_type
    :type entity_type: EntityType
    :param first_name: First name of the beneficiary. Relevant when `entity_type` is individual., defaults to None
    :type first_name: str, optional
    :param identification_type: Type of identification document for the beneficiary., defaults to None
    :type identification_type: str, optional
    :param identification_value: Identification number on the document mentioned in `identification_type`., defaults to None
    :type identification_value: str, optional
    :param last_name: Family name of the beneficiary. Relevant when `entity_type` is individual., defaults to None
    :type last_name: str, optional
    :param merchant_reference_id: ID defined by the client., defaults to None
    :type merchant_reference_id: str, optional
    """

    def __init__(
        self,
        category: Category,
        country: str,
        currency: str,
        entity_type: EntityType,
        company_name: str = None,
        default_payout_method_type: str = None,
        first_name: str = None,
        identification_type: str = None,
        identification_value: str = None,
        last_name: str = None,
        merchant_reference_id: str = None,
    ):
        """PayoutsBeneficiaryBody

        :param category: category
        :type category: Category
        :param company_name: Name of the beneficiary company. Relevant when `entity_type` is company., defaults to None
        :type company_name: str, optional
        :param country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code.
        :type country: str
        :param currency: currency
        :type currency: str
        :param default_payout_method_type: The type of payout method for the beneficiary. The two-letter prefix must match the beneficiary country code., defaults to None
        :type default_payout_method_type: str, optional
        :param entity_type: entity_type
        :type entity_type: EntityType
        :param first_name: First name of the beneficiary. Relevant when `entity_type` is individual., defaults to None
        :type first_name: str, optional
        :param identification_type: Type of identification document for the beneficiary., defaults to None
        :type identification_type: str, optional
        :param identification_value: Identification number on the document mentioned in `identification_type`., defaults to None
        :type identification_value: str, optional
        :param last_name: Family name of the beneficiary. Relevant when `entity_type` is individual., defaults to None
        :type last_name: str, optional
        :param merchant_reference_id: ID defined by the client., defaults to None
        :type merchant_reference_id: str, optional
        """
        self.category = self._enum_matching(category, Category.list(), "category")
        self.company_name = self._define_str(
            "company_name", company_name, nullable=True
        )
        self.country = country
        self.currency = self._define_str(
            "currency",
            currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.default_payout_method_type = self._define_str(
            "default_payout_method_type", default_payout_method_type, nullable=True
        )
        self.entity_type = self._enum_matching(
            entity_type, EntityType.list(), "entity_type"
        )
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.identification_type = self._define_str(
            "identification_type", identification_type, nullable=True
        )
        self.identification_value = self._define_str(
            "identification_value", identification_value, nullable=True
        )
        self.last_name = self._define_str("last_name", last_name, nullable=True)
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
