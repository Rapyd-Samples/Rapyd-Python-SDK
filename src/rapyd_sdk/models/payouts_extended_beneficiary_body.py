from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .category import Category
from .entity_type import EntityType
from .gender import Gender


class IdentificationType(Enum):
    """An enumeration representing different categories.

    :cvar DRIVERSLICENSE: "drivers_license"
    :vartype DRIVERSLICENSE: str
    :cvar IDENTIFICATIONID: "identification_id"
    :vartype IDENTIFICATIONID: str
    :cvar INTERNATIONALPASSPORT: "international_passport"
    :vartype INTERNATIONALPASSPORT: str
    :cvar RESIDENCEPERMIT: "residence_permit"
    :vartype RESIDENCEPERMIT: str
    :cvar SOCIALSECURITY: "social_security"
    :vartype SOCIALSECURITY: str
    :cvar WORKPERMIT: "work_permit"
    :vartype WORKPERMIT: str
    """

    DRIVERSLICENSE = "drivers_license"
    IDENTIFICATIONID = "identification_id"
    INTERNATIONALPASSPORT = "international_passport"
    RESIDENCEPERMIT = "residence_permit"
    SOCIALSECURITY = "social_security"
    WORKPERMIT = "work_permit"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, IdentificationType._member_map_.values()))


@JsonMap({})
class PayoutsExtendedBeneficiaryBody(BaseModel):
    """PayoutsExtendedBeneficiaryBody

    :param address: Beneficiary's street address including the build number.
    :type address: str
    :param city: City of the beneficiary.
    :type city: str
    :param category: category
    :type category: Category
    :param company_name: Name of the beneficiary company. Required when `entity_type` is **company**., defaults to None
    :type company_name: str, optional
    :param country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code.
    :type country: str
    :param country_of_incorporation: The country where the company was registered. Two-letter ISO 3166-1 ALPHA-2 code. Required when `entity_type` is **company**., defaults to None
    :type country_of_incorporation: str, optional
    :param currency: currency
    :type currency: str
    :param date_of_birth: Date of birth of the individual. Format: DD/MM/YYYY. Required when `entity_type` is **individual**., defaults to None
    :type date_of_birth: str, optional
    :param date_of_incorporation: The date when the company was registered. Format: DD/MM/YYYY. Required when `entity_type` is **company**., defaults to None
    :type date_of_incorporation: str, optional
    :param default_payout_method_type: The type of payout method for the beneficiary. The two-letter prefix must match the beneficiary country code., defaults to None
    :type default_payout_method_type: str, optional
    :param entity_type: entity_type
    :type entity_type: EntityType
    :param first_name: First name of the beneficiary. Required when `entity_type` is **individual**., defaults to None
    :type first_name: str, optional
    :param gender: Gender of the individual. Required when `entity_type` is **individual**., defaults to None
    :type gender: Gender, optional
    :param identification_type: Type of identification document for the beneficiary. When `entity_type` is **company**, this field must be**company_registered_number**. When `entity_type` is **individual**:
    :type identification_type: IdentificationType
    :param identification_value: Identification number on the document mentioned in `identification_type`.
    :type identification_value: str
    :param last_name: Family name of the beneficiary. Required when `entity_type` is **individual**. Required when `entity_type` is **individual**., defaults to None
    :type last_name: str, optional
    :param merchant_reference_id: ID defined by the client., defaults to None
    :type merchant_reference_id: str, optional
    :param nationality: The citizenship of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code for the country. To determine the code for a country, see 'List Countries'. Required when `entity_type` is **individual**., defaults to None
    :type nationality: str, optional
    """

    def __init__(
        self,
        address: str,
        city: str,
        category: Category,
        country: str,
        currency: str,
        entity_type: EntityType,
        identification_type: IdentificationType,
        identification_value: str,
        company_name: str = None,
        country_of_incorporation: str = None,
        date_of_birth: str = None,
        date_of_incorporation: str = None,
        default_payout_method_type: str = None,
        first_name: str = None,
        gender: Gender = None,
        last_name: str = None,
        merchant_reference_id: str = None,
        nationality: str = None,
    ):
        """PayoutsExtendedBeneficiaryBody

        :param address: Beneficiary's street address including the build number.
        :type address: str
        :param city: City of the beneficiary.
        :type city: str
        :param category: category
        :type category: Category
        :param company_name: Name of the beneficiary company. Required when `entity_type` is **company**., defaults to None
        :type company_name: str, optional
        :param country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code.
        :type country: str
        :param country_of_incorporation: The country where the company was registered. Two-letter ISO 3166-1 ALPHA-2 code. Required when `entity_type` is **company**., defaults to None
        :type country_of_incorporation: str, optional
        :param currency: currency
        :type currency: str
        :param date_of_birth: Date of birth of the individual. Format: DD/MM/YYYY. Required when `entity_type` is **individual**., defaults to None
        :type date_of_birth: str, optional
        :param date_of_incorporation: The date when the company was registered. Format: DD/MM/YYYY. Required when `entity_type` is **company**., defaults to None
        :type date_of_incorporation: str, optional
        :param default_payout_method_type: The type of payout method for the beneficiary. The two-letter prefix must match the beneficiary country code., defaults to None
        :type default_payout_method_type: str, optional
        :param entity_type: entity_type
        :type entity_type: EntityType
        :param first_name: First name of the beneficiary. Required when `entity_type` is **individual**., defaults to None
        :type first_name: str, optional
        :param gender: Gender of the individual. Required when `entity_type` is **individual**., defaults to None
        :type gender: Gender, optional
        :param identification_type: Type of identification document for the beneficiary. When `entity_type` is **company**, this field must be**company_registered_number**. When `entity_type` is **individual**:
        :type identification_type: IdentificationType
        :param identification_value: Identification number on the document mentioned in `identification_type`.
        :type identification_value: str
        :param last_name: Family name of the beneficiary. Required when `entity_type` is **individual**. Required when `entity_type` is **individual**., defaults to None
        :type last_name: str, optional
        :param merchant_reference_id: ID defined by the client., defaults to None
        :type merchant_reference_id: str, optional
        :param nationality: The citizenship of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code for the country. To determine the code for a country, see 'List Countries'. Required when `entity_type` is **individual**., defaults to None
        :type nationality: str, optional
        """
        self.address = address
        self.city = city
        self.category = self._enum_matching(category, Category.list(), "category")
        self.company_name = self._define_str(
            "company_name", company_name, nullable=True
        )
        self.country = country
        self.country_of_incorporation = self._define_str(
            "country_of_incorporation", country_of_incorporation, nullable=True
        )
        self.currency = self._define_str(
            "currency",
            currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.date_of_birth = self._define_str(
            "date_of_birth", date_of_birth, nullable=True
        )
        self.date_of_incorporation = self._define_str(
            "date_of_incorporation", date_of_incorporation, nullable=True
        )
        self.default_payout_method_type = self._define_str(
            "default_payout_method_type", default_payout_method_type, nullable=True
        )
        self.entity_type = self._enum_matching(
            entity_type, EntityType.list(), "entity_type"
        )
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.gender = (
            self._enum_matching(gender, Gender.list(), "gender") if gender else None
        )
        self.identification_type = self._enum_matching(
            identification_type, IdentificationType.list(), "identification_type"
        )
        self.identification_value = identification_value
        self.last_name = self._define_str("last_name", last_name, nullable=True)
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.nationality = self._define_str("nationality", nationality, nullable=True)
