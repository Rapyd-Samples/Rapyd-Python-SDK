from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .customer import Customer
from .status import Status


@JsonMap({})
class InlineResponse200_35(BaseModel):
    """InlineResponse200_35

    :param data: customer, defaults to None
    :type data: Customer, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Customer = None, status: Status = None):
        """InlineResponse200_35

        :param data: customer, defaults to None
        :type data: Customer, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Customer)
        self.status = self._define_object(status, Status)
