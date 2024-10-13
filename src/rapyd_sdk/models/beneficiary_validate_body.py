from __future__ import annotations
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel
from .entity_type import EntityType
from .beneficiary import Beneficiary


class BeneficiaryValidateBodyBeneficiaryGuard(OneOfBaseModel):
    class_list = {"str": str, "Beneficiary": Beneficiary}


BeneficiaryValidateBodyBeneficiary = Union[str, Beneficiary]


@JsonMap({})
class BeneficiaryValidateBody(BaseModel):
    """BeneficiaryValidateBody

    :param amount: Maximum payout amount to validate, in units of the currency defined in `sender_currency`. Decimal.
    :type amount: float
    :param beneficiary: String starting with **beneficiary_** or the object describing the beneficiary.
    :type beneficiary: BeneficiaryValidateBodyBeneficiary
    :param identifier_type: Identifier type of beneficiary, defaults to None
    :type identifier_type: str, optional
    :param identifier_value: Identifier value to filter with, defaults to None
    :type identifier_value: str, optional
    :param payout_method_type: The type of the payout method. Set to a value included in the response to List Payout Method Types. The two-letter prefix must match the beneficiary country code.
    :type payout_method_type: str
    :param sender_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code.
    :type sender_country: str
    :param sender_currency: sender_currency
    :type sender_currency: str
    :param sender_entity_type: sender_entity_type
    :type sender_entity_type: EntityType
    """

    def __init__(
        self,
        amount: float,
        beneficiary: BeneficiaryValidateBodyBeneficiary,
        payout_method_type: str,
        sender_country: str,
        sender_currency: str,
        sender_entity_type: EntityType,
        identifier_type: str = None,
        identifier_value: str = None,
    ):
        """BeneficiaryValidateBody

        :param amount: Maximum payout amount to validate, in units of the currency defined in `sender_currency`. Decimal.
        :type amount: float
        :param beneficiary: String starting with **beneficiary_** or the object describing the beneficiary.
        :type beneficiary: BeneficiaryValidateBodyBeneficiary
        :param identifier_type: Identifier type of beneficiary, defaults to None
        :type identifier_type: str, optional
        :param identifier_value: Identifier value to filter with, defaults to None
        :type identifier_value: str, optional
        :param payout_method_type: The type of the payout method. Set to a value included in the response to List Payout Method Types. The two-letter prefix must match the beneficiary country code.
        :type payout_method_type: str
        :param sender_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code.
        :type sender_country: str
        :param sender_currency: sender_currency
        :type sender_currency: str
        :param sender_entity_type: sender_entity_type
        :type sender_entity_type: EntityType
        """
        self.amount = amount
        self.beneficiary = BeneficiaryValidateBodyBeneficiaryGuard.return_one_of(
            beneficiary
        )
        self.identifier_type = self._define_str(
            "identifier_type", identifier_type, nullable=True
        )
        self.identifier_value = self._define_str(
            "identifier_value", identifier_value, nullable=True
        )
        self.payout_method_type = payout_method_type
        self.sender_country = sender_country
        self.sender_currency = self._define_str(
            "sender_currency",
            sender_currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.sender_entity_type = self._enum_matching(
            sender_entity_type, EntityType.list(), "sender_entity_type"
        )
