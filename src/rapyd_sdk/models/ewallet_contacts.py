from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .contact import Contact


@JsonMap({})
class EwalletContacts(BaseModel):
    """EwalletContacts

    :param data: data, defaults to None
    :type data: List[Contact], optional
    :param has_more: has_more, defaults to None
    :type has_more: bool, optional
    :param total_count: total_count, defaults to None
    :type total_count: int, optional
    :param url: url, defaults to None
    :type url: str, optional
    """

    def __init__(
        self,
        data: List[Contact] = None,
        has_more: bool = None,
        total_count: int = None,
        url: str = None,
    ):
        """EwalletContacts

        :param data: data, defaults to None
        :type data: List[Contact], optional
        :param has_more: has_more, defaults to None
        :type has_more: bool, optional
        :param total_count: total_count, defaults to None
        :type total_count: int, optional
        :param url: url, defaults to None
        :type url: str, optional
        """
        self.data = self._define_list(data, Contact)
        self.has_more = has_more
        self.total_count = self._define_number(
            "total_count", total_count, nullable=True
        )
        self.url = self._define_str("url", url, nullable=True)
