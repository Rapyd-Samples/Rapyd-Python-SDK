from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .subscription_item import SubscriptionItem


@JsonMap({})
class SubscriptionItems(BaseModel):
    """SubscriptionItems

    :param data: A list of up to three subscription items., defaults to None
    :type data: List[SubscriptionItem], optional
    :param has_more: Indicates whether there are more than three items in this subscription., defaults to None
    :type has_more: bool, optional
    :param total_count: Total number of items in this subscription., defaults to None
    :type total_count: float, optional
    :param url: URL for requesting all of the items in this subscription., defaults to None
    :type url: str, optional
    """

    def __init__(
        self,
        data: List[SubscriptionItem] = None,
        has_more: bool = None,
        total_count: float = None,
        url: str = None,
    ):
        """SubscriptionItems

        :param data: A list of up to three subscription items., defaults to None
        :type data: List[SubscriptionItem], optional
        :param has_more: Indicates whether there are more than three items in this subscription., defaults to None
        :type has_more: bool, optional
        :param total_count: Total number of items in this subscription., defaults to None
        :type total_count: float, optional
        :param url: URL for requesting all of the items in this subscription., defaults to None
        :type url: str, optional
        """
        self.data = self._define_list(data, SubscriptionItem)
        self.has_more = has_more
        self.total_count = self._define_number(
            "total_count", total_count, nullable=True
        )
        self.url = self._define_str("url", url, nullable=True)
