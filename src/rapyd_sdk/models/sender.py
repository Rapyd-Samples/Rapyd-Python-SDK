from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .entity_type import EntityType


@JsonMap({"id_": "id"})
class Sender(BaseModel):
    """Sender

    :param account_number: Bank account number of sender., defaults to None
    :type account_number: str, optional
    :param additional_data: Additional data required by the payout method. Object.., defaults to None
    :type additional_data: dict, optional
    :param additional_last_name: The person's second last name., defaults to None
    :type additional_last_name: str, optional
    :param address: The address of the sender., defaults to None
    :type address: str, optional
    :param bank_code: Domestic identifier of the bank., defaults to None
    :type bank_code: str, optional
    :param bank_name: Name of the bank., defaults to None
    :type bank_name: str, optional
    :param beneficiary_relationship: When the beneficiary is not a relative of the sender, the relationship should be specified as client or non-relative., defaults to None
    :type beneficiary_relationship: str, optional
    :param city: City where the sender is located., defaults to None
    :type city: str, optional
    :param company_name: Name of the sender company. Relevant when entity_type is company., defaults to None
    :type company_name: str, optional
    :param country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
    :type country: str, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param date_of_birth: The date of birth of the sender. Relevant when entity_type is individual., defaults to None
    :type date_of_birth: str, optional
    :param date_of_incorporation: Date of incorporation of the corporation., defaults to None
    :type date_of_incorporation: str, optional
    :param email: The person's email address., defaults to None
    :type email: str, optional
    :param entity_type: entity_type, defaults to None
    :type entity_type: EntityType, optional
    :param first_name: First name of the sender. Relevant when `entity_type` is **individual**., defaults to None
    :type first_name: str, optional
    :param id_: ID of the Sender object. String starting with **sender_**. Response only., defaults to None
    :type id_: str, optional
    :param id_date_of_issue: The date of issuance of the person's identification document., defaults to None
    :type id_date_of_issue: str, optional
    :param id_expiry: The expiration date of the person's identification document., defaults to None
    :type id_expiry: str, optional
    :param id_issue_authority: The government agency that issued the person's identification document., defaults to None
    :type id_issue_authority: str, optional
    :param id_issue_location: The location where the person's identification document was issued., defaults to None
    :type id_issue_location: str, optional
    :param identification_type: Type of identification document for the sender. When entity_type is company, this field must be company_registered_number. When entity_type is individual, one of the following values:  * drivers_license  * identification_id  * international_passport  * residence_permit* social_security  * work_permit , defaults to None
    :type identification_type: str, optional
    :param identification_value: identification number on the document mentioned in `identification_type`., defaults to None
    :type identification_value: str, optional
    :param last_name: Last name of the sender. Relevant when `entity_type` is individual., defaults to None
    :type last_name: str, optional
    :param merchant_reference_id: ID defined by the merchant. Rapyd does not validate this value to enforce uniqueness., defaults to None
    :type merchant_reference_id: str, optional
    :param middle_name: The person's middle name., defaults to None
    :type middle_name: str, optional
    :param mobile_number: Mobile phone number in E.164 format., defaults to None
    :type mobile_number: str, optional
    :param name: Name of the sender. Relevant when `entity_type` is company., defaults to None
    :type name: str, optional
    :param nationality: The person's nationality., defaults to None
    :type nationality: str, optional
    :param occupation: The person's occupation., defaults to None
    :type occupation: str, optional
    :param phone_country_code: The country code of the person's phone., defaults to None
    :type phone_country_code: str, optional
    :param phone_number: Phone number in E.164 format., defaults to None
    :type phone_number: str, optional
    :param postcode: Postal code of the sender., defaults to None
    :type postcode: str, optional
    :param province: Province portion of the address., defaults to None
    :type province: str, optional
    :param purpose_code: Reason for the payout., defaults to None
    :type purpose_code: str, optional
    :param source_of_income: The person's source of income., defaults to None
    :type source_of_income: str, optional
    :param state: State where the sender is located., defaults to None
    :type state: str, optional
    :param suburb: District of the sender's or beneficiary's city., defaults to None
    :type suburb: str, optional
    :param tax_id: Tax identification number., defaults to None
    :type tax_id: str, optional
    """

    def __init__(
        self,
        account_number: str = None,
        additional_data: dict = None,
        additional_last_name: str = None,
        address: str = None,
        bank_code: str = None,
        bank_name: str = None,
        beneficiary_relationship: str = None,
        city: str = None,
        company_name: str = None,
        country: str = None,
        currency: str = None,
        date_of_birth: str = None,
        date_of_incorporation: str = None,
        email: str = None,
        entity_type: EntityType = None,
        first_name: str = None,
        id_: str = None,
        id_date_of_issue: str = None,
        id_expiry: str = None,
        id_issue_authority: str = None,
        id_issue_location: str = None,
        identification_type: str = None,
        identification_value: str = None,
        last_name: str = None,
        merchant_reference_id: str = None,
        middle_name: str = None,
        mobile_number: str = None,
        name: str = None,
        nationality: str = None,
        occupation: str = None,
        phone_country_code: str = None,
        phone_number: str = None,
        postcode: str = None,
        province: str = None,
        purpose_code: str = None,
        source_of_income: str = None,
        state: str = None,
        suburb: str = None,
        tax_id: str = None,
    ):
        """Sender

        :param account_number: Bank account number of sender., defaults to None
        :type account_number: str, optional
        :param additional_data: Additional data required by the payout method. Object.., defaults to None
        :type additional_data: dict, optional
        :param additional_last_name: The person's second last name., defaults to None
        :type additional_last_name: str, optional
        :param address: The address of the sender., defaults to None
        :type address: str, optional
        :param bank_code: Domestic identifier of the bank., defaults to None
        :type bank_code: str, optional
        :param bank_name: Name of the bank., defaults to None
        :type bank_name: str, optional
        :param beneficiary_relationship: When the beneficiary is not a relative of the sender, the relationship should be specified as client or non-relative., defaults to None
        :type beneficiary_relationship: str, optional
        :param city: City where the sender is located., defaults to None
        :type city: str, optional
        :param company_name: Name of the sender company. Relevant when entity_type is company., defaults to None
        :type company_name: str, optional
        :param country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
        :type country: str, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param date_of_birth: The date of birth of the sender. Relevant when entity_type is individual., defaults to None
        :type date_of_birth: str, optional
        :param date_of_incorporation: Date of incorporation of the corporation., defaults to None
        :type date_of_incorporation: str, optional
        :param email: The person's email address., defaults to None
        :type email: str, optional
        :param entity_type: entity_type, defaults to None
        :type entity_type: EntityType, optional
        :param first_name: First name of the sender. Relevant when `entity_type` is **individual**., defaults to None
        :type first_name: str, optional
        :param id_: ID of the Sender object. String starting with **sender_**. Response only., defaults to None
        :type id_: str, optional
        :param id_date_of_issue: The date of issuance of the person's identification document., defaults to None
        :type id_date_of_issue: str, optional
        :param id_expiry: The expiration date of the person's identification document., defaults to None
        :type id_expiry: str, optional
        :param id_issue_authority: The government agency that issued the person's identification document., defaults to None
        :type id_issue_authority: str, optional
        :param id_issue_location: The location where the person's identification document was issued., defaults to None
        :type id_issue_location: str, optional
        :param identification_type: Type of identification document for the sender. When entity_type is company, this field must be company_registered_number. When entity_type is individual, one of the following values:  * drivers_license  * identification_id  * international_passport  * residence_permit* social_security  * work_permit , defaults to None
        :type identification_type: str, optional
        :param identification_value: identification number on the document mentioned in `identification_type`., defaults to None
        :type identification_value: str, optional
        :param last_name: Last name of the sender. Relevant when `entity_type` is individual., defaults to None
        :type last_name: str, optional
        :param merchant_reference_id: ID defined by the merchant. Rapyd does not validate this value to enforce uniqueness., defaults to None
        :type merchant_reference_id: str, optional
        :param middle_name: The person's middle name., defaults to None
        :type middle_name: str, optional
        :param mobile_number: Mobile phone number in E.164 format., defaults to None
        :type mobile_number: str, optional
        :param name: Name of the sender. Relevant when `entity_type` is company., defaults to None
        :type name: str, optional
        :param nationality: The person's nationality., defaults to None
        :type nationality: str, optional
        :param occupation: The person's occupation., defaults to None
        :type occupation: str, optional
        :param phone_country_code: The country code of the person's phone., defaults to None
        :type phone_country_code: str, optional
        :param phone_number: Phone number in E.164 format., defaults to None
        :type phone_number: str, optional
        :param postcode: Postal code of the sender., defaults to None
        :type postcode: str, optional
        :param province: Province portion of the address., defaults to None
        :type province: str, optional
        :param purpose_code: Reason for the payout., defaults to None
        :type purpose_code: str, optional
        :param source_of_income: The person's source of income., defaults to None
        :type source_of_income: str, optional
        :param state: State where the sender is located., defaults to None
        :type state: str, optional
        :param suburb: District of the sender's or beneficiary's city., defaults to None
        :type suburb: str, optional
        :param tax_id: Tax identification number., defaults to None
        :type tax_id: str, optional
        """
        self.account_number = self._define_str(
            "account_number", account_number, nullable=True
        )
        self.additional_data = additional_data
        self.additional_last_name = self._define_str(
            "additional_last_name", additional_last_name, nullable=True
        )
        self.address = self._define_str("address", address, nullable=True)
        self.bank_code = self._define_str("bank_code", bank_code, nullable=True)
        self.bank_name = self._define_str("bank_name", bank_name, nullable=True)
        self.beneficiary_relationship = self._define_str(
            "beneficiary_relationship", beneficiary_relationship, nullable=True
        )
        self.city = self._define_str("city", city, nullable=True)
        self.company_name = self._define_str(
            "company_name", company_name, nullable=True
        )
        self.country = self._define_str("country", country, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.date_of_birth = self._define_str(
            "date_of_birth", date_of_birth, nullable=True
        )
        self.date_of_incorporation = self._define_str(
            "date_of_incorporation", date_of_incorporation, nullable=True
        )
        self.email = self._define_str("email", email, nullable=True)
        self.entity_type = (
            self._enum_matching(entity_type, EntityType.list(), "entity_type")
            if entity_type
            else None
        )
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.id_date_of_issue = self._define_str(
            "id_date_of_issue", id_date_of_issue, nullable=True
        )
        self.id_expiry = self._define_str("id_expiry", id_expiry, nullable=True)
        self.id_issue_authority = self._define_str(
            "id_issue_authority", id_issue_authority, nullable=True
        )
        self.id_issue_location = self._define_str(
            "id_issue_location", id_issue_location, nullable=True
        )
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
        self.middle_name = self._define_str("middle_name", middle_name, nullable=True)
        self.mobile_number = self._define_str(
            "mobile_number", mobile_number, nullable=True
        )
        self.name = self._define_str("name", name, nullable=True)
        self.nationality = self._define_str("nationality", nationality, nullable=True)
        self.occupation = self._define_str("occupation", occupation, nullable=True)
        self.phone_country_code = self._define_str(
            "phone_country_code", phone_country_code, nullable=True
        )
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
        self.postcode = self._define_str("postcode", postcode, nullable=True)
        self.province = self._define_str("province", province, nullable=True)
        self.purpose_code = self._define_str(
            "purpose_code", purpose_code, nullable=True
        )
        self.source_of_income = self._define_str(
            "source_of_income", source_of_income, nullable=True
        )
        self.state = self._define_str("state", state, nullable=True)
        self.suburb = self._define_str("suburb", suburb, nullable=True)
        self.tax_id = self._define_str("tax_id", tax_id, nullable=True)
