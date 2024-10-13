from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .contact import Contact


@JsonMap({"type_": "type"})
class V1ewalletsContact(BaseModel):
    """V1ewalletsContact

    :param data: data, defaults to None
    :type data: List[Contact], optional
    :param total_count: total_count, defaults to None
    :type total_count: float, optional
    :param has_more: has_more, defaults to None
    :type has_more: bool, optional
    :param url: url, defaults to None
    :type url: str, optional
    :param ewallet_reference_id: Rapyd Wallet ID defined by the customer or end user. Must be unique., defaults to None
    :type ewallet_reference_id: str, optional
    :param first_name: First name of the Rapyd Wallet owner., defaults to None
    :type first_name: str, optional
    :param last_name: Last name of the Rapyd Wallet owner., defaults to None
    :type last_name: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param type_: Type of wallet, company or person. Default is person., defaults to None
    :type type_: str, optional
    :param phone_number: Phone number of the Rapyd Wallet owner., defaults to None
    :type phone_number: str, optional
    """

    def __init__(
        self,
        data: List[Contact] = None,
        total_count: float = None,
        has_more: bool = None,
        url: str = None,
        ewallet_reference_id: str = None,
        first_name: str = None,
        last_name: str = None,
        metadata: dict = None,
        type_: str = None,
        phone_number: str = None,
    ):
        """V1ewalletsContact

        :param data: data, defaults to None
        :type data: List[Contact], optional
        :param total_count: total_count, defaults to None
        :type total_count: float, optional
        :param has_more: has_more, defaults to None
        :type has_more: bool, optional
        :param url: url, defaults to None
        :type url: str, optional
        :param ewallet_reference_id: Rapyd Wallet ID defined by the customer or end user. Must be unique., defaults to None
        :type ewallet_reference_id: str, optional
        :param first_name: First name of the Rapyd Wallet owner., defaults to None
        :type first_name: str, optional
        :param last_name: Last name of the Rapyd Wallet owner., defaults to None
        :type last_name: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param type_: Type of wallet, company or person. Default is person., defaults to None
        :type type_: str, optional
        :param phone_number: Phone number of the Rapyd Wallet owner., defaults to None
        :type phone_number: str, optional
        """
        self.data = self._define_list(data, Contact)
        self.total_count = self._define_number(
            "total_count", total_count, nullable=True
        )
        self.has_more = has_more
        self.url = self._define_str("url", url, nullable=True)
        self.ewallet_reference_id = self._define_str(
            "ewallet_reference_id", ewallet_reference_id, nullable=True
        )
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.last_name = self._define_str("last_name", last_name, nullable=True)
        self.metadata = metadata
        self.type_ = self._define_str("type_", type_, nullable=True)
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
