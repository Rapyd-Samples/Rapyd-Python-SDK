from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payout_amount_range_per_currency_inner import PayoutAmountRangePerCurrencyInner
from .entity_type import EntityType
from .category import Category


@JsonMap({})
class PayoutMethodType(BaseModel):
    """PayoutMethodType

    :param amount_range_per_currency: An array of objects that describe limits on the amount, per currency. Contains the following fields: maximum_amount - Maximum amount supported by this payout method for the indicated currency. Decimal number. minimum_amount - Minimum amount supported by this payout method for the indicated currency. Decimal number. * payout_currency - Currency of the payout. Three-letter ISO 4217 code. Uppercase., defaults to None
    :type amount_range_per_currency: List[List[PayoutAmountRangePerCurrencyInner]], optional
    :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
    :type beneficiary_country: str, optional
    :param beneficiary_entity_types: A list of the beneficiary entity types supported by this payout method. One or more of the following: company individual Response only., defaults to None
    :type beneficiary_entity_types: List[EntityType], optional
    :param category: category, defaults to None
    :type category: Category, optional
    :param image: URL of an image that the merchant can use to represent the payout method., defaults to None
    :type image: str, optional
    :param is_cancelable: Indicates whether the payout can be canceled. Relevant when category is cash. One of the following values 0 - Not cancelable. 1 - cancelable.', defaults to None
    :type is_cancelable: int, optional
    :param is_expirable: Indicates whether the payout expires if not completed. Relevant when category is cash. One of the following values 0 - Not expirable. 1 - expirable.', defaults to None
    :type is_expirable: int, optional
    :param is_location_specific: Indicates whether the payout must be made at a specific physical location. Relevant when category is cash. One of the following values 0 - Not locationspecific. 1 - location specific.', defaults to None
    :type is_location_specific: int, optional
    :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payout. Relevant when is_expirable is true., defaults to None
    :type maximum_expiration_seconds: float, optional
    :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payout. Relevant when is_expirable is true., defaults to None
    :type minimum_expiration_seconds: float, optional
    :param name: Payout method name., defaults to None
    :type name: str, optional
    :param payout_currencies: A list of the currencies supported by this payout method. Three-letter ISO 4217 code. Uppercase. Response only., defaults to None
    :type payout_currencies: List[str], optional
    :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country code. Required when default_payout_method_type is not used., defaults to None
    :type payout_method_type: str, optional
    :param sender_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
    :type sender_country: str, optional
    :param sender_currencies: List of currencies that the sender is paying with. Currency consists of a three-letter ISO 4217 code. Response only., defaults to None
    :type sender_currencies: List[str], optional
    :param sender_entity_types: A list of the sender entity types supported by this payout method. One or more of the following: company individual Response only. , defaults to None
    :type sender_entity_types: List[EntityType], optional
    :param estimated_time_of_arrival: The estimated time period in which the beneficiary will receive the funds., defaults to None
    :type estimated_time_of_arrival: str, optional
    :param status: Indicates whether the payout method is currently available. One of the following values: 0 - Not available. 1 - Available., defaults to None
    :type status: int, optional
    """

    def __init__(
        self,
        amount_range_per_currency: List[List[PayoutAmountRangePerCurrencyInner]] = None,
        beneficiary_country: str = None,
        beneficiary_entity_types: List[EntityType] = None,
        category: Category = None,
        image: str = None,
        is_cancelable: int = None,
        is_expirable: int = None,
        is_location_specific: int = None,
        maximum_expiration_seconds: float = None,
        minimum_expiration_seconds: float = None,
        name: str = None,
        payout_currencies: List[str] = None,
        payout_method_type: str = None,
        sender_country: str = None,
        sender_currencies: List[str] = None,
        sender_entity_types: List[EntityType] = None,
        estimated_time_of_arrival: str = None,
        status: int = None,
    ):
        """PayoutMethodType

        :param amount_range_per_currency: An array of objects that describe limits on the amount, per currency. Contains the following fields: maximum_amount - Maximum amount supported by this payout method for the indicated currency. Decimal number. minimum_amount - Minimum amount supported by this payout method for the indicated currency. Decimal number. * payout_currency - Currency of the payout. Three-letter ISO 4217 code. Uppercase., defaults to None
        :type amount_range_per_currency: List[List[PayoutAmountRangePerCurrencyInner]], optional
        :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
        :type beneficiary_country: str, optional
        :param beneficiary_entity_types: A list of the beneficiary entity types supported by this payout method. One or more of the following: company individual Response only., defaults to None
        :type beneficiary_entity_types: List[EntityType], optional
        :param category: category, defaults to None
        :type category: Category, optional
        :param image: URL of an image that the merchant can use to represent the payout method., defaults to None
        :type image: str, optional
        :param is_cancelable: Indicates whether the payout can be canceled. Relevant when category is cash. One of the following values 0 - Not cancelable. 1 - cancelable.', defaults to None
        :type is_cancelable: int, optional
        :param is_expirable: Indicates whether the payout expires if not completed. Relevant when category is cash. One of the following values 0 - Not expirable. 1 - expirable.', defaults to None
        :type is_expirable: int, optional
        :param is_location_specific: Indicates whether the payout must be made at a specific physical location. Relevant when category is cash. One of the following values 0 - Not locationspecific. 1 - location specific.', defaults to None
        :type is_location_specific: int, optional
        :param maximum_expiration_seconds: The maximum time (in seconds) that the merchant can set for completing the payout. Relevant when is_expirable is true., defaults to None
        :type maximum_expiration_seconds: float, optional
        :param minimum_expiration_seconds: The minimum time (in seconds) that the merchant can set for completing the payout. Relevant when is_expirable is true., defaults to None
        :type minimum_expiration_seconds: float, optional
        :param name: Payout method name., defaults to None
        :type name: str, optional
        :param payout_currencies: A list of the currencies supported by this payout method. Three-letter ISO 4217 code. Uppercase. Response only., defaults to None
        :type payout_currencies: List[str], optional
        :param payout_method_type: The type of payout method. The two-letter prefix must match the beneficiary country code. Required when default_payout_method_type is not used., defaults to None
        :type payout_method_type: str, optional
        :param sender_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. The two-letter prefix of the payout method type must match the beneficiary country code., defaults to None
        :type sender_country: str, optional
        :param sender_currencies: List of currencies that the sender is paying with. Currency consists of a three-letter ISO 4217 code. Response only., defaults to None
        :type sender_currencies: List[str], optional
        :param sender_entity_types: A list of the sender entity types supported by this payout method. One or more of the following: company individual Response only. , defaults to None
        :type sender_entity_types: List[EntityType], optional
        :param estimated_time_of_arrival: The estimated time period in which the beneficiary will receive the funds., defaults to None
        :type estimated_time_of_arrival: str, optional
        :param status: Indicates whether the payout method is currently available. One of the following values: 0 - Not available. 1 - Available., defaults to None
        :type status: int, optional
        """
        self.amount_range_per_currency = amount_range_per_currency
        self.beneficiary_country = self._define_str(
            "beneficiary_country", beneficiary_country, nullable=True
        )
        self.beneficiary_entity_types = self._define_list(
            beneficiary_entity_types, EntityType
        )
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
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
        self.maximum_expiration_seconds = self._define_number(
            "maximum_expiration_seconds", maximum_expiration_seconds, nullable=True
        )
        self.minimum_expiration_seconds = self._define_number(
            "minimum_expiration_seconds", minimum_expiration_seconds, nullable=True
        )
        self.name = self._define_str("name", name, nullable=True)
        self.payout_currencies = payout_currencies
        self.payout_method_type = self._define_str(
            "payout_method_type", payout_method_type, nullable=True
        )
        self.sender_country = self._define_str(
            "sender_country", sender_country, nullable=True
        )
        self.sender_currencies = sender_currencies
        self.sender_entity_types = self._define_list(sender_entity_types, EntityType)
        self.estimated_time_of_arrival = self._define_str(
            "estimated_time_of_arrival", estimated_time_of_arrival, nullable=True
        )
        self.status = self._define_number("status", status, nullable=True)
