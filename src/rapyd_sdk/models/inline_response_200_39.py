from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .customer import Customer


@JsonMap({})
class InlineResponse200_39(BaseModel):
    """InlineResponse200_39

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: customer, defaults to None
    :type data: Customer, optional
    """

    def __init__(self, status: Status1 = None, data: Customer = None):
        """InlineResponse200_39

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: customer, defaults to None
        :type data: Customer, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, Customer)
