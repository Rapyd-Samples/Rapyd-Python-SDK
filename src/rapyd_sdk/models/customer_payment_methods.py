from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .customer_payment_method import CustomerPaymentMethod


@JsonMap({})
class CustomerPaymentMethods(BaseModel):
    """An object containing the following fields - * data - A list of up to three payment methods. For more information, see Customer Payment Method Object. * has_more - Indicates whether there are more than three payment methods for this customer. * total_count - Total number of payment methods for this customer. * url - URL for requesting all of the payment methods for this customer..

    :param data: data, defaults to None
    :type data: List[CustomerPaymentMethod], optional
    :param has_more: has_more, defaults to None
    :type has_more: bool, optional
    :param total_count: total_count, defaults to None
    :type total_count: int, optional
    :param url: url, defaults to None
    :type url: str, optional
    """

    def __init__(
        self,
        data: List[CustomerPaymentMethod] = None,
        has_more: bool = None,
        total_count: int = None,
        url: str = None,
    ):
        """An object containing the following fields - * data - A list of up to three payment methods. For more information, see Customer Payment Method Object. * has_more - Indicates whether there are more than three payment methods for this customer. * total_count - Total number of payment methods for this customer. * url - URL for requesting all of the payment methods for this customer..

        :param data: data, defaults to None
        :type data: List[CustomerPaymentMethod], optional
        :param has_more: has_more, defaults to None
        :type has_more: bool, optional
        :param total_count: total_count, defaults to None
        :type total_count: int, optional
        :param url: url, defaults to None
        :type url: str, optional
        """
        self.data = self._define_list(data, CustomerPaymentMethod)
        self.has_more = has_more
        self.total_count = self._define_number(
            "total_count", total_count, nullable=True
        )
        self.url = self._define_str("url", url, nullable=True)
