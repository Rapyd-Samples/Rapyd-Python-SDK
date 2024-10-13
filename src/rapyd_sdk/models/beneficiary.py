from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .category import Category
from .entity_type import EntityType


@JsonMap({"id_": "id"})
class Beneficiary(BaseModel):
    """Beneficiary

    :param aba: American Bankers Association routing transit number. United States., defaults to None
    :type aba: str, optional
    :param account_number: The person's account number., defaults to None
    :type account_number: str, optional
    :param ach_code: Automated Clearing House (ACH) code., defaults to None
    :type ach_code: str, optional
    :param additional_data: Additional data required by the payout method. Object., defaults to None
    :type additional_data: dict, optional
    :param additional_last_name: The person's second last name., defaults to None
    :type additional_last_name: str, optional
    :param address: Street and number portion of the person's address., defaults to None
    :type address: str, optional
    :param bank_account_holder_name: Name of the account holder., defaults to None
    :type bank_account_holder_name: str, optional
    :param bank_account_type: Type of bank account, such as checking or savings., defaults to None
    :type bank_account_type: str, optional
    :param bank_address: Street and number portion of the bank's address., defaults to None
    :type bank_address: str, optional
    :param bank_branch_code: Identifier for the bank branch., defaults to None
    :type bank_branch_code: str, optional
    :param bank_branch_name: Name of the bank branch., defaults to None
    :type bank_branch_name: str, optional
    :param bank_city: City portion of the bank's address., defaults to None
    :type bank_city: str, optional
    :param bank_code: Domestic identifier of the bank., defaults to None
    :type bank_code: str, optional
    :param bank_country: Two-letter ISO 3166-1 ALPHA-2 code for the bank's country., defaults to None
    :type bank_country: str, optional
    :param bank_name: Name of the bank., defaults to None
    :type bank_name: str, optional
    :param bank_province: State or province portion of the bank's address., defaults to None
    :type bank_province: str, optional
    :param beneficiary_bic_local: NA., defaults to None
    :type beneficiary_bic_local: str, optional
    :param beneficiary_relationship: Relationship between the sender and the beneficiary., defaults to None
    :type beneficiary_relationship: str, optional
    :param bic_swift: BIC (SWIFT) code for the bank account., defaults to None
    :type bic_swift: str, optional
    :param bsb_code: Bank State Branch code for Australia., defaults to None
    :type bsb_code: str, optional
    :param card_expiration_month: The cardâ€™s expiration month., defaults to None
    :type card_expiration_month: str, optional
    :param card_expiration_year: The cardâ€™s expiration year., defaults to None
    :type card_expiration_year: str, optional
    :param card_number: The card number., defaults to None
    :type card_number: str, optional
    :param category: category, defaults to None
    :type category: Category, optional
    :param city: City portion of the address., defaults to None
    :type city: str, optional
    :param clabe: Standardized bank code for Mexico., defaults to None
    :type clabe: str, optional
    :param cnaps: China National Advanced Payments System (CNAPS) code number., defaults to None
    :type cnaps: str, optional
    :param company_name: Name of the beneficiary company. Relevant when entity_type is company., defaults to None
    :type company_name: str, optional
    :param confirmation_required: Indicates whether the beneficiary must respond to accept or decline a payout. Default is false. Relevant to the rapyd_ewallet payout method type, defaults to None
    :type confirmation_required: bool, optional
    :param country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
    :type country: str, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param date_of_birth: The person's date of birth., defaults to None
    :type date_of_birth: str, optional
    :param date_of_incorporation: Date of incorporation of the corporation., defaults to None
    :type date_of_incorporation: str, optional
    :param default_payout_method_type: The type of payout method for the beneficiary. The two-letter prefix must match the beneficiary country code., defaults to None
    :type default_payout_method_type: str, optional
    :param email: The person's email address., defaults to None
    :type email: str, optional
    :param entity_type: entity_type, defaults to None
    :type entity_type: EntityType, optional
    :param ewallet: ID of the wallet that the money is transferred to. String starting with **ewallet_**. Relevant to payout to Rapyd Wallet., defaults to None
    :type ewallet: str, optional
    :param first_name: First name of the beneficiary. Relevant when **entity_type** is individual., defaults to None
    :type first_name: str, optional
    :param iban: International Bank Account Number., defaults to None
    :type iban: str, optional
    :param id_: ID of the 'beneficiary' object. String starting with **beneficiary_**. Response only., defaults to None
    :type id_: str, optional
    :param id_date_of_issue: The date of issuance of the person's identification document., defaults to None
    :type id_date_of_issue: str, optional
    :param id_issue_authority: The government agency that issued the person's identification document., defaults to None
    :type id_issue_authority: str, optional
    :param id_issue_location: The location where the person's identification document was issued., defaults to None
    :type id_issue_location: str, optional
    :param identification_type: Type of identification document for the beneficiary. When entity_type is company, this field must be company_registered_number. When entity_type is individual, one of the following values: * drivers_license * identification_id * international_passport * residence_permit* social_security * work_permit , defaults to None
    :type identification_type: str, optional
    :param identification_value: identification number on the document mentioned in identification_type., defaults to None
    :type identification_value: str, optional
    :param ifsc: Indian Financial System Code for a bank branch., defaults to None
    :type ifsc: str, optional
    :param issuer_code: NA., defaults to None
    :type issuer_code: str, optional
    :param last_name: Last name of the beneficiary. Relevant when `entity_type` is individual., defaults to None
    :type last_name: str, optional
    :param merchant_reference_id: ID defined by the merchant. Rapyd does not validate this value to enforce uniqueness., defaults to None
    :type merchant_reference_id: str, optional
    :param middle_name: The person's middle name., defaults to None
    :type middle_name: str, optional
    :param mobile_number: Mobile phone number in E.164 format., defaults to None
    :type mobile_number: str, optional
    :param name: The person's full name., defaults to None
    :type name: str, optional
    :param nationality: The person's nationality., defaults to None
    :type nationality: str, optional
    :param payment_type: Additional classification of the type of payment, as required by the bank. Possible values: priority , regular, defaults to None
    :type payment_type: str, optional
    :param phone_country_code: The country code of the person's phone., defaults to None
    :type phone_country_code: str, optional
    :param phone_number: Phone number in E.164 format., defaults to None
    :type phone_number: str, optional
    :param postcode: Postal code portion of the address., defaults to None
    :type postcode: str, optional
    :param province: Province portion of the address., defaults to None
    :type province: str, optional
    :param purpose_code: Purpose of the transaction., defaults to None
    :type purpose_code: str, optional
    :param routing_code_type_1: NA., defaults to None
    :type routing_code_type_1: str, optional
    :param routing_code_type_2: NA., defaults to None
    :type routing_code_type_2: str, optional
    :param routing_code_type_3: NA., defaults to None
    :type routing_code_type_3: str, optional
    :param routing_code_value_1: NA., defaults to None
    :type routing_code_value_1: str, optional
    :param routing_code_value_2: NA., defaults to None
    :type routing_code_value_2: str, optional
    :param routing_code_value_3: NA., defaults to None
    :type routing_code_value_3: str, optional
    :param sort_code: Routing number for the UK., defaults to None
    :type sort_code: str, optional
    :param state: State portion of the address., defaults to None
    :type state: str, optional
    :param statement_narrative: Additional description suitable for a customer transaction statement., defaults to None
    :type statement_narrative: str, optional
    :param suburb: District of the sender's or beneficiary's city., defaults to None
    :type suburb: str, optional
    :param tax_id: Tax identification number., defaults to None
    :type tax_id: str, optional
    :param vpa: Virtual Payment Address., defaults to None
    :type vpa: str, optional
    """

    def __init__(
        self,
        aba: str = None,
        account_number: str = None,
        ach_code: str = None,
        additional_data: dict = None,
        additional_last_name: str = None,
        address: str = None,
        bank_account_holder_name: str = None,
        bank_account_type: str = None,
        bank_address: str = None,
        bank_branch_code: str = None,
        bank_branch_name: str = None,
        bank_city: str = None,
        bank_code: str = None,
        bank_country: str = None,
        bank_name: str = None,
        bank_province: str = None,
        beneficiary_bic_local: str = None,
        beneficiary_relationship: str = None,
        bic_swift: str = None,
        bsb_code: str = None,
        card_expiration_month: str = None,
        card_expiration_year: str = None,
        card_number: str = None,
        category: Category = None,
        city: str = None,
        clabe: str = None,
        cnaps: str = None,
        company_name: str = None,
        confirmation_required: bool = None,
        country: str = None,
        currency: str = None,
        date_of_birth: str = None,
        date_of_incorporation: str = None,
        default_payout_method_type: str = None,
        email: str = None,
        entity_type: EntityType = None,
        ewallet: str = None,
        first_name: str = None,
        iban: str = None,
        id_: str = None,
        id_date_of_issue: str = None,
        id_issue_authority: str = None,
        id_issue_location: str = None,
        identification_type: str = None,
        identification_value: str = None,
        ifsc: str = None,
        issuer_code: str = None,
        last_name: str = None,
        merchant_reference_id: str = None,
        middle_name: str = None,
        mobile_number: str = None,
        name: str = None,
        nationality: str = None,
        payment_type: str = None,
        phone_country_code: str = None,
        phone_number: str = None,
        postcode: str = None,
        province: str = None,
        purpose_code: str = None,
        routing_code_type_1: str = None,
        routing_code_type_2: str = None,
        routing_code_type_3: str = None,
        routing_code_value_1: str = None,
        routing_code_value_2: str = None,
        routing_code_value_3: str = None,
        sort_code: str = None,
        state: str = None,
        statement_narrative: str = None,
        suburb: str = None,
        tax_id: str = None,
        vpa: str = None,
    ):
        """Beneficiary

        :param aba: American Bankers Association routing transit number. United States., defaults to None
        :type aba: str, optional
        :param account_number: The person's account number., defaults to None
        :type account_number: str, optional
        :param ach_code: Automated Clearing House (ACH) code., defaults to None
        :type ach_code: str, optional
        :param additional_data: Additional data required by the payout method. Object., defaults to None
        :type additional_data: dict, optional
        :param additional_last_name: The person's second last name., defaults to None
        :type additional_last_name: str, optional
        :param address: Street and number portion of the person's address., defaults to None
        :type address: str, optional
        :param bank_account_holder_name: Name of the account holder., defaults to None
        :type bank_account_holder_name: str, optional
        :param bank_account_type: Type of bank account, such as checking or savings., defaults to None
        :type bank_account_type: str, optional
        :param bank_address: Street and number portion of the bank's address., defaults to None
        :type bank_address: str, optional
        :param bank_branch_code: Identifier for the bank branch., defaults to None
        :type bank_branch_code: str, optional
        :param bank_branch_name: Name of the bank branch., defaults to None
        :type bank_branch_name: str, optional
        :param bank_city: City portion of the bank's address., defaults to None
        :type bank_city: str, optional
        :param bank_code: Domestic identifier of the bank., defaults to None
        :type bank_code: str, optional
        :param bank_country: Two-letter ISO 3166-1 ALPHA-2 code for the bank's country., defaults to None
        :type bank_country: str, optional
        :param bank_name: Name of the bank., defaults to None
        :type bank_name: str, optional
        :param bank_province: State or province portion of the bank's address., defaults to None
        :type bank_province: str, optional
        :param beneficiary_bic_local: NA., defaults to None
        :type beneficiary_bic_local: str, optional
        :param beneficiary_relationship: Relationship between the sender and the beneficiary., defaults to None
        :type beneficiary_relationship: str, optional
        :param bic_swift: BIC (SWIFT) code for the bank account., defaults to None
        :type bic_swift: str, optional
        :param bsb_code: Bank State Branch code for Australia., defaults to None
        :type bsb_code: str, optional
        :param card_expiration_month: The cardâ€™s expiration month., defaults to None
        :type card_expiration_month: str, optional
        :param card_expiration_year: The cardâ€™s expiration year., defaults to None
        :type card_expiration_year: str, optional
        :param card_number: The card number., defaults to None
        :type card_number: str, optional
        :param category: category, defaults to None
        :type category: Category, optional
        :param city: City portion of the address., defaults to None
        :type city: str, optional
        :param clabe: Standardized bank code for Mexico., defaults to None
        :type clabe: str, optional
        :param cnaps: China National Advanced Payments System (CNAPS) code number., defaults to None
        :type cnaps: str, optional
        :param company_name: Name of the beneficiary company. Relevant when entity_type is company., defaults to None
        :type company_name: str, optional
        :param confirmation_required: Indicates whether the beneficiary must respond to accept or decline a payout. Default is false. Relevant to the rapyd_ewallet payout method type, defaults to None
        :type confirmation_required: bool, optional
        :param country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
        :type country: str, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param date_of_birth: The person's date of birth., defaults to None
        :type date_of_birth: str, optional
        :param date_of_incorporation: Date of incorporation of the corporation., defaults to None
        :type date_of_incorporation: str, optional
        :param default_payout_method_type: The type of payout method for the beneficiary. The two-letter prefix must match the beneficiary country code., defaults to None
        :type default_payout_method_type: str, optional
        :param email: The person's email address., defaults to None
        :type email: str, optional
        :param entity_type: entity_type, defaults to None
        :type entity_type: EntityType, optional
        :param ewallet: ID of the wallet that the money is transferred to. String starting with **ewallet_**. Relevant to payout to Rapyd Wallet., defaults to None
        :type ewallet: str, optional
        :param first_name: First name of the beneficiary. Relevant when **entity_type** is individual., defaults to None
        :type first_name: str, optional
        :param iban: International Bank Account Number., defaults to None
        :type iban: str, optional
        :param id_: ID of the 'beneficiary' object. String starting with **beneficiary_**. Response only., defaults to None
        :type id_: str, optional
        :param id_date_of_issue: The date of issuance of the person's identification document., defaults to None
        :type id_date_of_issue: str, optional
        :param id_issue_authority: The government agency that issued the person's identification document., defaults to None
        :type id_issue_authority: str, optional
        :param id_issue_location: The location where the person's identification document was issued., defaults to None
        :type id_issue_location: str, optional
        :param identification_type: Type of identification document for the beneficiary. When entity_type is company, this field must be company_registered_number. When entity_type is individual, one of the following values: * drivers_license * identification_id * international_passport * residence_permit* social_security * work_permit , defaults to None
        :type identification_type: str, optional
        :param identification_value: identification number on the document mentioned in identification_type., defaults to None
        :type identification_value: str, optional
        :param ifsc: Indian Financial System Code for a bank branch., defaults to None
        :type ifsc: str, optional
        :param issuer_code: NA., defaults to None
        :type issuer_code: str, optional
        :param last_name: Last name of the beneficiary. Relevant when `entity_type` is individual., defaults to None
        :type last_name: str, optional
        :param merchant_reference_id: ID defined by the merchant. Rapyd does not validate this value to enforce uniqueness., defaults to None
        :type merchant_reference_id: str, optional
        :param middle_name: The person's middle name., defaults to None
        :type middle_name: str, optional
        :param mobile_number: Mobile phone number in E.164 format., defaults to None
        :type mobile_number: str, optional
        :param name: The person's full name., defaults to None
        :type name: str, optional
        :param nationality: The person's nationality., defaults to None
        :type nationality: str, optional
        :param payment_type: Additional classification of the type of payment, as required by the bank. Possible values: priority , regular, defaults to None
        :type payment_type: str, optional
        :param phone_country_code: The country code of the person's phone., defaults to None
        :type phone_country_code: str, optional
        :param phone_number: Phone number in E.164 format., defaults to None
        :type phone_number: str, optional
        :param postcode: Postal code portion of the address., defaults to None
        :type postcode: str, optional
        :param province: Province portion of the address., defaults to None
        :type province: str, optional
        :param purpose_code: Purpose of the transaction., defaults to None
        :type purpose_code: str, optional
        :param routing_code_type_1: NA., defaults to None
        :type routing_code_type_1: str, optional
        :param routing_code_type_2: NA., defaults to None
        :type routing_code_type_2: str, optional
        :param routing_code_type_3: NA., defaults to None
        :type routing_code_type_3: str, optional
        :param routing_code_value_1: NA., defaults to None
        :type routing_code_value_1: str, optional
        :param routing_code_value_2: NA., defaults to None
        :type routing_code_value_2: str, optional
        :param routing_code_value_3: NA., defaults to None
        :type routing_code_value_3: str, optional
        :param sort_code: Routing number for the UK., defaults to None
        :type sort_code: str, optional
        :param state: State portion of the address., defaults to None
        :type state: str, optional
        :param statement_narrative: Additional description suitable for a customer transaction statement., defaults to None
        :type statement_narrative: str, optional
        :param suburb: District of the sender's or beneficiary's city., defaults to None
        :type suburb: str, optional
        :param tax_id: Tax identification number., defaults to None
        :type tax_id: str, optional
        :param vpa: Virtual Payment Address., defaults to None
        :type vpa: str, optional
        """
        self.aba = self._define_str("aba", aba, nullable=True)
        self.account_number = self._define_str(
            "account_number", account_number, nullable=True
        )
        self.ach_code = self._define_str("ach_code", ach_code, nullable=True)
        self.additional_data = additional_data
        self.additional_last_name = self._define_str(
            "additional_last_name", additional_last_name, nullable=True
        )
        self.address = self._define_str("address", address, nullable=True)
        self.bank_account_holder_name = self._define_str(
            "bank_account_holder_name", bank_account_holder_name, nullable=True
        )
        self.bank_account_type = self._define_str(
            "bank_account_type", bank_account_type, nullable=True
        )
        self.bank_address = self._define_str(
            "bank_address", bank_address, nullable=True
        )
        self.bank_branch_code = self._define_str(
            "bank_branch_code", bank_branch_code, nullable=True
        )
        self.bank_branch_name = self._define_str(
            "bank_branch_name", bank_branch_name, nullable=True
        )
        self.bank_city = self._define_str("bank_city", bank_city, nullable=True)
        self.bank_code = self._define_str("bank_code", bank_code, nullable=True)
        self.bank_country = self._define_str(
            "bank_country", bank_country, nullable=True
        )
        self.bank_name = self._define_str("bank_name", bank_name, nullable=True)
        self.bank_province = self._define_str(
            "bank_province", bank_province, nullable=True
        )
        self.beneficiary_bic_local = self._define_str(
            "beneficiary_bic_local", beneficiary_bic_local, nullable=True
        )
        self.beneficiary_relationship = self._define_str(
            "beneficiary_relationship", beneficiary_relationship, nullable=True
        )
        self.bic_swift = self._define_str("bic_swift", bic_swift, nullable=True)
        self.bsb_code = self._define_str("bsb_code", bsb_code, nullable=True)
        self.card_expiration_month = self._define_str(
            "card_expiration_month", card_expiration_month, nullable=True
        )
        self.card_expiration_year = self._define_str(
            "card_expiration_year", card_expiration_year, nullable=True
        )
        self.card_number = self._define_str("card_number", card_number, nullable=True)
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.city = self._define_str("city", city, nullable=True)
        self.clabe = self._define_str("clabe", clabe, nullable=True)
        self.cnaps = self._define_str("cnaps", cnaps, nullable=True)
        self.company_name = self._define_str(
            "company_name", company_name, nullable=True
        )
        self.confirmation_required = confirmation_required
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
        self.default_payout_method_type = self._define_str(
            "default_payout_method_type", default_payout_method_type, nullable=True
        )
        self.email = self._define_str("email", email, nullable=True)
        self.entity_type = (
            self._enum_matching(entity_type, EntityType.list(), "entity_type")
            if entity_type
            else None
        )
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.iban = self._define_str("iban", iban, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.id_date_of_issue = self._define_str(
            "id_date_of_issue", id_date_of_issue, nullable=True
        )
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
        self.ifsc = self._define_str("ifsc", ifsc, nullable=True)
        self.issuer_code = self._define_str("issuer_code", issuer_code, nullable=True)
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
        self.payment_type = self._define_str(
            "payment_type", payment_type, nullable=True
        )
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
        self.routing_code_type_1 = self._define_str(
            "routing_code_type_1", routing_code_type_1, nullable=True
        )
        self.routing_code_type_2 = self._define_str(
            "routing_code_type_2", routing_code_type_2, nullable=True
        )
        self.routing_code_type_3 = self._define_str(
            "routing_code_type_3", routing_code_type_3, nullable=True
        )
        self.routing_code_value_1 = self._define_str(
            "routing_code_value_1", routing_code_value_1, nullable=True
        )
        self.routing_code_value_2 = self._define_str(
            "routing_code_value_2", routing_code_value_2, nullable=True
        )
        self.routing_code_value_3 = self._define_str(
            "routing_code_value_3", routing_code_value_3, nullable=True
        )
        self.sort_code = self._define_str("sort_code", sort_code, nullable=True)
        self.state = self._define_str("state", state, nullable=True)
        self.statement_narrative = self._define_str(
            "statement_narrative", statement_narrative, nullable=True
        )
        self.suburb = self._define_str("suburb", suburb, nullable=True)
        self.tax_id = self._define_str("tax_id", tax_id, nullable=True)
        self.vpa = self._define_str("vpa", vpa, nullable=True)
